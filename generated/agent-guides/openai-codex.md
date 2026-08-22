---
schema_version: 0.1
harness_id: openai-codex
generated_at: 2026-08-22T13:02:17.406799Z
artifact_kind: harness_capability_guide
---

# OpenAI Codex — Agent Capability Guide

**Vendor:** OpenAI  
**Lifecycle:** active  
**Current version in registry:** 0.147.0  
**Last verified:** 2026-08-08T20:00:00Z

> UI availability does not imply that an in-harness model or an external orchestrator can invoke the capability. Use the actor-specific sections below.

## Human operator

- **CI/GitHub automation** (`supported`): The official Codex GitHub Action runs `codex exec` in CI to apply patches or post reviews. Invocation: `See evidence`.
- **Scheduled tasks** (`configurable`): Scheduled tasks are supported through Codex/ChatGPT workflow surfaces; exact availability depends on surface and workspace. Invocation: `See evidence`.
- **Hierarchical project instructions** (`configurable`): Codex discovers layered AGENTS.md and AGENTS.override.md instructions from global and project scopes. Invocation: `See evidence`.
- **Agent-native file editing** (`supported`): Codex can inspect and edit repository files under sandbox and approval policies. Invocation: `See evidence`.
- **Agent-native shell execution** (`supported`): Codex runs commands within configurable sandbox and approval modes. Invocation: `See evidence`.
- **Embeddable SDK** (`supported`): Official Python and TypeScript Codex SDKs embed local Codex threads for applications and CI. Invocation: `See evidence`.
- **Headless/non-interactive execution** (`supported`): `codex exec` is the supported non-interactive interface for scripts and CI. Invocation: `codex exec`.
- **Machine-readable output** (`supported`): `codex exec` streams text or JSONL and can resume scripted sessions. Invocation: `codex exec --json`.
- **RPC/app-server protocol** (`supported`): Codex app-server exposes version-specific JSON-RPC schemas and event notifications. Invocation: `codex app-server, generate-json-schema`.
- **Agent Skills** (`configurable`): Agent Skills package instructions and resources; Codex can select them or invoke them through `$` mentions. Invocation: `See evidence`.
- **MCP client** (`configurable`): Local Codex clients connect to local or remote MCP servers and share configuration. Invocation: `See evidence`.
- **Plugins/extensions** (`configurable`): Portable plugins can bundle skills and MCP-backed connectors across ChatGPT and Codex surfaces. Invocation: `See evidence`.
- **Desktop or web surface** (`native`): Codex spans the ChatGPT desktop app and Codex cloud/web surfaces. Invocation: `See evidence`.
- **IDE integration** (`native`): Codex is available through an IDE extension sharing core sessions and agent capabilities. Invocation: `See evidence`.
- **Interactive terminal/TUI** (`native`): Interactive Codex CLI for repository inspection, editing, commands, review, and cloud handoff. Invocation: `codex`.
- **Artifacts, diffs, and rich result views** (`native`): The app, IDE, CLI, and cloud surfaces expose diffs, conversation sections, and task results for review. Invocation: `See evidence`.
- **Model and reasoning controls** (`native`): Model and reasoning effort can be selected through CLI, IDE, app, and configuration. Invocation: `See evidence`.
- **Model/provider portability** (`configurable`): Codex is primarily an OpenAI-model harness; custom API targets do not imply arbitrary provider compatibility. Invocation: `See evidence`.
- **Agent tracing/event telemetry** (`supported`): App-server notifications and JSONL execution events expose turn and tool lifecycle data. Invocation: `See evidence`.
- **Usage and cost telemetry** (`native`): Structured outputs and product surfaces expose usage, limits, and model information for attribution. Invocation: `See evidence`.
- **First-class multi-agent coordination** (`supported`): The main thread can coordinate multiple subagent threads and collect their results. Invocation: `See evidence`.
- **Parallel/background agents** (`native`): Codex cloud and local subagent surfaces support parallel/background work. Invocation: `See evidence`.
- **Subagents/delegation** (`supported`): Codex can delegate work to subagents from app, CLI, and IDE sessions and exposes child threads for inspection. Invocation: `See evidence`.
- **Browser/computer use** (`supported`): Codex models and connected tools can support browser/computer-use workflows depending on model and surface. Invocation: `See evidence`.
- **Web search/research** (`supported`): Codex supports opt-in web search and MCP-based external tools. Invocation: `See evidence`.
- **Remote/cloud execution** (`native`): CLI and IDE can hand work to Codex cloud and later inspect or apply results locally. Invocation: `See evidence`.
- **Execution sandbox** (`configurable`): Codex provides platform-specific sandbox commands and read-only/workspace-write modes. Invocation: `See evidence`.
- **Granular permissions and approvals** (`native`): Approval policies and permission profiles define when commands can run automatically. Invocation: `See evidence`.
- **Programmatic human approval** (`supported`): App-server and SDK clients can mediate approvals through machine interfaces rather than terminal-only prompts. Invocation: `See evidence`.
- **Resume, fork, and session lineage** (`native`): Saved sessions can be resumed, forked, named, and deleted through stable CLI commands. Invocation: `See evidence`.

