---
schema_version: 0.1
id: hci.data-model.v0.1
type: specification
artifact_kind: technical_spec
title: Harness Capability Registry Data Model and Schemas
project: Agentic Operating System
domain: harness_capability_intelligence
status: implemented_seed
owner: Nick Miethe
created_at: 2026-08-08
updated_at: 2026-08-08
system_of_record: GitHub
current_location: specs/01_Data_Model_and_Schemas.md
related_systems:
  - SkillMeat
  - Agentic Control Plane
  - Governance and Evaluation
source_context:
  - registry JSON files
  - JSON Schema 2020-12 definitions
intended_use: Contract for producers, consumers, agents, and future APIs.
next_action: Add compatibility/migration tests when schema_version advances.
review_cadence: quarterly
confidentiality: personal
tags:
  - json-schema
  - harnessbom
  - agent-readable
---

# Data Model and Schemas

## 1. Canonical entities

| Entity | File | Cardinality | Role |
|---|---|---:|---|
| Registry metadata | `registry/registry-meta.json` | 1 | Scope, quality policy, schema version |
| Source | `registry/sources.json` | many | Official evidence locations and collectors |
| Harness track | `registry/harnesses.json` | many | Product/SDK identity, lifecycle, routing metadata |
| Capability taxonomy | `registry/taxonomy.json` | many | Stable cross-product comparison concepts |
| Capability implementation | `registry/capabilities.json` | many | Product-specific, actor-aware current-state claim |
| Release event | `registry/releases.json` | many | Historical version and normalized change ledger |
| HarnessBOM | `registry/harnesses/<id>.json` | one per track | Materialized source, capability, and release bundle |
| Agent guide | `generated/agent-guides/<id>.json` | one per track | Compact runtime/routing view |

## 2. Identity rules

- Identifiers are stable, lowercase, and namespaced with dot-separated semantic components where practical.
- Product display names may change without changing the identifier.
- A true successor is represented by `predecessor`/`successor`, not by overwriting the old track.
- Release IDs use `rel.<harness-id>.<version>`.
- Change IDs use `chg.<harness-id>.<version>.<ordinal>`.
- Capability implementation IDs use `impl.<harness-id>.<capability-id>`.

## 3. Source

A source records both authority and collection mechanics.

```json
{
  "id": "src.claude-code.changelog",
  "name": "Claude Code raw changelog",
  "url": "https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md",
  "harness_ids": ["claude-code"],
  "source_type": "markdown_changelog",
  "purpose": "release_history",
  "authority": "official_primary",
  "official": true,
  "enabled": true,
  "collector": {
    "kind": "markdown_changelog",
    "local_seed_path": "raw/claude-code/CHANGELOG.md"
  },
  "refresh": {
    "cadence": "six_hourly",
    "historical_backfill_days": 120,
    "staleness_sla_hours": 24
  }
}
```

`purpose` is semantically important:

- `release_history`
- `capability_reference`
- `lifecycle_reference`
- `comparison_reference`
- `package_metadata`
- `discovery_only`

## 4. Harness track

A harness track can represent an interactive harness, a general agent harness, an agent SDK, or a provider SDK.

Key fields:

- Identity: `id`, `name`, `vendor`, `family`
- Lifecycle: `lifecycle`, `predecessor`, `successor`, `lifecycle_events`
- Freshness: `current_version`, `version_as_of`, `last_verified_at`
- Surfaces and authentication
- Source references
- Routing metadata: `recommended_when`, `avoid_when`, `control_plane_dimensions`

`control_plane_dimensions` are qualitative routing hints, not benchmark results.

## 5. Canonical capability

A taxonomy node is a stable question.

```json
{
  "id": "execution.headless",
  "name": "Headless/non-interactive execution",
  "category": "execution",
  "definition": "A supported one-shot or scripted interface without an interactive TUI.",
  "comparison_question": "Can an external agent or CI runner invoke the harness non-interactively?"
}
```

A vendor term is mapped to a taxonomy node only when the behavior is semantically comparable.

## 6. Capability implementation

```json
{
  "id": "impl.claude-code.execution.headless",
  "harness_id": "claude-code",
  "capability_id": "execution.headless",
  "status": "stable",
  "summary": "Claude Code supports non-interactive print mode with machine-readable output modes.",
  "actor_access": {
    "human_operator": "supported",
    "in_harness_agent": "unavailable",
    "external_orchestrator": "native",
    "ci_runner": "native",
    "administrator": "configurable"
  },
  "requires_human_mediation": false,
  "surfaces": ["terminal_headless"],
  "invocation": ["claude -p"],
  "minimum_version": null,
  "current_version_verified": "2.1.226",
  "limitations": [],
  "confidence": "verified_official",
  "verified_at": "2026-08-08T20:00:00Z",
  "evidence": [
    {
      "source_id": "src.claude-code.docs.headless",
      "url": "https://docs.anthropic.com/en/docs/claude-code/headless",
      "claim": "Supported programmatic mode and output formats.",
      "version": null,
      "verified_at": "2026-08-08T20:00:00Z"
    }
  ]
}
```

## 7. Release event

The release record separates source provenance from normalized change interpretation.

Important fields:

- `published_at` may be null when upstream changelogs omit dates.
- `date_precision` prevents false precision.
- `raw_sha256` detects upstream edits.
- `provenance.immutable` indicates whether the source is an immutable release object or a mutable branch file.
- `changes[].normalization.review_status` distinguishes raw candidate extraction from approved interpretation.

## 8. HarnessBOM

A HarnessBOM is a materialized read model:

```json
{
  "harness": {},
  "capabilities": [],
  "releases": [],
  "sources": []
}
```

It intentionally duplicates canonical registry data for portability and agent context loading. Canonical edits occur in the top-level registry files, then materialization regenerates HarnessBOMs.

## 9. Agent guide

The agent guide removes most historical detail and groups positive capability access by actor. It also includes:

- Freshness warning
- Human-mediation list
- Low-confidence/unknown list
- Routing hints
- Evidence links

Use the guide for runtime routing. Use the HarnessBOM for planning, auditing, or implementation design.

## 10. Schema evolution

- Schema versions use semantic intent, beginning at `0.1`.
- Additive optional fields may remain within a minor schema version.
- Renames, semantic changes, and enum removals require a migration.
- Generated artifacts include their schema version.
- Consumers must reject a future major version they do not understand.
- Migration scripts belong under `hcr/migrations/` once needed.

## 11. Validation

The validator uses JSON Schema plus cross-file invariants. A valid document can still be semantically wrong, so evidence review remains mandatory for capability promotion.
