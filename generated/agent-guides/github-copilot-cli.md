---
schema_version: 0.1
harness_id: github-copilot-cli
generated_at: 2026-08-18T18:58:02.113278Z
artifact_kind: harness_capability_guide
---

# GitHub Copilot CLI — Agent Capability Guide

**Vendor:** GitHub  
**Lifecycle:** active  
**Current version in registry:** 1.0.81-1  
**Last verified:** 2026-08-18T18:57:45.521496Z

> UI availability does not imply that an in-harness model or an external orchestrator can invoke the capability. Use the actor-specific sections below.

## Human operator

- **CI/GitHub automation** (`supported`): GitHub Agentic Workflows provides first-class Copilot engine support with custom agents and continuation controls. Invocation: `See evidence`.
- **Headless/non-interactive execution** (`supported`): Copilot CLI is the default engine in GitHub Agentic Workflows and supports unattended workflow execution. Invocation: `See evidence`.
- **Interactive terminal/TUI** (`native`): GitHub Copilot CLI provides an interactive terminal agent. Invocation: `See evidence`.

## In-harness agent

No positively verified capabilities in the current seed.

## External agent/orchestrator

- **CI/GitHub automation** (`native`): GitHub Agentic Workflows provides first-class Copilot engine support with custom agents and continuation controls. Invocation: `See evidence`.
- **Headless/non-interactive execution** (`native`): Copilot CLI is the default engine in GitHub Agentic Workflows and supports unattended workflow execution. Invocation: `See evidence`.

## CI or scheduled automation

- **CI/GitHub automation** (`native`): GitHub Agentic Workflows provides first-class Copilot engine support with custom agents and continuation controls. Invocation: `See evidence`.
- **Headless/non-interactive execution** (`native`): Copilot CLI is the default engine in GitHub Agentic Workflows and supports unattended workflow execution. Invocation: `See evidence`.

## Administrator

- **CI/GitHub automation** (`configurable`): GitHub Agentic Workflows provides first-class Copilot engine support with custom agents and continuation controls. Invocation: `See evidence`.
- **Headless/non-interactive execution** (`configurable`): Copilot CLI is the default engine in GitHub Agentic Workflows and supports unattended workflow execution. Invocation: `See evidence`.
- **Interactive terminal/TUI** (`configurable`): GitHub Copilot CLI provides an interactive terminal agent. Invocation: `See evidence`.
- **Enterprise managed policy** (`native`): GitHub organization controls and workflow permissions govern Copilot use. Invocation: `See evidence`.

## Freshness rule

Treat unavailable or unknown actor access as unsupported until verified. UI-only capability is not agent-callable by implication.
