---
schema_version: 0.1
harness_id: codex-sdk-python
generated_at: 2026-08-15T20:10:35.204766Z
artifact_kind: harness_capability_guide
---

# Codex SDK — Python — Agent Capability Guide

**Vendor:** OpenAI  
**Lifecycle:** active  
**Current version in registry:** 0.144.4  
**Last verified:** 2026-08-08T20:00:00Z

> UI availability does not imply that an in-harness model or an external orchestrator can invoke the capability. Use the actor-specific sections below.

## Human operator

- **Embeddable SDK** (`supported`): Python SDK controls the local Codex app-server over JSON-RPC and bundles a pinned runtime. Invocation: `See evidence`.
- **Machine-readable output** (`supported`): Typed notifications and generated schemas expose machine-readable turn events. Invocation: `See evidence`.
- **RPC/app-server protocol** (`supported`): The SDK consumes Codex app-server JSON-RPC methods and version-specific schemas. Invocation: `See evidence`.
- **Execution sandbox** (`supported`): Python SDK thread and turn calls expose Codex sandbox presets such as read-only and workspace-write. Invocation: `See evidence`.
- **Programmatic human approval** (`supported`): SDK/app-server clients can participate in approval flows and return decisions through the machine protocol. Invocation: `See evidence`.
- **Resume, fork, and session lineage** (`supported`): SDK clients control Codex threads and turns. Invocation: `See evidence`.

## In-harness agent

No positively verified capabilities in the current seed.

## External agent/orchestrator

- **Embeddable SDK** (`native`): Python SDK controls the local Codex app-server over JSON-RPC and bundles a pinned runtime. Invocation: `See evidence`.
- **Machine-readable output** (`native`): Typed notifications and generated schemas expose machine-readable turn events. Invocation: `See evidence`.
- **RPC/app-server protocol** (`native`): The SDK consumes Codex app-server JSON-RPC methods and version-specific schemas. Invocation: `See evidence`.
- **Execution sandbox** (`native`): Python SDK thread and turn calls expose Codex sandbox presets such as read-only and workspace-write. Invocation: `See evidence`.
- **Programmatic human approval** (`native`): SDK/app-server clients can participate in approval flows and return decisions through the machine protocol. Invocation: `See evidence`.
- **Resume, fork, and session lineage** (`native`): SDK clients control Codex threads and turns. Invocation: `See evidence`.

## CI or scheduled automation

- **Embeddable SDK** (`native`): Python SDK controls the local Codex app-server over JSON-RPC and bundles a pinned runtime. Invocation: `See evidence`.
- **Machine-readable output** (`native`): Typed notifications and generated schemas expose machine-readable turn events. Invocation: `See evidence`.
- **RPC/app-server protocol** (`native`): The SDK consumes Codex app-server JSON-RPC methods and version-specific schemas. Invocation: `See evidence`.
- **Execution sandbox** (`native`): Python SDK thread and turn calls expose Codex sandbox presets such as read-only and workspace-write. Invocation: `See evidence`.
- **Programmatic human approval** (`native`): SDK/app-server clients can participate in approval flows and return decisions through the machine protocol. Invocation: `See evidence`.
- **Resume, fork, and session lineage** (`native`): SDK clients control Codex threads and turns. Invocation: `See evidence`.

## Administrator

- **Embeddable SDK** (`configurable`): Python SDK controls the local Codex app-server over JSON-RPC and bundles a pinned runtime. Invocation: `See evidence`.
- **Machine-readable output** (`configurable`): Typed notifications and generated schemas expose machine-readable turn events. Invocation: `See evidence`.
- **RPC/app-server protocol** (`configurable`): The SDK consumes Codex app-server JSON-RPC methods and version-specific schemas. Invocation: `See evidence`.
- **Execution sandbox** (`configurable`): Python SDK thread and turn calls expose Codex sandbox presets such as read-only and workspace-write. Invocation: `See evidence`.
- **Programmatic human approval** (`configurable`): SDK/app-server clients can participate in approval flows and return decisions through the machine protocol. Invocation: `See evidence`.
- **Resume, fork, and session lineage** (`configurable`): SDK clients control Codex threads and turns. Invocation: `See evidence`.

## Freshness rule

Treat unavailable or unknown actor access as unsupported until verified. UI-only capability is not agent-callable by implication.
