# CLAUDE.md — `harness-capability-registry` (HCR)

**The AOS's harness-intelligence layer**: an evidence-backed release-event ledger and
current-capability graph for AI coding harnesses (Claude Code, Codex CLI, Gemini CLI, goose,
Copilot CLI, the agent/provider SDKs — 20 products tracked). It answers *"which harness can do X,
for which actor, on which version, with what evidence"* so routing decisions (delegation-router,
`op`, model/harness selection) read data instead of memory.

- **AOS role:** standalone subsystem of the control-plane routing layer. It *publishes* to
  SkillMeat / IntentTree / CCDash / MeatyWiki; it never merges into them.
  Canonical design: [`specs/04_AOS_Integration.md`](specs/04_AOS_Integration.md).
- **IntentTree tree:** `tree_01M00XMCKKFRT80FJYA3R9VFY1` (workspace `agentic-os`); binding in
  `.claude/aos.env` — the SDLC sync arms automatically.

## Architecture (data flow)

```
registry/sources.json (69 official sources)
  → hcr collect / hcr snapshot        (stdlib-only collectors; raw/ keeps raw responses)
  → registry/releases.json            (release-event ledger — dedup by release id)
  → hcr/normalizers/heuristic.py      (capability CANDIDATES — triage, never ground truth)
  → registry/capabilities.json        (curated claims, vs registry/taxonomy.json)
  → hcr generate                      (no network)
      registry/harnesses/<id>.json    (HarnessBOM, per product)
      generated/agent-guides/<id>.*   (compact actor-aware routing guides)
      generated/registry.bundle.json  (+ copy into app/data/ for the web app)
      generated/Harness_Matrix_Standalone.html
  → hcr validate                      (invariant + cross-reference checks)
```

`hcr update` = collect → snapshot → generate → validate. `hcr serve` serves the static
Harness Matrix app (read-only; no curator UI yet). `make seed|collect|generate|validate|update|test|serve`.

## Working in this repo

- Python **3.11+**, zero runtime dependencies (stdlib `urllib` only). Tests: `make test`
  (offline, deterministic). Only env var: `GITHUB_TOKEN` (optional, for release APIs).
- **`generated/` and `app/data/` are build artifacts** — regenerable via `hcr generate`; never
  hand-edit them. `registry/` is the curated source of truth; **files are canonical** (AOS
  constraint 2).
- **Heuristic capability candidates are not claims.** Promotion into `capabilities.json` is a
  curation step; actor-access values never change from doc-drift hashes alone. Human review is
  mandatory for: sandbox/approval reductions, credential/auth changes, deprecations touching
  active SkillBOMs, product transitions, `unavailable` (negative) claims (spec 04 §10).
- Schemas in `schemas/` (JSON Schema 2020-12) govern every registry file; `hcr validate` is the
  gate. Run it before committing registry changes.
- The four `agents/*.md` (release-curator, capability-auditor, product-lineage-auditor,
  harness-routing-advisor) are **SkillMeat-registered artifacts** — edit here (upstream), deploy
  via SkillMeat, per the launchpad's ARTIFACT-UPSTREAM-REGISTRY discipline.

## Update model

Designed cadence: six-hourly automated `hcr update` (`.github/workflows/update-registry.yml`,
**not yet armed**) writing to a rolling automation branch + single PR — never direct to main.
Curation of capability candidates stays human-gated. Alert classes and the review matrix:
[`specs/03_Automation_and_Operations.md`](specs/03_Automation_and_Operations.md).

## Doc map

- `specs/00`–`06` — full spec set (data model, sources, automation, AOS integration, web app,
  handoff). `docs/DELIVERY_GUIDE.md`, `docs/COVERAGE_AND_LIMITS.md` — operational honesty.
- `docs/AOS-ABSORPTION-PLAN.md` — how the AOS consumes HCR and keeps it current (utilization +
  refresh plan; the absorption record).
- `docs/PRD.md`, `docs/DECISIONS.md` — op-scaffolded stubs; decisions land in DECISIONS.md.
