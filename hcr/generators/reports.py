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


def generate_invocation_coverage_report(bundle: dict[str, Any], path: Path) -> None:
    """Coverage-honest report over each capability's ``invocation_status``.

    Mirrors the three-state discipline the AOS consumer side already applies
    (agentic_meta_dev/scripts/report_unused_capabilities.py, M4 of
    harness-capability-awareness-v1.md): ``resolved`` (a real invocation
    token is on record), ``not_applicable`` (confirmed no single token
    exists, with a reason), and ``unreviewed`` (nobody has looked yet). The
    report always prints (checked, total) and never lets ``unreviewed`` rows
    be silently absent from the output — a run below 100% resolved+n/a must
    read as partial, not as a clean bill of health.
    """
    capabilities = bundle["capabilities"]
    names = {item["id"]: item["name"] for item in bundle["harnesses"]}
    by_harness: dict[str, dict[str, int]] = defaultdict(lambda: {"resolved": 0, "not_applicable": 0, "unreviewed": 0})
    unreviewed_ids: list[tuple[str, str]] = []
    for capability in capabilities:
        status = capability.get("invocation_status", "unreviewed")
        by_harness[capability["harness_id"]][status] += 1
        if status == "unreviewed":
            unreviewed_ids.append((capability["harness_id"], capability["capability_id"]))

    total = len(capabilities)
    checked = sum(v["resolved"] + v["not_applicable"] for v in by_harness.values())

    lines = [
        "# Invocation Coverage Report",
        "",
        f"Generated for registry state: {bundle.get('generated_at', 'unknown')}",
        "",
        f"**coverage: ({checked}, {total})**",
        "",
        (
            "PARTIAL — not every capability has a resolved invocation token or a recorded not-applicable reason."
            if checked < total
            else "COMPLETE — every capability is resolved or explicitly marked not-applicable."
        ),
        "",
        "| Harness | Resolved | Not applicable | Unreviewed |",
        "|---|---:|---:|---:|",
    ]
    for harness_id, values in sorted(by_harness.items(), key=lambda item: names.get(item[0], item[0])):
        lines.append(
            f"| {names.get(harness_id, harness_id)} | {values['resolved']} | {values['not_applicable']} | {values['unreviewed']} |"
        )

    lines.extend(["", "## Unreviewed capability_ids", ""])
    if unreviewed_ids:
        for harness_id, capability_id in sorted(unreviewed_ids):
            lines.append(f"- {capability_id} [{harness_id}]")
    else:
        lines.append("(none)")

    lines.extend([
        "",
        "## Interpretation",
        "",
        "An empty `invocation` array is no longer ambiguous: `invocation_status` distinguishes a "
        "confirmed not-applicable capability from one nobody has reviewed yet. Silent truncation — "
        "a report that skips what it has no evidence for — is the defect this report exists to "
        "prevent; the unreviewed list above is never elided.",
        "",
    ])
    write_text(path, "\n".join(lines))
