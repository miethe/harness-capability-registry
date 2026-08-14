from __future__ import annotations

import json
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from hcr.collectors.markdown_changelog import channel_for
from hcr.io import sha256_text, write_content_addressed_json_snapshot


class PackageRegistryError(RuntimeError):
    pass


def _get_json(url: str) -> Any:
    request = urllib.request.Request(
        url,
        headers={"Accept": "application/json", "User-Agent": "harness-capability-registry/0.1"},
    )
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            return json.loads(response.read().decode("utf-8"))
    except (urllib.error.HTTPError, urllib.error.URLError, json.JSONDecodeError) as exc:
        raise PackageRegistryError(f"Unable to query package registry {url}: {exc}") from exc


def _release(
    *,
    harness_id: str,
    source_id: str,
    source_url: str,
    package: str,
    version: str,
    published_at: str | None,
    ecosystem: str,
    assets: list[dict[str, Any]],
) -> dict[str, Any]:
    summary = f"Published {package} {version} to {ecosystem}."
    return {
        "id": f"rel.{harness_id}.{version}",
        "harness_id": harness_id,
        "version": version,
        "channel": channel_for(version),
        "published_at": published_at,
        "date_precision": "second" if published_at else "unknown",
        "retrieved_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "source_id": source_id,
        "source_url": source_url,
        "raw_snapshot_path": None,
        "raw_sha256": sha256_text(json.dumps(assets, sort_keys=True)),
        "title": f"{package} {version}",
        "notes_excerpt": summary,
        "change_count": 1,
        "flags": {"security": False, "breaking": False, "deprecation": False},
        "changes": [
            {
                "id": f"chg.{harness_id}.{version}.001",
                "kind": "changed",
                "summary": summary,
                "category": "distribution_runtime",
                "surfaces": ["package_registry"],
                "actors": ["administrator", "external_orchestrator", "ci_runner"],
                "capability_refs": [],
                "security_relevant": False,
                "breaking_or_deprecated": False,
                "normalization": {
                    "method": "package_registry_metadata_v1",
                    "confidence": "verified_official",
                    "review_status": "approved",
                },
            }
        ],
        "assets": assets,
        "provenance": {
            "authority": "package_registry",
            "ingestion": f"{ecosystem.lower()}_registry_api",
            "immutable": True,
            "package": package,
        },
    }


def collect_pypi_releases(
    *,
    package: str,
    harness_id: str,
    source_id: str,
    source_url: str,
    since_days: int = 120,
    raw_dir: Path | None = None,
) -> list[dict[str, Any]]:
    payload = _get_json(f"https://pypi.org/pypi/{urllib.parse.quote(package)}/json")
    cutoff = datetime.now(timezone.utc) - timedelta(days=since_days)
    releases: list[dict[str, Any]] = []
    for version, files in payload.get("releases", {}).items():
        uploads = [item.get("upload_time_iso_8601") for item in files if item.get("upload_time_iso_8601")]
        published = min(uploads) if uploads else None
        if published and datetime.fromisoformat(published.replace("Z", "+00:00")) < cutoff:
            continue
        assets = [
            {
                "name": item.get("filename"),
                "url": item.get("url"),
                "size": item.get("size"),
                "content_type": item.get("packagetype"),
                "digest": (item.get("digests") or {}).get("sha256"),
            }
            for item in files
        ]
        releases.append(
            _release(
                harness_id=harness_id,
                source_id=source_id,
                source_url=source_url,
                package=package,
                version=version,
                published_at=published,
                ecosystem="PyPI",
                assets=assets,
            )
        )
    if raw_dir is not None:
        write_content_addressed_json_snapshot(raw_dir / harness_id, "pypi", payload)
    return releases


def collect_npm_releases(
    *,
    package: str,
    harness_id: str,
    source_id: str,
    source_url: str,
    since_days: int = 120,
    raw_dir: Path | None = None,
) -> list[dict[str, Any]]:
    encoded = urllib.parse.quote(package, safe="")
    payload = _get_json(f"https://registry.npmjs.org/{encoded}")
    cutoff = datetime.now(timezone.utc) - timedelta(days=since_days)
    times = payload.get("time", {})
    releases: list[dict[str, Any]] = []
    for version, metadata in payload.get("versions", {}).items():
        published = times.get(version)
        if published and datetime.fromisoformat(published.replace("Z", "+00:00")) < cutoff:
            continue
        dist = metadata.get("dist", {})
        assets = [
            {
                "name": f"{package}-{version}.tgz",
                "url": dist.get("tarball"),
                "size": dist.get("unpackedSize"),
                "content_type": "npm-tarball",
                "digest": dist.get("integrity") or dist.get("shasum"),
            }
        ]
        releases.append(
            _release(
                harness_id=harness_id,
                source_id=source_id,
                source_url=source_url,
                package=package,
                version=version,
                published_at=published,
                ecosystem="npm",
                assets=assets,
            )
        )
    if raw_dir is not None:
        write_content_addressed_json_snapshot(raw_dir / harness_id, "npm", payload)
    return releases
