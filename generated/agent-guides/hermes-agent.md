---
schema_version: 0.1
harness_id: hermes-agent
generated_at: 2026-08-24T13:14:55.511915Z
artifact_kind: harness_capability_guide
---

# Hermes Agent — Agent Capability Guide

**Vendor:** Nous Research  
**Lifecycle:** active  
**Current version in registry:** 2026.8.19  
**Last verified:** 2026-08-24T13:14:39.999942Z

> UI availability does not imply that an in-harness model or an external orchestrator can invoke the capability. Use the actor-specific sections below.

## Human operator

- **Scheduled tasks** (`configurable`): Hermes includes scheduled and gateway-driven automation paths. Invocation: `See evidence`.
- **Persistent memory** (`configurable`): Persistent memory and conversation search are first-class parts of Hermes' self-improving agent model. Invocation: `See evidence`.
- **Agent-native file editing** (`supported`): Hermes agents can inspect and edit files through built-in and learned tools. Invocation: `See evidence`.
- **Agent-native shell execution** (`supported`): Hermes can execute shell commands, including direct `!` command shortcuts in recent releases. Invocation: `!<command>`.
- **Headless/non-interactive execution** (`supported`): Hermes can be invoked through CLI/gateway automation, but the seed does not yet verify a stable event protocol equivalent to Codex app-server. Invocation: `See evidence`.
- **Agent Skills** (`configurable`): Hermes discovers skills progressively and can create or improve them through its learning loop and `/learn` workflow. Invocation: `See evidence`.
- **MCP client** (`configurable`): Hermes supports MCP servers and Docker-based MCP commands. Invocation: `See evidence`.
- **Plugins/extensions** (`configurable`): Hermes 0.20 added a desktop plugin SDK and extensibility surfaces. Invocation: `See evidence`.
- **Desktop or web surface** (`native`): Hermes 0.20 introduced desktop artifacts, a plugin SDK, and multi-window operation. Invocation: `See evidence`.
- **Interactive terminal/TUI** (`native`): Hermes provides a CLI/TUI with session resume, interruption, and command shortcuts. Invocation: `hermes`.
- **Artifacts, diffs, and rich result views** (`native`): Desktop artifacts and multiple windows provide richer outputs than plain terminal text. Invocation: `See evidence`.
- **Voice interaction** (`native`): Streaming voice supports barge-in and wake words. Invocation: `See evidence`.
- **Model/provider portability** (`native`): Hermes supports multiple hosted and local model providers. Invocation: `See evidence`.
- **First-class multi-agent coordination** (`supported`): Mixture-of-Agents is a first-class coordination mode rather than only ad hoc subagent prompting. Invocation: `See evidence`.
- **Parallel/background agents** (`supported`): Hermes supports background work and Mixture-of-Agents execution. Invocation: `See evidence`.
- **Subagents/delegation** (`supported`): Hermes can delegate work to specialized agents. Invocation: `See evidence`.
- **Web search/research** (`supported`): Hermes 0.20 added grounded research and citation support. Invocation: `See evidence`.
- **Remote/cloud execution** (`native`): Hermes gateways let users interact through messaging channels while work runs on another machine or cloud VM. Invocation: `See evidence`.
- **Self-hosted worker/runtime** (`configurable`): Hermes can run on user-owned machines, VPSs, clusters, or serverless infrastructure. Invocation: `See evidence`.
- **Granular permissions and approvals** (`native`): Permission modes such as `/yolo` and gateway/tool configuration govern autonomy; use conservative defaults for unattended runs. Invocation: `See evidence`.
- **Resume, fork, and session lineage** (`native`): Hermes persists and resumes sessions across CLI and gateway surfaces. Invocation: `See evidence`.

## In-harness agent

- **Scheduled tasks** (`supported`): Hermes includes scheduled and gateway-driven automation paths. Invocation: `See evidence`.
- **Persistent memory** (`native`): Persistent memory and conversation search are first-class parts of Hermes' self-improving agent model. Invocation: `See evidence`.
- **Agent-native file editing** (`native`): Hermes agents can inspect and edit files through built-in and learned tools. Invocation: `See evidence`.
- **Agent-native shell execution** (`native`): Hermes can execute shell commands, including direct `!` command shortcuts in recent releases. Invocation: `!<command>`.
- **Agent Skills** (`native`): Hermes discovers skills progressively and can create or improve them through its learning loop and `/learn` workflow. Invocation: `See evidence`.
- **MCP client** (`native`): Hermes supports MCP servers and Docker-based MCP commands. Invocation: `See evidence`.
- **Plugins/extensions** (`native`): Hermes 0.20 added a desktop plugin SDK and extensibility surfaces. Invocation: `See evidence`.
- **Model/provider portability** (`supported`): Hermes supports multiple hosted and local model providers. Invocation: `See evidence`.
- **First-class multi-agent coordination** (`native`): Mixture-of-Agents is a first-class coordination mode rather than only ad hoc subagent prompting. Invocation: `See evidence`.
- **Parallel/background agents** (`native`): Hermes supports background work and Mixture-of-Agents execution. Invocation: `See evidence`.
- **Subagents/delegation** (`native`): Hermes can delegate work to specialized agents. Invocation: `See evidence`.
- **Web search/research** (`native`): Hermes 0.20 added grounded research and citation support. Invocation: `See evidence`.

