---
schema_version: 0.1
harness_id: antigravity-cli
generated_at: 2026-08-15T20:10:35.204766Z
artifact_kind: harness_capability_guide
---

# Antigravity CLI — Agent Capability Guide

**Vendor:** Google  
**Lifecycle:** active  
**Current version in registry:** 1.1.13  
**Last verified:** 2026-08-15T20:10:18.746297Z

> UI availability does not imply that an in-harness model or an external orchestrator can invoke the capability. Use the actor-specific sections below.

## Human operator

- **Scheduled tasks** (`configurable`): Antigravity projects support scheduled messages/tasks. Invocation: `See evidence`.
- **Hierarchical project instructions** (`configurable`): Custom agents can be defined in Markdown with frontmatter controlling role, inheritance, and command policy. Invocation: `See evidence`.
- **Output schema enforcement** (`supported`): `--json-schema` constrains the final structured result in JSON and stream-json modes. Invocation: `--json-schema`.
- **Agent-native file editing** (`supported`): Antigravity agents understand codebases and edit files under permission controls. Invocation: `See evidence`.
- **Agent-native shell execution** (`supported`): Agents execute shell commands, and users can issue direct commands from the CLI. Invocation: `See evidence`.
- **Embeddable SDK** (`supported`): The Antigravity SDK provides programmatic access to the same platform capabilities. Invocation: `See evidence`.
- **Headless/non-interactive execution** (`supported`): Print mode provides non-interactive execution and direct read-only slash-command queries. Invocation: `agy -p`.
- **Machine-readable output** (`supported`): Print mode emits text, JSON, or typed NDJSON `stream-json`, including tool and subagent metadata. Invocation: `--output-format json, --output-format stream-json`.
- **Agent Skills** (`configurable`): Agent Skills can be discovered and expanded in interactive and headless print modes. Invocation: `See evidence`.
- **Lifecycle hooks** (`configurable`): Hooks run before/after invocations and at stop points with explicit ordering. Invocation: `PostInvocation, Stop, PostToolUse`.
- **MCP client** (`configurable`): Antigravity CLI supports MCP tools, progress reporting, OAuth, and admin controls. Invocation: `See evidence`.
- **Plugins/extensions** (`configurable`): Plugins package customizations and share enablement with Antigravity configuration. Invocation: `See evidence`.
- **Desktop or web surface** (`native`): Antigravity CLI shares a backend with the Antigravity desktop command center. Invocation: `See evidence`.
- **Interactive terminal/TUI** (`native`): Terminal-first interface to Antigravity agents with slash commands, Vim mode, and artifact views. Invocation: `agy`.
- **Artifacts, diffs, and rich result views** (`native`): Artifact views, diffs, images, comments, and rich desktop panels support result review. Invocation: `See evidence`.
- **Model and reasoning controls** (`native`): Model and reasoning effort are selectable interactively and through headless flags. Invocation: `See evidence`.
- **Agent tracing/event telemetry** (`supported`): Typed step, tool, subagent, and terminal result events form a machine-consumable execution trace. Invocation: `See evidence`.
- **Usage and cost telemetry** (`native`): Structured output includes token/cache usage; read-only print commands expose usage, quota, credits, model, and effort without an agent turn. Invocation: `See evidence`.
- **First-class multi-agent coordination** (`native`): The Antigravity backend provides explicit multi-agent orchestration and coordinator/subagent state. Invocation: `See evidence`.
- **Parallel/background agents** (`native`): Antigravity orchestrates multiple agents and background tasks without blocking the terminal. Invocation: `See evidence`.
- **Subagents/delegation** (`supported`): Custom and dynamic subagents are first-class and expose child conversation metadata in structured output. Invocation: `See evidence`.
- **Browser/computer use** (`supported`): Built-in Chrome DevTools MCP and Antigravity integrations support browser workflows. Invocation: `See evidence`.
- **Web search/research** (`supported`): Antigravity supports research through tools and connected MCP knowledge sources. Invocation: `See evidence`.
- **Remote/cloud execution** (`native`): CLI and desktop share a unified Antigravity backend for background and multi-workspace work. Invocation: `See evidence`.
- **Execution sandbox** (`configurable`): Terminal execution uses filesystem/network sandboxing and records blocked network requests. Invocation: `See evidence`.
- **Granular permissions and approvals** (`native`): Permission modes, allowlists, project/user settings, and strict review modes govern commands. Invocation: `See evidence`.
- **Resume, fork, and session lineage** (`native`): Conversations are persistent, can be forked, and warn about concurrent access. Invocation: `/fork`.