## In-harness agent

- **Hierarchical project instructions** (`native`): Codex discovers layered AGENTS.md and AGENTS.override.md instructions from global and project scopes. Invocation: `See evidence`.
- **Agent-native file editing** (`native`): Codex can inspect and edit repository files under sandbox and approval policies. Invocation: `See evidence`.
- **Agent-native shell execution** (`native`): Codex runs commands within configurable sandbox and approval modes. Invocation: `See evidence`.
- **Agent Skills** (`native`): Agent Skills package instructions and resources; Codex can select them or invoke them through `$` mentions. Invocation: `See evidence`.
- **MCP client** (`native`): Local Codex clients connect to local or remote MCP servers and share configuration. Invocation: `See evidence`.
- **Plugins/extensions** (`native`): Portable plugins can bundle skills and MCP-backed connectors across ChatGPT and Codex surfaces. Invocation: `See evidence`.
- **Model and reasoning controls** (`supported`): Model and reasoning effort can be selected through CLI, IDE, app, and configuration. Invocation: `See evidence`.
- **First-class multi-agent coordination** (`native`): The main thread can coordinate multiple subagent threads and collect their results. Invocation: `See evidence`.
- **Parallel/background agents** (`native`): Codex cloud and local subagent surfaces support parallel/background work. Invocation: `See evidence`.
- **Subagents/delegation** (`native`): Codex can delegate work to subagents from app, CLI, and IDE sessions and exposes child threads for inspection. Invocation: `See evidence`.
- **Browser/computer use** (`native`): Codex models and connected tools can support browser/computer-use workflows depending on model and surface. Invocation: `See evidence`.
- **Web search/research** (`native`): Codex supports opt-in web search and MCP-based external tools. Invocation: `See evidence`.

## External agent/orchestrator

