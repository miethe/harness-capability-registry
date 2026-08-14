from pathlib import Path

from hcr.io import read_json
from hcr.validators.core import validate_registry


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_ACTORS = {
    "human_operator",
    "in_harness_agent",
    "external_orchestrator",
    "ci_runner",
    "administrator",
}


def test_registry_validates_without_errors() -> None:
    report = validate_registry(ROOT)
    assert report["valid"] is True
    assert report["counts"]["errors"] == 0
    assert report["counts"]["harnesses"] >= 20
    assert report["counts"]["releases"] >= 490


def test_every_capability_has_explicit_actor_assessments() -> None:
    capabilities = read_json(ROOT / "registry" / "capabilities.json")
    for capability in capabilities:
        assert set(capability["actor_access"]) == EXPECTED_ACTORS, capability["id"]


def test_ui_only_capability_does_not_imply_agent_access() -> None:
    capabilities = read_json(ROOT / "registry" / "capabilities.json")
    terminal = next(item for item in capabilities if item["id"] == "impl.claude-code.interaction.terminal")
    assert terminal["actor_access"]["human_operator"] == "native"
    assert terminal["actor_access"]["in_harness_agent"] == "unavailable"
    assert terminal["actor_access"]["external_orchestrator"] == "unavailable"
