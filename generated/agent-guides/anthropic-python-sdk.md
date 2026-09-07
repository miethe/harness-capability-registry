---
schema_version: 0.1
harness_id: anthropic-python-sdk
generated_at: 2026-09-07T04:43:09.252238Z
artifact_kind: harness_capability_guide
---

# Claude API SDK — Python — Agent Capability Guide

**Vendor:** Anthropic  
**Lifecycle:** active  
**Current version in registry:** 1.4.0  
**Last verified:** 2026-09-07T04:42:52.719081Z

> UI availability does not imply that an in-harness model or an external orchestrator can invoke the capability. Use the actor-specific sections below.

## Human operator

- **Embeddable SDK** (`supported`): Typed Python access to the Anthropic API. Invocation: `pip install anthropic, from anthropic import Anthropic; client = Anthropic()`.
- **Machine-readable output** (`supported`): Streaming and typed response objects support machine-readable application logic. Invocation: `client.messages.create(tools=[...], tool_choice=...), strict: true (tool definition), client.messages.create(stream=True)`.
- **Model and reasoning controls** (`supported`): Model and API feature parameters are exposed as generated typed interfaces. Invocation: `model="claude-...", thinking={"type": "enabled", "budget_tokens": N}, thinking={"type": "adaptive"}, output_config={"effort": "high"}`.

## In-harness agent

No positively verified capabilities in the current seed.

## External agent/orchestrator

- **Embeddable SDK** (`native`): Typed Python access to the Anthropic API. Invocation: `pip install anthropic, from anthropic import Anthropic; client = Anthropic()`.
- **Machine-readable output** (`native`): Streaming and typed response objects support machine-readable application logic. Invocation: `client.messages.create(tools=[...], tool_choice=...), strict: true (tool definition), client.messages.create(stream=True)`.
- **Model and reasoning controls** (`native`): Model and API feature parameters are exposed as generated typed interfaces. Invocation: `model="claude-...", thinking={"type": "enabled", "budget_tokens": N}, thinking={"type": "adaptive"}, output_config={"effort": "high"}`.

## CI or scheduled automation

- **Embeddable SDK** (`native`): Typed Python access to the Anthropic API. Invocation: `pip install anthropic, from anthropic import Anthropic; client = Anthropic()`.
- **Machine-readable output** (`native`): Streaming and typed response objects support machine-readable application logic. Invocation: `client.messages.create(tools=[...], tool_choice=...), strict: true (tool definition), client.messages.create(stream=True)`.
- **Model and reasoning controls** (`native`): Model and API feature parameters are exposed as generated typed interfaces. Invocation: `model="claude-...", thinking={"type": "enabled", "budget_tokens": N}, thinking={"type": "adaptive"}, output_config={"effort": "high"}`.

## Administrator

- **Embeddable SDK** (`configurable`): Typed Python access to the Anthropic API. Invocation: `pip install anthropic, from anthropic import Anthropic; client = Anthropic()`.
- **Machine-readable output** (`configurable`): Streaming and typed response objects support machine-readable application logic. Invocation: `client.messages.create(tools=[...], tool_choice=...), strict: true (tool definition), client.messages.create(stream=True)`.
- **Model and reasoning controls** (`configurable`): Model and API feature parameters are exposed as generated typed interfaces. Invocation: `model="claude-...", thinking={"type": "enabled", "budget_tokens": N}, thinking={"type": "adaptive"}, output_config={"effort": "high"}`.

## Freshness rule

Treat unavailable or unknown actor access as unsupported until verified. UI-only capability is not agent-callable by implication.
