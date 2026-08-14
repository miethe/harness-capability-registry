import hashlib
import json
from pathlib import Path

from hcr.generators.bundle import build_bundle


ROOT = Path(__file__).resolve().parents[1]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_generated_guide_tracks_materialized_current_version() -> None:
    bundle = build_bundle(ROOT)
    harness = next(item for item in bundle["harnesses"] if item["id"] == "claude-code")
    guide = next(item for item in bundle["agent_guides"] if item["harness"]["id"] == "claude-code")
    assert guide["harness"]["current_version"] == harness["current_version"]
    assert guide["freshness"]["latest_release_in_registry"] == harness["current_version"]


def test_generation_is_idempotent_for_unchanged_registry() -> None:
    targets = [
        ROOT / "generated" / "registry.bundle.json",
        ROOT / "generated" / "Harness_Matrix_Standalone.html",
        ROOT / "generated" / "agent-guides" / "claude-code.json",
    ]
    build_bundle(ROOT)
    first = [digest(path) for path in targets]
    build_bundle(ROOT)
    assert [digest(path) for path in targets] == first


def test_standalone_app_contains_embedded_registry_and_application() -> None:
    path = ROOT / "generated" / "Harness_Matrix_Standalone.html"
    text = path.read_text(encoding="utf-8")
    assert "window.HCR_DATA" in text
    assert "Harness Matrix" in text
    assert 'src="app.js"' not in text
    assert 'href="styles.css"' not in text


def test_bundle_is_valid_json_and_has_actor_aware_matrix() -> None:
    bundle = json.loads((ROOT / "generated" / "registry.bundle.json").read_text(encoding="utf-8"))
    assert bundle["matrix"]
    first_implementation = next(iter(bundle["matrix"][0]["implementations"].values()))
    assert "external_orchestrator" in first_implementation["actor_access"]
