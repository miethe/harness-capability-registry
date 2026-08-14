# Harness Capability Registry Deep Research Audit

**Research snapshot:** 2026-08-08, America/New_York  
**Primary historical window:** 2026-04-10 through 2026-08-08  
**Evidence policy:** official release objects/package metadata → official current docs/API references → official source repos/lifecycle announcements → maintainer clarification only for limitations.

**TL;DR**

The most important registry correction is architectural rather than feature-specific: **product availability, agent reachability, external orchestration, CI safety, and administrator control must be modeled independently per surface.** Codex, Claude Code, OpenCode, Qwen Code, goose, Copilot CLI, Pi, and Antigravity all now have materially different programmable surfaces from their human-facing UI paths. citeturn15search0turn20search12turn18search0turn17search0turn18search2turn17search15  
The largest lifecycle event is Google's consumer transition from Gemini CLI to Antigravity CLI on June 18, 2026; enterprise Gemini status should remain **unknown**, not unavailable, until separately evidenced. citeturn4search3  
The most consequential recent governance changes are Codex 0.147.0's trust/redaction/plugin and automation changes, Claude Code's expanded permission/hook/subagent controls, Antigravity's noninteractive approval semantics, OpenCode's permission model, and Copilot CLI's mode-dependent approval behavior. citeturn12view0turn21search1turn21search0turn13view3turn20search5turn18search4  
Three additions deserve separate HCR treatment now: **Google Antigravity SDK Python, OpenAI Codex Security, and Pi's direct agent-core/AgentSession embedding**. GitHub's Copilot SDK also deserves a track once its package/release inventory is collected. citeturn20search3turn16search4turn17search15turn18search2  
The supplied HCR baseline files/schemas were not retrievable in this run. I therefore did **not** invent canonical capability IDs or claim schema validation. The attached bundle is a syntax-validated, source-grounded **candidate overlay**, with explicit merge fragments and a verification backlog rather than fabricated RFC 6902 paths.

## Executive findings and research boundary

The audit produced **42 source records, 64 release/lifecycle records, 35 current capability implementation records, 14 harness/candidate-track records, eight conflict records, and a 113-change source map**. All generated JSON parses successfully and its internal source references were checked. Exact JSON Schema validation, canonical taxonomy mapping, and path-correct RFC 6902 generation remain blocked because `registry/*.json`, `schemas/*.schema.json`, and the two requested HCR specs were unavailable to the retrieval layer and were not found at the requested paths in the connected repository.

That limitation changes what can responsibly be called “complete.” The work is strong enough to identify high-confidence lifecycle changes, actor-access distinctions, current capabilities, and many releases, but **it is not merge-final or genuinely exhaustive across every release of every one of the 20 requested tracks**. In particular, very high-volume release lines such as Codex and OpenCode, and some generated SDK lines, require a feed/package collector rather than search-result archaeology. This distinction matters because the retrieval layer itself exposed stale repository snapshots: for example, an official Codex repository result still reported 0.139.0 as its latest indexed release while the live official release page exposed 0.147.0 on August 7 and a 0.148.0 alpha on August 8. The release feed therefore outranks search-index metadata. citeturn15search0turn12view0

The strongest cross-product finding is that **“supports automation” is too coarse for HCR**. OpenCode exposes a standalone OpenAPI-backed HTTP server; Pi has JSON-RPC over stdio plus direct `AgentSession` embedding; Qwen has headless execution and an experimental ACP daemon; goose exposes desktop, CLI, API, MCP and ACP surfaces; Codex has separate CLI, app, web/cloud, app-server and language SDK paths; and Copilot's remote-control feature remains anchored to a running local interactive CLI session rather than becoming a generic autonomous remote execution API. citeturn20search12turn17search15turn18search0turn18search3turn17search0turn15search0turn18search9

A second major finding is that **approval state is increasingly mode- and actor-specific**. Claude Code has `default`, `acceptEdits`, `plan`, research-preview `auto`, `dontAsk`, and `bypassPermissions`, with managed settings able to disable the more permissive modes; OpenCode uses `allow|ask|deny` and `--auto` while retaining explicit deny rules; Qwen subagents have several approval modes; Antigravity deliberately soft-denies tools requiring human approval in headless mode; and Copilot supports both persisted tool approvals and an autopilot workflow, meaning “always human-mediated” is not an accurate product-wide representation. citeturn21search1turn20search5turn18search5turn13view3turn18search4turn18search2

A third finding is that **SDK parity must be versioned as an evidence claim, not inferred from branding**. The Codex TypeScript SDK explicitly wraps/spawns the Codex CLI and exchanges JSONL over stdio, while the Python SDK installs a matching `openai-codex-cli-bin` runtime and says its releases track corresponding Codex CLI releases. Claude Agent SDK release notes explicitly announce particular CLI parity levels, and the Python release line bundles a specific Claude CLI version. Those are useful parity mechanisms, but they do not prove option-for-option or language-for-language parity at arbitrary versions. citeturn16search1turn15search9turn23search8turn23search11

**Recommended new tracks.** Google Antigravity SDK Python should be added: it is not merely another way to launch the CLI; its documented architecture has high-level `Agent`, stateful `Conversation`, connection adapters, hooks, MCP, in-process tools, triggers and background/event execution. citeturn20search3 OpenAI Codex Security should also be a separate child/sibling track because its CLI/TypeScript SDK is deliberately CI-oriented and has a materially different security policy: security scans use their own filesystem profile and `approvalPolicy: "never"` rather than inheriting ordinary Codex interactive approval semantics. citeturn16search3turn16search4 Pi's `@earendil-works/pi-agent-core`/direct `AgentSession` embedding merits a child SDK track because Pi documentation explicitly recommends direct embedding over subprocess RPC for Node/TypeScript applications. citeturn17search15 GitHub also now advertises a Copilot SDK built on the same agent runtime as Copilot CLI; that is a strong candidate, but I would not promote it to final HCR status until its official package/API/release sources are inventoried. citeturn18search2

By contrast, the official Claude Code Action and Qwen Code Action are best modeled first as **CI surfaces of their parent harnesses**, not as independent harnesses, unless their permission/session/runtime behavior proves materially divergent. Anthropic's organization exposes a distinct Claude Code Action repository, and Qwen's official organization likewise exposes `qwen-code-action`. citeturn22search3turn18search10

## Current capability and actor-access audit

The actor shorthand below is **H** = `human_operator`, **A** = `in_harness_agent`, **E** = `external_orchestrator`, **CI** = `ci_runner`, and **Adm** = `administrator`. These values describe the strongest directly evidenced path for the cited capability/surface, **not** one product-wide state. The downloadable capability patch contains actor state and `requires_human_mediation` separately for every normalized implementation claim.

