---
schema_version: 0.1
harness_id: claude-agent-sdk-python
generated_at: 2026-09-07T04:43:09.252238Z
artifact_kind: harness_capability_guide
---

# Claude Agent SDK — Python — Agent Capability Guide

**Vendor:** Anthropic  
**Lifecycle:** active  
**Current version in registry:** 0.2.152  
**Last verified:** 2026-09-03T11:16:00.695788Z

> UI availability does not imply that an in-harness model or an external orchestrator can invoke the capability. Use the actor-specific sections below.

## Human operator

- **Embeddable SDK** (`supported`): Python API embeds the Claude Code agent loop, tools, and context management. Invocation: `query(), ClaudeSDKClient`.
- **Machine-readable output** (`supported`): Typed message streams expose assistant, tool, task, usage, and terminal-result events. Invocation: `ClaudeAgentOptions(output_format={"type": "json_schema", "schema": ...})`.
- **Lifecycle hooks** (`supported`): Lifecycle hooks and permission callbacks are available to embedding applications. Invocation: `ClaudeAgentOptions(hooks=...), HookMatcher`.
- **MCP client** (`supported`): SDK applications can configure MCP servers and SDK-defined MCP tools. Invocation: `ClaudeAgentOptions(mcp_servers=...), create_sdk_mcp_server()`.
- **Agent tracing/event telemetry** (`supported`): Typed result and task events provide execution telemetry. Invocation: `CLAUDE_CODE_ENABLE_TELEMETRY=1 (via ClaudeAgentOptions.env), OTEL_TRACES_EXPORTER`.
- **Subagents/delegation** (`supported`): SDK applications can use Claude Code subagents and background tasks. Invocation: `ClaudeAgentOptions(agents={...: AgentDefinition(...)})`.
- **Granular permissions and approvals** (`supported`): Allowed tools, permission modes, and callbacks govern actions. Invocation: `ClaudeAgentOptions(permission_mode=...), ClaudeAgentOptions(can_use_tool=...)`.
- **Programmatic human approval** (`supported`): Embedding applications can implement human/tool approval callbacks. Invocation: `ClaudeAgentOptions(can_use_tool=...), PermissionResultAllow/PermissionResultDeny`.
- **Resume, fork, and session lineage** (`supported`): SDK session IDs and stores support resume and session lifecycle management. Invocation: `ClaudeAgentOptions(resume=...), ClaudeAgentOptions(fork_session=True)`.

## In-harness agent

No positively verified capabilities in the current seed.

## External agent/orchestrator

- **Embeddable SDK** (`native`): Python API embeds the Claude Code agent loop, tools, and context management. Invocation: `query(), ClaudeSDKClient`.
- **Machine-readable output** (`native`): Typed message streams expose assistant, tool, task, usage, and terminal-result events. Invocation: `ClaudeAgentOptions(output_format={"type": "json_schema", "schema": ...})`.
- **Lifecycle hooks** (`native`): Lifecycle hooks and permission callbacks are available to embedding applications. Invocation: `ClaudeAgentOptions(hooks=...), HookMatcher`.
- **MCP client** (`native`): SDK applications can configure MCP servers and SDK-defined MCP tools. Invocation: `ClaudeAgentOptions(mcp_servers=...), create_sdk_mcp_server()`.
- **Agent tracing/event telemetry** (`native`): Typed result and task events provide execution telemetry. Invocation: `CLAUDE_CODE_ENABLE_TELEMETRY=1 (via ClaudeAgentOptions.env), OTEL_TRACES_EXPORTER`.
- **Subagents/delegation** (`native`): SDK applications can use Claude Code subagents and background tasks. Invocation: `ClaudeAgentOptions(agents={...: AgentDefinition(...)})`.
- **Granular permissions and approvals** (`native`): Allowed tools, permission modes, and callbacks govern actions. Invocation: `ClaudeAgentOptions(permission_mode=...), ClaudeAgentOptions(can_use_tool=...)`.
- **Programmatic human approval** (`native`): Embedding applications can implement human/tool approval callbacks. Invocation: `ClaudeAgentOptions(can_use_tool=...), PermissionResultAllow/PermissionResultDeny`.
- **Resume, fork, and session lineage** (`native`): SDK session IDs and stores support resume and session lifecycle management. Invocation: `ClaudeAgentOptions(resume=...), ClaudeAgentOptions(fork_session=True)`.