## External agent/orchestrator

- **Scheduled tasks** (`supported`): Hermes includes scheduled and gateway-driven automation paths. Invocation: `See evidence`.
- **Persistent memory** (`supported`): Persistent memory and conversation search are first-class parts of Hermes' self-improving agent model. Invocation: `See evidence`.
- **Agent-native file editing** (`supported`): Hermes agents can inspect and edit files through built-in and learned tools. Invocation: `See evidence`.
- **Agent-native shell execution** (`supported`): Hermes can execute shell commands, including direct `!` command shortcuts in recent releases. Invocation: `!<command>`.
- **Headless/non-interactive execution** (`native`): Hermes can be invoked through CLI/gateway automation, but the seed does not yet verify a stable event protocol equivalent to Codex app-server. Invocation: `See evidence`.
- **Agent Skills** (`supported`): Hermes discovers skills progressively and can create or improve them through its learning loop and `/learn` workflow. Invocation: `See evidence`.
- **MCP client** (`supported`): Hermes supports MCP servers and Docker-based MCP commands. Invocation: `See evidence`.
- **Plugins/extensions** (`supported`): Hermes 0.20 added a desktop plugin SDK and extensibility surfaces. Invocation: `See evidence`.
- **Voice interaction** (`supported`): Streaming voice supports barge-in and wake words. Invocation: `See evidence`.
- **Model/provider portability** (`configurable`): Hermes supports multiple hosted and local model providers. Invocation: `See evidence`.
- **First-class multi-agent coordination** (`supported`): Mixture-of-Agents is a first-class coordination mode rather than only ad hoc subagent prompting. Invocation: `See evidence`.
- **Parallel/background agents** (`supported`): Hermes supports background work and Mixture-of-Agents execution. Invocation: `See evidence`.
- **Subagents/delegation** (`supported`): Hermes can delegate work to specialized agents. Invocation: `See evidence`.
- **Web search/research** (`supported`): Hermes 0.20 added grounded research and citation support. Invocation: `See evidence`.
- **Remote/cloud execution** (`supported`): Hermes gateways let users interact through messaging channels while work runs on another machine or cloud VM. Invocation: `See evidence`.
- **Self-hosted worker/runtime** (`supported`): Hermes can run on user-owned machines, VPSs, clusters, or serverless infrastructure. Invocation: `See evidence`.
- **Granular permissions and approvals** (`supported`): Permission modes such as `/yolo` and gateway/tool configuration govern autonomy; use conservative defaults for unattended runs. Invocation: `See evidence`.
- **Resume, fork, and session lineage** (`supported`): Hermes persists and resumes sessions across CLI and gateway surfaces. Invocation: `See evidence`.

## CI or scheduled automation