## In-harness agent

- **Scheduled tasks** (`supported`): Antigravity projects support scheduled messages/tasks. Invocation: `See evidence`.
- **Hierarchical project instructions** (`native`): Custom agents can be defined in Markdown with frontmatter controlling role, inheritance, and command policy. Invocation: `See evidence`.
- **Agent-native file editing** (`native`): Antigravity agents understand codebases and edit files under permission controls. Invocation: `See evidence`.
- **Agent-native shell execution** (`native`): Agents execute shell commands, and users can issue direct commands from the CLI. Invocation: `See evidence`.
- **Agent Skills** (`native`): Agent Skills can be discovered and expanded in interactive and headless print modes. Invocation: `See evidence`.
- **MCP client** (`native`): Antigravity CLI supports MCP tools, progress reporting, OAuth, and admin controls. Invocation: `See evidence`.
- **Plugins/extensions** (`native`): Plugins package customizations and share enablement with Antigravity configuration. Invocation: `See evidence`.
- **Model and reasoning controls** (`supported`): Model and reasoning effort are selectable interactively and through headless flags. Invocation: `See evidence`.
- **First-class multi-agent coordination** (`native`): The Antigravity backend provides explicit multi-agent orchestration and coordinator/subagent state. Invocation: `See evidence`.
- **Parallel/background agents** (`native`): Antigravity orchestrates multiple agents and background tasks without blocking the terminal. Invocation: `See evidence`.
- **Subagents/delegation** (`native`): Custom and dynamic subagents are first-class and expose child conversation metadata in structured output. Invocation: `See evidence`.
- **Browser/computer use** (`native`): Built-in Chrome DevTools MCP and Antigravity integrations support browser workflows. Invocation: `See evidence`.
- **Web search/research** (`native`): Antigravity supports research through tools and connected MCP knowledge sources. Invocation: `See evidence`.

## External agent/orchestrator

- **Scheduled tasks** (`supported`): Antigravity projects support scheduled messages/tasks. Invocation: `See evidence`.
- **Hierarchical project instructions** (`supported`): Custom agents can be defined in Markdown with frontmatter controlling role, inheritance, and command policy. Invocation: `See evidence`.
- **Output schema enforcement** (`native`): `--json-schema` constrains the final structured result in JSON and stream-json modes. Invocation: `--json-schema`.
- **Agent-native file editing** (`supported`): Antigravity agents understand codebases and edit files under permission controls. Invocation: `See evidence`.
- **Agent-native shell execution** (`supported`): Agents execute shell commands, and users can issue direct commands from the CLI. Invocation: `See evidence`.
- **Embeddable SDK** (`native`): The Antigravity SDK provides programmatic access to the same platform capabilities. Invocation: `See evidence`.
- **Headless/non-interactive execution** (`native`): Print mode provides non-interactive execution and direct read-only slash-command queries. Invocation: `agy -p`.
- **Machine-readable output** (`native`): Print mode emits text, JSON, or typed NDJSON `stream-json`, including tool and subagent metadata. Invocation: `--output-format json, --output-format stream-json`.
- **Agent Skills** (`supported`): Agent Skills can be discovered and expanded in interactive and headless print modes. Invocation: `See evidence`.
- **Lifecycle hooks** (`supported`): Hooks run before/after invocations and at stop points with explicit ordering. Invocation: `PostInvocation, Stop, PostToolUse`.
- **MCP client** (`supported`): Antigravity CLI supports MCP tools, progress reporting, OAuth, and admin controls. Invocation: `See evidence`.
- **Plugins/extensions** (`supported`): Plugins package customizations and share enablement with Antigravity configuration. Invocation: `See evidence`.
- **Model and reasoning controls** (`configurable`): Model and reasoning effort are selectable interactively and through headless flags. Invocation: `See evidence`.
- **Agent tracing/event telemetry** (`native`): Typed step, tool, subagent, and terminal result events form a machine-consumable execution trace. Invocation: `See evidence`.
- **Usage and cost telemetry** (`native`): Structured output includes token/cache usage; read-only print commands expose usage, quota, credits, model, and effort without an agent turn. Invocation: `See evidence`.
- **First-class multi-agent coordination** (`supported`): The Antigravity backend provides explicit multi-agent orchestration and coordinator/subagent state. Invocation: `See evidence`.
- **Parallel/background agents** (`supported`): Antigravity orchestrates multiple agents and background tasks without blocking the terminal. Invocation: `See evidence`.
- **Subagents/delegation** (`supported`): Custom and dynamic subagents are first-class and expose child conversation metadata in structured output. Invocation: `See evidence`.
- **Browser/computer use** (`supported`): Built-in Chrome DevTools MCP and Antigravity integrations support browser workflows. Invocation: `See evidence`.
- **Web search/research** (`supported`): Antigravity supports research through tools and connected MCP knowledge sources. Invocation: `See evidence`.
- **Remote/cloud execution** (`supported`): CLI and desktop share a unified Antigravity backend for background and multi-workspace work. Invocation: `See evidence`.
- **Execution sandbox** (`supported`): Terminal execution uses filesystem/network sandboxing and records blocked network requests. Invocation: `See evidence`.
- **Granular permissions and approvals** (`supported`): Permission modes, allowlists, project/user settings, and strict review modes govern commands. Invocation: `See evidence`.
- **Resume, fork, and session lineage** (`supported`): Conversations are persistent, can be forked, and warn about concurrent access. Invocation: `/fork`.

