from __future__ import annotations

from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from hcr.io import read_json, write_json

ALLOWED_ACCESS = {"native", "supported", "configurable", "experimental", "mediated", "unavailable", "unknown", "deprecated"}
ALLOWED_CONFIDENCE = {"verified_official", "inferred_high", "inferred_low", "unknown"}
ALLOWED_LIFECYCLE = {"active", "maintenance", "transitioning", "legacy", "archived", "monitoring_only"}
ALLOWED_INVOCATION_STATUS = {"resolved", "not_applicable", "unreviewed"}


def _duplicates(values: list[str]) -> list[str]:
    return [value for value, count in Counter(values).items() if count > 1]


def _validate_json_schemas(root: Path, errors: list[str], warnings: list[str]) -> None:
    try:
        from jsonschema import Draft202012Validator
        from referencing import Registry, Resource
    except ImportError:
        warnings.append("jsonschema/referencing is not installed; structural JSON Schema checks were skipped")
        return

    schema_dir = root / "schemas"
    common_path = schema_dir / "common.schema.json"
    if not common_path.exists():
        warnings.append("schemas/common.schema.json is missing; structural checks were skipped")
        return
    common = read_json(common_path)
    common_resource = Resource.from_contents(common)
    schema_registry = Registry().with_resource(common["$id"], common_resource)
    schema_registry = schema_registry.with_resource(common_path.as_uri(), common_resource)
    targets = {
        "registry-meta.schema.json": root / "registry" / "registry-meta.json",
        "sources.schema.json": root / "registry" / "sources.json",
        "harnesses.schema.json": root / "registry" / "harnesses.json",
        "taxonomy.schema.json": root / "registry" / "taxonomy.json",
        "capabilities.schema.json": root / "registry" / "capabilities.json",
        "releases.schema.json": root / "registry" / "releases.json",
    }
    for schema_name, data_path in targets.items():
        schema_path = schema_dir / schema_name
        if not schema_path.exists():
            warnings.append(f"Schema is missing: {schema_name}")
            continue
        schema = read_json(schema_path)
        validator = Draft202012Validator(schema, registry=schema_registry)
        schema_errors = sorted(validator.iter_errors(read_json(data_path)), key=lambda item: list(item.absolute_path))
        for issue in schema_errors[:100]:
            location = "/".join(str(part) for part in issue.absolute_path) or "$"
            errors.append(f"Schema {schema_name} at {location}: {issue.message}")
        if len(schema_errors) > 100:
            errors.append(f"Schema {schema_name}: {len(schema_errors) - 100} additional errors suppressed")


