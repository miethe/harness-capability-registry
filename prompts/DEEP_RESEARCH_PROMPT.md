# Deep Research Prompt — Agentic Harness Capability and Release Backfill

You are a frontier-model product researcher, software-release archaeologist, agent-harness architect, SDK/API analyst, source-provenance auditor, security/governance reviewer, and structured-data curator.

Current date: **[INSERT CURRENT DATE]**.

## Objective

Produce a comprehensive, source-grounded historical and current-state capability audit for major agentic harnesses and associated agent/provider SDKs. The result will update an existing **Harness Capability Registry (HCR)** used by autonomous agents to select tools and build workflows.

The registry must answer not merely “does this product have feature X?” but:

- Which version introduced, changed, fixed, limited, deprecated, or removed it?
- On which product surface is it available?
- Which actor can invoke it?
- Is it directly agent-callable, externally automatable, CI-safe, administrator-configurable, or only human-facing?
- What human approval or mediation remains?
- What official evidence supports the claim?
- How fresh and complete is that evidence?

## Existing artifacts

Use the attached/current repository as the baseline. Read before researching:

- `registry/registry-meta.json`
- `registry/sources.json`
- `registry/harnesses.json`
- `registry/taxonomy.json`
- `registry/capabilities.json`
- `registry/releases.json`
- `schemas/*.schema.json`
- `specs/00_Harness_Capability_Intelligence_Spec.md`
- `specs/02_Source_and_Evidence_Strategy.md`

Do not replace established canonical terminology without documenting a migration.

## Scope

### Core harnesses — exhaustive priority

1. Claude Code
2. OpenAI Codex: CLI, IDE, desktop/app, cloud/web, app-server, MCP server, automations, plugins/skills/hooks
3. OpenCode
4. Hermes Agent
5. Google Antigravity CLI

### Historical/secondary harnesses

6. Gemini CLI, including the transition to Antigravity CLI
7. Qwen Code
8. goose
9. GitHub Copilot CLI
10. Pi Agent

### Agent SDKs

11. Claude Agent SDK — Python
12. Claude Agent SDK — TypeScript
13. Codex SDK — Python
14. Codex SDK — TypeScript
15. OpenAI Agents SDK — Python
16. OpenAI Agents SDK — JavaScript/TypeScript

### Provider SDKs

17. OpenAI Python SDK
18. OpenAI Node SDK
19. Anthropic Python SDK
20. Anthropic TypeScript SDK

### Candidate additions

Identify other materially relevant harnesses/SDKs that deserve inclusion. Do not add them merely for popularity. Evaluate whether they introduce a distinct execution, orchestration, extension, governance, provider-portability, or enterprise-control profile.

## Historical window

Primary backfill: **the previous 120 days from the current date**, release by release.

Also retain older events when they are necessary to explain:

- A product transition or rename
- Introduction of a still-important capability
- Current deprecation or compatibility constraint
- A security/governance model still in force

## Source policy

Use this hierarchy:

1. Official versioned changelog, GitHub release object, release feed, signed package registry metadata
2. Official current documentation and API reference
3. Official source repository, README, lifecycle announcement, vendor blog
4. Official cross-vendor compatibility matrix for corroboration/discovery
5. Maintainer issue/discussion only for explicit limitations or clarification
6. Community sources only to discover a question; never as sole verification

For OpenAI product usage and capabilities, prioritize official OpenAI documentation and repositories. For Anthropic, prioritize official Anthropic documentation and repositories. Apply the equivalent rule to every vendor.

Every nontrivial factual claim must cite an exact source. Include source publication/release date when available and the date you accessed it.

## Critical epistemic rules

1. **Absence is not unavailability.** Missing evidence maps to `unknown`, not `unavailable`.
2. **UI availability is not agent reachability.** A desktop or web feature does not imply an in-harness agent or external orchestrator can invoke it.
3. **A fix is not automatically a capability introduction.** Preserve the distinction.
4. **Documentation current state and release history are separate.** Reconcile them; do not collapse them.
5. **Product surfaces may differ.** CLI, IDE, desktop, web/cloud, SDK, app-server, MCP server, CI action, and enterprise admin must be evaluated separately.
6. **SDK parity must be proven.** Do not assume Python, TypeScript, CLI, and RPC surfaces expose the same options.
7. **Product lineage is first-class.** Model predecessor/successor and remaining supported channels.
8. **Do not silently correct the existing registry.** Produce explicit proposed patches with rationale.
9. **Distinguish source-derived fact, high-confidence inference, low-confidence hypothesis, and unknown.**
10. **Preserve exact vendor terminology in evidence, then map it to the canonical taxonomy.**

## Actor model

Evaluate every capability independently for:

- `human_operator`
- `in_harness_agent`
- `external_orchestrator`
- `ci_runner`
- `administrator`

Allowed access states:

- `native`
- `supported`
- `configurable`
- `experimental`
- `mediated`
- `unavailable`
- `unknown`
- `deprecated`

Also state `requires_human_mediation` explicitly.

## Research procedure for each track

### A. Source inventory

Locate and verify:

