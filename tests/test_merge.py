from copy import deepcopy

from hcr.cli import _merge_releases


def release(retrieved_at: str) -> dict:
    return {
        "id": "rel.test.1.0.0",
        "harness_id": "test",
        "version": "1.0.0",
        "published_at": "2026-08-08T00:00:00Z",
        "retrieved_at": retrieved_at,
        "source_id": "src.test",
        "raw_sha256": "same-content",
        "changes": [],
    }


def test_same_upstream_payload_preserves_existing_record() -> None:
    existing = release("2026-08-08T12:00:00Z")
    incoming = release("2026-08-08T18:00:00Z")
    merged = _merge_releases([deepcopy(existing)], [incoming])
    assert merged == [existing]
