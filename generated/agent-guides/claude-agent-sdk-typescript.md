---
schema_version: 0.1
harness_id: claude-agent-sdk-typescript
generated_at: 2026-08-30T21:07:07.656998Z
artifact_kind: harness_capability_guide
---

# Claude Agent SDK — TypeScript — Agent Capability Guide

**Vendor:** Anthropic  
**Lifecycle:** active  
**Current version in registry:** 0.3.251  
**Last verified:** 2026-08-30T21:06:52.344015Z

> UI availability does not imply that an in-harness model or an external orchestrator can invoke the capability. Use the actor-specific sections below.

## Human operator

- **Embeddable SDK** (`supported`): TypeScript API embeds the Claude Code agent loop, tools, and context management. Invocation: `query()`.
- **Machine-readable output** (`supported`): Typed message streams expose assistant, tool, task, usage, and terminal-result events. Invocation: `options.outputFormat = { type: 'json_schema', schema: ... }`.
- **Lifecycle hooks** (`supported`): Lifecycle hooks and permission callbacks are available to embedding applications. Invocation: `options.hooks, HookCallbackMatcher`.
- **MCP client** (`supported`): SDK applications can configure MCP servers and SDK-defined MCP tools. Invocation: `options.mcpServers, strictMcpConfig`.
- **Agent tracing/event telemetry** (`supported`): Typed result and task events provide execution telemetry. Invocation: `CLAUDE_CODE_ENABLE_TELEMETRY=1 (via options.env), OTEL_TRACES_EXPORTER`.
- **Subagents/delegation** (`supported`): SDK applications can use Claude Code subagents and background tasks. Invocation: `options.agents, AgentDefinition`.
- **Granular permissions and approvals** (`supported`): Allowed tools, permission modes, and callbacks govern actions. Invocation: `options.permissionMode, options.canUseTool`.
- **Programmatic human approval** (`supported`): Embedding applications can implement human/tool approval callbacks. Invocation: `options.canUseTool`.
- **Resume, fork, and session lineage** (`supported`): SDK session IDs and stores support resume and session lifecycle management. Invocation: `options.resume, options.forkSession`.

## In-harness agent

No positively verified capabilities in the current seed.

## External agent/orchestrator

- **Embeddable SDK** (`native`): TypeScript API embeds the Claude Code agent loop, tools, and context management. Invocation: `query()`.
- **Machine-readable output** (`native`): Typed message streams expose assistant, tool, task, usage, and terminal-result events. Invocation: `options.outputFormat = { type: 'json_schema', schema: ... }`.
- **Lifecycle hooks** (`native`): Lifecycle hooks and permission callbacks are available to embedding applications. Invocation: `options.hooks, HookCallbackMatcher`.
- **MCP client** (`native`): SDK applications can configure MCP servers and SDK-defined MCP tools. Invocation: `options.mcpServers, strictMcpConfig`.
- **Agent tracing/event telemetry** (`native`): Typed result and task events provide execution telemetry. Invocation: `CLAUDE_CODE_ENABLE_TELEMETRY=1 (via options.env), OTEL_TRACES_EXPORTER`.
- **Subagents/delegation** (`native`): SDK applications can use Claude Code subagents and background tasks. Invocation: `options.agents, AgentDefinition`.
- **Granular permissions and approvals** (`native`): Allowed tools, permission modes, and callbacks govern actions. Invocation: `options.permissionMode, options.canUseTool`.
- **Programmatic human approval** (`native`): Embedding applications can implement human/tool approval callbacks. Invocation: `options.canUseTool`.
- **Resume, fork, and session lineage** (`native`): SDK session IDs and stores support resume and session lifecycle management. Invocation: `options.resume, options.forkSession`.

## CI or scheduled automation

- **Embeddable SDK** (`native`): TypeScript API embeds the Claude Code agent loop, tools, and context management. Invocation: `query()`.
- **Machine-readable output** (`native`): Typed message streams expose assistant, tool, task, usage, and terminal-result events. Invocation: `options.outputFormat = { type: 'json_schema', schema: ... }`.
- **Lifecycle hooks** (`native`): Lifecycle hooks and permission callbacks are available to embedding applications. Invocation: `options.hooks, HookCallbackMatcher`.
- **MCP client** (`native`): SDK applications can configure MCP servers and SDK-defined MCP tools. Invocation: `options.mcpServers, strictMcpConfig`.
- **Agent tracing/event telemetry** (`native`): Typed result and task events provide execution telemetry. Invocation: `CLAUDE_CODE_ENABLE_TELEMETRY=1 (via options.env), OTEL_TRACES_EXPORTER`.
- **Subagents/delegation** (`native`): SDK applications can use Claude Code subagents and background tasks. Invocation: `options.agents, AgentDefinition`.
- **Granular permissions and approvals** (`native`): Allowed tools, permission modes, and callbacks govern actions. Invocation: `options.permissionMode, options.canUseTool`.
- **Programmatic human approval** (`native`): Embedding applications can implement human/tool approval callbacks. Invocation: `options.canUseTool`.
- **Resume, fork, and session lineage** (`native`): SDK session IDs and stores support resume and session lifecycle management. Invocation: `options.resume, options.forkSession`.

## Administrator

- **Embeddable SDK** (`configurable`): TypeScript API embeds the Claude Code agent loop, tools, and context management. Invocation: `query()`.
- **Machine-readable output** (`configurable`): Typed message streams expose assistant, tool, task, usage, and terminal-result events. Invocation: `options.outputFormat = { type: 'json_schema', schema: ... }`.
- **Lifecycle hooks** (`configurable`): Lifecycle hooks and permission callbacks are available to embedding applications. Invocation: `options.hooks, HookCallbackMatcher`.
- **MCP client** (`configurable`): SDK applications can configure MCP servers and SDK-defined MCP tools. Invocation: `options.mcpServers, strictMcpConfig`.
- **Agent tracing/event telemetry** (`configurable`): Typed result and task events provide execution telemetry. Invocation: `CLAUDE_CODE_ENABLE_TELEMETRY=1 (via options.env), OTEL_TRACES_EXPORTER`.
- **Subagents/delegation** (`configurable`): SDK applications can use Claude Code subagents and background tasks. Invocation: `options.agents, AgentDefinition`.
- **Granular permissions and approvals** (`configurable`): Allowed tools, permission modes, and callbacks govern actions. Invocation: `options.permissionMode, options.canUseTool`.
- **Programmatic human approval** (`configurable`): Embedding applications can implement human/tool approval callbacks. Invocation: `options.canUseTool`.
- **Resume, fork, and session lineage** (`configurable`): SDK session IDs and stores support resume and session lifecycle management. Invocation: `options.resume, options.forkSession`.

## Freshness rule

Treat unavailable or unknown actor access as unsupported until verified. UI-only capability is not agent-callable by implication.
