---
schema_version: 0.1
id: hci.web-app.v0.1
type: specification
artifact_kind: prd
title: Harness Matrix Web App Product Spec
project: Agentic Operating System
domain: harness_capability_intelligence
status: implemented_seed
owner: Nick Miethe
created_at: 2026-08-08
updated_at: 2026-08-08
system_of_record: GitHub
current_location: specs/05_Web_App_Product_Spec.md
related_systems:
  - Harness Capability Registry
  - Agentic Control Plane
  - CCDash
source_context:
  - generated registry bundle
intended_use: Product and UX contract for the comparison and audit interface.
next_action: Add curator review and environment inventory views.
review_cadence: monthly
confidentiality: personal
tags:
  - web-app
  - comparison-matrix
  - capability-intelligence
---

# Harness Matrix Web App PRD

## 1. Purpose

Make the registry understandable to humans without weakening its agent-readable precision.

## 2. Primary users

- Nick selecting or designing a workflow
- AOS agents resolving available execution surfaces
- Builders comparing harness integration options
- Curators reviewing releases and evidence
- Administrators evaluating governance surfaces

## 3. Core jobs

1. See what changed recently.
2. Compare products by canonical capability.
3. Switch actor perspective and expose access differences.
4. Inspect the evidence behind a capability claim.
5. Identify human mediation and unknowns.
6. Understand product lineage and lifecycle.
7. Export/open an agent guide or HarnessBOM.

## 4. Views

### Overview

- Registry health and freshness
- Product/source/capability/release counts
- Core harness cards
- Recent high-impact changes
- Coverage and lifecycle warnings

### Harnesses

- Searchable cards/table
- Family, lifecycle, current version, vendor
- Surfaces, routing strengths, and limitations
- Drill-down details and evidence

### Capability Matrix

- Rows: canonical capabilities
- Columns: selected harnesses
- Cell: actor access state
- Filters: actor, category, family, lifecycle, confidence
- Detail drawer: summary, invocation, version, limitations, evidence

### Actor Access

- One actor at a time
- Positive, mediated, unavailable, and unknown capability groupings
- Clear warning that access differs by actor

### Releases

- Search/filter by harness, date, kind, category, security, breaking, deprecation
- Expand release into normalized changes
- Show provenance and review status

### Sources

- Authority, purpose, collector, cadence, and tracked products
- Documentation drift state when available
- Direct official-source link

### Agent Guide

- Select a harness
- Show compact machine/runtime guidance
- Copy JSON
- Open generated Markdown/JSON artifact

## 5. Interaction principles

- Unknown is visually distinct from unavailable.
- No green checkmark without actor context.
- Human-only UI features are not presented as agent-native.
- Evidence is one click away.
- Dense comparison remains legible on wide screens; cards collapse responsively on mobile.
- The static app has no build step and can be hosted on GitHub Pages, object storage, LAN, or any basic web server.

## 6. Data contract

The app consumes `app/data/registry.bundle.js`, generated from canonical registry files. It performs no inference and should never mutate canonical data.

## 7. MVP success criteria

- A user can compare Claude Code, Codex, OpenCode, Hermes, and Antigravity for an external orchestrator in under one minute.
- A capability cell exposes its official evidence and limitations.
- Release and capability filters work without a backend.
- The UI remains usable at 390-pixel mobile width.
- Direct URL state preserves the active tab and core filters where practical.

## 8. Next-stage features

- Installed environment/version inventory
- Capability impact graph showing affected SkillBOMs
- Curator review queue and patch editor
- Source-drift semantic diff
- CCDash runtime success overlays
- Harness recommendation wizard
- Authentication/RBAC for enterprise use
- Signed evidence and approval records