| Track | High-confidence current surfaces and invocation | Actor/access conclusion | Human mediation / important limit |
|---|---|---|---|
| **Claude Code** | TUI/CLI, file/shell tools, MCP client/server, hooks, skills/subagents, permission-managed operation. Hooks can intervene at tool and permission lifecycle events; `claude mcp serve` exposes Claude Code tools to MCP clients. citeturn21search0turn21search1turn21search2turn20search6 | H `native`; A `native`; E `supported`; CI `supported/configurable`; Adm `configurable`. | **Yes in normal modes.** Ask/deny/allow rules and multiple permission modes alter mediation. MCP clients using Claude Code as a server are responsible for their own user-confirmation behavior. citeturn21search1turn20search6 |
| **OpenAI Codex family** | CLI, IDE, desktop/app, web/cloud plus language SDKs; current repo explicitly separates these surfaces. 0.147.0 added portable Agent Plugins and major trust/automation changes. citeturn15search0turn12view0 | H `native`; A `native`; E `native` through SDK/app-server-class surfaces; CI `supported/configurable`; Adm `configurable`. | **Policy-dependent.** Do not carry CLI approval semantics onto cloud/app/SDK surfaces without separate evidence. 0.147.0 removed deprecated `codex exec --full-auto`. citeturn12view0 |
| **OpenCode** | TUI plus a standalone `opencode serve` HTTP server exposing OpenAPI 3.1; IDE clients use the same server model. Agent-callable skills use a native `skill` tool. citeturn20search12turn20search1 | H `native`; A `native`; E `native`; CI `supported`; Adm `configurable`. | **Configurable.** Permissions resolve `allow`, `ask`, or `deny`; `--auto` auto-approves otherwise-ask operations while explicit deny remains enforced. citeturn20search5 |
| **Hermes Agent** | CLI, Electron desktop, remote gateway, multi-agent/subagent execution, skills/MCP/tool gateway. 0.18.0 made Mixture-of-Agents and background fan-out first-class; 0.16.0 introduced native desktop and remote gateway surfaces. citeturn3search0 | H `native`; A `native`; E `supported`; CI `supported` for suitable CLI paths; Adm `configurable`. | Remote desktop/gateway reachability must not be equated with unattended CI reachability. Current per-tool approval evidence is less complete than release evidence. |
| **Antigravity CLI** | TUI, SSH-oriented remote usage, `-p` print/headless operation, custom agents, nested subagents, plugin skills, MCP and execution policies. citeturn4search0turn13view3 | H `native`; A `native`; E `supported`; CI `supported`; Adm `configurable`. | **Headless human-required calls are not magically approved.** Since 1.1.3 such tools are soft-denied instead of hanging/auto-approving; 1.1.4 made `-p` honor persisted permission/file/sandbox/auto-execution/artifact-review policy. citeturn13view3 |
| **Gemini CLI** | Historical predecessor with TUI/headless-style coding-agent lineage and MCP/tooling. Consumer channel transitioned to Antigravity CLI. citeturn2search2turn4search3 | Consumer H/A/E/CI: `deprecated` as a routing target after transition; enterprise actors: `unknown`. | Do **not** map the lack of enterprise evidence to `unavailable`. The official announcement establishes the individual/Google AI Pro/Ultra transition, not every enterprise entitlement. citeturn4search3 |
| **Qwen Code** | Interactive TUI, `qwen -p` headless mode with text/JSON and resumable sessions, IDE integration, SDKs, MCP, subagents and experimental `qwen serve` ACP-over-HTTP/SSE daemon. citeturn18search0turn18search3turn18search5turn18search8 | H `native`; A `native`; E `native` for headless / `experimental` daemon; CI `native` headless; Adm `configurable`. | Headless is specifically documented for automation/CI. Subagent approval modes differ; detached fork subagents are documented as interactive-session-only. citeturn18search3turn18search5 |
| **goose** | Desktop, CLI, embeddable API, 70+ documented MCP extensions, ACP-server operation, ACP agents as providers, recipes, subagents and provider portability. citeturn17search0 | H `native`; A `native`; E `native`; CI `supported/native` for recipe/API paths; Adm `configurable`. | Recipe automation is a stronger CI claim than desktop availability. ACP/MCP capabilities should be independently modeled as server/client roles. citeturn17search0 |
| **GitHub Copilot CLI** | CLI, GitHub MCP, `/fleet` parallel subagents, session resume, custom agents/skills, CLI↔IDE handoff, autopilot, `/remote`, plus ACP preview. citeturn18search2turn11search8 | H `native`; A `native`; E `experimental/supported` through ACP, not `/remote`; CI `unknown` for general autonomous CLI path; Adm `configurable`. | Persisted permission grants can remove repeated prompts, while remote steering still requires a live local CLI session. Organizational policy can disable CLI capabilities. citeturn18search4turn18search9turn18search7 |
| **Pi Agent** | Interactive coding agent/TUI, JSON RPC over stdin/stdout, direct `AgentSession` embedding, TypeScript extension API, provider selection and persistent sessions. citeturn17search15turn17search10turn17search2 | H `native`; A `native`; E `native`; CI `supported`; Adm `configurable`. | RPC is genuinely headless/programmatic. For Node/TS, Pi explicitly recommends direct `AgentSession` instead of subprocess RPC. citeturn17search15 |
| **Claude Agent SDK — Python** | `query()`, bidirectional `ClaudeSDKClient`, Claude Code tools, in-process SDK MCP servers, custom tools/hooks, programmatic subagents and session-forking capabilities. citeturn23search1 | H `supported`; A `native`; E `native`; CI `native`; Adm `configurable`. | `allowed_tools` auto-approves rather than removing tools; blocking requires disallowed-tool policy. Bundled CLI parity is version-specific. citeturn23search1turn23search8 |
| **Claude Agent SDK — TypeScript** | Programmatic Claude Code agent runtime with SDK-managed sessions/hooks and a release line that periodically declares parity with specific Claude Code versions. citeturn23search0turn23search11 | H `supported`; A `native`; E `native`; CI `native`; Adm `configurable`. | **Licensing is not parity-neutral:** the TS repo says use is governed by Anthropic Commercial Terms; do not inherit the Python repository's MIT characterization. citeturn23search0turn23search9 |
| **Codex SDK — Python** | `Codex`/`AsyncCodex`, threads, turns, streaming/control APIs and browser/device/API-key login; package installs a matching Codex CLI runtime dependency. citeturn15search2turn15search4turn15search9 | H `supported`; A `supported`; E `native`; CI `supported`; Adm `configurable`. | Strong version-coupling claim exists, but platform binary-wheel coverage is a separate compatibility dimension; an official issue documented a Linux ARM64 wheel gap in June. citeturn15search9turn15search10 |
| **Codex SDK — TypeScript** | Spawns/wraps Codex CLI using JSONL over stdio; supports multi-turn threads, streaming events, structured JSON output, resume and working-directory/environment/config controls. citeturn16search1 | H `supported`; A `supported`; E `native`; CI `supported`; Adm `configurable`. | This is an SDK over the CLI runtime, not independent proof that every app-server/cloud feature exists in the TS SDK. citeturn16search1 |
| **OpenAI Agents SDK — Python** | Agent/Runner loop, handoffs/agents-as-tools, tools, guardrails, sessions, tracing, MCP and current Sandbox Agent support. citeturn14search2turn14search3 | H `supported`; A `native`; E `native`; CI `native`; Adm `configurable`. | Guardrail scope is not universal across every hosted/built-in tool class; therefore “has guardrails” must not become “every tool invocation is guardrailed.” |
| **OpenAI Agents SDK — JS/TS** | Agent loop, handoffs, tools, HITL, tracing, realtime voice and beta Sandbox Agents with filesystem/shell/edit, snapshots, resume and memory. citeturn14search0turn14search1 | H `supported`; A `native`; E `native`; CI `native`; Adm `configurable`. | Sandbox Agents are beta; 0.11.0 tightened local-source materialization boundaries, requiring explicit path grants for outside-base-directory sources. citeturn14search1 |
| **OpenAI Python SDK** | Typed sync/async OpenAI REST/API client; Responses API is identified as its primary model API. citeturn22search0 | H `supported`; A intrinsic `unavailable`; E `native`; CI `native`; Adm `configurable` through application/environment policy. | **Not a harness.** It does not itself establish an agent loop, human approvals, session orchestration or sandbox. Those belong to caller code or a higher-level SDK. citeturn22search0 |
| **OpenAI Node SDK** | Generated JavaScript/TypeScript API client with WebSocket and administration/API surfaces; release line evolves with API schema. citeturn22search1turn16search8 | H `supported`; A intrinsic `unavailable`; E `native`; CI `native`; Adm `configurable`. | Provider/API feature availability must not be promoted to agent-native capability without a harness or orchestration layer. |
| **Anthropic Python SDK** | Claude API client plus newly generated Managed Agents, memory, MCP tunnel and related API surfaces in its July release line. citeturn23search6 | H `supported`; A intrinsic `unavailable` as an SDK actor; E `native`; CI `native`; Adm `configurable`. | Keep separate from Claude Agent SDK. 0.120.1's MCP-v2 restriction was superseded by 0.120.2 on the same day. citeturn23search6 |
| **Anthropic TypeScript SDK** | Server-side TS/JS Claude API SDK, Node 18+, separate from Claude Agent SDK. citeturn22search2 | H `supported`; A intrinsic `unavailable`; E `native`; CI `native`; Adm `configurable`. | Recent release-history/parity evidence was not retrieved well enough to make version-specific Managed-Agent/MCP claims; those remain `unknown`, not unavailable. |

