# Harness Capability Registry — Delivery Guide

## Recommended first openings

> Two rows below point at untracked build outputs — `generated/Harness_Matrix_Standalone.html` and
> `generated/registry.bundle.json`. Run `make generate` before opening either in a fresh clone; the
> `registry/` rows are tracked and need no build step.

| Need | Artifact |
|---|---|
| Browse and compare products | `generated/Harness_Matrix_Standalone.html` |
| Understand the architecture | `specs/00_Harness_Capability_Intelligence_Spec.md` |
| Integrate into the AOS | `specs/04_AOS_Integration.md` |
| Hand to a builder | `specs/06_Implementation_Handoff.md` |
| Run a comprehensive evidence audit | `prompts/DEEP_RESEARCH_PROMPT.md` |
| Give an agent one product's capabilities | `generated/agent-guides/<harness-id>.json` |
| Query the complete materialized registry | `generated/registry.bundle.json` |
| Inspect canonical source definitions | `registry/sources.json` |
| Inspect historical releases | `registry/releases.json` |
| Inspect the normalized capability graph | `registry/capabilities.json` |

## What is implemented

- Twenty separately versioned product and SDK tracks
- Sixty-nine official evidence sources
- Thirty-eight canonical comparison capabilities
- Actor-specific access modeling for human, in-harness agent, external orchestrator, CI runner, and administrator
- Append-oriented release history with source-faithful notes and normalized changes
- Product lineage, predecessor, successor, deprecation, and lifecycle state
- JSON Schemas and cross-registry invariant validation
- Per-product HarnessBOMs and compact agent-routing guides
- Static comparison application and self-contained standalone build
- GitHub, Markdown changelog, PyPI, npm, and documentation-drift collection paths
- Six-hour GitHub Actions refresh with pull-request gating
- Deterministic offline generation and an automated test suite

## Fastest local path

```bash
python -m pip install -e '.[dev]'
python -m hcr validate
python -m hcr serve --port 8765
```

Then open `http://127.0.0.1:8765`.

## First production integration

1. Import this directory into its own Git repository.
2. Run the workflow once with network access and a GitHub token to backfill release-only tracks and create documentation snapshots.
3. Review the first generated delta rather than automatically promoting semantic capability changes.
4. Register `HarnessBOM` as a SkillMeat artifact type.
5. Add a control-plane adapter that resolves task requirements against actor access, version scope, environment, and risk boundaries.
6. Emit selected-harness, rejected-harness, fallback, and observed-capability events to CCDash.

## Interpretation guardrails

- Missing evidence is `unknown`, not `unavailable`.
- A feature exposed in a human UI is not automatically callable by an agent.
- A release-note item is evidence of a change event, not by itself proof of the complete current behavior.
- Provider SDKs, agent SDKs, and end-user harnesses are separate tracks even when one embeds another.
- Product lineage is explicit; successor products do not erase predecessor history.
- The current seed is broad but does not claim exhaustive history for every GitHub-release-only product before the first networked backfill.