def validate_registry(root: Path) -> dict[str, Any]:
    registry = root / "registry"
    sources: list[dict[str, Any]] = read_json(registry / "sources.json")
    harnesses: list[dict[str, Any]] = read_json(registry / "harnesses.json")
    taxonomy: list[dict[str, Any]] = read_json(registry / "taxonomy.json")
    capabilities: list[dict[str, Any]] = read_json(registry / "capabilities.json")
    releases: list[dict[str, Any]] = read_json(registry / "releases.json")

    errors: list[str] = []
    warnings: list[str] = []
    source_ids = {item["id"] for item in sources}
    harness_ids = {item["id"] for item in harnesses}
    taxonomy_ids = {item["id"] for item in taxonomy}

    for label, values in {
        "source": [item["id"] for item in sources],
        "harness": [item["id"] for item in harnesses],
        "taxonomy": [item["id"] for item in taxonomy],
        "capability implementation": [item["id"] for item in capabilities],
        "release": [item["id"] for item in releases],
    }.items():
        for duplicate in _duplicates(values):
            errors.append(f"Duplicate {label} id: {duplicate}")

    for source in sources:
        parsed = urlparse(source["url"])
        if parsed.scheme not in {"https", "http"} or not parsed.netloc:
            errors.append(f"Source {source['id']} has invalid URL: {source['url']}")
        if source.get("authority") == "official_primary" and source.get("official") is not True:
            errors.append(f"Source {source['id']} is official_primary but official is not true")
        for harness_id in source.get("harness_ids", []):
            if harness_id not in harness_ids:
                errors.append(f"Source {source['id']} references unknown harness {harness_id}")

    for harness in harnesses:
        if harness.get("lifecycle") not in ALLOWED_LIFECYCLE:
            errors.append(f"Harness {harness['id']} has invalid lifecycle {harness.get('lifecycle')}")
        for source_id in harness.get("source_ids", []):
            if source_id not in source_ids:
                errors.append(f"Harness {harness['id']} references unknown source {source_id}")
        successor = harness.get("successor")
        predecessor = harness.get("predecessor")
        if successor and successor not in harness_ids:
            errors.append(f"Harness {harness['id']} references unknown successor {successor}")
        if predecessor and predecessor not in harness_ids:
            errors.append(f"Harness {harness['id']} references unknown predecessor {predecessor}")

    for capability in capabilities:
        if capability.get("harness_id") not in harness_ids:
            errors.append(f"Capability {capability['id']} references unknown harness {capability.get('harness_id')}")
        if capability.get("capability_id") not in taxonomy_ids:
            errors.append(f"Capability {capability['id']} references unknown taxonomy id {capability.get('capability_id')}")
        if capability.get("confidence") not in ALLOWED_CONFIDENCE:
            errors.append(f"Capability {capability['id']} has invalid confidence {capability.get('confidence')}")
        for actor, access in capability.get("actor_access", {}).items():
            if access not in ALLOWED_ACCESS:
                errors.append(f"Capability {capability['id']} has invalid access {actor}={access}")
        if capability.get("confidence") == "verified_official" and not capability.get("evidence"):
            errors.append(f"Verified capability {capability['id']} has no evidence")
        for evidence in capability.get("evidence", []):
            if evidence.get("source_id") not in source_ids:
                errors.append(f"Capability {capability['id']} evidence references unknown source {evidence.get('source_id')}")
        invocation = capability.get("invocation") or []
        invocation_status = capability.get("invocation_status")
        na_reason = capability.get("invocation_na_reason")
        if invocation_status not in ALLOWED_INVOCATION_STATUS:
            errors.append(f"Capability {capability['id']} has invalid invocation_status {invocation_status}")
        elif invocation_status == "resolved" and not invocation:
            errors.append(f"Capability {capability['id']} is invocation_status=resolved but invocation is empty")
        elif invocation_status in ("not_applicable", "unreviewed") and invocation:
            errors.append(f"Capability {capability['id']} is invocation_status={invocation_status} but invocation is non-empty")
        if invocation_status == "not_applicable" and not na_reason:
            errors.append(f"Capability {capability['id']} is invocation_status=not_applicable but invocation_na_reason is empty")
        if invocation_status != "not_applicable" and na_reason:
            errors.append(f"Capability {capability['id']} has invocation_na_reason set but invocation_status is {invocation_status}")

    for release in releases:
        if release.get("harness_id") not in harness_ids:
            errors.append(f"Release {release['id']} references unknown harness {release.get('harness_id')}")
        if release.get("source_id") not in source_ids:
            errors.append(f"Release {release['id']} references unknown source {release.get('source_id')}")
        if release.get("change_count") != len(release.get("changes", [])):
            warnings.append(f"Release {release['id']} change_count does not match changes length")

    _validate_json_schemas(root, errors, warnings)

    meta = read_json(registry / "registry-meta.json")
    report = {
        "schema_version": "0.1",
        "validated_at": meta.get("updated_at") or datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "valid": not errors,
        "counts": {
            "sources": len(sources),
            "harnesses": len(harnesses),
            "taxonomy": len(taxonomy),
            "capabilities": len(capabilities),
            "releases": len(releases),
            "errors": len(errors),
            "warnings": len(warnings),
        },
        "errors": errors,
        "warnings": warnings,
    }
    write_json(root / "generated" / "validation-report.json", report)
    return report
