from __future__ import annotations

from collections import defaultdict
from pathlib import Path
from typing import Any

from hcr.io import write_text


def generate_coverage_report(bundle: dict[str, Any], path: Path) -> None:
    by_harness: dict[str, dict[str, int]] = defaultdict(lambda: {"verified": 0, "candidate": 0, "unknown": 0, "releases": 0})
    for capability in bundle["capabilities"]:
        confidence = capability.get("confidence", "unknown")
        bucket = "verified" if confidence == "verified_official" else "candidate" if confidence.startswith("inferred") else "unknown"
        by_harness[capability["harness_id"]][bucket] += 1
    for release in bundle["releases"]:
        by_harness[release["harness_id"]]["releases"] += 1

    lines = [
        "# Registry Coverage Report",
        "",
        f"Generated for registry state: {bundle.get('generated_at', 'unknown')}",
        "",
        "| Harness | Verified capabilities | Candidate | Unknown | Releases |",
        "|---|---:|---:|---:|---:|",
    ]
    names = {item["id"]: item["name"] for item in bundle["harnesses"]}
    for harness_id, values in sorted(by_harness.items(), key=lambda item: names.get(item[0], item[0])):
        lines.append(
            f"| {names.get(harness_id, harness_id)} | {values['verified']} | {values['candidate']} | {values['unknown']} | {values['releases']} |"
        )
    lines.extend([
        "",
        "## Interpretation",
        "",
        "A high release count does not imply comprehensive capability coverage. Release collection and documentation-derived capability verification are separate pipelines by design.",
        "",
    ])
    write_text(path, "\n".join(lines))