Several capability families should explicitly remain **unknown** where this pass did not collect adequate product-specific evidence. In particular, a product's access to web research, browser/computer use, voice or artifact generation through a model/provider/MCP extension does not prove a native harness capability. Hermes, for example, did explicitly add optional gateway web search, image generation, TTS and browser automation in 0.10.0, while goose documents browser-like functionality primarily through extensions. Those should map differently in the taxonomy. citeturn3search1turn17search0

Likewise, **structured output must be surface-specific**. Qwen's headless documentation explicitly promises text or JSON output with consistent exit codes, while Codex's TypeScript SDK explicitly accepts a JSON schema per turn. Those are strong CI/evaluation claims. A current TUI displaying JSON is not equivalent evidence. citeturn18search3turn16search1

The strongest current **deterministic policy interception** evidence belongs to Claude Code hooks: its hook lifecycle includes `PreToolUse`, `PermissionRequest`, post-tool events, subagent events and more; permission hooks can allow/deny requests, modify tool input and apply permission updates, while matching deny/ask policy still takes precedence. This is materially stronger governance evidence than “supports hooks.” citeturn21search0turn21search1

## Release backfill and product lineage

The attached release ledger contains 64 high/medium-confidence release or lifecycle objects. It preserves fixes as fixes rather than retroactively treating them as capability introductions. Versions with a confirmed release object but incompletely normalized body are deliberately marked `review_needed` rather than populated with guessed feature items.

