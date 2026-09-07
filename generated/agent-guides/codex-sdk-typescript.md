---
schema_version: 0.1
harness_id: codex-sdk-typescript
generated_at: 2026-09-07T04:43:09.252238Z
artifact_kind: harness_capability_guide
---

# Codex SDK — TypeScript — Agent Capability Guide

**Vendor:** OpenAI  
**Lifecycle:** active  
**Current version in registry:** 0.154.0-alpha.3  
**Last verified:** 2026-09-07T04:42:52.719081Z

> UI availability does not imply that an in-harness model or an external orchestrator can invoke the capability. Use the actor-specific sections below.

## Human operator

- **Embeddable SDK** (`supported`): The server-side TypeScript SDK starts, continues, and resumes local Codex threads. Invocation: `npm install @openai/codex-sdk, import { Codex } from "@openai/codex-sdk", new Codex(), codex.startThread()`.
- **Machine-readable output** (`supported`): The TypeScript SDK exchanges JSONL events with the bundled/local Codex CLI for machine-readable progress. Invocation: `thread.run(input, { outputSchema }), thread.runStreamed(input, { outputSchema })`.
- **Execution sandbox** (`supported`): Thread options inherit Codex sandbox and approval controls available through the underlying CLI. Invocation: `codex.startThread({ sandboxMode: "read-only" | "workspace-write" | "danger-full-access" })`.
- **Resume, fork, and session lineage** (`supported`): Applications can continue the same thread or resume a prior thread by ID. Invocation: `codex.resumeThread(threadId, options)`.

## In-harness agent

No positively verified capabilities in the current seed.

## External agent/orchestrator

- **Embeddable SDK** (`native`): The server-side TypeScript SDK starts, continues, and resumes local Codex threads. Invocation: `npm install @openai/codex-sdk, import { Codex } from "@openai/codex-sdk", new Codex(), codex.startThread()`.
- **Machine-readable output** (`native`): The TypeScript SDK exchanges JSONL events with the bundled/local Codex CLI for machine-readable progress. Invocation: `thread.run(input, { outputSchema }), thread.runStreamed(input, { outputSchema })`.
- **Execution sandbox** (`native`): Thread options inherit Codex sandbox and approval controls available through the underlying CLI. Invocation: `codex.startThread({ sandboxMode: "read-only" | "workspace-write" | "danger-full-access" })`.
- **Resume, fork, and session lineage** (`native`): Applications can continue the same thread or resume a prior thread by ID. Invocation: `codex.resumeThread(threadId, options)`.

## CI or scheduled automation

- **Embeddable SDK** (`native`): The server-side TypeScript SDK starts, continues, and resumes local Codex threads. Invocation: `npm install @openai/codex-sdk, import { Codex } from "@openai/codex-sdk", new Codex(), codex.startThread()`.
- **Machine-readable output** (`native`): The TypeScript SDK exchanges JSONL events with the bundled/local Codex CLI for machine-readable progress. Invocation: `thread.run(input, { outputSchema }), thread.runStreamed(input, { outputSchema })`.
- **Execution sandbox** (`native`): Thread options inherit Codex sandbox and approval controls available through the underlying CLI. Invocation: `codex.startThread({ sandboxMode: "read-only" | "workspace-write" | "danger-full-access" })`.
- **Resume, fork, and session lineage** (`native`): Applications can continue the same thread or resume a prior thread by ID. Invocation: `codex.resumeThread(threadId, options)`.

## Administrator

- **Embeddable SDK** (`configurable`): The server-side TypeScript SDK starts, continues, and resumes local Codex threads. Invocation: `npm install @openai/codex-sdk, import { Codex } from "@openai/codex-sdk", new Codex(), codex.startThread()`.
- **Machine-readable output** (`configurable`): The TypeScript SDK exchanges JSONL events with the bundled/local Codex CLI for machine-readable progress. Invocation: `thread.run(input, { outputSchema }), thread.runStreamed(input, { outputSchema })`.
- **Execution sandbox** (`configurable`): Thread options inherit Codex sandbox and approval controls available through the underlying CLI. Invocation: `codex.startThread({ sandboxMode: "read-only" | "workspace-write" | "danger-full-access" })`.
- **Resume, fork, and session lineage** (`configurable`): Applications can continue the same thread or resume a prior thread by ID. Invocation: `codex.resumeThread(threadId, options)`.

## Freshness rule

Treat unavailable or unknown actor access as unsupported until verified. UI-only capability is not agent-callable by implication.
