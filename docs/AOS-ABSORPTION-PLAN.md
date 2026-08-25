# AOS Absorption Plan — Harness Capability Registry

> **Status:** proposed 2026-08-14 (absorption day); adopted when Nick merges the PR carrying it.
> Reviewed by a Codex gpt-5.6 second-opinion leg the same day; its 14 findings are folded in. This is the utilization + freshness plan for
> HCR inside the AOS — how the OS *consumes* it, and how it *stays current*. The proposed
> integration surface it implements is [`../specs/04_AOS_Integration.md`](../specs/04_AOS_Integration.md);
> this doc sequences that spec against AOS reality and marks what is live vs. planned.
> Backlog nodes live in IntentTree tree `tree_01M00XMCKKFRT80FJYA3R9VFY1`.

## 1. What is live today (absorption baseline)

- Repo: `~/dev/homelab/development/harness-capability-registry`, public mirror
  `github.com/miethe/harness-capability-registry`. AOS wiring (`.claude/` deployed bundle
  content) is deliberately untracked in the public repo.
- T4 scaffold: starter bundle deployed, writeback Stop-hook, `aos-artifacts.yaml` manifest,
  IntentTree tree bound (`.claude/aos.env`).
- The four HCR agents (`release-curator`, `capability-auditor`, `product-lineage-auditor`,
  `harness-routing-advisor`) registered in SkillMeat enterprise and deployed project-level;
  upstream edit point is `agents/` in this repo.
- Data is the 2026-08-08 delivered seed. **The first networked `hcr update` has never run.**

## 2. Utilization — who reads HCR, for what

Ordered by nearness to value; each consumption seam is (or will be) an itt node.

1. **Delegation-router / model-registry join (primary consumer).**
   `~/.claude/config/model-registry.yaml` holds model×provider routing; HCR holds
   harness×capability×actor evidence. The join answers "can this leg run on that harness at all,
   and via which surface." ⚠️ **Superseded 2026-08-16 by agentic_meta_dev PR #360** (node_01M05TK7TV9J7G8A46QDYF3Z7K):
   the "First increment" below described `harness-routing-advisor` (agent, model-call-per-lookup)
   as the live path — it never became reachable outside HCR itself (node_01M05TD19Q2FYSJVRC1TD25WT3,
   re-verified 2026-08-25: still not in `~/.claude/agents/`, still undeclared in any consuming
   project's `.claude/aos-artifacts.yaml`), and PR #360 built the cheaper alternative this doc's
   own §2 item 2 language already anticipated: a **committed, generated projection**
   (`agentic_meta_dev/docs/agentic-operator/HARNESS-CAPABILITIES.md` + `.yaml`, produced by
   `scripts/generate_harness_capabilities.py` reading HCR via a pinned git ref) that is a pure
   file read — constraint 4, no agent dispatch, no model call on the lookup path. That is now the
   live consumption path for the common case; the advisor agent stays undeployed by decision, not
   by oversight. `scripts/check_harness_capability_staleness.py` gates projection freshness at
   commit time (refreshed 2026-08-25: 0 commits behind `origin/main`, was 4 behind). Original text
   preserved below for history:
   ~~First increment: `harness-routing-advisor` agent (already deployed)
   reads `generated/agent-guides/<id>.json` on demand — no resolver change.~~ Later increment:
   registry entries carry `harness_id` + minimum-version pins validated against HarnessBOMs.
   Constraint 4 holds: the read path is a file read, never a model call.
2. **"What did we miss" feature harvesting (the `/advisor`-class discovery Nick named).**
   The release ledger for claude-code/codex/gemini-cli, diffed against what the AOS actually
   uses, yields a periodic "unused capability" report — the exact "we aren't utilizing new
   features" gap that motivated HCR. Runs as a report-only generator; findings file itt nodes
   per `finding-capture.md`. **Live on both sides as of 2026-08-25** (node_01M05TBRKCN0Z9HG1S8M3ZN658):
   consumer-side, `agentic_meta_dev/scripts/report_unused_capabilities.py` (predicate-based,
   grep against the AOS's own code — 17/88 checked against the four allow-listed harnesses as of
   this writing, never a silent clean bill); producer-side, `hcr generate` now also emits
   `generated/reports/invocation-coverage.md` off each capability's own `invocation_status`
   (46/237 resolved-or-n/a registry-wide; claude-code specifically at 31/36). The two are
   deliberately not merged — one measures "does HCR know an invocation token", the other measures
   "does the AOS actually use it" — but both share the same never-silent-truncation discipline.
3. **Impact review on releases.** A release event touching a harness the AOS runs (Claude Code
   above all) triggers an impact-review node in the affected repo's tree (spec 04 §3, writebacks
   §11). Starts manual/curated — deliberately, because the SkillBOM/CCDash/environment mappings
   that would *identify* affected workflows are W4 work; automation waits for them.
