from __future__ import annotations

from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from hcr.io import write_json, write_text
from hcr.versions import release_version_key

ACTOR_LABELS = {
    "human_operator": "Human operator",
    "in_harness_agent": "In-harness agent",
    "external_orchestrator": "External agent/orchestrator",
    "ci_runner": "CI or scheduled automation",
    "administrator": "Administrator",
}

ACCESS_POSITIVE = {"native", "supported", "configurable", "experimental"}


def _evidence_summary(capability: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        {
            "source_id": item.get("source_id"),
            "url": item.get("url"),
            "version": item.get("version"),
            "verified_at": item.get("verified_at"),
            "claim": item.get("claim"),
        }
        for item in capability.get("evidence", [])
    ]


def build_agent_guide(
    harness: dict[str, Any],
    implementations: list[dict[str, Any]],
    taxonomy_by_id: dict[str, dict[str, Any]],
    releases: list[dict[str, Any]],
    *,
    generated_at: str,
) -> dict[str, Any]:
    relevant = [item for item in implementations if item["harness_id"] == harness["id"]]
    by_actor: dict[str, list[dict[str, Any]]] = defaultdict(list)
    requires_human: list[dict[str, Any]] = []
    unknown: list[dict[str, Any]] = []

    for implementation in relevant:
        canonical = taxonomy_by_id.get(implementation["capability_id"], {})
        actor_access = implementation.get("actor_access", {})
        concise = {
            "capability_id": implementation["capability_id"],
            "name": canonical.get("name", implementation["capability_id"]),
            "category": canonical.get("category", "other"),
            "status": implementation.get("status"),
            "summary": implementation.get("summary"),
            "surfaces": implementation.get("surfaces", []),
            "invocation": implementation.get("invocation", []),
            "minimum_version": implementation.get("minimum_version"),
            "limitations": implementation.get("limitations", []),
            "confidence": implementation.get("confidence"),
            "evidence": _evidence_summary(implementation),
        }
        for actor, access in actor_access.items():
            if access in ACCESS_POSITIVE:
                by_actor[actor].append({**concise, "access": access})
        if implementation.get("requires_human_mediation"):
            requires_human.append(concise)
        if implementation.get("confidence") in {"unknown", "inferred_low"}:
            unknown.append(concise)

    sorted_releases = sorted(
        [item for item in releases if item["harness_id"] == harness["id"]],
        key=release_version_key,
        reverse=True,
    )
    current_version = harness.get("current_version")
    latest = next((item for item in sorted_releases if item.get("version") == current_version), None)
    if latest is None:
        latest = sorted_releases[0] if sorted_releases else None
    return {
        "schema_version": "0.1",
        "generated_at": generated_at,
        "guide_type": "agent_consumable_harness_capability_guide",
        "harness": {
            "id": harness["id"],
            "name": harness["name"],
            "vendor": harness["vendor"],
            "family": harness["family"],
            "lifecycle": harness["lifecycle"],
            "current_version": harness.get("current_version"),
            "predecessor": harness.get("predecessor"),
            "successor": harness.get("successor"),
        },
        "freshness": {
            "last_verified_at": harness.get("last_verified_at"),
            "latest_release_in_registry": latest["version"] if latest else None,
            "latest_release_published_at": latest.get("published_at") if latest else None,
            "warning": "Treat unavailable or unknown actor access as unsupported until verified. UI-only capability is not agent-callable by implication.",
        },
        "capabilities_by_actor": dict(by_actor),
        "human_mediation_required": requires_human,
        "unverified_or_low_confidence": unknown,
        "routing_hint": {
            "recommended_when": harness.get("recommended_when", []),
            "avoid_when": harness.get("avoid_when", []),
            "control_plane_dimensions": harness.get("control_plane_dimensions", {}),
        },
    }


def guide_to_markdown(guide: dict[str, Any]) -> str:
    harness = guide["harness"]
    lines = [
        "---",
        "schema_version: 0.1",
        f"harness_id: {harness['id']}",
        f"generated_at: {guide['generated_at']}",
        "artifact_kind: harness_capability_guide",
        "---",
        "",
        f"# {harness['name']} — Agent Capability Guide",
        "",
        f"**Vendor:** {harness['vendor']}  ",
        f"**Lifecycle:** {harness['lifecycle']}  ",
        f"**Current version in registry:** {harness.get('current_version') or 'unknown'}  ",
        f"**Last verified:** {guide['freshness'].get('last_verified_at') or 'unknown'}",
        "",
        "> UI availability does not imply that an in-harness model or an external orchestrator can invoke the capability. Use the actor-specific sections below.",
        "",
    ]
    for actor, label in ACTOR_LABELS.items():
        items = guide["capabilities_by_actor"].get(actor, [])
        lines.extend([f"## {label}", ""])
        if not items:
            lines.extend(["No positively verified capabilities in the current seed.", ""])
            continue
        for item in sorted(items, key=lambda value: (value["category"], value["name"])):
            invocation = ", ".join(item.get("invocation") or []) or "See evidence"
            lines.append(f"- **{item['name']}** (`{item['access']}`): {item['summary']} Invocation: `{invocation}`.")
        lines.append("")
    if guide["human_mediation_required"]:
        lines.extend(["## Human mediation required", ""])
        for item in guide["human_mediation_required"]:
            lines.append(f"- **{item['name']}**: {item['summary']}")
        lines.append("")
    lines.extend([
        "## Freshness rule",
        "",
        guide["freshness"]["warning"],
        "",
    ])
    return "\n".join(lines)


def generate_guides(
    *,
    output_dir: Path,
    harnesses: list[dict[str, Any]],
    taxonomy: list[dict[str, Any]],
    implementations: list[dict[str, Any]],
    releases: list[dict[str, Any]],
    generated_at: str | None = None,
) -> list[dict[str, Any]]:
    generated_at = generated_at or datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    taxonomy_by_id = {item["id"]: item for item in taxonomy}
    guides = []
    for harness in harnesses:
        guide = build_agent_guide(harness, implementations, taxonomy_by_id, releases, generated_at=generated_at)
        guides.append(guide)
        write_json(output_dir / f"{harness['id']}.json", guide)
        write_text(output_dir / f"{harness['id']}.md", guide_to_markdown(guide))
    write_json(output_dir / "index.json", guides)
    return guides