- **CI/GitHub automation** (`native`): The official Codex GitHub Action runs `codex exec` in CI to apply patches or post reviews. Invocation: `See evidence`.
- **Scheduled tasks** (`supported`): Scheduled tasks are supported through Codex/ChatGPT workflow surfaces; exact availability depends on surface and workspace. Invocation: `See evidence`.
- **Hierarchical project instructions** (`supported`): Codex discovers layered AGENTS.md and AGENTS.override.md instructions from global and project scopes. Invocation: `See evidence`.
- **Agent-native file editing** (`supported`): Codex can inspect and edit repository files under sandbox and approval policies. Invocation: `See evidence`.
- **Agent-native shell execution** (`supported`): Codex runs commands within configurable sandbox and approval modes. Invocation: `See evidence`.
- **Embeddable SDK** (`native`): Official Python and TypeScript Codex SDKs embed local Codex threads for applications and CI. Invocation: `See evidence`.
- **Headless/non-interactive execution** (`native`): `codex exec` is the supported non-interactive interface for scripts and CI. Invocation: `codex exec`.
- **Machine-readable output** (`native`): `codex exec` streams text or JSONL and can resume scripted sessions. Invocation: `codex exec --json`.
- **RPC/app-server protocol** (`native`): Codex app-server exposes version-specific JSON-RPC schemas and event notifications. Invocation: `codex app-server, generate-json-schema`.
- **Agent Skills** (`supported`): Agent Skills package instructions and resources; Codex can select them or invoke them through `$` mentions. Invocation: `See evidence`.
- **MCP client** (`supported`): Local Codex clients connect to local or remote MCP servers and share configuration. Invocation: `See evidence`.
- **Plugins/extensions** (`supported`): Portable plugins can bundle skills and MCP-backed connectors across ChatGPT and Codex surfaces. Invocation: `See evidence`.
- **Model and reasoning controls** (`configurable`): Model and reasoning effort can be selected through CLI, IDE, app, and configuration. Invocation: `See evidence`.
- **Model/provider portability** (`configurable`): Codex is primarily an OpenAI-model harness; custom API targets do not imply arbitrary provider compatibility. Invocation: `See evidence`.
- **Agent tracing/event telemetry** (`native`): App-server notifications and JSONL execution events expose turn and tool lifecycle data. Invocation: `See evidence`.
- **Usage and cost telemetry** (`supported`): Structured outputs and product surfaces expose usage, limits, and model information for attribution. Invocation: `See evidence`.
- **First-class multi-agent coordination** (`supported`): The main thread can coordinate multiple subagent threads and collect their results. Invocation: `See evidence`.
- **Parallel/background agents** (`supported`): Codex cloud and local subagent surfaces support parallel/background work. Invocation: `See evidence`.
- **Subagents/delegation** (`supported`): Codex can delegate work to subagents from app, CLI, and IDE sessions and exposes child threads for inspection. Invocation: `See evidence`.
- **Browser/computer use** (`supported`): Codex models and connected tools can support browser/computer-use workflows depending on model and surface. Invocation: `See evidence`.
- **Web search/research** (`supported`): Codex supports opt-in web search and MCP-based external tools. Invocation: `See evidence`.
- **Remote/cloud execution** (`supported`): CLI and IDE can hand work to Codex cloud and later inspect or apply results locally. Invocation: `See evidence`.
- **Execution sandbox** (`supported`): Codex provides platform-specific sandbox commands and read-only/workspace-write modes. Invocation: `See evidence`.
- **Granular permissions and approvals** (`supported`): Approval policies and permission profiles define when commands can run automatically. Invocation: `See evidence`.
- **Programmatic human approval** (`native`): App-server and SDK clients can mediate approvals through machine interfaces rather than terminal-only prompts. Invocation: `See evidence`.
- **Resume, fork, and session lineage** (`supported`): Saved sessions can be resumed, forked, named, and deleted through stable CLI commands. Invocation: `See evidence`.

## CI or scheduled automation

