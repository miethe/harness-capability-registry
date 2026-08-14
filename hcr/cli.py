from __future__ import annotations

import argparse
import copy
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from hcr.collectors.github_releases import GitHubAPIError, collect_github_releases
from hcr.collectors.http_text import HTTPCollectorError, collect_text_snapshot
from hcr.collectors.package_registries import (
    PackageRegistryError,
    collect_npm_releases,
    collect_pypi_releases,
)
from hcr.collectors.markdown_changelog import filter_release_window, parse_changelog_file
from hcr.generators.bundle import build_bundle
from hcr.generators.reports import generate_coverage_report
from hcr.io import read_json, write_json, write_text
from hcr.validators.core import validate_registry
from hcr.versions import release_timeline_key, release_version_key


def _root(value: str | None) -> Path:
    return Path(value or Path.cwd()).resolve()


def _merge_releases(existing: list[dict[str, Any]], incoming: list[dict[str, Any]]) -> list[dict[str, Any]]:
    merged = {item["id"]: item for item in existing}
    for item in incoming:
        current = merged.get(item["id"])
        if current is None:
            merged[item["id"]] = item
            continue

        candidate = copy.deepcopy(item)
        if current.get("published_at") and not candidate.get("published_at"):
            candidate["published_at"] = current["published_at"]
            candidate["date_precision"] = current.get("date_precision", "unknown")

        reviewed = [
            change
            for change in current.get("changes", [])
            if change.get("normalization", {}).get("review_status") == "approved"
        ]
        if reviewed:
            candidate["changes"] = reviewed
            candidate["change_count"] = len(reviewed)

        # Polling the same immutable release must not rewrite retrieved_at or
        # create a full-registry diff. Replace only when upstream content or a
        # material field changed (for example, a newly precise publication date).
        same_payload = bool(current.get("raw_sha256")) and current.get("raw_sha256") == candidate.get("raw_sha256")
        same_date = current.get("published_at") == candidate.get("published_at")
        same_source = current.get("source_id") == candidate.get("source_id")
        if same_payload and same_date and same_source:
            merged[item["id"]] = current
        else:
            merged[item["id"]] = candidate
    return sorted(merged.values(), key=release_timeline_key, reverse=True)


def _reconcile_harness_versions(
    harnesses: list[dict[str, Any]], releases: list[dict[str, Any]], *, verified_at: str
) -> list[dict[str, Any]]:
    reconciled = copy.deepcopy(harnesses)
    by_harness: dict[str, list[dict[str, Any]]] = {}
    for release in releases:
        by_harness.setdefault(release["harness_id"], []).append(release)
    for harness in reconciled:
        candidates = by_harness.get(harness["id"], [])
        if not candidates:
            continue
        latest = max(candidates, key=release_version_key)
        latest_version = latest.get("version")
        precise_as_of = latest.get("published_at")
        version_changed = harness.get("current_version") != latest_version
        date_became_precise = bool(precise_as_of) and harness.get("version_as_of") != precise_as_of[:10]
        if version_changed or date_became_precise or not harness.get("last_verified_at"):
            harness["current_version"] = latest_version
            harness["version_as_of"] = (precise_as_of or verified_at)[:10]
            harness["last_verified_at"] = verified_at
    return reconciled


def _snapshot_source(root: Path, source: dict[str, Any]) -> dict[str, Any]:
    """Snapshot a source, retaining a new payload only when its content changed."""
    base = root / "raw" / "source-snapshots"
    safe_id = source["id"].replace("/", "_")
    previous_meta = sorted((base / safe_id).glob("*.meta.json"))
    previous = read_json(previous_meta[-1]) if previous_meta else None
    record = collect_text_snapshot(
        url=source["url"],
        source_id=source["id"],
        output_dir=base,
    )
    new_snapshot = Path(record["snapshot_path"])
    new_meta = new_snapshot.with_suffix(".meta.json")
    changed = previous is None or previous.get("sha256") != record.get("sha256")
    record["changed"] = changed
    record["previous_sha256"] = previous.get("sha256") if previous else None

    # Six-hourly polling must not create an identical full snapshot each run.
    if not changed and previous:
        new_snapshot.unlink(missing_ok=True)
        new_meta.unlink(missing_ok=True)
        record["snapshot_path"] = previous.get("snapshot_path")
        record["deduplicated"] = True
    else:
        record["snapshot_path"] = str(new_snapshot.relative_to(root))
        record["deduplicated"] = False
        write_json(new_meta, record)
    return record


def _touch_registry_meta(root: Path, *, updated_at: str) -> None:
    path = root / "registry" / "registry-meta.json"
    meta = read_json(path)
    meta["updated_at"] = updated_at
    write_json(path, meta)


