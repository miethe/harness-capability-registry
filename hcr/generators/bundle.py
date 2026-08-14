from __future__ import annotations

import json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from hcr.io import read_json, write_json, write_text
from hcr.versions import release_timeline_key
from hcr.generators.guides import generate_guides
from hcr.generators.standalone import build_standalone_app


def _sort_releases(releases: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(
        releases,
        key=release_timeline_key,
        reverse=True,
    )


def build_bundle(root: Path) -> dict[str, Any]:
    registry = root / "registry"
    meta = read_json(registry / "registry-meta.json")
    sources = read_json(registry / "sources.json")
    harnesses = read_json(registry / "harnesses.json")
    taxonomy = read_json(registry / "taxonomy.json")
    implementations = read_json(registry / "capabilities.json")
    releases = _sort_releases(read_json(registry / "releases.json"))

    # Materialized artifacts are deterministic for a registry state. A routine
    # regenerate with no upstream change should produce a byte-identical bundle.
    generated_at = meta.get("updated_at") or meta.get("created_at") or datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    taxonomy_by_id = {item["id"]: item for item in taxonomy}
    harness_by_id = {item["id"]: item for item in harnesses}

    stats = {
        "harness_count": len(harnesses),
        "active_harness_count": sum(1 for item in harnesses if item["lifecycle"] == "active"),
        "source_count": len(sources),
        "capability_taxonomy_count": len(taxonomy),
        "capability_implementation_count": len(implementations),
        "release_count": len(releases),
        "release_change_count": sum(item.get("change_count", len(item.get("changes", []))) for item in releases),
        "verified_capability_count": sum(1 for item in implementations if item.get("confidence") == "verified_official"),
        "low_confidence_capability_count": sum(1 for item in implementations if item.get("confidence") in {"unknown", "inferred_low"}),
    }

    category_counts = Counter(taxonomy_by_id.get(item["capability_id"], {}).get("category", "other") for item in implementations)
    harness_capability_counts = Counter(item["harness_id"] for item in implementations)
    release_counts = Counter(item["harness_id"] for item in releases)

    actor_summary: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for item in implementations:
        for actor, access in item.get("actor_access", {}).items():
            actor_summary[actor][access] += 1

    matrix_rows = []
    for capability in taxonomy:
        row = {"capability": capability, "implementations": {}}
        for implementation in implementations:
            if implementation["capability_id"] == capability["id"]:
                row["implementations"][implementation["harness_id"]] = implementation
        matrix_rows.append(row)

    bundles_by_harness: dict[str, dict[str, Any]] = {}
    for harness in harnesses:
        hid = harness["id"]
        bundles_by_harness[hid] = {
            "harness": harness,
            "capabilities": [item for item in implementations if item["harness_id"] == hid],
            "releases": [item for item in releases if item["harness_id"] == hid],
            "sources": [item for item in sources if hid in item.get("harness_ids", [])],
        }
        write_json(registry / "harnesses" / f"{hid}.json", bundles_by_harness[hid])
        write_json(registry / "releases" / f"{hid}.json", bundles_by_harness[hid]["releases"])
        write_json(registry / "capabilities" / f"{hid}.json", bundles_by_harness[hid]["capabilities"])

    guides = generate_guides(
        output_dir=root / "generated" / "agent-guides",
        harnesses=harnesses,
        taxonomy=taxonomy,
        implementations=implementations,
        releases=releases,
        generated_at=generated_at,
    )

    bundle = {
        "schema_version": "0.1",
        "generated_at": generated_at,
        "registry_meta": meta,
        "stats": stats,
        "summaries": {
            "category_counts": dict(category_counts),
            "harness_capability_counts": dict(harness_capability_counts),
            "release_counts": dict(release_counts),
            "actor_access_counts": {key: dict(value) for key, value in actor_summary.items()},
        },
        "sources": sources,
        "harnesses": harnesses,
        "taxonomy": taxonomy,
        "capabilities": implementations,
        "matrix": matrix_rows,
        "releases": releases,
        "agent_guides": guides,
    }
    write_json(root / "app" / "data" / "registry.bundle.json", bundle)
    write_json(root / "generated" / "registry.bundle.json", bundle)
    js_payload = "window.HCR_DATA = " + json.dumps(bundle, ensure_ascii=False, separators=(",", ":")) + ";\n"
    write_text(root / "app" / "data" / "registry.bundle.js", js_payload)
    build_standalone_app(root)
    return bundle