- **CI/GitHub automation** (`native`): The official Codex GitHub Action runs `codex exec` in CI to apply patches or post reviews. Invocation: `See evidence`.
- **Scheduled tasks** (`native`): Scheduled tasks are supported through Codex/ChatGPT workflow surfaces; exact availability depends on surface and workspace. Invocation: `See evidence`.
- **Hierarchical project instructions** (`supported`): Codex discovers layered AGENTS.md and AGENTS.override.md instructions from global and project scopes. Invocation: `See evidence`.
- **Agent-native file editing** (`supported`): Codex can inspect and edit repository files under sandbox and approval policies. Invocation: `See evidence`.
- **Agent-native shell execution** (`supported`): Codex runs commands within configurable sandbox and approval modes. Invocation: `See evidence`.
- **Embeddable SDK** (`native`): Official Python and TypeScript Codex SDKs embed local Codex threads for applications and CI. Invocation: `See evidence`.
- **Headless/non-interactive execution** (`native`): `codex exec` is the supported non-interactive interface for scripts and CI. Invocation: `codex exec`.
- **Machine-readable output** (`native`): `codex exec` streams text or JSONL and can resume scripted sessions. Invocation: `codex exec --json`.
- **RPC/app-server protocol** (`native`): Codex app-server exposes version-specific JSON-RPC schemas and event notifications. Invocation: `codex app-server, generate-json-schema`.
- **Agent Skills** (`supported`): Agent Skills package instructions and resources; Codex can select them or invoke them through `$` mentions. Invocation: `See evidence`.
- **MCP client** (`supported`): Local Codex clients connect to local or remote MCP servers and share configuration. Invocation: `See evidence`.
- **Plugins/extensions** (`supported`): Portable plugins can bundle skills and MCP-backed connectors across ChatGPT and Codex surfaces. Invocation: `See evidence`.
- **Model and reasoning controls** (`configurable`): Model and reasoning effort can be selected through CLI, IDE, app, and configuration. Invocation: `See evidence`.
- **Model/provider portability** (`configurable`): Codex is primarily an OpenAI-model harness; custom API targets do not imply arbitrary provider compatibility. Invocation: `See evidence`.
- **Agent tracing/event telemetry** (`native`): App-server notifications and JSONL execution events expose turn and tool lifecycle data. Invocation: `See evidence`.
- **Usage and cost telemetry** (`supported`): Structured outputs and product surfaces expose usage, limits, and model information for attribution. Invocation: `See evidence`.
- **First-class multi-agent coordination** (`supported`): The main thread can coordinate multiple subagent threads and collect their results. Invocation: `See evidence`.
- **Parallel/background agents** (`supported`): Codex cloud and local subagent surfaces support parallel/background work. Invocation: `See evidence`.
- **Subagents/delegation** (`supported`): Codex can delegate work to subagents from app, CLI, and IDE sessions and exposes child threads for inspection. Invocation: `See evidence`.
- **Browser/computer use** (`supported`): Codex models and connected tools can support browser/computer-use workflows depending on model and surface. Invocation: `See evidence`.
- **Web search/research** (`supported`): Codex supports opt-in web search and MCP-based external tools. Invocation: `See evidence`.
- **Remote/cloud execution** (`supported`): CLI and IDE can hand work to Codex cloud and later inspect or apply results locally. Invocation: `See evidence`.
- **Execution sandbox** (`supported`): Codex provides platform-specific sandbox commands and read-only/workspace-write modes. Invocation: `See evidence`.
- **Granular permissions and approvals** (`supported`): Approval policies and permission profiles define when commands can run automatically. Invocation: `See evidence`.
- **Programmatic human approval** (`supported`): App-server and SDK clients can mediate approvals through machine interfaces rather than terminal-only prompts. Invocation: `See evidence`.
- **Resume, fork, and session lineage** (`supported`): Saved sessions can be resumed, forked, named, and deleted through stable CLI commands. Invocation: `See evidence`.

## Administrator

