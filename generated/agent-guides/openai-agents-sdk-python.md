---
schema_version: 0.1
harness_id: openai-agents-sdk-python
generated_at: 2026-08-15T20:10:35.204766Z
artifact_kind: harness_capability_guide
---

# OpenAI Agents SDK — Python — Agent Capability Guide

**Vendor:** OpenAI  
**Lifecycle:** active  
**Current version in registry:** 0.21.0  
**Last verified:** 2026-08-15T20:10:18.746297Z

> UI availability does not imply that an in-harness model or an external orchestrator can invoke the capability. Use the actor-specific sections below.

## Human operator

- **Persistent memory** (`supported`): Sessions persist conversation state across agent runs. Invocation: `See evidence`.
- **Embeddable SDK** (`supported`): Python framework for building agent applications. Invocation: `See evidence`.
- **Machine-readable output** (`supported`): Typed agent results and structured outputs support downstream automation. Invocation: `See evidence`.
- **MCP client** (`supported`): Agents can connect to MCP servers and expose MCP-backed tools. Invocation: `See evidence`.
- **Model/provider portability** (`supported`): The SDK supports OpenAI APIs and provider-compatible model adapters. Invocation: `See evidence`.
- **Agent tracing/event telemetry** (`supported`): Built-in tracing records agents, generations, tools, handoffs, and guardrails. Invocation: `See evidence`.
- **First-class multi-agent coordination** (`supported`): Supervisor/handoff patterns are first-class in the SDK. Invocation: `See evidence`.
- **Subagents/delegation** (`supported`): Handoffs and agents-as-tools compose multi-agent workflows. Invocation: `See evidence`.
- **Granular permissions and approvals** (`supported`): Guardrails and tool policies validate inputs, outputs, and actions. Invocation: `See evidence`.
- **Programmatic human approval** (`supported`): Tool approval/guardrail patterns can be implemented in application code. Invocation: `See evidence`.

## In-harness agent

No positively verified capabilities in the current seed.

## External agent/orchestrator

- **Persistent memory** (`native`): Sessions persist conversation state across agent runs. Invocation: `See evidence`.
- **Embeddable SDK** (`native`): Python framework for building agent applications. Invocation: `See evidence`.
- **Machine-readable output** (`native`): Typed agent results and structured outputs support downstream automation. Invocation: `See evidence`.
- **MCP client** (`native`): Agents can connect to MCP servers and expose MCP-backed tools. Invocation: `See evidence`.
- **Model/provider portability** (`native`): The SDK supports OpenAI APIs and provider-compatible model adapters. Invocation: `See evidence`.
- **Agent tracing/event telemetry** (`native`): Built-in tracing records agents, generations, tools, handoffs, and guardrails. Invocation: `See evidence`.
- **First-class multi-agent coordination** (`native`): Supervisor/handoff patterns are first-class in the SDK. Invocation: `See evidence`.
- **Subagents/delegation** (`native`): Handoffs and agents-as-tools compose multi-agent workflows. Invocation: `See evidence`.
- **Granular permissions and approvals** (`native`): Guardrails and tool policies validate inputs, outputs, and actions. Invocation: `See evidence`.
- **Programmatic human approval** (`native`): Tool approval/guardrail patterns can be implemented in application code. Invocation: `See evidence`.

## CI or scheduled automation

- **Persistent memory** (`native`): Sessions persist conversation state across agent runs. Invocation: `See evidence`.
- **Embeddable SDK** (`native`): Python framework for building agent applications. Invocation: `See evidence`.
- **Machine-readable output** (`native`): Typed agent results and structured outputs support downstream automation. Invocation: `See evidence`.
- **MCP client** (`native`): Agents can connect to MCP servers and expose MCP-backed tools. Invocation: `See evidence`.
- **Model/provider portability** (`native`): The SDK supports OpenAI APIs and provider-compatible model adapters. Invocation: `See evidence`.
- **Agent tracing/event telemetry** (`native`): Built-in tracing records agents, generations, tools, handoffs, and guardrails. Invocation: `See evidence`.
- **First-class multi-agent coordination** (`native`): Supervisor/handoff patterns are first-class in the SDK. Invocation: `See evidence`.
- **Subagents/delegation** (`native`): Handoffs and agents-as-tools compose multi-agent workflows. Invocation: `See evidence`.
- **Granular permissions and approvals** (`native`): Guardrails and tool policies validate inputs, outputs, and actions. Invocation: `See evidence`.
- **Programmatic human approval** (`native`): Tool approval/guardrail patterns can be implemented in application code. Invocation: `See evidence`.

## Administrator

- **Persistent memory** (`configurable`): Sessions persist conversation state across agent runs. Invocation: `See evidence`.
- **Embeddable SDK** (`configurable`): Python framework for building agent applications. Invocation: `See evidence`.
- **Machine-readable output** (`configurable`): Typed agent results and structured outputs support downstream automation. Invocation: `See evidence`.
- **MCP client** (`configurable`): Agents can connect to MCP servers and expose MCP-backed tools. Invocation: `See evidence`.
- **Model/provider portability** (`configurable`): The SDK supports OpenAI APIs and provider-compatible model adapters. Invocation: `See evidence`.
- **Agent tracing/event telemetry** (`configurable`): Built-in tracing records agents, generations, tools, handoffs, and guardrails. Invocation: `See evidence`.
- **First-class multi-agent coordination** (`configurable`): Supervisor/handoff patterns are first-class in the SDK. Invocation: `See evidence`.
- **Subagents/delegation** (`configurable`): Handoffs and agents-as-tools compose multi-agent workflows. Invocation: `See evidence`.
- **Granular permissions and approvals** (`configurable`): Guardrails and tool policies validate inputs, outputs, and actions. Invocation: `See evidence`.
- **Programmatic human approval** (`configurable`): Tool approval/guardrail patterns can be implemented in application code. Invocation: `See evidence`.

## Freshness rule

Treat unavailable or unknown actor access as unsupported until verified. UI-only capability is not agent-callable by implication.
