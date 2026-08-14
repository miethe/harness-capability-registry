---
schema_version: 0.1
harness_id: pi-agent
generated_at: 2026-08-08T20:00:00Z
artifact_kind: harness_capability_guide
---

# Pi Agent Harness — Agent Capability Guide

**Vendor:** Earendil Works  
**Lifecycle:** active  
**Current version in registry:** unknown  
**Last verified:** 2026-08-08T20:00:00Z

> UI availability does not imply that an in-harness model or an external orchestrator can invoke the capability. Use the actor-specific sections below.

## Human operator

- **Embeddable SDK** (`supported`): Pi includes an agent core runtime and unified LLM API packages. Invocation: `See evidence`.
- **Agent Skills** (`configurable`): Pi skills are compatible with Claude Code and Codex-style skill bundles. Invocation: `See evidence`.
- **Plugins/extensions** (`configurable`): Pi supports installable extensions. Invocation: `See evidence`.
- **Interactive terminal/TUI** (`native`): Pi includes an interactive coding-agent CLI. Invocation: `See evidence`.
- **Model/provider portability** (`native`): Pi includes a unified multi-provider LLM API. Invocation: `See evidence`.

## In-harness agent

- **Agent Skills** (`native`): Pi skills are compatible with Claude Code and Codex-style skill bundles. Invocation: `See evidence`.
- **Plugins/extensions** (`native`): Pi supports installable extensions. Invocation: `See evidence`.
- **Model/provider portability** (`supported`): Pi includes a unified multi-provider LLM API. Invocation: `See evidence`.

## External agent/orchestrator

- **Embeddable SDK** (`native`): Pi includes an agent core runtime and unified LLM API packages. Invocation: `See evidence`.
- **Agent Skills** (`supported`): Pi skills are compatible with Claude Code and Codex-style skill bundles. Invocation: `See evidence`.
- **Plugins/extensions** (`supported`): Pi supports installable extensions. Invocation: `See evidence`.
- **Model/provider portability** (`configurable`): Pi includes a unified multi-provider LLM API. Invocation: `See evidence`.

## CI or scheduled automation

- **Embeddable SDK** (`native`): Pi includes an agent core runtime and unified LLM API packages. Invocation: `See evidence`.
- **Agent Skills** (`supported`): Pi skills are compatible with Claude Code and Codex-style skill bundles. Invocation: `See evidence`.
- **Plugins/extensions** (`supported`): Pi supports installable extensions. Invocation: `See evidence`.
- **Model/provider portability** (`configurable`): Pi includes a unified multi-provider LLM API. Invocation: `See evidence`.

## Administrator

- **Embeddable SDK** (`configurable`): Pi includes an agent core runtime and unified LLM API packages. Invocation: `See evidence`.
- **Agent Skills** (`configurable`): Pi skills are compatible with Claude Code and Codex-style skill bundles. Invocation: `See evidence`.
- **Plugins/extensions** (`configurable`): Pi supports installable extensions. Invocation: `See evidence`.
- **Interactive terminal/TUI** (`configurable`): Pi includes an interactive coding-agent CLI. Invocation: `See evidence`.
- **Model/provider portability** (`configurable`): Pi includes a unified multi-provider LLM API. Invocation: `See evidence`.

## Freshness rule

Treat unavailable or unknown actor access as unsupported until verified. UI-only capability is not agent-callable by implication.