| Date | Track/version | Evidence-derived event | Registry consequence |
|---|---|---|---|
| **2026-04-15** | Qwen Code lifecycle | Qwen OAuth free tier was discontinued; users must move to Coding Plan or API/provider credentials. citeturn18search0 | Auth routing/entitlement change; do not generate workflows assuming free Qwen OAuth. |
| **2026-04-16** | Hermes 0.10.0 | Tool Gateway added optional web search, image generation, TTS and browser automation through Nous Portal. citeturn3search1 | First known version for several external-tool/media capabilities. |
| **2026-04-28** | OpenAI Node 6.35.0 | Added Responses compact/cache and web-search inclusion changes plus expanded WebSocket support. citeturn22search1 | Provider-SDK capability/type update, not an agent-harness introduction. |
| **2026-05-01** | OpenAI Node 6.36.0 | Added/changed Admin API Key and admin-resource support. citeturn22search1 | Administrator/API governance surface. |
| **2026-05-05** | Agents JS 0.9.0 | Introduced beta Sandbox Agents with persistent workspaces, filesystem/shell/patch capabilities, snapshots/resume, memory and multiple sandbox backends. citeturn14search1 | Major new execution/orchestration node; external orchestrator and CI become first-class for sandbox agents. |
| **2026-05-06** | OpenAI Python 2.35.0/2.35.1 | API/image changes and legacy Python CLI removal, followed by image-size enum regression fix. citeturn22search9 | Preserve `changed/removed` separately from next-day fix. |
| **2026-05-07** | Pi 0.74.0 | Pi moved repository/package identity to Earendil; `@earendil-works/*` became the new package scope and old packages were deprecated. citeturn3search3turn17search6 | First-class predecessor/successor and package-coordinate migration. |
| **2026-05-07** | Agents JS 0.10.0 | Changed default model and added unlimited-turn option, SDK-side function-tool concurrency and server-prefixed MCP tool naming. citeturn14search1 | Model/default behavior and orchestration controls should be versioned. |
| **2026-05-08** | Agents JS 0.11.0 | Tightened Sandbox Agent local-source materialization boundary and changed realtime default model. citeturn14search1 | Security/governance change; external path grants may become required. |
| **2026-05-11 to 2026-05-22** | Agents JS 0.11.2–0.11.5 | Sandbox extraction limits, tracing resilience, local approval-rejection preservation and tracing-usage fixes. citeturn14search1 | Mostly fixes/improvements, **not** new capability introductions. |
| **2026-05-22** | Claude Agent SDK TS 0.3.149 | Corrected custom environment handling and documented that SDK `env` replaces rather than merges process environment. citeturn23search11 | CI/environment isolation behavior; possible secret/config impact. |
| **2026-05-27** | Claude Agent SDK TS 0.3.152 | Added SessionStart abilities to reload skills/set title and MessageDisplay transformation/hiding. citeturn9search6 | New hook/event capability. |
| **2026-05-27** | Qwen 0.16.2 | Added worktree startup, memory-related behavior and permission-command-substitution changes among other features. citeturn5search4 | Worktree/memory/permission entries need version floor. |
| **2026-05-29** | Hermes 0.15.1/0.15.2 | Skills/MCP/UI fixes followed by package-manifest correction. citeturn3search0 | Do not promote patch fixes to first introduction without earlier release proof. |
| **2026-06-05** | Hermes 0.16.0 | Added native Electron desktop, authenticated remote gateway and concurrent sessions, alongside security fixes. citeturn3search0 | New desktop/remote surfaces plus security review trigger. |
| **2026-06-08** | Claude Code 2.1.169 | Added `--safe-mode`/`CLAUDE_CODE_SAFE_MODE`, `/cd`, bundled-skill control and managed-MCP fixes. citeturn2search4 | New safe execution profile and enterprise policy behavior. |
| **2026-06-12** | Qwen 0.18.0 | Stable 0.18.0 appears in official repository release metadata. citeturn18search0 | Version lineage confirmed; release body still requires detailed collector normalization. |
| **2026-06-18** | Gemini → Antigravity | Google-set consumer transition deadline for Gemini CLI/Code Assist extensions to Antigravity CLI. citeturn4search3 | **Breaking lifecycle/routing event.** Preserve Gemini history; add successor relation. |
| **2026-06-19** | Hermes 0.17.0 | “Reach” release on official release feed. citeturn3search0 | Version lineage confirmed; item-by-item backfill still needs release-body traversal. |
| **2026-06-30** | Anthropic Python 0.115.0 | Added Managed Agents event-delta streaming, overrides, reverse pagination, scoped vault credentials and agent/deployment webhook events. citeturn23search6 | Major provider-SDK Managed Agents control surface. |
| **2026-06-30** | Antigravity 1.0.14 | Subagent/plugin/MCP behavior fixes on the first collected Antigravity sequence. citeturn13view3 | Start of high-confidence contiguous Antigravity backfill. |
| **2026-07-01** | Hermes 0.18.0 | “Judgment”: Mixture-of-Agents, completion contracts, gateway scaling/draining, desktop coding projects/memory graph and background fan-out. citeturn3search0 | One of the largest orchestration capability jumps in the window. |
| **2026-07-01 to 2026-07-02** | Antigravity 1.0.15–1.0.16 | Added/changed background-task visibility, dynamic subagent representation, permission-hook handling and MCP behavior. citeturn13view3 | Subagent/background execution maturity. |
| **2026-07-02** | Anthropic Python 0.116.0 | Added `agent-memory-2026-07-22` beta-header support. citeturn23search6 | Experimental provider-level memory surface; do not equate with Claude Code local memory. |
| **2026-07-08** | Antigravity 1.1.0 | Introduced/changed execution-mode cycle, request-review before writes and `/plan` behavior. citeturn13view3 | Human mediation becomes explicit versioned surface. |
| **2026-07-10** | Antigravity 1.1.1 | Added `--agent`/agents, nested subagents and permission-related fixes. citeturn13view3 | First known custom/nested-agent floor in ledger. |
| **2026-07-13** | Antigravity 1.1.2 | Improved headless OAuth/fail-fast/exit behavior and command-substitution allowlist handling. citeturn13view3 | CI robustness/security change. |
| **2026-07-16** | Antigravity 1.1.3 | Headless tools that need approval became soft-denied instead of hanging or silently approving. citeturn13view3 | **Major actor-access change** for CI/external orchestration. |
| **2026-07-16** | Anthropic Python 0.117.0 | Added dreaming and MCP Tunnels; protected credential material from traceback frame locals. citeturn23search6 | Capability plus credential-security event. |
| **2026-07-18** | Antigravity 1.1.4 | `-p` began honoring persisted permissions/file/sandbox/auto-execution/artifact-review policy. citeturn13view3 | Recommended minimum version for policy-sensitive headless routing. |
| **2026-07-21** | Claude Code 2.1.217 | Added/fixed substantial managed OTEL, TLS/mTLS/OAuth/proxy, permission, workspace-symlink, MCP-output and subagent governance behavior; documented max concurrent subagents default 20 and nested-subagent controls. citeturn13view1 | Security/governance minimum-version review for enterprise adapters. |
| **2026-07-21** | Antigravity 1.1.5 | Added `/effort`/`--effort`, stable model slugs and custom-agent model selection. citeturn13view3 | Model/reasoning control and custom-agent parity. |
| **2026-07-22** | Anthropic Python 0.118.0 | Added Managed Agents model effort, initial session events and thread delta streaming. citeturn23search6 | Agent control/streaming API expansion. |
| **2026-07-23** | Anthropic Python 0.119.0 | Added `model_context_window_exceeded` stop reason and fixed binary-file handling in agent toolset read/edit. citeturn23search6 | Output/error-state taxonomy plus tool fix. |
| **2026-07-24** | Antigravity 1.1.6 | Added richer custom-agent policy fields, progressive code search and plugin skill discovery, with additional execution hardening. citeturn4search1turn13view3 | Current high-confidence Antigravity baseline in this run. |
| **2026-07-24** | Anthropic Python 0.120.0 | Added Claude Opus 5 types, tool addition/removal blocks and `tool_change` events. citeturn23search6 | Dynamic tool-set/provider-event support. |
| **2026-07-27** | OpenCode 1.18.6/1.18.7 | Immutable releases with branch-cache/desktop/MCP compatibility and desktop fixes. citeturn13view2 | Valuable immutable provenance, but fixes should not be interpreted as feature introductions. |
| **2026-07-28** | Anthropic Python 0.120.1 → 0.120.2 | 0.120.1 pinned MCP `<2`; 0.120.2 one hour later added MCP SDK v2 alongside v1. citeturn23search6 | Preserve both historical facts; current state is v1+v2 support at 0.120.2. |
| **2026-08-07** | Codex 0.147.0 | Portable Agent Plugins, persistent conversation sections, `--approve-for-me`, Cursor skill/conversation import, opt-in MCP 2026-07-28, trust/redaction hardening and removal of deprecated `exec --full-auto`. citeturn12view0 | **Highest-priority Codex adapter/governance migration in the window.** |
| **2026-08-08** | Codex 0.148.0-alpha.5 | Alpha published on official release feed. citeturn12view0 | Preserve prerelease channel; do not route stable production adapters to it implicitly. |