def cmd_collect(args: argparse.Namespace) -> int:
    root = _root(args.root)
    registry_path = root / "registry" / "releases.json"
    existing = read_json(registry_path)
    sources = read_json(root / "registry" / "sources.json")
    harness_records: list[dict[str, Any]] = read_json(root / "registry" / "harnesses.json")
    incoming: list[dict[str, Any]] = []
    failures: list[str] = []

    if args.offline:
        result = {
            "collected_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
            "mode": "offline_regeneration_no_collection",
            "incoming_count": 0,
            "registry_release_count": len(existing),
            "registry_changed": False,
            "failures": [],
        }
        print(json.dumps(result, indent=2))
        return 0

    for source in sources:
        if not source.get("enabled", True) or source.get("purpose") != "release_history":
            continue
        collector = source.get("collector", {})
        kind = collector.get("kind")
        harness_id = source.get("harness_ids", [None])[0]
        if args.harness and harness_id != args.harness:
            continue
        try:
            if kind == "github_releases":
                incoming.extend(
                    collect_github_releases(
                        repo=collector["repo"],
                        harness_id=harness_id,
                        source_id=source["id"],
                        since_days=args.since_days,
                        include_prereleases=args.include_prereleases,
                        max_pages=args.max_pages,
                        raw_dir=root / "raw",
                    )
                )
            elif kind == "markdown_changelog" and collector.get("local_seed_path"):
                path = root / collector["local_seed_path"]
                if not args.offline:
                    try:
                        snapshot = _snapshot_source(root, source)
                        snapshot_path = Path(snapshot["snapshot_path"])
                        write_text(path, snapshot_path.read_text(encoding="utf-8"))
                    except (HTTPCollectorError, OSError) as exc:
                        failures.append(f"{source['id']} remote refresh: {exc}; used local snapshot")
                parsed = parse_changelog_file(
                    path,
                    harness_id=harness_id,
                    source_id=source["id"],
                    source_url=source["url"],
                    raw_path=collector["local_seed_path"],
                )
                incoming.extend(
                    filter_release_window(
                        parsed,
                        since_days=args.since_days,
                        max_dateless_releases=int(collector.get("max_dateless_releases", 110)),
                    )
                )
            elif kind == "pypi":
                incoming.extend(
                    collect_pypi_releases(
                        package=collector["package"],
                        harness_id=harness_id,
                        source_id=source["id"],
                        source_url=source["url"],
                        since_days=args.since_days,
                        raw_dir=root / "raw",
                    )
                )
            elif kind == "npm":
                incoming.extend(
                    collect_npm_releases(
                        package=collector["package"],
                        harness_id=harness_id,
                        source_id=source["id"],
                        source_url=source["url"],
                        since_days=args.since_days,
                        raw_dir=root / "raw",
                    )
                )
        except (GitHubAPIError, HTTPCollectorError, PackageRegistryError, OSError, KeyError, ValueError) as exc:
            failures.append(f"{source['id']}: {exc}")
            if args.fail_fast:
                raise

    merged = _merge_releases(existing, incoming)
    collected_at = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    reconciled_harnesses = _reconcile_harness_versions(harness_records, merged, verified_at=collected_at)
    registry_changed = merged != existing or reconciled_harnesses != harness_records
    if merged != existing:
        write_json(registry_path, merged)
    if reconciled_harnesses != harness_records:
        write_json(root / "registry" / "harnesses.json", reconciled_harnesses)
    if registry_changed:
        _touch_registry_meta(root, updated_at=collected_at)
    result = {
        "collected_at": collected_at,
        "incoming_count": len(incoming),
        "registry_release_count": len(merged),
        "registry_changed": registry_changed,
        "failures": failures,
    }
    collection_report_path = root / "generated" / "collection-report.json"
    if registry_changed or not collection_report_path.exists():
        write_json(collection_report_path, result)
    print(json.dumps(result, indent=2))
    return 1 if failures and args.strict else 0