- **CI/GitHub automation** (`configurable`): The official Codex GitHub Action runs `codex exec` in CI to apply patches or post reviews. Invocation: `See evidence`.
- **Scheduled tasks** (`configurable`): Scheduled tasks are supported through Codex/ChatGPT workflow surfaces; exact availability depends on surface and workspace. Invocation: `See evidence`.
- **Hierarchical project instructions** (`configurable`): Codex discovers layered AGENTS.md and AGENTS.override.md instructions from global and project scopes. Invocation: `See evidence`.
- **Agent-native file editing** (`configurable`): Codex can inspect and edit repository files under sandbox and approval policies. Invocation: `See evidence`.
- **Agent-native shell execution** (`configurable`): Codex runs commands within configurable sandbox and approval modes. Invocation: `See evidence`.
- **Embeddable SDK** (`configurable`): Official Python and TypeScript Codex SDKs embed local Codex threads for applications and CI. Invocation: `See evidence`.
- **Headless/non-interactive execution** (`configurable`): `codex exec` is the supported non-interactive interface for scripts and CI. Invocation: `codex exec`.
- **Machine-readable output** (`configurable`): `codex exec` streams text or JSONL and can resume scripted sessions. Invocation: `codex exec --json`.
- **RPC/app-server protocol** (`configurable`): Codex app-server exposes version-specific JSON-RPC schemas and event notifications. Invocation: `codex app-server, generate-json-schema`.
- **Agent Skills** (`configurable`): Agent Skills package instructions and resources; Codex can select them or invoke them through `$` mentions. Invocation: `See evidence`.
- **MCP client** (`configurable`): Local Codex clients connect to local or remote MCP servers and share configuration. Invocation: `See evidence`.
- **Plugins/extensions** (`configurable`): Portable plugins can bundle skills and MCP-backed connectors across ChatGPT and Codex surfaces. Invocation: `See evidence`.
- **Desktop or web surface** (`configurable`): Codex spans the ChatGPT desktop app and Codex cloud/web surfaces. Invocation: `See evidence`.
- **IDE integration** (`configurable`): Codex is available through an IDE extension sharing core sessions and agent capabilities. Invocation: `See evidence`.
- **Interactive terminal/TUI** (`configurable`): Interactive Codex CLI for repository inspection, editing, commands, review, and cloud handoff. Invocation: `codex`.
- **Artifacts, diffs, and rich result views** (`configurable`): The app, IDE, CLI, and cloud surfaces expose diffs, conversation sections, and task results for review. Invocation: `See evidence`.
- **Model and reasoning controls** (`native`): Model and reasoning effort can be selected through CLI, IDE, app, and configuration. Invocation: `See evidence`.
- **Model/provider portability** (`configurable`): Codex is primarily an OpenAI-model harness; custom API targets do not imply arbitrary provider compatibility. Invocation: `See evidence`.
- **Agent tracing/event telemetry** (`configurable`): App-server notifications and JSONL execution events expose turn and tool lifecycle data. Invocation: `See evidence`.
- **Usage and cost telemetry** (`native`): Structured outputs and product surfaces expose usage, limits, and model information for attribution. Invocation: `See evidence`.
- **First-class multi-agent coordination** (`configurable`): The main thread can coordinate multiple subagent threads and collect their results. Invocation: `See evidence`.
- **Parallel/background agents** (`configurable`): Codex cloud and local subagent surfaces support parallel/background work. Invocation: `See evidence`.
- **Subagents/delegation** (`configurable`): Codex can delegate work to subagents from app, CLI, and IDE sessions and exposes child threads for inspection. Invocation: `See evidence`.
- **Browser/computer use** (`configurable`): Codex models and connected tools can support browser/computer-use workflows depending on model and surface. Invocation: `See evidence`.
- **Web search/research** (`configurable`): Codex supports opt-in web search and MCP-based external tools. Invocation: `See evidence`.
- **Remote/cloud execution** (`configurable`): CLI and IDE can hand work to Codex cloud and later inspect or apply results locally. Invocation: `See evidence`.
- **Enterprise managed policy** (`native`): Managed workspace roles, permissions, retention, residency, and authentication policies apply to Codex surfaces. Invocation: `See evidence`.
- **Execution sandbox** (`native`): Codex provides platform-specific sandbox commands and read-only/workspace-write modes. Invocation: `See evidence`.
- **Granular permissions and approvals** (`native`): Approval policies and permission profiles define when commands can run automatically. Invocation: `See evidence`.
- **Programmatic human approval** (`configurable`): App-server and SDK clients can mediate approvals through machine interfaces rather than terminal-only prompts. Invocation: `See evidence`.
- **Resume, fork, and session lineage** (`configurable`): Saved sessions can be resumed, forked, named, and deleted through stable CLI commands. Invocation: `See evidence`.

## Freshness rule

Treat unavailable or unknown actor access as unsupported until verified. UI-only capability is not agent-callable by implication.
