---
schema_version: 0.1
harness_id: github-copilot-cli
generated_at: 2026-09-03T11:16:21.860159Z
artifact_kind: harness_capability_guide
---

# GitHub Copilot CLI — Agent Capability Guide

**Vendor:** GitHub  
**Lifecycle:** active  
**Current version in registry:** 1.0.83-3  
**Last verified:** 2026-09-03T11:16:00.695788Z

> UI availability does not imply that an in-harness model or an external orchestrator can invoke the capability. Use the actor-specific sections below.

## Human operator

- **CI/GitHub automation** (`supported`): GitHub Agentic Workflows provides first-class Copilot engine support with custom agents and continuation controls. Invocation: `engine: copilot, engine:
  id: copilot`.
- **Headless/non-interactive execution** (`supported`): Copilot CLI is the default engine in GitHub Agentic Workflows and supports unattended workflow execution. Invocation: `copilot -p "<prompt>", copilot --prompt "<prompt>", --allow-all-tools, --allow-tool='<tool>'`.
- **Interactive terminal/TUI** (`native`): GitHub Copilot CLI provides an interactive terminal agent. Invocation: `copilot`.

## In-harness agent

No positively verified capabilities in the current seed.

## External agent/orchestrator

- **CI/GitHub automation** (`native`): GitHub Agentic Workflows provides first-class Copilot engine support with custom agents and continuation controls. Invocation: `engine: copilot, engine:
  id: copilot`.
- **Headless/non-interactive execution** (`native`): Copilot CLI is the default engine in GitHub Agentic Workflows and supports unattended workflow execution. Invocation: `copilot -p "<prompt>", copilot --prompt "<prompt>", --allow-all-tools, --allow-tool='<tool>'`.

## CI or scheduled automation

- **CI/GitHub automation** (`native`): GitHub Agentic Workflows provides first-class Copilot engine support with custom agents and continuation controls. Invocation: `engine: copilot, engine:
  id: copilot`.
- **Headless/non-interactive execution** (`native`): Copilot CLI is the default engine in GitHub Agentic Workflows and supports unattended workflow execution. Invocation: `copilot -p "<prompt>", copilot --prompt "<prompt>", --allow-all-tools, --allow-tool='<tool>'`.

## Administrator

- **CI/GitHub automation** (`configurable`): GitHub Agentic Workflows provides first-class Copilot engine support with custom agents and continuation controls. Invocation: `engine: copilot, engine:
  id: copilot`.
- **Headless/non-interactive execution** (`configurable`): Copilot CLI is the default engine in GitHub Agentic Workflows and supports unattended workflow execution. Invocation: `copilot -p "<prompt>", copilot --prompt "<prompt>", --allow-all-tools, --allow-tool='<tool>'`.
- **Interactive terminal/TUI** (`configurable`): GitHub Copilot CLI provides an interactive terminal agent. Invocation: `copilot`.
- **Enterprise managed policy** (`native`): GitHub organization controls and workflow permissions govern Copilot use. Invocation: `Copilot CLI policy (Enterprise/Organization settings → Copilot → Policies → Clients → Copilot CLI: Enabled everywhere / Disabled everywhere / Let organizations decide)`.

## Freshness rule

Treat unavailable or unknown actor access as unsupported until verified. UI-only capability is not agent-callable by implication.
