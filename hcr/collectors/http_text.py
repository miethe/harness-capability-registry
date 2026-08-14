from __future__ import annotations

import gzip
import os
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from hcr.io import sha256_text, write_json, write_text


class HTTPCollectorError(RuntimeError):
    pass


def collect_text_snapshot(
    *,
    url: str,
    source_id: str,
    output_dir: Path,
    token_env: str | None = None,
) -> dict[str, Any]:
    headers = {"User-Agent": "harness-capability-registry/0.1", "Accept-Encoding": "gzip"}
    if token_env and os.getenv(token_env):
        headers["Authorization"] = f"Bearer {os.environ[token_env]}"
    request = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            body = response.read()
            if response.headers.get("Content-Encoding") == "gzip":
                body = gzip.decompress(body)
            charset = response.headers.get_content_charset() or "utf-8"
            text = body.decode(charset, errors="replace")
            headers_out = {key.lower(): value for key, value in response.headers.items()}
    except (urllib.error.HTTPError, urllib.error.URLError) as exc:
        raise HTTPCollectorError(f"Unable to snapshot {url}: {exc}") from exc

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    safe_id = source_id.replace("/", "_")
    snapshot_path = output_dir / safe_id / f"{stamp}.txt"
    write_text(snapshot_path, text)
    record = {
        "source_id": source_id,
        "url": url,
        "retrieved_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "sha256": sha256_text(text),
        "content_type": headers_out.get("content-type"),
        "etag": headers_out.get("etag"),
        "last_modified": headers_out.get("last-modified"),
        "snapshot_path": str(snapshot_path),
        "bytes": len(body),
    }
    write_json(snapshot_path.with_suffix(".meta.json"), record)
    return record
