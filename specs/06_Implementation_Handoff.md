---
schema_version: 0.1
id: hci.implementation-handoff.v0.1
type: specification
artifact_kind: implementation_handoff
title: Harness Capability Registry Implementation Handoff
project: Agentic Operating System
domain: harness_capability_intelligence
status: ready_for_integration
owner: Nick Miethe
created_at: 2026-08-08
updated_at: 2026-08-08
system_of_record: GitHub
current_location: specs/06_Implementation_Handoff.md
related_systems:
  - Agentic Control Plane
  - SkillMeat
  - CCDash
source_context:
  - initial HCR source tree
intended_use: Builder handoff for integration, hardening, and deployment.
next_action: Import this directory into a dedicated repository and run a networked update.
review_cadence: per_release
confidentiality: personal
tags:
  - implementation
  - handoff
  - roadmap
---

# Implementation Handoff

## 1. Current implementation

- Python 3.11+ package with no mandatory runtime dependencies
- Optional `pytest` and `jsonschema` development dependencies
- Source adapters for GitHub, Markdown, PyPI, npm, and generic HTTP snapshots
- Deterministic release-note normalization
- Canonical JSON registry and JSON Schema definitions
- Materialized HarnessBOMs, agent guides, reports, and web bundle
- Static no-build web app
- Scheduled GitHub Actions design
- Offline tests and validation

## 2. Bootstrap

```bash
git init
python -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install -e '.[dev]'
python scripts/build_seed.py
python -m hcr generate
python -m hcr validate
pytest
python -m hcr serve
```

## 3. Environment variables

| Variable | Required | Use |
|---|---:|---|
| `GITHUB_TOKEN` | Recommended in CI | Higher API limits and private-source extension |

Future enterprise connectors should use source-specific secret names and never store credentials in `sources.json`.

## 4. Extension points

### New harness

1. Add official sources to `scripts/build_seed.py`/`registry/sources.json`.
2. Add a harness track and lifecycle state.
3. Map reviewed current capabilities to the taxonomy.
4. Add at least one release-history source.
5. Run generation and validation.
6. Add tests for nonstandard release syntax.

### New collector

Implement a function returning normalized release records, add a declarative `collector.kind`, and wire it into `cmd_collect`.

### New capability

Add one canonical taxonomy node only when existing nodes cannot represent the behavior. Then map implementations product by product; do not assume absence means unavailable.

## 5. Validation gates

A pull request must pass:

```bash
python -m hcr validate
pytest
```

Additional production gates:

- No unresolved critical source failures
- No unreviewed security/deprecation changes
- No verified capability without official evidence
- No product transition without control-plane impact review
- No schema breaking change without migration notes

## 6. Deployment options

### GitHub Pages

Publish `app/` after generation. Suitable for public or internal-static use where source sensitivity is low.

### LAN/self-hosted

Run `python -m hcr serve --bind 0.0.0.0 --port 8765` behind the existing reverse proxy. Add authentication before exposing work-sensitive overlays.

### Control-plane service

Serve `generated/registry.bundle.json` through an API gateway or load it directly into the control-plane process. The static bundle is intentionally backend-neutral.

## 7. Roadmap

### Phase 0 — Seed complete

- Initial sources, schema, historical corpus, guides, UI, and automation skeleton

### Phase 1 — Evidence hardening

- Full networked backfill
- ETag caching
- Semantic documentation diff
- Review queue and signed approvals
- Coverage targets per track

### Phase 2 — AOS integration

- SkillMeat HarnessBOM artifact type
- Control-plane resolver API
- Intent/I-BOM requirement schema
- CCDash runtime evidence events
- MeatyWiki decision/source-note templates

### Phase 3 — Environment-aware routing

- Installed version inventory
- Authentication/entitlement inventory
- Capability self-tests
- Workflow impact analysis
- Automatic adapter/version pin proposals

### Phase 4 — Enterprise productization

- RBAC and tenant separation
- Approved source policies
- Audit export
- Vendor support/SLA metadata
- Signed registry releases
- Fleet and workspace policy integration

## 8. Known limits

- The initial corpus is not yet a claim of exhaustive history for every GitHub-release-only product.
- Documentation drift detection is hash-based in the seed.
- Heuristic normalization is useful for triage but not sufficient for critical semantic claims.
- Qualitative routing dimensions are architecture guidance, not measured benchmark results.
- The app is read-only and has no curator workflow yet.
