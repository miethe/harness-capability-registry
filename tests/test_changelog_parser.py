from hcr.collectors.markdown_changelog import parse_sections, section_to_release


SAMPLE = """
# Changelog

## 2.1.10 - 2026-08-08

### Added
- Added MCP server support for external orchestrators.
- Fixed a security permission bypass in the sandbox.

## [2.1.9] - 2026-08-07
- Deprecated the legacy command and added a migration path.
"""


def test_parses_versions_and_dates() -> None:
    sections = parse_sections(SAMPLE)
    assert [item.version for item in sections] == ["2.1.10", "2.1.9"]
    assert sections[0].published_at == "2026-08-08T00:00:00Z"


def test_normalizes_release_changes_and_flags() -> None:
    release = section_to_release(
        parse_sections(SAMPLE)[0],
        harness_id="test-harness",
        source_id="src.test",
        source_url="https://example.invalid/changelog",
        raw_path="raw/test/CHANGELOG.md",
        retrieved_at="2026-08-08T20:00:00Z",
    )
    assert release["change_count"] == 2
    assert release["flags"]["security"] is True
    assert "extensions.mcp_client" in release["changes"][0]["capability_refs"]
    assert release["changes"][0]["normalization"]["review_status"] == "unreviewed"


def test_release_window_bounds_dateless_changelogs() -> None:
    from datetime import datetime, timezone
    from hcr.collectors.markdown_changelog import filter_release_window

    releases = [
        {"version": f"1.0.{index}", "published_at": None}
        for index in range(10, 0, -1)
    ]
    retained = filter_release_window(
        releases,
        since_days=120,
        max_dateless_releases=3,
        now=datetime(2026, 8, 8, tzinfo=timezone.utc),
    )
    assert [item["version"] for item in retained] == ["1.0.10", "1.0.9", "1.0.8"]