The Antigravity sequence is the closest to a genuinely contiguous, release-by-release backfill in this pass because the product is young and the official release page exposed a tractable sequence from 1.0.14 through 1.1.6. citeturn13view3 By comparison, OpenCode and Codex have extremely high release volume, and repository/search snapshots were demonstrably stale; a complete HCR backfill for those products should be generated from release/package APIs rather than assuming a search page listed every event. citeturn15search0turn13view2turn12view0

The **Gemini → Antigravity lineage must be first-class** rather than modeled as a rename. Google describes Antigravity CLI as sharing the Antigravity 2.0 harness while announcing the consumer transition away from Gemini CLI. That makes predecessor/successor, channel and entitlement fields more accurate than changing `name` in place. citeturn4search0turn4search3

The same applies to **Pi**. The May 7 migration changed repository ownership and npm package scope to Earendil while preserving the product lineage; deleting old `@mariozechner/*` coordinates from historical records would make prior environment manifests irreproducible. citeturn3search3turn17search6

## Source quality, conflicts, coverage, and provenance

The source inventory favors direct vendor evidence. The full 42-record inventory records authority tier, purpose, cadence, collector feasibility, access date and known limitations.

| Source family | Authority / collector assessment | Key evidence |
|---|---|---|
| Claude Code | GitHub Releases are Tier 1 for version events; `code.claude.com` is Tier 2 current-state evidence. Hooks/permissions/subagent docs are particularly precise. | citeturn13view1turn21search0turn21search1turn21search2 |
| OpenAI Codex | Official OpenAI GitHub release objects and repo/source docs. Release feed should beat stale repository-search metadata. | citeturn12view0turn15search0 |
| Codex SDKs | Official source docs in `openai/codex`; strong API/invocation detail, but main-branch docs are mutable. | citeturn15search2turn15search4turn16search1 |
| OpenCode | Official docs plus GitHub immutable release objects on recent versions. Strong programmatic-server and permissions evidence. | citeturn20search12turn20search5turn13view2 |
| Hermes | Official GitHub Releases are strong for version chronology; some releases summarize very large PR batches, so full item normalization requires PR traversal. | citeturn3search0 |
| Antigravity | Official Google GitHub repo/releases plus Google lifecycle announcement. Strongest bounded release inventory in this pass. | citeturn4search0turn13view3turn4search3 |
| Qwen | Official repository and dedicated current docs. Stable/nightly/preview channels require explicit channel preservation. | citeturn18search0turn18search3turn18search5 |
| goose | Official AAIF/legacy Block-hosted docs are strong for current capabilities; release-feed indexing was incomplete. | citeturn17search0turn17search3 |
| Copilot CLI | GitHub product/docs/repo sources are strong for current behavior; public-preview ACP and changing autopilot semantics require versioned/mode-specific modeling. | citeturn18search2turn18search4turn11search8 |
| Pi | Official Pi docs provide unusually explicit RPC/SDK/extension detail; lifecycle move is officially documented. | citeturn17search15turn17search10turn3search3 |
| OpenAI Agents SDKs | Official SDK docs/repos and signed GitHub releases. JS has particularly useful versioned Sandbox Agent history. | citeturn14search2turn14search0turn14search1 |
| Provider SDKs | Official generated SDK repos/releases. They are excellent evidence of API shape but weak evidence for harness-native actor behavior because they are not agent harnesses. | citeturn22search0turn22search1turn23search6turn22search2 |

**Principal unresolved conflicts**

| Conflict | Assessment | HCR state now |
|---|---|---|
| **HCR baseline/schema unavailable** | Canonical IDs, existing claims and true RFC 6902 paths cannot be inspected. Silently synthesizing them would violate the registry's epistemic rules. | `unknown`; reviewer-blocked. |
| **Claude Agent SDK licensing parity** | Python repository metadata identifies MIT licensing while the TypeScript README states use is governed by Anthropic's Commercial Terms. Language parity cannot be assumed for procurement/governance. citeturn23search1turn23search0turn23search9 | Separate track-level governance metadata. |
| **Copilot “every action requires approval” vs autopilot/persisted permissions** | Not truly contradictory once mode is modeled. Persisted approvals can suppress repeated prompts, and GitHub markets autopilot as operating without step-by-step approval. citeturn18search4turn18search2 | `configurable`, with mediation per permission/mode. |
| **Gemini fully dead after June 18** | Official evidence proves a consumer transition, not universal enterprise termination. citeturn4search3 | Consumer `deprecated`; enterprise `unknown`. |
| **Anthropic Python MCP v2** | 0.120.1 pinning `<2` was superseded approximately an hour later by 0.120.2 supporting v2 alongside v1. citeturn23search6 | Current `supported`; retain both historical events. |
| **Codex `exec --full-auto`** | 0.147.0 explicitly removes this deprecated form. Any registry claim showing it as current is stale. citeturn12view0 | `deprecated/removed`; route to explicit sandbox policy. |
| **OpenCode `tools` booleans as current policy** | Current docs say they were deprecated as of v1.1.1 and merged into `permission`, while compatibility remains. citeturn20search5 | `deprecated`, with compatibility note. |
| **Qwen release ordering from version alone** | Stable, preview/nightly and SDK lines coexist; channel and publication timestamp must be first-class. citeturn18search0 | Collector review required. |

**Coverage scoring** uses 0–5 independently for **RH** release-history completeness, **Docs** current documentation, **Actors**, **Inv** invocation detail, **Lin** version/product lineage, **Gov** security/governance and **Conf** overall evidentiary confidence. There is deliberately **no aggregate rank**.