4. **SkillBOM runtime requirements (later).** SkillMeat artifact types `harnessbom` /
   `harness_agent_guide` / `harness_adapter` / `capability_eval` per spec 04 §5 (integration
   contract §6) — real SkillMeat schema work, sequenced behind the join in (1) proving useful.
5. **CCDash claimed-vs-observed join (later).** Needs CCDash-side keys; parked until CCDash
   telemetry work resumes.

**Spec surfaces not listed above are deferred, not dropped.** Every integration spec 04/06
proposes is filed as a node in the itt backlog (tag `absorption-2026-08-14`): Intent/I-BOM
`harness_requirements` + environment inventory, the control-plane resolver API, MeatyWiki
decision/source-note writebacks, CCDash event emission, the Researcher→Architect→Critic→
Operator→Red-Team posture chain, the Execution-Engine smallest-adequate-update selector, and
the governance approval workflow all have their own nodes. This doc sequences; the tree holds
the full surface.

## 3. Freshness — how it stays current

Doctrine constraints applied: no model call on the refresh path's happy case; curation stays
human-gated; Hermes is out of the active path (`op hop` is the direction), so **no new Hermes
agent lanes** — only zero-model script lanes are eligible.

- **Collection (zero-model, automatable now):** `hcr update` (collect → snapshot → generate →
  validate) is zero-model and stdlib-only; the generate/validate half is deterministic, the
  networked collect half is not (spec 03 §2 draws the same line). ⚠️ The shipped workflow runs
  collection without `--strict`, so source failures don't fail the update — fix filed before
  arming. Two candidate homes, in preference order:
  1. **GitHub Actions** — the shipped `update-registry.yml` (six-hourly, rolling automation
     branch + single PR, never direct-to-main). Public repo exists, so arming it is one click +
     a repo `GITHUB_TOKEN` default. **Arming is Nick's call** (it's a standing outward-facing
     automation on a public repo).
  2. **Node script lane** — a `hermes cron --script` zero-model job running `hcr update` on the
     nuc, PR-ing via the existing lanes. Only if GH Actions is declined; must be declared in
     `ph_autonomy` before arming (undeclare-before-pause lesson applies in reverse).
- **Curation (human-gated by design):** heuristic candidates → `capabilities.json` promotion is
  the `release-curator` agent + Nick. Mandatory-human-review classes (sandbox/approval
  reductions, auth changes, negative claims, product transitions, deprecations touching active
  SkillBOMs) per spec 04 §10. **Honest edge: nothing enforces this today** — the update PR is an
  ordinary PR and `validate_registry` checks no approvals; enforcement is the governance-workflow
  backlog node. Until it lands, the gate is Nick reading the PR.
- **The rolling-PR pattern is the gate.** Automation writes a branch; the registry's canonical
  state changes only on PR merge. This matches AOS constraint 6 (stop-and-confirm encoded).
- **Cadence sanity:** six-hourly collection; a weekly curation pass (aspirational — no
  checklist mechanism exists yet; becomes real with the review-queue node in W3);
  release-triggered impact reviews as they land.

## 4. Sequencing (mirrors the filed itt backlog)

| Wave | Content | Gate |
|---|---|---|
| W0 (done) | Move, scaffold, SkillMeat registration, public repo, tree | — |
| W1 | First networked `hcr update`; validate against live sources; arm GH Actions cron | Nick arms the workflow |
| W2 | Routing-advisor consumption seam (agent-guide reads as *advisory evidence* in delegation decisions — not resolver-integrated; governed registration + environment inputs are W4 prerequisites for that); unused-capability report v1 | — |
| W3 | Impact-review node automation; curation workflow hardening (review queue per spec 03) | curation stays human-gated |
| W4+ | SkillMeat artifact types (harnessbom etc.); CCDash join; environment-aware routing (spec 06 Phase 3) | per-item |

## 5. Honest edges

- Nothing in §2 items 3–5 exists in code; spec 04 is a design document. Do not cite it as live.
- Heuristic capability extraction is triage-grade; treating candidates as ground truth
  misstates actor access (COVERAGE_AND_LIMITS).
- The shipped GH workflow force-pushes its automation branch by design (single rolling PR) —
  known, intentional, scoped to that branch.
- No credential scanning on raw snapshots yet — required before any enterprise promotion
  (spec 06 §8); filed as a backlog node.