## CI or scheduled automation

- **Embeddable SDK** (`native`): Python API embeds the Claude Code agent loop, tools, and context management. Invocation: `query(), ClaudeSDKClient`.
- **Machine-readable output** (`native`): Typed message streams expose assistant, tool, task, usage, and terminal-result events. Invocation: `ClaudeAgentOptions(output_format={"type": "json_schema", "schema": ...})`.
- **Lifecycle hooks** (`native`): Lifecycle hooks and permission callbacks are available to embedding applications. Invocation: `ClaudeAgentOptions(hooks=...), HookMatcher`.
- **MCP client** (`native`): SDK applications can configure MCP servers and SDK-defined MCP tools. Invocation: `ClaudeAgentOptions(mcp_servers=...), create_sdk_mcp_server()`.
- **Agent tracing/event telemetry** (`native`): Typed result and task events provide execution telemetry. Invocation: `CLAUDE_CODE_ENABLE_TELEMETRY=1 (via ClaudeAgentOptions.env), OTEL_TRACES_EXPORTER`.
- **Subagents/delegation** (`native`): SDK applications can use Claude Code subagents and background tasks. Invocation: `ClaudeAgentOptions(agents={...: AgentDefinition(...)})`.
- **Granular permissions and approvals** (`native`): Allowed tools, permission modes, and callbacks govern actions. Invocation: `ClaudeAgentOptions(permission_mode=...), ClaudeAgentOptions(can_use_tool=...)`.
- **Programmatic human approval** (`native`): Embedding applications can implement human/tool approval callbacks. Invocation: `ClaudeAgentOptions(can_use_tool=...), PermissionResultAllow/PermissionResultDeny`.
- **Resume, fork, and session lineage** (`native`): SDK session IDs and stores support resume and session lifecycle management. Invocation: `ClaudeAgentOptions(resume=...), ClaudeAgentOptions(fork_session=True)`.

## Administrator

- **Embeddable SDK** (`configurable`): Python API embeds the Claude Code agent loop, tools, and context management. Invocation: `query(), ClaudeSDKClient`.
- **Machine-readable output** (`configurable`): Typed message streams expose assistant, tool, task, usage, and terminal-result events. Invocation: `ClaudeAgentOptions(output_format={"type": "json_schema", "schema": ...})`.
- **Lifecycle hooks** (`configurable`): Lifecycle hooks and permission callbacks are available to embedding applications. Invocation: `ClaudeAgentOptions(hooks=...), HookMatcher`.
- **MCP client** (`configurable`): SDK applications can configure MCP servers and SDK-defined MCP tools. Invocation: `ClaudeAgentOptions(mcp_servers=...), create_sdk_mcp_server()`.
- **Agent tracing/event telemetry** (`configurable`): Typed result and task events provide execution telemetry. Invocation: `CLAUDE_CODE_ENABLE_TELEMETRY=1 (via ClaudeAgentOptions.env), OTEL_TRACES_EXPORTER`.
- **Subagents/delegation** (`configurable`): SDK applications can use Claude Code subagents and background tasks. Invocation: `ClaudeAgentOptions(agents={...: AgentDefinition(...)})`.
- **Granular permissions and approvals** (`configurable`): Allowed tools, permission modes, and callbacks govern actions. Invocation: `ClaudeAgentOptions(permission_mode=...), ClaudeAgentOptions(can_use_tool=...)`.
- **Programmatic human approval** (`configurable`): Embedding applications can implement human/tool approval callbacks. Invocation: `ClaudeAgentOptions(can_use_tool=...), PermissionResultAllow/PermissionResultDeny`.
- **Resume, fork, and session lineage** (`configurable`): SDK session IDs and stores support resume and session lifecycle management. Invocation: `ClaudeAgentOptions(resume=...), ClaudeAgentOptions(fork_session=True)`.

## Freshness rule

Treat unavailable or unknown actor access as unsupported until verified. UI-only capability is not agent-callable by implication.