| Track | RH | Docs | Actors | Inv | Lin | Gov | Conf | Why |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Claude Code | 3 | 5 | 5 | 5 | 4 | 5 | 4 | Current official permission/hook/subagent evidence is excellent, but the entire 120-day release feed was not enumerated. citeturn21search0turn21search1turn13view1 |
| OpenAI Codex | 3 | 5 | 4 | 5 | 4 | 5 | 4 | Excellent current surfaces/SDKs and 0.147 evidence; very high release cadence prevents an exhaustive historical claim. citeturn12view0turn15search0turn16search1 |
| OpenCode | 2 | 5 | 5 | 5 | 3 | 5 | 4 | Excellent server/skills/permission documentation but only a narrow slice of its high-volume release history was normalized. citeturn20search12turn20search1turn13view2 |
| Hermes | 4 | 3 | 3 | 3 | 4 | 4 | 4 | Strong major-release chronology; less precise current actor/invocation documentation than the leading tracks. citeturn3search0 |
| Antigravity CLI | 5 | 4 | 5 | 5 | 5 | 5 | 5 | Bounded young release line, precise headless semantics and explicit Gemini transition. citeturn13view3turn4search3 |
| Gemini CLI | 2 | 3 | 2 | 2 | 5 | 2 | 3 | Lifecycle is clear for consumers; enterprise status and complete pre-transition history are not. citeturn4search3 |
| Qwen Code | 2 | 5 | 5 | 5 | 4 | 4 | 4 | Strong headless/MCP/subagent docs; channel/version normalization remains incomplete. citeturn18search0turn18search3turn18search5 |
| goose | 1 | 5 | 4 | 4 | 4 | 4 | 3 | Current capability docs are rich; release history was not retrieved with sufficient freshness. citeturn17search0turn17search3 |
| Copilot CLI | 2 | 5 | 5 | 5 | 4 | 5 | 4 | Excellent current permission/remote/fleet/governance evidence; historical version mapping remains partial. citeturn18search2turn18search4turn18search9 |
| Pi | 2 | 5 | 4 | 5 | 5 | 4 | 4 | Excellent RPC/extensions/lineage docs; post-migration release enumeration is partial. citeturn17search15turn17search10turn3search3 |
| Claude Agent SDK Py | 2 | 4 | 4 | 4 | 4 | 4 | 3 | Strong API/repo evidence; exact current package sequence and bundled CLI parity need automated collection. citeturn23search1turn23search8 |
| Claude Agent SDK TS | 2 | 4 | 4 | 4 | 4 | 4 | 3 | Good API/release evidence, but later releases remain incomplete and licensing is an important language-specific distinction. citeturn23search0turn23search11 |
| Codex SDK Py | 1 | 5 | 4 | 5 | 4 | 4 | 4 | Excellent current docs and explicit runtime coupling, but package history was not independently enumerated. citeturn15search2turn15search9 |
| Codex SDK TS | 1 | 5 | 4 | 5 | 3 | 4 | 4 | Excellent embedding/streaming/structured-output detail, weak historical release coverage. citeturn16search1 |
| Agents SDK Py | 1 | 5 | 5 | 5 | 3 | 5 | 4 | Strong current architecture/governance docs; release ledger is the principal gap. citeturn14search2turn14search3 |
| Agents SDK JS/TS | 3 | 5 | 5 | 5 | 4 | 5 | 4 | Detailed May release sequence plus excellent current docs; later history may be missing. citeturn14search0turn14search1 |
| OpenAI Python SDK | 2 | 4 | 4 | 4 | 4 | 4 | 3 | Official generated SDK evidence is sound but release-index freshness prevented complete July/August backfill. citeturn22search0turn22search9 |
| OpenAI Node SDK | 2 | 4 | 4 | 4 | 4 | 4 | 3 | Detailed April/May releases collected; later history remains incomplete. citeturn22search1 |
| Anthropic Python SDK | 4 | 4 | 4 | 4 | 4 | 5 | 5 | Strong official release sequence through 0.120.2, including Managed Agents, memory/MCP and credential-security changes. citeturn23search6 |
| Anthropic TypeScript SDK | 1 | 4 | 3 | 3 | 3 | 3 | 2 | Current API basics are well evidenced, but recent release history and feature parity were not retrieved sufficiently. citeturn22search2 |

The critical methodological lesson from those scores is that **documentation coverage and release-history coverage are orthogonal**. OpenCode, goose, Pi and several SDKs have excellent current documentation but incomplete historical ledgers; Anthropic Python currently has unusually good release chronology. Treating either dimension as a proxy for the other would produce overconfident HCR state.

**Representative source map** — the complete machine-readable map contains all 113 proposed changes. Access date for every source below is **2026-08-08**.

| Proposed change | Authoritative evidence | Source date |
|---|---|---|
| `rel.codex.0.147.0` | Official OpenAI Codex release object. citeturn12view0 | 2026-08-07 |
| `cap.codex.sdk-ts` | Official Codex TS SDK README. citeturn16search1 | current docs |
| `cap.codex.sdk-py` | Official Codex Python SDK README/getting started/API. citeturn15search2turn15search4turn15search9 | current docs |
| `cap.claude-code.permissions` | Claude Code permissions reference. citeturn21search1 | current docs |
| `cap.claude-code.hooks` | Claude Code hooks reference. citeturn21search0 | current docs |
| `cap.opencode.server` | OpenCode server documentation. citeturn20search12 | current docs |
| `cap.antigravity.headless` | Antigravity official releases. citeturn13view3 | 2026-07-16/18 |
| `rel.gemini.consumer-transition` | Official Google transition announcement. citeturn4search3 | 2026-06-18 deadline |
| `cap.qwen.headless` | Qwen headless docs. citeturn18search3 | current docs |
| `cap.goose.protocols` | Official goose documentation. citeturn17search0 | current docs |
| `cap.copilot.permissions` | GitHub permissions and current product docs. citeturn18search4turn18search2 | current docs |
| `cap.pi.rpc` | Official Pi RPC docs. citeturn17search15 | current docs |
| `cap.agents-js.sandbox` | Official OpenAI Agents JS release history/repo. citeturn14search1turn14search0 | introduced 2026-05-05 |
| `rel.anthropic-py.0.120.2` | Anthropic Python release object. citeturn23search6 | 2026-07-28 |
| `harness.candidate.antigravity-sdk-python` | Official Google SDK repository. citeturn20search3 | current |
| `harness.candidate.openai-codex-security` | Official OpenAI Codex Security SDK/CLI repository. citeturn16search4 | current |
| `harness.candidate.github-copilot-sdk` | GitHub's current Copilot CLI product page. citeturn18search2 | current |

## Registry patch artifacts

The complete artifact set is attached as syntactically valid JSON. Because the requested schemas were unavailable, these are explicitly **file-level merge fragments**, which satisfies the requested alternative to RFC 6902 without inventing JSON Pointer paths or canonical IDs.

