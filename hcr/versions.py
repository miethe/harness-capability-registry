from __future__ import annotations

import re
from datetime import datetime
from typing import Any

_TOKEN = re.compile(r"\d+|[A-Za-z]+")


def version_key(version: str | None) -> tuple[Any, ...]:
    """Return a deterministic natural-order key for semver-ish release labels.

    It intentionally avoids requiring strict SemVer because harnesses commonly use
    nightly/date/build suffixes. Numeric components sort numerically; stable
    versions sort after prereleases with the same numeric core.
    """
    if not version:
        return ((-1,), 0, ())
    normalized = version.strip().lstrip("vV")
    main, separator, suffix = normalized.partition("-")
    numeric: list[int] = []
    for part in main.split("."):
        match = re.match(r"^(\d+)", part)
        numeric.append(int(match.group(1)) if match else -1)
    while len(numeric) < 4:
        numeric.append(0)
    suffix_tokens: list[tuple[int, Any]] = []
    for token in _TOKEN.findall(suffix.lower() if separator else ""):
        suffix_tokens.append((1, int(token)) if token.isdigit() else (0, token))
    # Stable releases sort after alpha/beta/rc/nightly variants of the same core.
    stability = 1 if not separator else 0
    return (tuple(numeric), stability, tuple(suffix_tokens), normalized.lower())


def date_key(value: str | None) -> tuple[int, str]:
    if not value:
        return (0, "")
    try:
        # ISO timestamps compare lexicographically after normalization.
        datetime.fromisoformat(value.replace("Z", "+00:00"))
        return (1, value)
    except ValueError:
        return (0, value)


def release_version_key(release: dict[str, Any]) -> tuple[Any, ...]:
    """Sort releases of one product by version, with date as a tie breaker."""
    return (version_key(release.get("version")), date_key(release.get("published_at")))


def release_timeline_key(release: dict[str, Any]) -> tuple[Any, ...]:
    """Sort a cross-product timeline by known date, then semver-ish version."""
    return (
        date_key(release.get("published_at")),
        version_key(release.get("version")),
        release.get("harness_id") or "",
    )
