---
schema_version: 0.1
harness_id: gemini-cli
generated_at: 2026-08-24T13:14:55.511915Z
artifact_kind: harness_capability_guide
---

# Gemini CLI — Agent Capability Guide

**Vendor:** Google  
**Lifecycle:** legacy  
**Current version in registry:** 0.57.0-preview.0  
**Last verified:** 2026-08-24T13:14:39.999942Z

> UI availability does not imply that an in-harness model or an external orchestrator can invoke the capability. Use the actor-specific sections below.

## Human operator

- **Agent-native file editing** (`supported`): Gemini CLI agents can inspect and modify repository files. Invocation: `See evidence`.
- **Agent-native shell execution** (`supported`): Gemini CLI agents can run shell tools under configured policies. Invocation: `See evidence`.
- **Headless/non-interactive execution** (`supported`): Gemini CLI exposes headless mode for scripts and automation. Invocation: `See evidence`.
- **Machine-readable output** (`supported`): Headless mode supports structured JSON output. Invocation: `See evidence`.
- **Agent Skills** (`configurable`): Agent Skills were supported and ported to Antigravity CLI. Invocation: `See evidence`.
- **Lifecycle hooks** (`configurable`): Gemini CLI supports lifecycle hooks. Invocation: `See evidence`.
- **MCP client** (`configurable`): Gemini CLI supports MCP servers. Invocation: `See evidence`.
- **Plugins/extensions** (`configurable`): Gemini CLI extensions were supported and became Antigravity plugins in the successor product. Invocation: `See evidence`.
- **Interactive terminal/TUI** (`native`): Gemini CLI provides an interactive terminal agent. Invocation: `See evidence`.
- **Model and reasoning controls** (`native`): Model selection and plan-mode workflows are configurable. Invocation: `See evidence`.
- **Subagents/delegation** (`supported`): Subagents were supported and ported to Antigravity CLI. Invocation: `See evidence`.
- **Granular permissions and approvals** (`native`): Gemini CLI provides approval and policy controls for tools. Invocation: `See evidence`.

## In-harness agent

- **Agent-native file editing** (`native`): Gemini CLI agents can inspect and modify repository files. Invocation: `See evidence`.
- **Agent-native shell execution** (`native`): Gemini CLI agents can run shell tools under configured policies. Invocation: `See evidence`.
- **Agent Skills** (`native`): Agent Skills were supported and ported to Antigravity CLI. Invocation: `See evidence`.
- **MCP client** (`native`): Gemini CLI supports MCP servers. Invocation: `See evidence`.
- **Plugins/extensions** (`native`): Gemini CLI extensions were supported and became Antigravity plugins in the successor product. Invocation: `See evidence`.
- **Model and reasoning controls** (`supported`): Model selection and plan-mode workflows are configurable. Invocation: `See evidence`.
- **Subagents/delegation** (`native`): Subagents were supported and ported to Antigravity CLI. Invocation: `See evidence`.

## External agent/orchestrator

- **Agent-native file editing** (`supported`): Gemini CLI agents can inspect and modify repository files. Invocation: `See evidence`.
- **Agent-native shell execution** (`supported`): Gemini CLI agents can run shell tools under configured policies. Invocation: `See evidence`.
- **Headless/non-interactive execution** (`native`): Gemini CLI exposes headless mode for scripts and automation. Invocation: `See evidence`.
- **Machine-readable output** (`native`): Headless mode supports structured JSON output. Invocation: `See evidence`.
- **Agent Skills** (`supported`): Agent Skills were supported and ported to Antigravity CLI. Invocation: `See evidence`.
- **Lifecycle hooks** (`supported`): Gemini CLI supports lifecycle hooks. Invocation: `See evidence`.
- **MCP client** (`supported`): Gemini CLI supports MCP servers. Invocation: `See evidence`.
- **Plugins/extensions** (`supported`): Gemini CLI extensions were supported and became Antigravity plugins in the successor product. Invocation: `See evidence`.
- **Model and reasoning controls** (`configurable`): Model selection and plan-mode workflows are configurable. Invocation: `See evidence`.
- **Subagents/delegation** (`supported`): Subagents were supported and ported to Antigravity CLI. Invocation: `See evidence`.
- **Granular permissions and approvals** (`supported`): Gemini CLI provides approval and policy controls for tools. Invocation: `See evidence`.

## CI or scheduled automation

- **Agent-native file editing** (`supported`): Gemini CLI agents can inspect and modify repository files. Invocation: `See evidence`.
- **Agent-native shell execution** (`supported`): Gemini CLI agents can run shell tools under configured policies. Invocation: `See evidence`.
- **Headless/non-interactive execution** (`native`): Gemini CLI exposes headless mode for scripts and automation. Invocation: `See evidence`.
- **Machine-readable output** (`native`): Headless mode supports structured JSON output. Invocation: `See evidence`.
- **Agent Skills** (`supported`): Agent Skills were supported and ported to Antigravity CLI. Invocation: `See evidence`.
- **Lifecycle hooks** (`supported`): Gemini CLI supports lifecycle hooks. Invocation: `See evidence`.
- **MCP client** (`supported`): Gemini CLI supports MCP servers. Invocation: `See evidence`.
- **Plugins/extensions** (`supported`): Gemini CLI extensions were supported and became Antigravity plugins in the successor product. Invocation: `See evidence`.
- **Model and reasoning controls** (`configurable`): Model selection and plan-mode workflows are configurable. Invocation: `See evidence`.
- **Subagents/delegation** (`supported`): Subagents were supported and ported to Antigravity CLI. Invocation: `See evidence`.
- **Granular permissions and approvals** (`supported`): Gemini CLI provides approval and policy controls for tools. Invocation: `See evidence`.

## Administrator

- **Agent-native file editing** (`configurable`): Gemini CLI agents can inspect and modify repository files. Invocation: `See evidence`.
- **Agent-native shell execution** (`configurable`): Gemini CLI agents can run shell tools under configured policies. Invocation: `See evidence`.
- **Headless/non-interactive execution** (`configurable`): Gemini CLI exposes headless mode for scripts and automation. Invocation: `See evidence`.
- **Machine-readable output** (`configurable`): Headless mode supports structured JSON output. Invocation: `See evidence`.
- **Agent Skills** (`configurable`): Agent Skills were supported and ported to Antigravity CLI. Invocation: `See evidence`.
- **Lifecycle hooks** (`configurable`): Gemini CLI supports lifecycle hooks. Invocation: `See evidence`.
- **MCP client** (`configurable`): Gemini CLI supports MCP servers. Invocation: `See evidence`.
- **Plugins/extensions** (`configurable`): Gemini CLI extensions were supported and became Antigravity plugins in the successor product. Invocation: `See evidence`.
- **Interactive terminal/TUI** (`configurable`): Gemini CLI provides an interactive terminal agent. Invocation: `See evidence`.
- **Model and reasoning controls** (`configurable`): Model selection and plan-mode workflows are configurable. Invocation: `See evidence`.
- **Subagents/delegation** (`configurable`): Subagents were supported and ported to Antigravity CLI. Invocation: `See evidence`.
- **Granular permissions and approvals** (`configurable`): Gemini CLI provides approval and policy controls for tools. Invocation: `See evidence`.

## Freshness rule

Treat unavailable or unknown actor access as unsupported until verified. UI-only capability is not agent-callable by implication.