**Primary bundle:** [Download the complete HCR audit bundle](sandbox:/mnt/data/hcr_agentic_harness_audit_2026-08-08.zip)

| Deliverable | Artifact |
|---|---|
| Research/validation manifest | [manifest.json](sandbox:/mnt/data/hcr_agentic_harness_audit_2026-08-08/manifest.json) |
| Source inventory | [sources.proposed.json](sandbox:/mnt/data/hcr_agentic_harness_audit_2026-08-08/sources.proposed.json) |
| Release ledger patch | [releases.proposed.json](sandbox:/mnt/data/hcr_agentic_harness_audit_2026-08-08/releases.proposed.json) |
| Capability implementation patch | [capabilities.proposed.json](sandbox:/mnt/data/hcr_agentic_harness_audit_2026-08-08/capabilities.proposed.json) |
| Harness/track patch | [harnesses.proposed.json](sandbox:/mnt/data/hcr_agentic_harness_audit_2026-08-08/harnesses.proposed.json) |
| Conflict log | [conflicts.json](sandbox:/mnt/data/hcr_agentic_harness_audit_2026-08-08/conflicts.json) |
| Coverage report | [coverage.json](sandbox:/mnt/data/hcr_agentic_harness_audit_2026-08-08/coverage.json) |
| File-level patch plan | [patch-plan.json](sandbox:/mnt/data/hcr_agentic_harness_audit_2026-08-08/patch-plan.json) |
| Complete change→source map | [source-map.json](sandbox:/mnt/data/hcr_agentic_harness_audit_2026-08-08/source-map.json) |
| Runtime verification backlog | [verification-backlog.json](sandbox:/mnt/data/hcr_agentic_harness_audit_2026-08-08/verification-backlog.json) |
| AOS workflow impacts | [workflow-impacts.json](sandbox:/mnt/data/hcr_agentic_harness_audit_2026-08-08/workflow-impacts.json) |
| Bundle notes | [README.md](sandbox:/mnt/data/hcr_agentic_harness_audit_2026-08-08/README.md) |

The manifest's validation state is intentionally equivalent to:

```json
{
  "validation": {
    "json_syntax": "passed",
    "referential_checks": "passed_for_local_source_ids",
    "json_schema": "not_run_baseline_schemas_unavailable",
    "rfc6902": "not_generated_baseline_paths_unavailable"
  }
}
```

The capability patch likewise does **not** make up taxonomy identifiers. Each provisional implementation uses a human-readable `candidate_capability_key` plus:

```json
{
  "canonical_mapping_status": "blocked_baseline_taxonomy_unavailable"
}
```

That is preferable to silently replacing established HCR terminology. Once `registry/taxonomy.json` is available, each candidate key should be mapped to an existing canonical node or submitted as a documented taxonomy migration.

The patch plan is grouped by reviewer responsibility rather than pretending every item has the same confidence. Source records go first to the provenance owner; release events to the release-archaeology owner; capabilities jointly to taxonomy and harness owners; lineage/track changes to the registry maintainer. Low/medium-confidence release records are flagged `review_needed`, and unknown dates remain `null` instead of guessed.

## Verification backlog and AOS workflow impact

The highest-value runtime tests are those that turn **documentation statements into observed actor-access evidence**, especially where documentation describes approval behavior.

| Priority | Runtime verification | Why it matters |
|---|---|---|
| **P0** | Load the real HCR baseline and schemas; map candidate IDs, validate objects and generate true RFC 6902 patches. | Converts the current candidate overlay into mergeable registry state. |
| **P0** | Codex same-version matrix: CLI/TUI, app-server, Python SDK and TS SDK; test approvals, sandbox, structured output, resume/fork, MCP and plugins. | Prevents unjustified CLI↔SDK↔RPC parity assumptions. Official SDK architecture already shows materially different transports. citeturn16search1turn15search9 |
| **P0** | Claude Code default/`dontAsk`/`auto`/`bypassPermissions` plus managed-deny matrix under noninteractive execution and permission hooks. | Converts the current detailed policy documentation into CI-observed mediation evidence. citeturn21search1turn21search0 |
| **P0** | Antigravity `-p` under request-review, accept-edits and plan policies on ≥1.1.4, including tools that would require human approval. | Confirms documented soft-deny/no-hang behavior and the safe CI minimum. citeturn13view3 |
| **P0** | Copilot default vs persisted allow vs autopilot vs organization-managed policy for shell, edits and MCP. | Resolves the strongest current “explicit approval” ambiguity into a mode matrix. citeturn18search2turn18search4 |
| **P1** | OpenCode HTTP server with and without Basic Auth; drive prompt/tool/permission flows through OpenAPI. | Proves true external-orchestrator reach rather than merely server existence. citeturn20search12 |
| **P1** | Qwen `-p` JSON, stdin, exit codes, resume, subagent modes, MCP and experimental ACP daemon in a TTY-less runner. | Converts its strong headless docs into CCDash CI evidence. citeturn18search3turn18search5 |
| **P1** | goose CLI/API/ACP parity with identical recipe, MCP, provider and subagent task. | Separates its unusually broad protocol/surface profile into observable behavior. citeturn17search0 |
| **P1** | Pi RPC vs direct `AgentSession`: session state, extension hooks, tool calls and provider switching. | Establishes whether `pi-agent-core` should be an independent routing track. citeturn17search15turn17search10 |
| **P1** | Claude Agent SDK Python/TS: record bundled/runtime CLI version and test option, hook, tool, session-fork and subagent parity. | Prevents release-number or branding parity from becoming assumed functional parity. citeturn23search8turn23search11 |
| **P1** | OpenAI Agents SDK Python/JS tool-guardrail/HITL matrix across function, MCP, shell, computer and sandbox tools. | Ensures “guardrails” is scoped to the exact tool classes they actually mediate. citeturn14search2turn14search0 |
| **P1** | Codex Security CI scan with minimal inherited environment, API-key authentication and attempted approval/sandbox overrides. | Confirms its intentionally distinct `approvalPolicy: "never"` and security boundary. citeturn16search4 |
| **P2** | Automated GitHub Releases + npm/PyPI collector across all tracks for 2026-04-10–2026-08-08. | Required to upgrade the release-history dimension from “substantial” to genuinely exhaustive. |
| **P2** | Google enterprise entitlement/lifecycle test for Gemini CLI and Antigravity. | Converts enterprise Gemini state from `unknown`. |
| **P2** | Antigravity SDK Python wheel/runtime matrix plus hooks/MCP/triggers/stateful session tests. | Final acceptance test for the recommended new SDK track. citeturn20search3 |
| **P2** | Inventory the official Copilot SDK package, reference docs and releases; compare its permission/session behavior with CLI ACP. | Determines whether Copilot SDK becomes a first-class track rather than a capability surface. citeturn18search2 |

