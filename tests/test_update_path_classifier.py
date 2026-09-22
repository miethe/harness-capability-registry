from scripts.classify_update_paths import unsafe_paths


def test_refresh_outputs_are_data_only() -> None:
    assert unsafe_paths(
        [
            "registry/harnesses.json",
            "raw/codex/CHANGELOG.md",
            "generated/agent-guides/openai-codex.json",
            "generated/reports/coverage.md",
            "generated/validation-report.json",
            "generated/source-drift-report.json",
        ]
    ) == []


def test_code_workflow_and_unlisted_generated_files_need_human_review() -> None:
    assert unsafe_paths(
        ["scripts/update.py", ".github/workflows/update-registry.yml", "generated/registry.bundle.json"]
    ) == ["scripts/update.py", ".github/workflows/update-registry.yml", "generated/registry.bundle.json"]
