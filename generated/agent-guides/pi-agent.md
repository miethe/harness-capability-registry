---
schema_version: 0.1
harness_id: pi-agent
generated_at: 2026-08-30T21:07:07.656998Z
artifact_kind: harness_capability_guide
---

# Pi Agent Harness — Agent Capability Guide

**Vendor:** Earendil Works  
**Lifecycle:** active  
**Current version in registry:** 0.84.4  
**Last verified:** 2026-08-30T21:06:52.344015Z

> UI availability does not imply that an in-harness model or an external orchestrator can invoke the capability. Use the actor-specific sections below.

## Human operator

- **Embeddable SDK** (`supported`): Pi includes an agent core runtime and unified LLM API packages. Invocation: `createAgentSession() from @earendil-works/pi-coding-agent (npm)`.
- **Agent Skills** (`configurable`): Pi skills are compatible with Claude Code and Codex-style skill bundles. Invocation: `--skill <path> flag, ~/.pi/agent/skills/ directory, .pi/skills/ directory, skills array in settings.json`.
- **Plugins/extensions** (`configurable`): Pi supports installable extensions. Invocation: `pi install npm:<pkg>, pi install git:<repo>, pi install <path>`.
- **Interactive terminal/TUI** (`native`): Pi includes an interactive coding-agent CLI. Invocation: `pi`.
- **Model/provider portability** (`native`): Pi includes a unified multi-provider LLM API. Invocation: `/login command, provider API-key env vars (e.g. ANTHROPIC_API_KEY, OPENAI_API_KEY)`.

## In-harness agent

- **Agent Skills** (`native`): Pi skills are compatible with Claude Code and Codex-style skill bundles. Invocation: `--skill <path> flag, ~/.pi/agent/skills/ directory, .pi/skills/ directory, skills array in settings.json`.
- **Plugins/extensions** (`native`): Pi supports installable extensions. Invocation: `pi install npm:<pkg>, pi install git:<repo>, pi install <path>`.
- **Model/provider portability** (`supported`): Pi includes a unified multi-provider LLM API. Invocation: `/login command, provider API-key env vars (e.g. ANTHROPIC_API_KEY, OPENAI_API_KEY)`.

## External agent/orchestrator

- **Embeddable SDK** (`native`): Pi includes an agent core runtime and unified LLM API packages. Invocation: `createAgentSession() from @earendil-works/pi-coding-agent (npm)`.
- **Agent Skills** (`supported`): Pi skills are compatible with Claude Code and Codex-style skill bundles. Invocation: `--skill <path> flag, ~/.pi/agent/skills/ directory, .pi/skills/ directory, skills array in settings.json`.
- **Plugins/extensions** (`supported`): Pi supports installable extensions. Invocation: `pi install npm:<pkg>, pi install git:<repo>, pi install <path>`.
- **Model/provider portability** (`configurable`): Pi includes a unified multi-provider LLM API. Invocation: `/login command, provider API-key env vars (e.g. ANTHROPIC_API_KEY, OPENAI_API_KEY)`.

## CI or scheduled automation

- **Embeddable SDK** (`native`): Pi includes an agent core runtime and unified LLM API packages. Invocation: `createAgentSession() from @earendil-works/pi-coding-agent (npm)`.
- **Agent Skills** (`supported`): Pi skills are compatible with Claude Code and Codex-style skill bundles. Invocation: `--skill <path> flag, ~/.pi/agent/skills/ directory, .pi/skills/ directory, skills array in settings.json`.
- **Plugins/extensions** (`supported`): Pi supports installable extensions. Invocation: `pi install npm:<pkg>, pi install git:<repo>, pi install <path>`.
- **Model/provider portability** (`configurable`): Pi includes a unified multi-provider LLM API. Invocation: `/login command, provider API-key env vars (e.g. ANTHROPIC_API_KEY, OPENAI_API_KEY)`.

## Administrator

- **Embeddable SDK** (`configurable`): Pi includes an agent core runtime and unified LLM API packages. Invocation: `createAgentSession() from @earendil-works/pi-coding-agent (npm)`.
- **Agent Skills** (`configurable`): Pi skills are compatible with Claude Code and Codex-style skill bundles. Invocation: `--skill <path> flag, ~/.pi/agent/skills/ directory, .pi/skills/ directory, skills array in settings.json`.
- **Plugins/extensions** (`configurable`): Pi supports installable extensions. Invocation: `pi install npm:<pkg>, pi install git:<repo>, pi install <path>`.
- **Interactive terminal/TUI** (`configurable`): Pi includes an interactive coding-agent CLI. Invocation: `pi`.
- **Model/provider portability** (`configurable`): Pi includes a unified multi-provider LLM API. Invocation: `/login command, provider API-key env vars (e.g. ANTHROPIC_API_KEY, OPENAI_API_KEY)`.

## Freshness rule

Treat unavailable or unknown actor access as unsupported until verified. UI-only capability is not agent-callable by implication.
