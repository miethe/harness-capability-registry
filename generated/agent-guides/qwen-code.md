---
schema_version: 0.1
harness_id: qwen-code
generated_at: 2026-08-15T20:10:35.204766Z
artifact_kind: harness_capability_guide
---

# Qwen Code — Agent Capability Guide

**Vendor:** Alibaba / Qwen  
**Lifecycle:** active  
**Current version in registry:** 0.21.12  
**Last verified:** 2026-08-15T20:10:18.746297Z

> UI availability does not imply that an in-harness model or an external orchestrator can invoke the capability. Use the actor-specific sections below.

## Human operator

- **Agent-native file editing** (`supported`): Qwen Code can inspect and edit repository files. Invocation: `See evidence`.
- **Agent-native shell execution** (`supported`): Qwen Code can run shell commands. Invocation: `See evidence`.
- **Agent Skills** (`configurable`): Qwen Code follows the modern coding-harness skill/instruction model. Invocation: `See evidence`.
- **MCP client** (`configurable`): Qwen Code supports MCP-style external tools. Invocation: `See evidence`.
- **Desktop or web surface** (`native`): Qwen Code provides an official desktop application. Invocation: `See evidence`.
- **Interactive terminal/TUI** (`native`): Qwen Code is an open-source terminal coding agent. Invocation: `See evidence`.
- **Model/provider portability** (`native`): Qwen Code supports OpenAI, Anthropic, Gemini, and Qwen APIs. Invocation: `See evidence`.
- **Resume, fork, and session lineage** (`native`): Sessions persist across interactive use. Invocation: `See evidence`.

## In-harness agent

- **Agent-native file editing** (`native`): Qwen Code can inspect and edit repository files. Invocation: `See evidence`.
- **Agent-native shell execution** (`native`): Qwen Code can run shell commands. Invocation: `See evidence`.
- **Agent Skills** (`native`): Qwen Code follows the modern coding-harness skill/instruction model. Invocation: `See evidence`.
- **MCP client** (`native`): Qwen Code supports MCP-style external tools. Invocation: `See evidence`.
- **Model/provider portability** (`supported`): Qwen Code supports OpenAI, Anthropic, Gemini, and Qwen APIs. Invocation: `See evidence`.

## External agent/orchestrator

- **Agent-native file editing** (`supported`): Qwen Code can inspect and edit repository files. Invocation: `See evidence`.
- **Agent-native shell execution** (`supported`): Qwen Code can run shell commands. Invocation: `See evidence`.
- **Agent Skills** (`supported`): Qwen Code follows the modern coding-harness skill/instruction model. Invocation: `See evidence`.
- **MCP client** (`supported`): Qwen Code supports MCP-style external tools. Invocation: `See evidence`.
- **Model/provider portability** (`configurable`): Qwen Code supports OpenAI, Anthropic, Gemini, and Qwen APIs. Invocation: `See evidence`.
- **Resume, fork, and session lineage** (`supported`): Sessions persist across interactive use. Invocation: `See evidence`.

## CI or scheduled automation

- **Agent-native file editing** (`supported`): Qwen Code can inspect and edit repository files. Invocation: `See evidence`.
- **Agent-native shell execution** (`supported`): Qwen Code can run shell commands. Invocation: `See evidence`.
- **Agent Skills** (`supported`): Qwen Code follows the modern coding-harness skill/instruction model. Invocation: `See evidence`.
- **MCP client** (`supported`): Qwen Code supports MCP-style external tools. Invocation: `See evidence`.
- **Model/provider portability** (`configurable`): Qwen Code supports OpenAI, Anthropic, Gemini, and Qwen APIs. Invocation: `See evidence`.
- **Resume, fork, and session lineage** (`supported`): Sessions persist across interactive use. Invocation: `See evidence`.

## Administrator

- **Agent-native file editing** (`configurable`): Qwen Code can inspect and edit repository files. Invocation: `See evidence`.
- **Agent-native shell execution** (`configurable`): Qwen Code can run shell commands. Invocation: `See evidence`.
- **Agent Skills** (`configurable`): Qwen Code follows the modern coding-harness skill/instruction model. Invocation: `See evidence`.
- **MCP client** (`configurable`): Qwen Code supports MCP-style external tools. Invocation: `See evidence`.
- **Desktop or web surface** (`configurable`): Qwen Code provides an official desktop application. Invocation: `See evidence`.
- **Interactive terminal/TUI** (`configurable`): Qwen Code is an open-source terminal coding agent. Invocation: `See evidence`.
- **Model/provider portability** (`configurable`): Qwen Code supports OpenAI, Anthropic, Gemini, and Qwen APIs. Invocation: `See evidence`.
- **Resume, fork, and session lineage** (`configurable`): Sessions persist across interactive use. Invocation: `See evidence`.

## Freshness rule

Treat unavailable or unknown actor access as unsupported until verified. UI-only capability is not agent-callable by implication.