The most urgent **workflow impact** is Codex 0.147.0. Any Execution Engine template or CI adapter still invoking deprecated `codex exec --full-auto` needs migration to explicit sandbox/approval configuration before a 0.147+ minimum is enforced. The same release also introduces new trust, redaction and plugin behavior, so SkillBOMs and governance rules that assume the pre-plugin architecture need review. citeturn12view0

The second is the **Gemini → Antigravity transition**. Control-plane rules for individual/Google AI Pro/Ultra users should point terminal work to Antigravity after June 18, while the Gemini track remains in HCR as historical/predecessor data and as an `unknown` enterprise channel until enterprise evidence closes the gap. citeturn4search3

The third is **noninteractive approval semantics**. Antigravity ≥1.1.3 must not be expected to conjure a human approval in CI; Claude Code's permission/hook modes need to be explicit in adapters; OpenCode generated configuration should use `permission` rather than deprecated `tools`; and Copilot must be routed based on its active approval/autopilot policy rather than a global “requires approval” flag. citeturn13view3turn21search1turn20search5turn18search4

The fourth is **environment and dependency governance**. Claude Agent SDK TS's custom `env` semantics can replace the subprocess environment, Pi changed npm coordinates at 0.74.0, Agents JS tightened host-to-sandbox source boundaries, and Anthropic Python 0.120.1 should not become an accidental MCP-v2 pin because 0.120.2 immediately superseded it. citeturn23search11turn3search3turn14search1turn23search6

The fifth is **subagent resource governance**. Claude Code 2.1.217's documented default max of 20 concurrent subagents and disabled-by-default nested subagents means Control Plane concurrency assumptions should be expressed as versioned harness constraints, not solely as AOS scheduler limits. citeturn13view1 Qwen and Antigravity also expose distinct subagent approval/nesting models, making a generic `supports_subagents: true` field inadequate. citeturn18search5turn13view3

## Integration plan

**HCR** should ingest source inventory first, then lifecycle/release facts, then capability claims. Product surfaces should become independently addressable routing dimensions: for example `codex.cli`, `codex.sdk.python`, `codex.sdk.typescript`, `codex.app_server`, `codex.app`, and `codex.web` should not inherit capability states from each other unless an evidence claim explicitly establishes parity. The same principle should apply to Claude Code vs Claude Agent SDK, and to provider SDKs vs agent SDKs. citeturn15search0turn15search2turn16search1turn23search1

**SkillMeat / SkillBOMs** should add minimum/maximum harness version, surface, actor and approval assumptions beside every skill dependency. A skill relying on Codex's removed `exec --full-auto`, an Antigravity interactive approval prompt, or OpenCode's old `tools` syntax should fail compatibility resolution before execution, not at runtime. citeturn12view0turn13view3turn20search5 Skill dependencies should also distinguish an **agent-callable native skill** from a human slash command: OpenCode explicitly exposes skills through an agent-native `skill` tool, while analogous interfaces on other products must be separately proven. citeturn20search1

**CCDash** should become the empirical layer for the actor model. Each observation should capture `harness_id`, exact version/hash, product surface, actor, invocation, permission mode, TTY presence, network/sandbox policy, approval requested/approved/denied, exit code, structured-output conformance, tool/MCP calls, session IDs and artifacts. Documentation evidence can then be tagged `documented`; CCDash runs become `observed`; contradictions become automatic conflict objects rather than silently selecting one source.

**MeatyWiki** should receive human-readable lineage and conflict pages generated from HCR, especially for Gemini→Antigravity, Pi's package/repository move, Codex skills→plugins evolution, and language-SDK parity/licensing distinctions. The registry should remain machine-normalized while MeatyWiki preserves vendor wording, rationale, migration impact and source chronology. Google's transition and Pi's move are particularly clear examples where overwriting the old product record would destroy useful history. citeturn4search3turn3search3

**Execution Engine** routing should use a capability predicate rather than a product-name predicate. A viable selection tuple is effectively:

```json
{
  "capability": "execution.headless",
  "actor": "ci_runner",
  "requires_human_mediation": false,
  "structured_output": true,
  "sandbox_policy": "required",
  "surface": ["cli", "sdk", "rpc"],
  "version_constraint": "registry-derived",
  "evidence_requirement": ["official", "ccdash_observed"]
}
```

That would distinguish Qwen's documented headless JSON mode, Pi RPC, OpenCode server orchestration, Antigravity's soft-deny headless semantics and a human-facing remote-control surface such as Copilot `/remote`. citeturn18search3turn17search15turn20search12turn13view3turn18search9

**Governance** should stop storing a single autonomy/approval flag. The normalized policy object needs at minimum tool/action scope, actor, product surface, default decision, persistent approval scope, headless behavior, sandbox boundary, administrator override, hook/policy interception and whether the enforcement mechanism is host-side or model-instruction-only. Claude Code explicitly says permissions are enforced by Claude Code rather than by model instructions, and its sandbox is a complementary OS-level boundary; that is exactly the kind of distinction HCR should preserve. citeturn21search1 OpenCode's explicit allow/ask/deny model and Codex Security's fixed scan profile give two other distinct governance profiles that should not collapse into one enum. citeturn20search5turn16search4

**Agentic Control Plane** should use HCR lineage and evidence freshness during routing. A route should fail closed when a required actor/surface combination is `unknown`; it should not treat missing docs as `unavailable`, nor downgrade human mediation simply because a UI demonstrates the feature. For lifecycle transitions, the router should select successor channels based on entitlement while retaining predecessor records for replay/reproducibility. For prereleases such as Codex 0.148.0-alpha.5, channel must be an explicit routing constraint rather than inferred from “latest.” citeturn12view0turn4search3

The merge sequence should therefore be: **source provenance → release/lifecycle ledger → lineage/surface model → canonical taxonomy reconciliation → current capability/actor claims → conflict review → runtime CCDash verification → routing/policy promotion**. The current bundle is suitable for the first four review stages except for canonical-taxonomy reconciliation, which remains blocked on the missing HCR baseline.

**Artifact bundle:** [hcr_agentic_harness_audit_2026-08-08.zip](sandbox:/mnt/data/hcr_agentic_harness_audit_2026-08-08.zip)

#AgenticAI #HarnessCapabilityRegistry #ClaudeCode #OpenAICodex #Antigravity #OpenCode #AgentSDK #MCP #AgentGovernance #ReleaseEngineering #CCDash #AOS

**Rough conversation token estimate:** ~135k tokens.