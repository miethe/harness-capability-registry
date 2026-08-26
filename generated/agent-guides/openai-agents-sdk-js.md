---
schema_version: 0.1
harness_id: openai-agents-sdk-js
generated_at: 2026-08-24T13:14:55.511915Z
artifact_kind: harness_capability_guide
---

# OpenAI Agents SDK — JavaScript/TypeScript — Agent Capability Guide

**Vendor:** OpenAI  
**Lifecycle:** active  
**Current version in registry:** 0.17.0  
**Last verified:** 2026-08-24T13:14:39.999942Z

> UI availability does not imply that an in-harness model or an external orchestrator can invoke the capability. Use the actor-specific sections below.

## Human operator

- **Persistent memory** (`supported`): Sessions persist conversation state across agent runs. Invocation: `MemorySession, OpenAIConversationsSession`.
- **Embeddable SDK** (`supported`): JavaScript/TypeScript framework for building agent applications. Invocation: `Agent, Runner, run()`.
- **Machine-readable output** (`supported`): Typed agent results and structured outputs support downstream automation. Invocation: `outputType, AgentOutputType`.
- **MCP client** (`supported`): Agents can connect to MCP servers and expose MCP-backed tools. Invocation: `MCPServerStdio, MCPServerSSE, MCPServerStreamableHttp, mcpServers`.
- **Model/provider portability** (`supported`): The SDK supports OpenAI APIs and provider-compatible model adapters. Invocation: `ModelProvider, setDefaultModelProvider, Agent.model`.
- **Agent tracing/event telemetry** (`supported`): Built-in tracing records agents, generations, tools, handoffs, and guardrails. Invocation: `Trace, Span, TraceProvider`.
- **First-class multi-agent coordination** (`supported`): Supervisor/handoff patterns are first-class in the SDK. Invocation: `handoffs, Agent.asTool`.
- **Subagents/delegation** (`supported`): Handoffs and agents-as-tools compose multi-agent workflows. Invocation: `handoffs, Agent.asTool`.
- **Granular permissions and approvals** (`supported`): Guardrails and tool policies validate inputs, outputs, and actions. Invocation: `inputGuardrails, outputGuardrails`.
- **Programmatic human approval** (`supported`): Tool approval/guardrail patterns can be implemented in application code. Invocation: `needsApproval, tool_approval_requested, interruptions`.

## In-harness agent

No positively verified capabilities in the current seed.

## External agent/orchestrator

- **Persistent memory** (`native`): Sessions persist conversation state across agent runs. Invocation: `MemorySession, OpenAIConversationsSession`.
- **Embeddable SDK** (`native`): JavaScript/TypeScript framework for building agent applications. Invocation: `Agent, Runner, run()`.
- **Machine-readable output** (`native`): Typed agent results and structured outputs support downstream automation. Invocation: `outputType, AgentOutputType`.
- **MCP client** (`native`): Agents can connect to MCP servers and expose MCP-backed tools. Invocation: `MCPServerStdio, MCPServerSSE, MCPServerStreamableHttp, mcpServers`.
- **Model/provider portability** (`native`): The SDK supports OpenAI APIs and provider-compatible model adapters. Invocation: `ModelProvider, setDefaultModelProvider, Agent.model`.
- **Agent tracing/event telemetry** (`native`): Built-in tracing records agents, generations, tools, handoffs, and guardrails. Invocation: `Trace, Span, TraceProvider`.
- **First-class multi-agent coordination** (`native`): Supervisor/handoff patterns are first-class in the SDK. Invocation: `handoffs, Agent.asTool`.
- **Subagents/delegation** (`native`): Handoffs and agents-as-tools compose multi-agent workflows. Invocation: `handoffs, Agent.asTool`.
- **Granular permissions and approvals** (`native`): Guardrails and tool policies validate inputs, outputs, and actions. Invocation: `inputGuardrails, outputGuardrails`.
- **Programmatic human approval** (`native`): Tool approval/guardrail patterns can be implemented in application code. Invocation: `needsApproval, tool_approval_requested, interruptions`.

## CI or scheduled automation

- **Persistent memory** (`native`): Sessions persist conversation state across agent runs. Invocation: `MemorySession, OpenAIConversationsSession`.
- **Embeddable SDK** (`native`): JavaScript/TypeScript framework for building agent applications. Invocation: `Agent, Runner, run()`.
- **Machine-readable output** (`native`): Typed agent results and structured outputs support downstream automation. Invocation: `outputType, AgentOutputType`.
- **MCP client** (`native`): Agents can connect to MCP servers and expose MCP-backed tools. Invocation: `MCPServerStdio, MCPServerSSE, MCPServerStreamableHttp, mcpServers`.
- **Model/provider portability** (`native`): The SDK supports OpenAI APIs and provider-compatible model adapters. Invocation: `ModelProvider, setDefaultModelProvider, Agent.model`.
- **Agent tracing/event telemetry** (`native`): Built-in tracing records agents, generations, tools, handoffs, and guardrails. Invocation: `Trace, Span, TraceProvider`.
- **First-class multi-agent coordination** (`native`): Supervisor/handoff patterns are first-class in the SDK. Invocation: `handoffs, Agent.asTool`.
- **Subagents/delegation** (`native`): Handoffs and agents-as-tools compose multi-agent workflows. Invocation: `handoffs, Agent.asTool`.
- **Granular permissions and approvals** (`native`): Guardrails and tool policies validate inputs, outputs, and actions. Invocation: `inputGuardrails, outputGuardrails`.
- **Programmatic human approval** (`native`): Tool approval/guardrail patterns can be implemented in application code. Invocation: `needsApproval, tool_approval_requested, interruptions`.

## Administrator

- **Persistent memory** (`configurable`): Sessions persist conversation state across agent runs. Invocation: `MemorySession, OpenAIConversationsSession`.
- **Embeddable SDK** (`configurable`): JavaScript/TypeScript framework for building agent applications. Invocation: `Agent, Runner, run()`.
- **Machine-readable output** (`configurable`): Typed agent results and structured outputs support downstream automation. Invocation: `outputType, AgentOutputType`.
- **MCP client** (`configurable`): Agents can connect to MCP servers and expose MCP-backed tools. Invocation: `MCPServerStdio, MCPServerSSE, MCPServerStreamableHttp, mcpServers`.
- **Model/provider portability** (`configurable`): The SDK supports OpenAI APIs and provider-compatible model adapters. Invocation: `ModelProvider, setDefaultModelProvider, Agent.model`.
- **Agent tracing/event telemetry** (`configurable`): Built-in tracing records agents, generations, tools, handoffs, and guardrails. Invocation: `Trace, Span, TraceProvider`.
- **First-class multi-agent coordination** (`configurable`): Supervisor/handoff patterns are first-class in the SDK. Invocation: `handoffs, Agent.asTool`.
- **Subagents/delegation** (`configurable`): Handoffs and agents-as-tools compose multi-agent workflows. Invocation: `handoffs, Agent.asTool`.
- **Granular permissions and approvals** (`configurable`): Guardrails and tool policies validate inputs, outputs, and actions. Invocation: `inputGuardrails, outputGuardrails`.
- **Programmatic human approval** (`configurable`): Tool approval/guardrail patterns can be implemented in application code. Invocation: `needsApproval, tool_approval_requested, interruptions`.

## Freshness rule

Treat unavailable or unknown actor access as unsupported until verified. UI-only capability is not agent-callable by implication.
