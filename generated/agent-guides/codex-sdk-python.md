---
schema_version: 0.1
harness_id: codex-sdk-python
generated_at: 2026-09-07T04:43:09.252238Z
artifact_kind: harness_capability_guide
---

# Codex SDK — Python — Agent Capability Guide

**Vendor:** OpenAI  
**Lifecycle:** active  
**Current version in registry:** 0.147.0  
**Last verified:** 2026-08-18T18:57:45.521496Z

> UI availability does not imply that an in-harness model or an external orchestrator can invoke the capability. Use the actor-specific sections below.

## Human operator

- **Embeddable SDK** (`supported`): Python SDK controls the local Codex app-server over JSON-RPC and bundles a pinned runtime. Invocation: `pip install openai-codex, from openai_codex import Codex, AsyncCodex, Codex().thread_start(...)`.
- **Machine-readable output** (`supported`): Typed notifications and generated schemas expose machine-readable turn events. Invocation: `See evidence`.
- **RPC/app-server protocol** (`supported`): The SDK consumes Codex app-server JSON-RPC methods and version-specific schemas. Invocation: `CodexClient.request(method, params), thread_start, turn_start, thread_resume, thread_fork (Codex app-server JSON-RPC protocol)`.
- **Execution sandbox** (`supported`): Python SDK thread and turn calls expose Codex sandbox presets such as read-only and workspace-write. Invocation: `Sandbox.read_only, Sandbox.workspace_write, Sandbox.full_access (passed as sandbox= to thread_start/turn_start)`.
- **Programmatic human approval** (`supported`): SDK/app-server clients can participate in approval flows and return decisions through the machine protocol. Invocation: `ApprovalMode.deny_all, ApprovalMode.auto_review (passed as approval_mode= to thread_start/turn_start)`.
- **Resume, fork, and session lineage** (`supported`): SDK clients control Codex threads and turns. Invocation: `codex.thread_resume(thread_id), codex.thread_fork(thread_id)`.

## In-harness agent

No positively verified capabilities in the current seed.

## External agent/orchestrator

- **Embeddable SDK** (`native`): Python SDK controls the local Codex app-server over JSON-RPC and bundles a pinned runtime. Invocation: `pip install openai-codex, from openai_codex import Codex, AsyncCodex, Codex().thread_start(...)`.
- **Machine-readable output** (`native`): Typed notifications and generated schemas expose machine-readable turn events. Invocation: `See evidence`.
- **RPC/app-server protocol** (`native`): The SDK consumes Codex app-server JSON-RPC methods and version-specific schemas. Invocation: `CodexClient.request(method, params), thread_start, turn_start, thread_resume, thread_fork (Codex app-server JSON-RPC protocol)`.
- **Execution sandbox** (`native`): Python SDK thread and turn calls expose Codex sandbox presets such as read-only and workspace-write. Invocation: `Sandbox.read_only, Sandbox.workspace_write, Sandbox.full_access (passed as sandbox= to thread_start/turn_start)`.
- **Programmatic human approval** (`native`): SDK/app-server clients can participate in approval flows and return decisions through the machine protocol. Invocation: `ApprovalMode.deny_all, ApprovalMode.auto_review (passed as approval_mode= to thread_start/turn_start)`.
- **Resume, fork, and session lineage** (`native`): SDK clients control Codex threads and turns. Invocation: `codex.thread_resume(thread_id), codex.thread_fork(thread_id)`.

## CI or scheduled automation

- **Embeddable SDK** (`native`): Python SDK controls the local Codex app-server over JSON-RPC and bundles a pinned runtime. Invocation: `pip install openai-codex, from openai_codex import Codex, AsyncCodex, Codex().thread_start(...)`.
- **Machine-readable output** (`native`): Typed notifications and generated schemas expose machine-readable turn events. Invocation: `See evidence`.
- **RPC/app-server protocol** (`native`): The SDK consumes Codex app-server JSON-RPC methods and version-specific schemas. Invocation: `CodexClient.request(method, params), thread_start, turn_start, thread_resume, thread_fork (Codex app-server JSON-RPC protocol)`.
- **Execution sandbox** (`native`): Python SDK thread and turn calls expose Codex sandbox presets such as read-only and workspace-write. Invocation: `Sandbox.read_only, Sandbox.workspace_write, Sandbox.full_access (passed as sandbox= to thread_start/turn_start)`.
- **Programmatic human approval** (`native`): SDK/app-server clients can participate in approval flows and return decisions through the machine protocol. Invocation: `ApprovalMode.deny_all, ApprovalMode.auto_review (passed as approval_mode= to thread_start/turn_start)`.
- **Resume, fork, and session lineage** (`native`): SDK clients control Codex threads and turns. Invocation: `codex.thread_resume(thread_id), codex.thread_fork(thread_id)`.

## Administrator

- **Embeddable SDK** (`configurable`): Python SDK controls the local Codex app-server over JSON-RPC and bundles a pinned runtime. Invocation: `pip install openai-codex, from openai_codex import Codex, AsyncCodex, Codex().thread_start(...)`.
- **Machine-readable output** (`configurable`): Typed notifications and generated schemas expose machine-readable turn events. Invocation: `See evidence`.
- **RPC/app-server protocol** (`configurable`): The SDK consumes Codex app-server JSON-RPC methods and version-specific schemas. Invocation: `CodexClient.request(method, params), thread_start, turn_start, thread_resume, thread_fork (Codex app-server JSON-RPC protocol)`.
- **Execution sandbox** (`configurable`): Python SDK thread and turn calls expose Codex sandbox presets such as read-only and workspace-write. Invocation: `Sandbox.read_only, Sandbox.workspace_write, Sandbox.full_access (passed as sandbox= to thread_start/turn_start)`.
- **Programmatic human approval** (`configurable`): SDK/app-server clients can participate in approval flows and return decisions through the machine protocol. Invocation: `ApprovalMode.deny_all, ApprovalMode.auto_review (passed as approval_mode= to thread_start/turn_start)`.
- **Resume, fork, and session lineage** (`configurable`): SDK clients control Codex threads and turns. Invocation: `codex.thread_resume(thread_id), codex.thread_fork(thread_id)`.

## Freshness rule

Treat unavailable or unknown actor access as unsupported until verified. UI-only capability is not agent-callable by implication.
