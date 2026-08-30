---
schema_version: 0.1
harness_id: openai-node-sdk
generated_at: 2026-08-30T21:07:07.656998Z
artifact_kind: harness_capability_guide
---

# OpenAI API SDK — Node — Agent Capability Guide

**Vendor:** OpenAI  
**Lifecycle:** active  
**Current version in registry:** 7.8.0  
**Last verified:** 2026-08-30T21:06:52.344015Z

> UI availability does not imply that an in-harness model or an external orchestrator can invoke the capability. Use the actor-specific sections below.

## Human operator

- **Embeddable SDK** (`supported`): Typed JavaScript/TypeScript access to the OpenAI API. Invocation: `npm install openai, import OpenAI from 'openai'; const client = new OpenAI();`.
- **Machine-readable output** (`supported`): Streaming and typed response objects support machine-readable application logic. Invocation: `client.responses.create({text: {format: {type: 'json_schema', strict: true, schema: ...}}}), client.responses.parse() with zodTextFormat()`.
- **Model and reasoning controls** (`supported`): Model and API feature parameters are exposed as generated typed interfaces. Invocation: `model: 'gpt-5...', reasoning: {effort: 'high'}`.

## In-harness agent

No positively verified capabilities in the current seed.

## External agent/orchestrator

- **Embeddable SDK** (`native`): Typed JavaScript/TypeScript access to the OpenAI API. Invocation: `npm install openai, import OpenAI from 'openai'; const client = new OpenAI();`.
- **Machine-readable output** (`native`): Streaming and typed response objects support machine-readable application logic. Invocation: `client.responses.create({text: {format: {type: 'json_schema', strict: true, schema: ...}}}), client.responses.parse() with zodTextFormat()`.
- **Model and reasoning controls** (`native`): Model and API feature parameters are exposed as generated typed interfaces. Invocation: `model: 'gpt-5...', reasoning: {effort: 'high'}`.

## CI or scheduled automation

- **Embeddable SDK** (`native`): Typed JavaScript/TypeScript access to the OpenAI API. Invocation: `npm install openai, import OpenAI from 'openai'; const client = new OpenAI();`.
- **Machine-readable output** (`native`): Streaming and typed response objects support machine-readable application logic. Invocation: `client.responses.create({text: {format: {type: 'json_schema', strict: true, schema: ...}}}), client.responses.parse() with zodTextFormat()`.
- **Model and reasoning controls** (`native`): Model and API feature parameters are exposed as generated typed interfaces. Invocation: `model: 'gpt-5...', reasoning: {effort: 'high'}`.

## Administrator

- **Embeddable SDK** (`configurable`): Typed JavaScript/TypeScript access to the OpenAI API. Invocation: `npm install openai, import OpenAI from 'openai'; const client = new OpenAI();`.
- **Machine-readable output** (`configurable`): Streaming and typed response objects support machine-readable application logic. Invocation: `client.responses.create({text: {format: {type: 'json_schema', strict: true, schema: ...}}}), client.responses.parse() with zodTextFormat()`.
- **Model and reasoning controls** (`configurable`): Model and API feature parameters are exposed as generated typed interfaces. Invocation: `model: 'gpt-5...', reasoning: {effort: 'high'}`.

## Freshness rule

Treat unavailable or unknown actor access as unsupported until verified. UI-only capability is not agent-callable by implication.