## CI or scheduled automation

- **Scheduled tasks** (`native`): Antigravity projects support scheduled messages/tasks. Invocation: `See evidence`.
- **Hierarchical project instructions** (`supported`): Custom agents can be defined in Markdown with frontmatter controlling role, inheritance, and command policy. Invocation: `See evidence`.
- **Output schema enforcement** (`native`): `--json-schema` constrains the final structured result in JSON and stream-json modes. Invocation: `--json-schema`.
- **Agent-native file editing** (`supported`): Antigravity agents understand codebases and edit files under permission controls. Invocation: `See evidence`.
- **Agent-native shell execution** (`supported`): Agents execute shell commands, and users can issue direct commands from the CLI. Invocation: `See evidence`.
- **Embeddable SDK** (`native`): The Antigravity SDK provides programmatic access to the same platform capabilities. Invocation: `See evidence`.
- **Headless/non-interactive execution** (`native`): Print mode provides non-interactive execution and direct read-only slash-command queries. Invocation: `agy -p`.
- **Machine-readable output** (`native`): Print mode emits text, JSON, or typed NDJSON `stream-json`, including tool and subagent metadata. Invocation: `--output-format json, --output-format stream-json`.
- **Agent Skills** (`supported`): Agent Skills can be discovered and expanded in interactive and headless print modes. Invocation: `See evidence`.
- **Lifecycle hooks** (`supported`): Hooks run before/after invocations and at stop points with explicit ordering. Invocation: `PostInvocation, Stop, PostToolUse`.
- **MCP client** (`supported`): Antigravity CLI supports MCP tools, progress reporting, OAuth, and admin controls. Invocation: `See evidence`.
- **Plugins/extensions** (`supported`): Plugins package customizations and share enablement with Antigravity configuration. Invocation: `See evidence`.
- **Model and reasoning controls** (`configurable`): Model and reasoning effort are selectable interactively and through headless flags. Invocation: `See evidence`.
- **Agent tracing/event telemetry** (`native`): Typed step, tool, subagent, and terminal result events form a machine-consumable execution trace. Invocation: `See evidence`.
- **Usage and cost telemetry** (`native`): Structured output includes token/cache usage; read-only print commands expose usage, quota, credits, model, and effort without an agent turn. Invocation: `See evidence`.
- **First-class multi-agent coordination** (`supported`): The Antigravity backend provides explicit multi-agent orchestration and coordinator/subagent state. Invocation: `See evidence`.
- **Parallel/background agents** (`supported`): Antigravity orchestrates multiple agents and background tasks without blocking the terminal. Invocation: `See evidence`.
- **Subagents/delegation** (`supported`): Custom and dynamic subagents are first-class and expose child conversation metadata in structured output. Invocation: `See evidence`.
- **Browser/computer use** (`supported`): Built-in Chrome DevTools MCP and Antigravity integrations support browser workflows. Invocation: `See evidence`.
- **Web search/research** (`supported`): Antigravity supports research through tools and connected MCP knowledge sources. Invocation: `See evidence`.
- **Remote/cloud execution** (`supported`): CLI and desktop share a unified Antigravity backend for background and multi-workspace work. Invocation: `See evidence`.
- **Execution sandbox** (`supported`): Terminal execution uses filesystem/network sandboxing and records blocked network requests. Invocation: `See evidence`.
- **Granular permissions and approvals** (`supported`): Permission modes, allowlists, project/user settings, and strict review modes govern commands. Invocation: `See evidence`.
- **Resume, fork, and session lineage** (`supported`): Conversations are persistent, can be forked, and warn about concurrent access. Invocation: `/fork`.

