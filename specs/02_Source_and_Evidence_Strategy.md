---
schema_version: 0.1
id: hci.source-strategy.v0.1
type: specification
artifact_kind: research_spec
title: Harness Capability Source and Evidence Strategy
project: Agentic Operating System
domain: harness_capability_intelligence
status: implemented_seed
owner: Nick Miethe
created_at: 2026-08-08
updated_at: 2026-08-08
system_of_record: GitHub
current_location: specs/02_Source_and_Evidence_Strategy.md
related_systems:
  - MeatyWiki
  - Governance and Evaluation
  - CCDash
source_context:
  - official changelogs
  - official documentation
  - official repositories
  - package registries
intended_use: Evidence hierarchy and curation policy for automated and human review.
next_action: Complete a source-by-source historical backfill audit.
review_cadence: monthly
confidentiality: personal
tags:
  - provenance
  - evidence
  - research
---

# Source and Evidence Strategy

## 1. Evidence hierarchy

| Tier | Source | Allowed use |
|---|---|---|
| 0 | Official versioned changelog, release object, signed package registry metadata | Release history, version lineage, immutable provenance |
| 1 | Official current documentation and API reference | Current capability verification and invocation contract |
| 2 | Official repository README/source and official lifecycle announcement | Implementation detail, transitions, deprecations, ownership |
| 3 | Official cross-vendor compatibility matrix | Corroboration and discovery; never sole negative evidence |
| 4 | Maintainer issue/discussion | Clarification or known limitation; requires explicit labeling |
| 5 | Community post, article, benchmark, or anecdote | Discovery and hypothesis only |

Only Tiers 0–3 are seeded as normal registry evidence. Tier 4 may support a limitation when first-party docs are silent. Tier 5 should create a research task, not a verified claim.

## 2. Why release notes are insufficient

Release notes commonly:

- Emphasize visible features over machine interfaces
- Omit previously shipped capabilities
- Combine CLI, IDE, desktop, web, SDK, and cloud surfaces
- Use product-specific terminology that does not compare cleanly
- Retroactively edit a mutable changelog file
- Omit precise dates
- Mention a fix without specifying whether the original capability remains limited

Therefore, every important capability should be corroborated against current documentation.

## 3. Why documentation is insufficient

Current docs commonly:

- Remove historical introduction points
- Describe latest behavior only
- Hide feature maturity or rollout timing
- Fail to distinguish exact version parity across SDKs and clients
- Change without a structured diff feed

Therefore, docs are snapshotted and hashed, while release events preserve lineage.

## 4. Positive and negative claims

### Positive claim

A current official document or release establishes that a capability exists for a specific surface and actor.

### Negative claim

`unavailable` requires explicit first-party evidence or a direct incompatibility test. Absence from documentation is not enough.

### Unknown claim

Use `unknown` when evidence is incomplete, contradictory, or stale.

## 5. Actor-reachability audit

For each claimed capability, answer independently:

1. Can a human invoke it?
2. Can the model inside the harness invoke it without human intervention?
3. Can an external agent invoke it through a supported interface?
4. Can it run in CI/scheduled automation?
5. Can an administrator configure or constrain it?
6. Is human mediation still required at an approval boundary?

Examples of invalid inference:

- “The desktop app supports parallel agents” does not prove an external orchestrator can create them.
- “The CLI can export JSON” does not prove it provides a stable streaming protocol.
- “The agent can use MCP tools” does not prove the harness can itself be exposed as an MCP server.
- “A hook can run a shell script” does not prove the model can discover or invoke that hook intentionally.

## 6. Source reconciliation

When sources disagree:

1. Prefer the source closest to the implementation and version.
2. Preserve both claims in the audit record.
3. Mark current access `unknown` or `experimental` if conflict remains.
4. Create a curator task.
5. Do not silently overwrite historical evidence.

When a newer document narrows a prior claim, update the current graph and retain the earlier release record.

## 7. Product lifecycle and lineage

A product transition is modeled as an event, not a rename. The predecessor remains queryable for:

- Historical workflows
- Enterprise channels that remain supported
- Compatibility analysis
- Migration guidance

Routing defaults may move to the successor based on lifecycle state and actor/entitlement context.

## 8. Historical coverage policy

Initial target: 120 days.

- Changelog-backed sources may include more history when dates are absent and section count is the only safe bound.
- GitHub/package sources use publication timestamps to enforce the window.
- Security, deprecation, and major lifecycle events should be retained indefinitely.
- A release count is not a completeness metric; coverage is reported separately for release history and current capabilities.

## 9. Review levels

| Review level | Trigger | Approval |
|---|---|---|
| Automatic | New package version with no semantic notes | Machine-approved ledger event |
| Curator | Feature/fix candidate from release text | Curator agent can propose patch |
| Human required | Security boundary, deprecation, product transition, actor-access reduction | Nick or designated owner |
| Runtime validated | Claim tested in an installed environment | CCDash evidence may raise confidence |

## 10. Freshness

A source can be fresh while a capability claim is stale. Track both:

- Source retrieval time
- Source content hash
- Capability verification time
- Version verified
- Current product version
- Documentation drift since verification

A routing consumer should surface a warning when the installed/current version exceeds the version verified for a critical capability.
