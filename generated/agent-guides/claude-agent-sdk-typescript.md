---
schema_version: 0.1
harness_id: claude-agent-sdk-typescript
generated_at: 2026-08-18T18:58:02.113278Z
artifact_kind: harness_capability_guide
---

# Claude Agent SDK — TypeScript — Agent Capability Guide

**Vendor:** Anthropic  
**Lifecycle:** active  
**Current version in registry:** 0.3.234  
**Last verified:** 2026-08-18T18:57:45.521496Z

> UI availability does not imply that an in-harness model or an external orchestrator can invoke the capability. Use the actor-specific sections below.

## Human operator

- **Embeddable SDK** (`supported`): TypeScript API embeds the Claude Code agent loop, tools, and context management. Invocation: `See evidence`.
- **Machine-readable output** (`supported`): Typed message streams expose assistant, tool, task, usage, and terminal-result events. Invocation: `See evidence`.
- **Lifecycle hooks** (`supported`): Lifecycle hooks and permission callbacks are available to embedding applications. Invocation: `See evidence`.
- **MCP client** (`supported`): SDK applications can configure MCP servers and SDK-defined MCP tools. Invocation: `See evidence`.
- **Agent tracing/event telemetry** (`supported`): Typed result and task events provide execution telemetry. Invocation: `See evidence`.
- **Subagents/delegation** (`supported`): SDK applications can use Claude Code subagents and background tasks. Invocation: `See evidence`.
- **Granular permissions and approvals** (`supported`): Allowed tools, permission modes, and callbacks govern actions. Invocation: `See evidence`.
- **Programmatic human approval** (`supported`): Embedding applications can implement human/tool approval callbacks. Invocation: `See evidence`.
- **Resume, fork, and session lineage** (`supported`): SDK session IDs and stores support resume and session lifecycle management. Invocation: `See evidence`.

## In-harness agent

No positively verified capabilities in the current seed.

## External agent/orchestrator

- **Embeddable SDK** (`native`): TypeScript API embeds the Claude Code agent loop, tools, and context management. Invocation: `See evidence`.
- **Machine-readable output** (`native`): Typed message streams expose assistant, tool, task, usage, and terminal-result events. Invocation: `See evidence`.
- **Lifecycle hooks** (`native`): Lifecycle hooks and permission callbacks are available to embedding applications. Invocation: `See evidence`.
- **MCP client** (`native`): SDK applications can configure MCP servers and SDK-defined MCP tools. Invocation: `See evidence`.
- **Agent tracing/event telemetry** (`native`): Typed result and task events provide execution telemetry. Invocation: `See evidence`.
- **Subagents/delegation** (`native`): SDK applications can use Claude Code subagents and background tasks. Invocation: `See evidence`.
- **Granular permissions and approvals** (`native`): Allowed tools, permission modes, and callbacks govern actions. Invocation: `See evidence`.
- **Programmatic human approval** (`native`): Embedding applications can implement human/tool approval callbacks. Invocation: `See evidence`.
- **Resume, fork, and session lineage** (`native`): SDK session IDs and stores support resume and session lifecycle management. Invocation: `See evidence`.

## CI or scheduled automation

- **Embeddable SDK** (`native`): TypeScript API embeds the Claude Code agent loop, tools, and context management. Invocation: `See evidence`.
- **Machine-readable output** (`native`): Typed message streams expose assistant, tool, task, usage, and terminal-result events. Invocation: `See evidence`.
- **Lifecycle hooks** (`native`): Lifecycle hooks and permission callbacks are available to embedding applications. Invocation: `See evidence`.
- **MCP client** (`native`): SDK applications can configure MCP servers and SDK-defined MCP tools. Invocation: `See evidence`.
- **Agent tracing/event telemetry** (`native`): Typed result and task events provide execution telemetry. Invocation: `See evidence`.
- **Subagents/delegation** (`native`): SDK applications can use Claude Code subagents and background tasks. Invocation: `See evidence`.
- **Granular permissions and approvals** (`native`): Allowed tools, permission modes, and callbacks govern actions. Invocation: `See evidence`.
- **Programmatic human approval** (`native`): Embedding applications can implement human/tool approval callbacks. Invocation: `See evidence`.
- **Resume, fork, and session lineage** (`native`): SDK session IDs and stores support resume and session lifecycle management. Invocation: `See evidence`.

## Administrator

- **Embeddable SDK** (`configurable`): TypeScript API embeds the Claude Code agent loop, tools, and context management. Invocation: `See evidence`.
- **Machine-readable output** (`configurable`): Typed message streams expose assistant, tool, task, usage, and terminal-result events. Invocation: `See evidence`.
- **Lifecycle hooks** (`configurable`): Lifecycle hooks and permission callbacks are available to embedding applications. Invocation: `See evidence`.
- **MCP client** (`configurable`): SDK applications can configure MCP servers and SDK-defined MCP tools. Invocation: `See evidence`.
- **Agent tracing/event telemetry** (`configurable`): Typed result and task events provide execution telemetry. Invocation: `See evidence`.
- **Subagents/delegation** (`configurable`): SDK applications can use Claude Code subagents and background tasks. Invocation: `See evidence`.
- **Granular permissions and approvals** (`configurable`): Allowed tools, permission modes, and callbacks govern actions. Invocation: `See evidence`.
- **Programmatic human approval** (`configurable`): Embedding applications can implement human/tool approval callbacks. Invocation: `See evidence`.
- **Resume, fork, and session lineage** (`configurable`): SDK session IDs and stores support resume and session lifecycle management. Invocation: `See evidence`.

## Freshness rule

Treat unavailable or unknown actor access as unsupported until verified. UI-only capability is not agent-callable by implication.