## Administrator

- **Scheduled tasks** (`configurable`): Antigravity projects support scheduled messages/tasks. Invocation: `See evidence`.
- **Hierarchical project instructions** (`configurable`): Custom agents can be defined in Markdown with frontmatter controlling role, inheritance, and command policy. Invocation: `See evidence`.
- **Output schema enforcement** (`configurable`): `--json-schema` constrains the final structured result in JSON and stream-json modes. Invocation: `--json-schema`.
- **Agent-native file editing** (`configurable`): Antigravity agents understand codebases and edit files under permission controls. Invocation: `See evidence`.
- **Agent-native shell execution** (`configurable`): Agents execute shell commands, and users can issue direct commands from the CLI. Invocation: `See evidence`.
- **Embeddable SDK** (`configurable`): The Antigravity SDK provides programmatic access to the same platform capabilities. Invocation: `See evidence`.
- **Headless/non-interactive execution** (`configurable`): Print mode provides non-interactive execution and direct read-only slash-command queries. Invocation: `agy -p`.
- **Machine-readable output** (`configurable`): Print mode emits text, JSON, or typed NDJSON `stream-json`, including tool and subagent metadata. Invocation: `--output-format json, --output-format stream-json`.
- **Agent Skills** (`configurable`): Agent Skills can be discovered and expanded in interactive and headless print modes. Invocation: `See evidence`.
- **Lifecycle hooks** (`native`): Hooks run before/after invocations and at stop points with explicit ordering. Invocation: `PostInvocation, Stop, PostToolUse`.
- **MCP client** (`configurable`): Antigravity CLI supports MCP tools, progress reporting, OAuth, and admin controls. Invocation: `See evidence`.
- **Plugins/extensions** (`configurable`): Plugins package customizations and share enablement with Antigravity configuration. Invocation: `See evidence`.
- **Desktop or web surface** (`configurable`): Antigravity CLI shares a backend with the Antigravity desktop command center. Invocation: `See evidence`.
- **Interactive terminal/TUI** (`configurable`): Terminal-first interface to Antigravity agents with slash commands, Vim mode, and artifact views. Invocation: `agy`.
- **Artifacts, diffs, and rich result views** (`configurable`): Artifact views, diffs, images, comments, and rich desktop panels support result review. Invocation: `See evidence`.
- **Model and reasoning controls** (`native`): Model and reasoning effort are selectable interactively and through headless flags. Invocation: `See evidence`.
- **Agent tracing/event telemetry** (`configurable`): Typed step, tool, subagent, and terminal result events form a machine-consumable execution trace. Invocation: `See evidence`.
- **Usage and cost telemetry** (`native`): Structured output includes token/cache usage; read-only print commands expose usage, quota, credits, model, and effort without an agent turn. Invocation: `See evidence`.
- **First-class multi-agent coordination** (`configurable`): The Antigravity backend provides explicit multi-agent orchestration and coordinator/subagent state. Invocation: `See evidence`.
- **Parallel/background agents** (`configurable`): Antigravity orchestrates multiple agents and background tasks without blocking the terminal. Invocation: `See evidence`.
- **Subagents/delegation** (`configurable`): Custom and dynamic subagents are first-class and expose child conversation metadata in structured output. Invocation: `See evidence`.
- **Browser/computer use** (`configurable`): Built-in Chrome DevTools MCP and Antigravity integrations support browser workflows. Invocation: `See evidence`.
- **Web search/research** (`configurable`): Antigravity supports research through tools and connected MCP knowledge sources. Invocation: `See evidence`.
- **Remote/cloud execution** (`native`): CLI and desktop share a unified Antigravity backend for background and multi-workspace work. Invocation: `See evidence`.
- **Enterprise managed policy** (`native`): Business sign-in, WIF, ADC, regional inference, and organization admin controls are supported. Invocation: `See evidence`.
- **Execution sandbox** (`native`): Terminal execution uses filesystem/network sandboxing and records blocked network requests. Invocation: `See evidence`.
- **Granular permissions and approvals** (`native`): Permission modes, allowlists, project/user settings, and strict review modes govern commands. Invocation: `See evidence`.
- **Resume, fork, and session lineage** (`configurable`): Conversations are persistent, can be forked, and warn about concurrent access. Invocation: `/fork`.

## Freshness rule

Treat unavailable or unknown actor access as unsupported until verified. UI-only capability is not agent-callable by implication.
