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

## Registry-tree materialized outputs — contract vs. convenience

`hcr generate` writes three per-harness split families under `registry/`, all derived from
`registry/{capabilities,releases}.json` (`hcr/generators/bundle.py`). They are not equivalent —
only one of them is a documented data-model artifact:

| Path | Status | Basis |
|---|---|---|
| `registry/harnesses/<id>.json` | **Published contract — the HarnessBOM.** | Named in `specs/01_Data_Model_and_Schemas.md` §Data Model and `README.md`'s materialized-outputs list. Untracking or reshaping it is a contract change for anything consuming HarnessBOMs. |
| `registry/releases/<id>.json` | **Regenerable convenience, not a documented artifact.** | Not named in any spec, README, or this guide. A per-harness slice of `registry/releases.json`, kept only for cheap per-track lookups. |
| `registry/capabilities/<id>.json` | **Regenerable convenience, not a documented artifact.** | Same shape as the releases split; a per-harness slice of `registry/capabilities.json`. |

All three regenerate deterministically from the canonical registry files, so none of them carries
data that would be lost by deleting and re-running `hcr generate` — the distinction above is about
*whether an external consumer's contract names the path*, not about whether the file is safe to
regenerate. See `node_01M043N0F6H8TEM2288RNRFSAB` for the measurement this table settles.

### `registry/releases.json` growth — measured distance to GitHub's 50MB line

Per-release `assets` download listings (URLs/sizes/content-types nothing reads — see the table
above) were removed 2026-08-25, both from the collectors going forward and from all 1,989
historical records; the field is no longer in `schemas/releases.schema.json`. Sizes measured with
`git cat-file -s <sha>:registry/releases.json`, with a second column showing what each commit's
size *would have been* had the `assets` field never existed (`json.dumps` after stripping it):

| Commit | Date | Tracked size (as committed) | Size with `assets` stripped |
|---|---|---:|---:|
| `a56c0b3` (pre-networked-collection seed) | 2026-08-14 | 3.06 MB | 2.32 MB |
| `d4c578c` (first networked collection — historical backfill) | 2026-08-15 | 41.0 MB | 17.1 MB |
| `88e2480` (steady-state six-hourly collection) | 2026-08-18 | 41.8 MB | 17.6 MB |
| `b113592` (steady-state six-hourly collection) | 2026-08-24 | 44.9 MB | 18.9 MB |
| *(this fix, all 1,989 records stripped in place)* | 2026-08-25 | — | **25 MB on disk** (pretty-printed; ~18.9 MB compact) |

The one-time historical backfill (08-14 → 08-15) is not representative of ongoing growth. The
**steady-state** rate — 08-15 → 08-24, post-backfill, `assets`-stripped — is `(18.9 − 17.1) MB /
9 days ≈ 0.2 MB/day`. At that rate, the ~25 MB gap between the current tracked size and GitHub's
50 MB warning line is **~120 days** of headroom, not the "already within one comparable jump"
distance the pre-fix trajectory was on track for (one collection cycle added ~38 MB before this
fix). Re-measure this table if the collected-track allowlist changes materially (more harnesses,
longer `historical_backfill_days`), since either widens the per-cycle delta this projection assumes.

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
