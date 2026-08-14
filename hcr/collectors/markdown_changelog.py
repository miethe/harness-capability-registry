from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from hcr.io import sha256_text
from hcr.normalizers.heuristic import (
    classify_category,
    classify_change,
    infer_actors,
    infer_capabilities,
    infer_surfaces,
    is_breaking_or_deprecated,
    is_security_relevant,
    normalize_bullets,
)

VERSION_HEADING = re.compile(
    r"^##\s+"
    r"(?:\[)?(?P<version>[vV]?\d+(?:\.\d+){1,3}(?:[-+][0-9A-Za-z.-]+)?)"
    r"(?:\]\([^)]*\)|\])?"
    r"(?:\s*(?:[-–—]\s*|\()(?P<date>\d{4}-\d{2}-\d{2})\)?)?"
    r"\s*$"
)


@dataclass(slots=True)
class ParsedSection:
    version: str
    published_at: str | None
    body: str


def channel_for(version: str) -> str:
    lowered = version.lower()
    if "nightly" in lowered:
        return "nightly"
    if "alpha" in lowered:
        return "alpha"
    if "beta" in lowered:
        return "beta"
    if "preview" in lowered:
        return "preview"
    if "rc" in lowered:
        return "release_candidate"
    return "stable"


def parse_sections(text: str) -> list[ParsedSection]:
    sections: list[ParsedSection] = []
    current_version: str | None = None
    current_date: str | None = None
    body: list[str] = []

    def flush() -> None:
        nonlocal current_version, current_date, body
        if current_version is not None:
            published = f"{current_date}T00:00:00Z" if current_date else None
            sections.append(ParsedSection(current_version.lstrip("vV"), published, "\n".join(body).strip()))
        current_version = None
        current_date = None
        body = []

    for line in text.splitlines():
        match = VERSION_HEADING.match(line)
        if match:
            flush()
            current_version = match.group("version")
            current_date = match.group("date")
        elif current_version is not None:
            body.append(line)
    flush()
    return sections


def section_to_release(
    section: ParsedSection,
    *,
    harness_id: str,
    source_id: str,
    source_url: str,
    raw_path: str,
    retrieved_at: str | None = None,
) -> dict[str, Any]:
    retrieved_at = retrieved_at or datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    bullets = normalize_bullets(section.body.splitlines())
    changes: list[dict[str, Any]] = []
    for index, bullet in enumerate(bullets, start=1):
        kind = classify_change(bullet)
        changes.append(
            {
                "id": f"chg.{harness_id}.{section.version}.{index:03d}",
                "kind": kind,
                "summary": bullet,
                "category": classify_category(bullet),
                "surfaces": infer_surfaces(bullet),
                "actors": infer_actors(bullet),
                "capability_refs": infer_capabilities(bullet),
                "security_relevant": is_security_relevant(bullet),
                "breaking_or_deprecated": is_breaking_or_deprecated(bullet),
                "normalization": {
                    "method": "deterministic_heuristic_v1",
                    "confidence": "candidate",
                    "review_status": "unreviewed",
                },
            }
        )
    return {
        "id": f"rel.{harness_id}.{section.version}",
        "harness_id": harness_id,
        "version": section.version,
        "channel": channel_for(section.version),
        "published_at": section.published_at,
        "date_precision": "day" if section.published_at else "unknown",
        "retrieved_at": retrieved_at,
        "source_id": source_id,
        "source_url": source_url,
        "raw_snapshot_path": raw_path,
        "raw_sha256": sha256_text(section.body),
        "title": f"{harness_id} {section.version}",
        "notes_excerpt": bullets[0] if bullets else "No bullet items found.",
        "change_count": len(changes),
        "flags": {
            "security": any(item["security_relevant"] for item in changes),
            "breaking": any(item["breaking_or_deprecated"] for item in changes),
            "deprecation": any(item["kind"] == "deprecated" for item in changes),
        },
        "changes": changes,
        "provenance": {
            "authority": "official_primary",
            "ingestion": "markdown_changelog",
            "immutable": False,
        },
    }



def filter_release_window(
    releases: list[dict[str, Any]],
    *,
    since_days: int,
    max_dateless_releases: int = 110,
    now: datetime | None = None,
) -> list[dict[str, Any]]:
    """Apply a time window while safely bounding changelogs without dates.

    Some high-velocity harness changelogs omit publication dates entirely. For
    those sources, section count is the only deterministic historical bound.
    """
    now = now or datetime.now(timezone.utc)
    cutoff = now - timedelta(days=since_days)
    retained: list[dict[str, Any]] = []
    dateless_count = 0
    for release in releases:
        published_at = release.get("published_at")
        if published_at:
            try:
                published = datetime.fromisoformat(published_at.replace("Z", "+00:00"))
            except ValueError:
                continue
            if published >= cutoff:
                retained.append(release)
        elif dateless_count < max_dateless_releases:
            retained.append(release)
            dateless_count += 1
    return retained

def parse_changelog_file(
    path: Path,
    *,
    harness_id: str,
    source_id: str,
    source_url: str,
    raw_path: str,
) -> list[dict[str, Any]]:
    text = path.read_text(encoding="utf-8")
    return [
        section_to_release(
            section,
            harness_id=harness_id,
            source_id=source_id,
            source_url=source_url,
            raw_path=raw_path,
        )
        for section in parse_sections(text)
    ]
