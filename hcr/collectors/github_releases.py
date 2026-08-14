from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from hcr.collectors.markdown_changelog import channel_for
from hcr.io import sha256_text, write_content_addressed_json_snapshot
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


class GitHubAPIError(RuntimeError):
    pass


def _request_json(url: str, *, token: str | None = None, etag: str | None = None) -> tuple[Any, dict[str, str]]:
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "harness-capability-registry/0.1",
    }
    token = token or os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    if etag:
        headers["If-None-Match"] = etag
    request = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            body = response.read().decode("utf-8")
            return json.loads(body), {key.lower(): value for key, value in response.headers.items()}
    except urllib.error.HTTPError as exc:
        if exc.code == 304:
            return None, {key.lower(): value for key, value in exc.headers.items()}
        detail = exc.read().decode("utf-8", errors="replace")
        raise GitHubAPIError(f"GitHub API returned {exc.code} for {url}: {detail[:500]}") from exc
    except urllib.error.URLError as exc:
        raise GitHubAPIError(f"Unable to reach GitHub API for {url}: {exc}") from exc


def _normalize_release(item: dict[str, Any], *, harness_id: str, source_id: str) -> dict[str, Any]:
    version = str(item.get("tag_name") or item.get("name") or item["id"]).lstrip("vV")
    body = item.get("body") or ""
    bullets = normalize_bullets(body.splitlines())
    if not bullets and body.strip():
        bullets = [line.strip() for line in body.splitlines() if line.strip() and not line.startswith("#")][:100]
    changes = []
    for index, bullet in enumerate(bullets, start=1):
        changes.append(
            {
                "id": f"chg.{harness_id}.{version}.{index:03d}",
                "kind": classify_change(bullet),
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
    prerelease = bool(item.get("prerelease"))
    channel = channel_for(version)
    if prerelease and channel == "stable":
        channel = "prerelease"
    return {
        "id": f"rel.{harness_id}.{version}",
        "harness_id": harness_id,
        "version": version,
        "channel": channel,
        "published_at": item.get("published_at") or item.get("created_at"),
        "date_precision": "second",
        "retrieved_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "source_id": source_id,
        "source_url": item.get("html_url"),
        "raw_snapshot_path": None,
        "raw_sha256": sha256_text(body),
        "title": item.get("name") or item.get("tag_name") or version,
        "notes_excerpt": bullets[0] if bullets else "No release-note body supplied.",
        "change_count": len(changes),
        "flags": {
            "security": any(change["security_relevant"] for change in changes),
            "breaking": any(change["breaking_or_deprecated"] for change in changes),
            "deprecation": any(change["kind"] == "deprecated" for change in changes),
        },
        "changes": changes,
        "assets": [
            {
                "name": asset.get("name"),
                "url": asset.get("browser_download_url"),
                "size": asset.get("size"),
                "content_type": asset.get("content_type"),
                "digest": asset.get("digest"),
            }
            for asset in item.get("assets", [])
        ],
        "provenance": {
            "authority": "official_primary",
            "ingestion": "github_releases_api",
            "immutable": True,
            "github_release_id": item.get("id"),
            "tag_commitish": item.get("target_commitish"),
        },
    }


def collect_github_releases(
    *,
    repo: str,
    harness_id: str,
    source_id: str,
    since_days: int = 120,
    include_prereleases: bool = True,
    max_pages: int = 20,
    raw_dir: Path | None = None,
    token: str | None = None,
) -> list[dict[str, Any]]:
    cutoff = datetime.now(timezone.utc) - timedelta(days=since_days)
    collected: list[dict[str, Any]] = []
    raw_items: list[dict[str, Any]] = []
    for page in range(1, max_pages + 1):
        query = urllib.parse.urlencode({"per_page": 100, "page": page})
        url = f"https://api.github.com/repos/{repo}/releases?{query}"
        payload, headers = _request_json(url, token=token)
        if not payload:
            break
        if not isinstance(payload, list):
            raise GitHubAPIError(f"Expected a list from {url}, got {type(payload).__name__}")
        raw_items.extend(payload)
        stop = False
        for item in payload:
            if item.get("draft"):
                continue
            if item.get("prerelease") and not include_prereleases:
                continue
            published = item.get("published_at") or item.get("created_at")
            if published:
                timestamp = datetime.fromisoformat(published.replace("Z", "+00:00"))
                if timestamp < cutoff:
                    stop = True
                    continue
            collected.append(_normalize_release(item, harness_id=harness_id, source_id=source_id))
        if stop or len(payload) < 100:
            break
        time.sleep(0.25)
    if raw_dir is not None:
        write_content_addressed_json_snapshot(
            raw_dir / harness_id,
            "github-releases",
            raw_items,
        )
    return collected