- **Scheduled tasks** (`native`): Hermes includes scheduled and gateway-driven automation paths. Invocation: `See evidence`.
- **Agent-native file editing** (`supported`): Hermes agents can inspect and edit files through built-in and learned tools. Invocation: `See evidence`.
- **Agent-native shell execution** (`supported`): Hermes can execute shell commands, including direct `!` command shortcuts in recent releases. Invocation: `!<command>`.
- **Headless/non-interactive execution** (`native`): Hermes can be invoked through CLI/gateway automation, but the seed does not yet verify a stable event protocol equivalent to Codex app-server. Invocation: `See evidence`.
- **Agent Skills** (`supported`): Hermes discovers skills progressively and can create or improve them through its learning loop and `/learn` workflow. Invocation: `See evidence`.
- **MCP client** (`supported`): Hermes supports MCP servers and Docker-based MCP commands. Invocation: `See evidence`.
- **Plugins/extensions** (`supported`): Hermes 0.20 added a desktop plugin SDK and extensibility surfaces. Invocation: `See evidence`.
- **Model/provider portability** (`configurable`): Hermes supports multiple hosted and local model providers. Invocation: `See evidence`.
- **First-class multi-agent coordination** (`supported`): Mixture-of-Agents is a first-class coordination mode rather than only ad hoc subagent prompting. Invocation: `See evidence`.
- **Parallel/background agents** (`supported`): Hermes supports background work and Mixture-of-Agents execution. Invocation: `See evidence`.
- **Subagents/delegation** (`supported`): Hermes can delegate work to specialized agents. Invocation: `See evidence`.
- **Web search/research** (`supported`): Hermes 0.20 added grounded research and citation support. Invocation: `See evidence`.
- **Remote/cloud execution** (`supported`): Hermes gateways let users interact through messaging channels while work runs on another machine or cloud VM. Invocation: `See evidence`.
- **Self-hosted worker/runtime** (`supported`): Hermes can run on user-owned machines, VPSs, clusters, or serverless infrastructure. Invocation: `See evidence`.
- **Granular permissions and approvals** (`supported`): Permission modes such as `/yolo` and gateway/tool configuration govern autonomy; use conservative defaults for unattended runs. Invocation: `See evidence`.
- **Resume, fork, and session lineage** (`supported`): Hermes persists and resumes sessions across CLI and gateway surfaces. Invocation: `See evidence`.

## Administrator

- **Scheduled tasks** (`configurable`): Hermes includes scheduled and gateway-driven automation paths. Invocation: `See evidence`.
- **Persistent memory** (`configurable`): Persistent memory and conversation search are first-class parts of Hermes' self-improving agent model. Invocation: `See evidence`.
- **Agent-native file editing** (`configurable`): Hermes agents can inspect and edit files through built-in and learned tools. Invocation: `See evidence`.
- **Agent-native shell execution** (`configurable`): Hermes can execute shell commands, including direct `!` command shortcuts in recent releases. Invocation: `!<command>`.
- **Headless/non-interactive execution** (`configurable`): Hermes can be invoked through CLI/gateway automation, but the seed does not yet verify a stable event protocol equivalent to Codex app-server. Invocation: `See evidence`.
- **Agent Skills** (`configurable`): Hermes discovers skills progressively and can create or improve them through its learning loop and `/learn` workflow. Invocation: `See evidence`.
- **MCP client** (`configurable`): Hermes supports MCP servers and Docker-based MCP commands. Invocation: `See evidence`.
- **Plugins/extensions** (`configurable`): Hermes 0.20 added a desktop plugin SDK and extensibility surfaces. Invocation: `See evidence`.
- **Desktop or web surface** (`configurable`): Hermes 0.20 introduced desktop artifacts, a plugin SDK, and multi-window operation. Invocation: `See evidence`.
- **Interactive terminal/TUI** (`configurable`): Hermes provides a CLI/TUI with session resume, interruption, and command shortcuts. Invocation: `hermes`.
- **Artifacts, diffs, and rich result views** (`configurable`): Desktop artifacts and multiple windows provide richer outputs than plain terminal text. Invocation: `See evidence`.
- **Voice interaction** (`configurable`): Streaming voice supports barge-in and wake words. Invocation: `See evidence`.
- **Model/provider portability** (`configurable`): Hermes supports multiple hosted and local model providers. Invocation: `See evidence`.
- **First-class multi-agent coordination** (`configurable`): Mixture-of-Agents is a first-class coordination mode rather than only ad hoc subagent prompting. Invocation: `See evidence`.
- **Parallel/background agents** (`configurable`): Hermes supports background work and Mixture-of-Agents execution. Invocation: `See evidence`.
- **Subagents/delegation** (`configurable`): Hermes can delegate work to specialized agents. Invocation: `See evidence`.
- **Web search/research** (`configurable`): Hermes 0.20 added grounded research and citation support. Invocation: `See evidence`.
- **Remote/cloud execution** (`configurable`): Hermes gateways let users interact through messaging channels while work runs on another machine or cloud VM. Invocation: `See evidence`.
- **Self-hosted worker/runtime** (`native`): Hermes can run on user-owned machines, VPSs, clusters, or serverless infrastructure. Invocation: `See evidence`.
- **Granular permissions and approvals** (`configurable`): Permission modes such as `/yolo` and gateway/tool configuration govern autonomy; use conservative defaults for unattended runs. Invocation: `See evidence`.
- **Resume, fork, and session lineage** (`configurable`): Hermes persists and resumes sessions across CLI and gateway surfaces. Invocation: `See evidence`.

## Freshness rule

Treat unavailable or unknown actor access as unsupported until verified. UI-only capability is not agent-callable by implication.
