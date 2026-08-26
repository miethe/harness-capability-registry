---
schema_version: 0.1
harness_id: qwen-code
generated_at: 2026-08-24T13:14:55.511915Z
artifact_kind: harness_capability_guide
---

# Qwen Code — Agent Capability Guide

**Vendor:** Alibaba / Qwen  
**Lifecycle:** active  
**Current version in registry:** 0.22.0  
**Last verified:** 2026-08-24T13:14:39.999942Z

> UI availability does not imply that an in-harness model or an external orchestrator can invoke the capability. Use the actor-specific sections below.

## Human operator

- **Agent-native file editing** (`supported`): Qwen Code can inspect and edit repository files. Invocation: `edit, write_file`.
- **Agent-native shell execution** (`supported`): Qwen Code can run shell commands. Invocation: `run_shell_command`.
- **Agent Skills** (`configurable`): Qwen Code follows the modern coding-harness skill/instruction model. Invocation: `/skills, /learn <source>, SKILL.md (in ~/.qwen/skills/<name>/ or .qwen/skills/<name>/)`.
- **MCP client** (`configurable`): Qwen Code supports MCP-style external tools. Invocation: `qwen mcp add <name> <commandOrUrl>, /mcp, mcpServers (in ~/.qwen/settings.json or .qwen/settings.json)`.
- **Desktop or web surface** (`native`): Qwen Code provides an official desktop application. Invocation: `Qwen Code Desktop (official macOS/Windows/Linux app)`.
- **Interactive terminal/TUI** (`native`): Qwen Code is an open-source terminal coding agent. Invocation: `qwen`.
- **Model/provider portability** (`native`): Qwen Code supports OpenAI, Anthropic, Gemini, and Qwen APIs. Invocation: `OPENAI_API_KEY, ANTHROPIC_API_KEY, GEMINI_API_KEY, modelProviders (in settings.json)`.
- **Resume, fork, and session lineage** (`native`): Sessions persist across interactive use. Invocation: `qwen --resume <sessionId>, qwen --continue, --checkpointing`.

## In-harness agent

- **Agent-native file editing** (`native`): Qwen Code can inspect and edit repository files. Invocation: `edit, write_file`.
- **Agent-native shell execution** (`native`): Qwen Code can run shell commands. Invocation: `run_shell_command`.
- **Agent Skills** (`native`): Qwen Code follows the modern coding-harness skill/instruction model. Invocation: `/skills, /learn <source>, SKILL.md (in ~/.qwen/skills/<name>/ or .qwen/skills/<name>/)`.
- **MCP client** (`native`): Qwen Code supports MCP-style external tools. Invocation: `qwen mcp add <name> <commandOrUrl>, /mcp, mcpServers (in ~/.qwen/settings.json or .qwen/settings.json)`.
- **Model/provider portability** (`supported`): Qwen Code supports OpenAI, Anthropic, Gemini, and Qwen APIs. Invocation: `OPENAI_API_KEY, ANTHROPIC_API_KEY, GEMINI_API_KEY, modelProviders (in settings.json)`.

## External agent/orchestrator

- **Agent-native file editing** (`supported`): Qwen Code can inspect and edit repository files. Invocation: `edit, write_file`.
- **Agent-native shell execution** (`supported`): Qwen Code can run shell commands. Invocation: `run_shell_command`.
- **Agent Skills** (`supported`): Qwen Code follows the modern coding-harness skill/instruction model. Invocation: `/skills, /learn <source>, SKILL.md (in ~/.qwen/skills/<name>/ or .qwen/skills/<name>/)`.
- **MCP client** (`supported`): Qwen Code supports MCP-style external tools. Invocation: `qwen mcp add <name> <commandOrUrl>, /mcp, mcpServers (in ~/.qwen/settings.json or .qwen/settings.json)`.
- **Model/provider portability** (`configurable`): Qwen Code supports OpenAI, Anthropic, Gemini, and Qwen APIs. Invocation: `OPENAI_API_KEY, ANTHROPIC_API_KEY, GEMINI_API_KEY, modelProviders (in settings.json)`.
- **Resume, fork, and session lineage** (`supported`): Sessions persist across interactive use. Invocation: `qwen --resume <sessionId>, qwen --continue, --checkpointing`.

## CI or scheduled automation

- **Agent-native file editing** (`supported`): Qwen Code can inspect and edit repository files. Invocation: `edit, write_file`.
- **Agent-native shell execution** (`supported`): Qwen Code can run shell commands. Invocation: `run_shell_command`.
- **Agent Skills** (`supported`): Qwen Code follows the modern coding-harness skill/instruction model. Invocation: `/skills, /learn <source>, SKILL.md (in ~/.qwen/skills/<name>/ or .qwen/skills/<name>/)`.
- **MCP client** (`supported`): Qwen Code supports MCP-style external tools. Invocation: `qwen mcp add <name> <commandOrUrl>, /mcp, mcpServers (in ~/.qwen/settings.json or .qwen/settings.json)`.
- **Model/provider portability** (`configurable`): Qwen Code supports OpenAI, Anthropic, Gemini, and Qwen APIs. Invocation: `OPENAI_API_KEY, ANTHROPIC_API_KEY, GEMINI_API_KEY, modelProviders (in settings.json)`.
- **Resume, fork, and session lineage** (`supported`): Sessions persist across interactive use. Invocation: `qwen --resume <sessionId>, qwen --continue, --checkpointing`.

## Administrator

- **Agent-native file editing** (`configurable`): Qwen Code can inspect and edit repository files. Invocation: `edit, write_file`.
- **Agent-native shell execution** (`configurable`): Qwen Code can run shell commands. Invocation: `run_shell_command`.
- **Agent Skills** (`configurable`): Qwen Code follows the modern coding-harness skill/instruction model. Invocation: `/skills, /learn <source>, SKILL.md (in ~/.qwen/skills/<name>/ or .qwen/skills/<name>/)`.
- **MCP client** (`configurable`): Qwen Code supports MCP-style external tools. Invocation: `qwen mcp add <name> <commandOrUrl>, /mcp, mcpServers (in ~/.qwen/settings.json or .qwen/settings.json)`.
- **Desktop or web surface** (`configurable`): Qwen Code provides an official desktop application. Invocation: `Qwen Code Desktop (official macOS/Windows/Linux app)`.
- **Interactive terminal/TUI** (`configurable`): Qwen Code is an open-source terminal coding agent. Invocation: `qwen`.
- **Model/provider portability** (`configurable`): Qwen Code supports OpenAI, Anthropic, Gemini, and Qwen APIs. Invocation: `OPENAI_API_KEY, ANTHROPIC_API_KEY, GEMINI_API_KEY, modelProviders (in settings.json)`.
- **Resume, fork, and session lineage** (`configurable`): Sessions persist across interactive use. Invocation: `qwen --resume <sessionId>, qwen --continue, --checkpointing`.

## Freshness rule

Treat unavailable or unknown actor access as unsupported until verified. UI-only capability is not agent-callable by implication.
