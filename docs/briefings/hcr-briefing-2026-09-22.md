# HCR Briefing — Harness Capability Registry
**Date:** 2026-09-22
**Purpose:** Context document for external ideation on a rich capability viewer
**Repo:** [miethe/harness-capability-registry](https://github.com/miethe/harness-capability-registry)

---

## 1. What HCR Is and Why It Exists

The **Harness Capability Registry (HCR)** is an evidence-backed release ledger and actor-aware capability graph for AI coding harnesses and SDKs. It answers one question that any automated routing system needs to answer without guessing: *"which tool can do X, for which actor (human, agent, CI runner…), on which version, with what evidence?"* Without it, an orchestration system must either hard-code capability assumptions in prose or re-derive them at runtime from memory — both of which drift silently the moment a product ships a breaking change. HCR replaces that guesswork with structured, versioned, evidence-linked claims. It tracks **20 products** — five core agentic harnesses, five secondary/historical harnesses, six agent SDKs, and four provider SDKs — and keeps two synchronized views of each: an immutable release-event ledger (what changed in each version) and a current capability graph (what each product can do *right now*, for each actor type, with citations).

---

## 2. How HCR Works Today

### Sources

HCR ingests **71 official sources** declared in `registry/sources.json`. For each tracked harness these typically include the product changelog, GitHub release feed, and key documentation pages (overview, headless/non-interactive execution, SDK references, CLI references, hooks/settings docs). A single harness like Claude Code has ten source records; a narrow SDK may have two. Source IDs follow the pattern `src.<harness-id>.<artifact>` (e.g. `src.claude-code.docs.headless`).

Raw collected responses land in `raw/` as content-addressed snapshots. This separation makes the downstream pipeline deterministic: `hcr generate` produces byte-identical output from unchanged inputs with no network access required.

### Refresh Pipeline — `update-registry.yml`

The GitHub Actions workflow (`.github/workflows/update-registry.yml`) fires on a **cron schedule every 6 hours at minute :17** (`17 */6 * * *`) and on manual dispatch. One job runs on `ubuntu-latest`:

1. **Check out** the repo at full depth.
2. **Install tooling** (`python -m pip install -e '.[dev]'`).
3. **Run `hcr update`** — `python -m hcr update --since-days 120 --max-pages 20 --snapshot-docs` — which:
   - Collects new releases from all 71 sources (GitHub release feeds, package registries, changelogs).
   - Snapshots current product documentation pages for drift detection.
   - Runs the heuristic normalizer to extract capability *candidates* from new release notes.
   - Updates `registry/releases.json` (append-only ledger, deduped by release id).
   - Regenerates `generated/agent-guides/`, coverage report, validation and drift reports.
4. **Run the test suite** (`python -m pytest` + `node --check app/app.js`).
5. **Stage curated paths only**: `registry/`, `raw/`, `generated/agent-guides/`, `generated/reports/coverage.md`, `generated/validation-report.json`, `generated/source-drift-report.json`. Large app bundles (`generated/registry.bundle.json`, `generated/Harness_Matrix_Standalone.html`, `app/data/`) are untracked build artifacts, regenerated locally via `make generate`.
6. **Open or refresh a single rolling PR** targeting `main` on branch `automation/harness-capability-registry-update`. The step checks for an existing open PR and edits it rather than creating a duplicate.

### Generated Outputs

| Path | Description |
|---|---|
| `generated/agent-guides/<id>.json` | Compact, agent-consumable routing guide per harness (capabilities keyed by actor) |
| `generated/agent-guides/<id>.md` | Human-readable version of the same guide |
| `generated/reports/coverage.md` | Per-harness counts: verified capabilities, candidates, unknowns, releases |
| `generated/reports/invocation-coverage.md` | Which capabilities have resolved invocation tokens |
| `generated/validation-report.json` | JSON Schema and cross-reference validation results |
| `generated/source-drift-report.json` | Doc page drift detected in the latest snapshot run |
| `registry/harnesses/<id>.json` | Full HarnessBOM per product (richer than the agent guide) |

The **Harness Matrix** (`generated/Harness_Matrix_Standalone.html`) is a browser UI with embedded data — a complete cross-harness comparison table. It is a local build artifact (`make generate`) and is not committed to git.

### Downstream Projection (AMD/Orchestration side)

A generator script in the Agentic OS repo (`scripts/generate_harness_capabilities.py`) reads HCR's `generated/agent-guides/<id>.json` files **via a pinned git ref** (`git show origin/main:<path>`) — never from a local working tree — and projects them into:

- `docs/agentic-operator/harness-capabilities.yaml` — a YAML projection of all actor-capability-access triples, with full provenance (which HCR commit it was generated from, how far behind the local clone was).
- `docs/agentic-operator/HARNESS-CAPABILITIES.md` — a generated human-readable version.

A staleness gate (`scripts/check_harness_capability_staleness.py`, configured by `scripts/harness-capability-staleness.yaml`) enforces the projection does not go stale: it compares the projection's *recorded HCR commit* against the real `origin/main` today and fails if the lag exceeds **10 commits** or **14 days**. It checks the *instance* (what the projection actually read), not the *mechanism* (whether the generator ran recently). A fourth script (`scripts/report_unused_capabilities.py`) cross-references the projection against hand-authored usage predicates to surface capabilities tracked in HCR but not yet referenced in orchestration logic.

A pre-commit hook in the orchestration repo enforces that any commit touching live markdown capability claims or the projection YAML must regenerate and re-validate the projection before landing.

---

## 3. Measured Current State

The refresh pipeline **runs successfully** — the last 20 cron runs all completed with `success`, averaging approximately 2.5 minutes each. The most recent run completed at **2026-09-22T16:57:12Z**.

However, **running ≠ delivered.** PR #10 (`automation/harness-capability-registry-update`) has been **open and unmerged since 2026-09-18T20:56:47Z** — approximately 4 days as of this briefing. The workflow updates the same rolling branch and PR on each run (most recently at 2026-09-22T16:59:56Z), but those updates only land on `main` when a human merges the PR. As a result:

- `main` — the only ref the downstream projection reads — is at commit `88455c7` from 2026-09-18.
- The downstream projection was last generated on **2026-09-20** from that same stale ref.
- The cron is healthy; the delivery gap is a **merge cadence gap**, not a CI gap.

**"Ran ≠ delivered."** This is the central operational gap today.

---

## 4. Data: Schema, Entities, Vocabulary

### Entity Counts

| Entity | File | Count |
|---|---|---|
| Harnesses | `registry/harnesses.json` | **20** |
| Capability taxonomy nodes | `registry/taxonomy.json` | **39** |
| Capability implementations | `registry/capabilities.json` | **237** |
| Release events | `registry/releases.json` | **2,435** |
| Sources | `registry/sources.json` | **71** |

### Harness Record (key fields)

| Field | Type | Meaning |
|---|---|---|
| `id` | string | Stable slug, e.g. `claude-code` |
| `name` | string | Display name |
| `vendor` | string | Product vendor |
| `family` | enum | `agentic_harness` / `general_agent_harness` / `agent_sdk` / `provider_sdk` |
| `lifecycle` | enum | `active` / `maintenance` / `transitioning` / `legacy` / `archived` / `monitoring_only` |
| `maturity` | string | e.g. `stable`, `beta` |
| `tracking_priority` | enum | `core` / `secondary` / `watch` / `historical` / `discovery` / `provider_sdk` |
| `current_version` | string\|null | Latest known version, e.g. `2.1.276` |
| `version_as_of` | date | When `current_version` was recorded |
| `last_verified_at` | timestamp | Last time any capability was verified |
| `predecessor` / `successor` | string\|null | Product lineage (e.g. Gemini CLI → Antigravity CLI) |
| `surfaces` | string[] | Where the harness is reachable: `terminal`, `IDE`, `web`, `SDK`, etc. |
| `auth_modes` | string[] | Auth mechanisms, e.g. `Anthropic API key`, `Amazon Bedrock` |
| `control_plane_dimensions` | object | Scored dimensions: `local_execution`, `remote_execution`, `multi_agent`, `structured_automation`, `provider_portability`, `enterprise_controls` — each `strong` / `moderate` / `limited` |
| `recommended_when` / `avoid_when` | string[] | Routing guidance bullets |

### Capability Implementation Record (key fields)

| Field | Type | Meaning |
|---|---|---|
| `id` | string | `impl.<harness-id>.<capability-id>` |
| `harness_id` | string | Links to a harness |
| `capability_id` | string | Links to a taxonomy node |
| `status` | string | `stable` / `experimental` / `candidate` / `deprecated` |
| `summary` | string | One-line description |
| `actor_access` | object | Per-actor access level (see vocabulary below) |
| `requires_human_mediation` | boolean | True if a human must be in the loop |
| `surfaces` | string[] | Surfaces where the capability is available |
| `invocation` | string[] | Command/token/flag, e.g. `claude -p`, `PreToolUse` |
| `minimum_version` | string\|null | Earliest version where this is available |
| `current_version_verified` | string\|null | Version where this was last confirmed |
| `confidence` | enum | `verified_official` / `inferred_high` / `inferred_low` / `unknown` |
| `verified_at` | timestamp | When evidence was last checked |
| `evidence` | array | Source citations: `source_id`, `url`, `claim`, `version`, `verified_at` |
| `invocation_status` | enum | `resolved` / `not_applicable` / `unreviewed` |

### Actor-Access Vocabulary

**5 actors:**
- `human_operator` — a person running the harness interactively
- `in_harness_agent` — an agent running *inside* the harness (e.g. a subagent that the harness itself spawned)
- `external_orchestrator` — an agent or script calling the harness *from outside* (e.g. via CLI flags or SDK)
- `ci_runner` — an automated pipeline
- `administrator` — a person or script configuring the harness (installing, provisioning, managing policy)

**8 access values** (ordered roughly best-to-worst for automation):
- `native` — built-in, first-class, no extra steps
- `supported` — documented and works as designed
- `configurable` — works with explicit configuration
- `experimental` — early / may change or break
- `mediated` — requires a proxy, wrapper, or approval step
- `unavailable` — explicitly not supported
- `unknown` — no evidence found (does **not** mean unavailable)
- `deprecated` — was supported, being removed

### Confidence Levels

- `verified_official` — from an official changelog, release note, or product documentation
- `inferred_high` — strong heuristic match in release notes
- `inferred_low` — weak heuristic
- `unknown` — no evidence; does not imply `unavailable`

### Capability Taxonomy (15 categories, 39 nodes)

| Category | Example capabilities |
|---|---|
| `interaction` | terminal/TUI, IDE integration, desktop/web surface |
| `execution` | file editing, shell execution, headless, structured output, SDK embedding, RPC/app-server |
| `extensions` | MCP client, skills, plugins, lifecycle hooks |
| `context_memory` | project instructions, persistent memory, knowledge tools |
| `session_state` | resume/fork/session lineage |
| `orchestration` | subagents/delegation, multi-agent coordination, parallel/background agents, cross-session messaging |
| `runtime` | self-hosted worker, remote/cloud execution |
| `automation` | CI/GitHub Action integration, app-server/embedding |
| `security_governance` | execution sandbox, granular permissions, enterprise policy, approval controls |
| `observability` | tracing/event telemetry, usage/cost telemetry |
| `research_tools` | web search/research, browser/computer use |
| `interfaces` | rich result views, image/media generation |
| `models_providers` | model/provider portability, model/reasoning controls |
| `evaluation` | evals framework |
| `tools` | image generation |

### Release Event Record (key fields)

| Field | Type | Meaning |
|---|---|---|
| `id` | string | Stable dedup key |
| `harness_id` | string | Product this release belongs to |
| `version` | string | Version string |
| `channel` | string | Release channel |
| `published_at` | timestamp | Upstream release date |
| `change_count` | integer | Number of normalized change items |
| `flags` | object | Boolean: `security`, `breaking`, `deprecation` |
| `changes` | array | Normalized change items |
| `provenance.immutable` | boolean | Whether the source is considered immutable |

**Change item `kind` values:** `added`, `changed`, `improved`, `fixed`, `deprecated`, `removed`, `security`, `unknown`

### Complete Example Capability Record

```json
{
  "id": "impl.claude-code.execution.headless",
  "harness_id": "claude-code",
  "capability_id": "execution.headless",
  "status": "stable",
  "summary": "`claude -p` provides supported non-interactive execution for scripts and CI; `--bare` disables ambient project customization for reproducibility.",
  "actor_access": {
    "human_operator": "supported",
    "in_harness_agent": "unavailable",
    "external_orchestrator": "native",
    "ci_runner": "native",
    "administrator": "configurable"
  },
  "requires_human_mediation": false,
  "surfaces": ["CLI", "stdin/stdout"],
  "invocation": ["claude -p", "claude -p --bare"],
  "minimum_version": null,
  "current_version_verified": "2.1.226",
  "limitations": [],
  "confidence": "verified_official",
  "verified_at": "2026-08-08T20:00:00Z",
  "evidence": [
    {
      "source_id": "src.claude-code.docs.headless",
      "url": "https://docs.anthropic.com/en/docs/claude-code/headless",
      "claim": "`claude -p` provides supported non-interactive execution for scripts and CI; `--bare` disables ambient project customization for reproducibility.",
      "version": null,
      "verified_at": "2026-08-08T20:00:00Z"
    }
  ],
  "invocation_status": "resolved",
  "invocation_na_reason": null
}
```

---

## 5. Who Reads HCR Today

### Automated Readers

**1. Delegation router** (Agentic OS control plane)
*Question:* "For this task's actor type and capability requirements, which harness has native/supported access? Which one to prefer when multiple qualify?"
*Input:* `generated/agent-guides/<id>.json` — `capabilities_by_actor.<actor>` filtered by `access` level, combined with `routing_hint.recommended_when` and `control_plane_dimensions`.

**2. Lane guard** (pre-commit hook and CI check in the orchestration repo)
*Question:* "Does the harness I'm routing this dispatch to actually support headless execution and structured output for an external orchestrator?"
*Input:* `docs/agentic-operator/harness-capabilities.yaml` (the AMD projection), cross-checked against `[HCR:<capability_id>]` tags in orchestration docs.

**3. Staleness gate** (`scripts/check_harness_capability_staleness.py`)
*Question:* "Is the projection fresh enough to trust? How many commits behind HCR origin/main is it? How old is it in wall-clock days?"
*Input:* The `provenance` block in `harness-capabilities.yaml` vs. actual HCR repo state.

**4. Unused-capability reporter** (`scripts/report_unused_capabilities.py`)
*Question:* "Which capabilities are in the projection but not yet referenced in any orchestration file?"
*Input:* `harness-capabilities.yaml` + `harness-capability-usage-predicates.yaml` + grep over git-tracked files.

**5. HCR curator agents** (release-curator, capability-auditor, product-lineage-auditor, harness-routing-advisor)
*Questions:* "Is this heuristic candidate plausible? Did this release touch a breaking change? Has this product announced a successor?"
*Input:* `registry/releases.json` (unreviewed items), `registry/capabilities.json` (candidates), `registry/harnesses.json` (lifecycle/lineage).

### Human Readers

- `generated/agent-guides/<id>.md` — comparing harnesses for a specific use case.
- `docs/agentic-operator/HARNESS-CAPABILITIES.md` — spot-checking routing decisions.
- `generated/reports/coverage.md` — checking which harnesses have thin evidence coverage.
- **Harness Matrix** (local build, `generated/Harness_Matrix_Standalone.html`) — full cross-harness table.

---

## 6. Viewer Ideation Seed

### Questions a human should answer at a glance (8–12)

1. **"Which harnesses support capability X for actor Y?"** — e.g. "Which have `native` headless execution for `external_orchestrator`?"
2. **"What changed this week?"** — new releases, `added`/`changed` items, `security`/`breaking` flags, across all 20 harnesses.
3. **"Which harnesses are stale?"** — `last_verified_at` older than N days, or `version_as_of` falling behind known releases.
4. **"What's the delta between harness A and harness B?"** — side-by-side capability comparison for a specific actor, with access-level differences highlighted.
5. **"Which capabilities still have low or unknown confidence?"** — `inferred_low` or `unknown` confidence, as a curation backlog view.
6. **"What requires human mediation?"** — `requires_human_mediation: true` entries, filterable by harness and actor.
7. **"What's experimental or deprecated right now?"** — early-warning view for unstable or retiring capabilities.
8. **"What are the security and breaking changes in the last 30 days?"** — release events with `flags.security` or `flags.breaking`, with summaries.
9. **"Which capabilities in the projection are unused?"** — unused-capability report result surfaced as a visual backlog.
10. **"What can harness A do that harness B can't?"** — unique capabilities or `native` access where peers are only `configurable` or `unavailable`.
11. **"For a task needing capabilities X, Y, Z — which harness fits?"** — requirement-matching: enter a capability set + actor, get ranked harness matches.
12. **"How stale is my projection vs. HCR?"** — commits and days of drift, last regeneration timestamp, which harnesses changed since last merge.

### Dimensions Available for Views

| Dimension | Values / Notes |
|---|---|
| **Harness** | 20 products; filterable by family, vendor, lifecycle, maturity, tracking priority |
| **Capability** | 39 taxonomy nodes; filterable by category (15 categories) |
| **Actor** | 5 types: human_operator, in_harness_agent, external_orchestrator, ci_runner, administrator |
| **Access level** | 8 values: native > supported > configurable > experimental > mediated > unavailable > unknown > deprecated |
| **Confidence** | 4 levels: verified_official > inferred_high > inferred_low > unknown |
| **Version** | minimum_version, current_version_verified, version_as_of, current_version |
| **Freshness** | verified_at, last_verified_at, latest_release_published_at, days since last verification |
| **Human mediation** | Boolean — splits automation-safe from human-in-the-loop |
| **Status** | stable / experimental / candidate / deprecated |
| **Change kind** | added / changed / improved / fixed / deprecated / removed / security / unknown |
| **Release flags** | security, breaking, deprecation — Boolean per release event |
| **Evidence quality** | Official-source evidence present/absent; invocation_status resolved vs. unreviewed |
| **Control plane dims** | strong/moderate/limited on: local_execution, remote_execution, multi_agent, structured_automation, provider_portability, enterprise_controls |
| **Projection staleness** | Commits behind HCR main, wall-clock age, last-generated timestamp (cross-repo derived) |

---

## Appendix: Repo Structure

```
miethe/harness-capability-registry/
├── registry/
│   ├── sources.json           71 official sources
│   ├── harnesses.json         20 harness records
│   ├── taxonomy.json          39 capability taxonomy nodes
│   ├── capabilities.json      237 capability implementations
│   ├── releases.json          2,435 release events
│   └── harnesses/<id>.json    Full HarnessBOM per product
├── schemas/                   JSON Schema 2020-12 (validates every registry file)
├── generated/
│   ├── agent-guides/<id>.json  Agent-consumable routing guide per harness
│   ├── agent-guides/<id>.md    Human-readable guide
│   └── reports/               Coverage, validation, drift reports
├── raw/                       Content-addressed upstream snapshots
├── hcr/                       Python package: collection, generation, validation
├── .github/workflows/
│   └── update-registry.yml    6-hourly cron refresh + rolling PR
└── specs/                     Architecture and integration specs
```

**Data quality policy:**
- Official changelogs, release feeds, and documentation are primary evidence; cross-vendor matrices can corroborate but never replace them.
- `unknown` means evidence is missing — it never implies `unavailable`.
- A UI-only capability is never assumed agent-callable.
- A source failure never silently converts an existing capability to `unavailable`.
- Capability promotion from heuristic candidate to curated claim requires human review.