def cmd_snapshot(args: argparse.Namespace) -> int:
    root = _root(args.root)
    sources = read_json(root / "registry" / "sources.json")
    records: list[dict[str, Any]] = []
    failures: list[str] = []
    purposes = set(args.purpose or ["capability_reference", "lifecycle_reference", "comparison_reference"])
    for source in sources:
        if not source.get("enabled", True) or source.get("purpose") not in purposes:
            continue
        if args.harness and args.harness not in source.get("harness_ids", []):
            continue
        try:
            records.append(_snapshot_source(root, source))
        except (HTTPCollectorError, OSError) as exc:
            failures.append(f"{source['id']}: {exc}")
            if args.fail_fast:
                raise
    snapshotted_at = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    changed_source_ids = [item["source_id"] for item in records if item.get("changed")]
    if changed_source_ids:
        _touch_registry_meta(root, updated_at=snapshotted_at)
    result = {
        "snapshotted_at": snapshotted_at,
        "source_count": len(records),
        "changed_source_ids": changed_source_ids,
        "unchanged_source_ids": [item["source_id"] for item in records if not item.get("changed")],
        "records": records,
        "failures": failures,
    }
    drift_report_path = root / "generated" / "source-drift-report.json"
    if changed_source_ids or not drift_report_path.exists():
        write_json(drift_report_path, result)
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, indent=2))
    return 1 if failures and args.strict else 0


def cmd_generate(args: argparse.Namespace) -> int:
    root = _root(args.root)
    bundle = build_bundle(root)
    generate_coverage_report(bundle, root / "generated" / "reports" / "coverage.md")
    print(json.dumps(bundle["stats"], indent=2))
    return 0


def cmd_validate(args: argparse.Namespace) -> int:
    root = _root(args.root)
    report = validate_registry(root)
    print(json.dumps(report, indent=2))
    return 0 if report["valid"] else 1


def cmd_update(args: argparse.Namespace) -> int:
    collect_args = argparse.Namespace(
        root=args.root,
        harness=args.harness,
        since_days=args.since_days,
        include_prereleases=args.include_prereleases,
        max_pages=args.max_pages,
        fail_fast=False,
        strict=args.strict,
        offline=args.offline,
    )
    statuses = [cmd_collect(collect_args)]
    if args.snapshot_docs and not args.offline:
        snapshot_args = argparse.Namespace(
            root=args.root,
            harness=args.harness,
            purpose=None,
            fail_fast=False,
            strict=args.strict,
        )
        statuses.append(cmd_snapshot(snapshot_args))
    cmd_generate(args)
    statuses.append(cmd_validate(args))
    return max(statuses)


def cmd_serve(args: argparse.Namespace) -> int:
    import http.server
    import os
    import socketserver

    root = _root(args.root)
    app_dir = root / "app"
    os.chdir(app_dir)
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer((args.bind, args.port), handler) as server:
        print(f"Serving HCR at http://{args.bind}:{args.port}")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="hcr", description="Harness Capability Registry")
    parser.add_argument("--root", help="Project root; defaults to current directory")
    subparsers = parser.add_subparsers(dest="command", required=True)

    collect = subparsers.add_parser("collect", help="Collect release history from configured official sources")
    collect.add_argument("--harness", help="Limit to one harness id")
    collect.add_argument("--since-days", type=int, default=120)
    collect.add_argument("--max-pages", type=int, default=20)
    collect.add_argument("--include-prereleases", action=argparse.BooleanOptionalAction, default=True)
    collect.add_argument("--fail-fast", action="store_true")
    collect.add_argument("--strict", action="store_true")
    collect.add_argument("--offline", action="store_true", help="Use local snapshots and skip network refreshes")
    collect.set_defaults(func=cmd_collect)

    snapshot = subparsers.add_parser("snapshot", help="Snapshot documentation sources and report source drift")
    snapshot.add_argument("--harness", help="Limit to one harness id")
    snapshot.add_argument("--purpose", action="append", help="Source purpose to snapshot; may be repeated")
    snapshot.add_argument("--fail-fast", action="store_true")
    snapshot.add_argument("--strict", action="store_true")
    snapshot.set_defaults(func=cmd_snapshot)

    generate = subparsers.add_parser("generate", help="Generate materialized views, web bundle, and agent guides")
    generate.set_defaults(func=cmd_generate)

    validate = subparsers.add_parser("validate", help="Validate registry references and invariants")
    validate.set_defaults(func=cmd_validate)

    update = subparsers.add_parser("update", help="Collect, generate, and validate")
    update.add_argument("--harness", help="Limit to one harness id")
    update.add_argument("--since-days", type=int, default=120)
    update.add_argument("--max-pages", type=int, default=20)
    update.add_argument("--include-prereleases", action=argparse.BooleanOptionalAction, default=True)
    update.add_argument("--strict", action="store_true")
    update.add_argument("--offline", action="store_true", help="Use local snapshots and skip network refreshes")
    update.add_argument("--snapshot-docs", action=argparse.BooleanOptionalAction, default=True)
    update.set_defaults(func=cmd_update)

    serve = subparsers.add_parser("serve", help="Serve the static comparison app")
    serve.add_argument("--bind", default="127.0.0.1")
    serve.add_argument("--port", type=int, default=8765)
    serve.set_defaults(func=cmd_serve)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":
    sys.exit(main())