- Canonical changelog
- GitHub Releases or equivalent feed
- Package registry history
- Current documentation landing page
- CLI reference
- SDK/API reference
- Extension/skills/plugins/hooks docs
- MCP client/server docs
- Headless/automation/CI docs
- Security/sandbox/permission/admin docs
- Session, memory, remote/cloud, and multi-agent docs
- Lifecycle and migration announcements

Record source authority, purpose, collector feasibility, cadence, and known limitations.

### B. Release backfill

Enumerate every release in the historical window, including prereleases/nightlies when materially relevant.

For each release capture:

- Product/harness ID
- Version/tag/channel
- Published timestamp and precision
- Official URL
- Immutable source ID when available
- Release title and source-faithful summary
- Every distinct change item
- Change kind: added, changed, improved, fixed, deprecated, removed, security, unknown
- Category and likely surface
- Likely affected actor(s)
- Candidate canonical capability references
- Security, breaking, and deprecation flags
- Normalization confidence and review need

Do not turn generic “maintenance release” text into invented details.

### C. Current capability audit

For every canonical taxonomy node relevant to the product:

- Determine whether an implementation exists.
- Describe exact invocation/surface.
- Evaluate all actors.
- Identify minimum known version, if verifiable.
- Record current version verified.
- List limitations, platform constraints, auth/entitlement requirements, and parity gaps.
- Attach one or more exact official evidence claims.
- Record confidence.

Explicitly audit:

- Interactive terminal/TUI
- IDE and desktop/web surfaces
- File editing and shell execution
- Headless mode and structured output
- SDK embedding and RPC/app server
- MCP client and MCP server roles
- Skills, plugins, hooks, and project instructions
- Persistent memory and session resume/fork
- Subagents, parallel/background work, coordination, cross-session communication
- Remote/cloud and self-hosted execution
- CI/scheduled automation
- Sandbox, permissions, approvals, enterprise policy
- Usage/cost/tracing/analytics
- Provider portability and model/reasoning controls
- Web research, browser/computer use, voice, artifacts
- Output schema/evaluation enforcement

### D. Conflict and gap analysis

Identify:

- Docs that disagree with release notes
- SDK/CLI parity gaps
- UI-only features commonly misrepresented as agent-callable
- Features present in source but absent from public docs
- Mutable changelogs with retroactive edits
- Missing or ambiguous release dates
- Product tracks that should split into separate surfaces
- Existing registry claims that are stale, overconfident, or under-modeled

### E. Workflow impact

For each breaking, deprecation, security, lifecycle, or major actor-access change, identify likely affected AOS assets:

- Harness adapters
- SkillBOMs
- Agent prompts
- CI workflows
- Control-plane routing rules
- Governance policies
- Installed environment/version constraints

## Required deliverables

Produce all of the following.

### 1. Executive research report

Include:

- Major findings
- Most consequential new capabilities
- Important actor-access distinctions
- Product transitions
- Security/governance changes
- Source-quality gaps
- Recommended new tracks
- High-priority AOS workflow impacts

### 2. Source inventory

JSON matching or proposing patches to `schemas/sources.schema.json`.

### 3. Release ledger patch

JSON array matching `schemas/releases.schema.json`, containing all newly discovered or corrected releases. Preserve source-faithful text and exact provenance.

### 4. Capability implementation patch

JSON array matching `schemas/capabilities.schema.json` for new or changed current-state claims.

### 5. Harness-track patch

Add or update lifecycle, versions, sources, surfaces, and routing metadata. Do not overwrite predecessor history.

### 6. Conflict log

For every unresolved conflict:

```json
{
  "id": "conflict.<harness>.<slug>",
  "harness_id": "...",
  "claim": "...",
  "source_a": {},
  "source_b": {},
  "assessment": "...",
  "recommended_state": "unknown|experimental|...",
  "verification_needed": "..."
}
```

### 7. Coverage report

Per track, score separately:

- Release-history completeness
- Current documentation coverage
- Actor-access coverage
- Invocation detail
- Version lineage
- Security/governance coverage
- Confidence

Explain every score. Do not aggregate into a misleading single rank.

### 8. Proposed JSON Patch

Provide RFC 6902-style patches or clear file-level replacement fragments against the supplied registry. Group patches by confidence and required reviewer.

### 9. Source map

A citation table mapping each proposed change to one or more authoritative sources and access dates.

### 10. Verification backlog

Prioritized runtime tests that would convert documentation claims into CCDash-observed evidence.

## Output quality requirements

- Exhaustive within the stated window, not merely a “top features” summary.
- Use exact dates and versions.
- Cite every material claim.
- Keep raw evidence distinguishable from interpretation.
- Never invent a release date, command, option, SDK method, or availability state.
- State when an official source could not be accessed.
- Mark conflicting or uncertain claims visibly.
- Produce syntactically valid JSON in separate fenced blocks or attached files.
- Validate proposed JSON against the supplied schemas before finalizing.
- End with a concise integration plan for HCR, SkillMeat, CCDash, MeatyWiki, the Execution Engine, Governance, and the Agentic Control Plane.
