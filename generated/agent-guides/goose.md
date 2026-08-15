---
schema_version: 0.1
harness_id: goose
generated_at: 2026-08-15T20:10:35.204766Z
artifact_kind: harness_capability_guide
---

# goose — Agent Capability Guide

**Vendor:** Block  
**Lifecycle:** active  
**Current version in registry:** 2.0.0-rc-04-27-0  
**Last verified:** 2026-08-15T20:10:18.746297Z

> UI availability does not imply that an in-harness model or an external orchestrator can invoke the capability. Use the actor-specific sections below.

## Human operator

- **Agent-native file editing** (`supported`): goose can install, execute, edit, and test through agent tools. Invocation: `See evidence`.
- **Agent-native shell execution** (`supported`): goose can execute local commands. Invocation: `See evidence`.
- **Headless/non-interactive execution** (`supported`): goose server and CLI paths support external automation. Invocation: `See evidence`.
- **RPC/app-server protocol** (`supported`): The goosed server exposes agent functionality to clients. Invocation: `See evidence`.
- **Agent Skills** (`configurable`): Recipes and reusable instructions package workflows for agents. Invocation: `See evidence`.
- **MCP client** (`configurable`): goose is MCP-first and can use MCP extensions and apps. Invocation: `See evidence`.
- **Desktop or web surface** (`native`): goose provides an Electron desktop interface. Invocation: `See evidence`.
- **Interactive terminal/TUI** (`native`): goose provides a CLI agent interface. Invocation: `See evidence`.
- **Model/provider portability** (`native`): goose is designed to work with multiple LLM providers and local models. Invocation: `See evidence`.
- **Subagents/delegation** (`supported`): goose supports delegated/subagent workflows through recipes and summon/delegate primitives. Invocation: `See evidence`.
- **Self-hosted worker/runtime** (`configurable`): goose runs locally or on user-managed servers. Invocation: `See evidence`.

## In-harness agent

- **Agent-native file editing** (`native`): goose can install, execute, edit, and test through agent tools. Invocation: `See evidence`.
- **Agent-native shell execution** (`native`): goose can execute local commands. Invocation: `See evidence`.
- **Agent Skills** (`native`): Recipes and reusable instructions package workflows for agents. Invocation: `See evidence`.
- **MCP client** (`native`): goose is MCP-first and can use MCP extensions and apps. Invocation: `See evidence`.
- **Model/provider portability** (`supported`): goose is designed to work with multiple LLM providers and local models. Invocation: `See evidence`.
- **Subagents/delegation** (`native`): goose supports delegated/subagent workflows through recipes and summon/delegate primitives. Invocation: `See evidence`.

## External agent/orchestrator

- **Agent-native file editing** (`supported`): goose can install, execute, edit, and test through agent tools. Invocation: `See evidence`.
- **Agent-native shell execution** (`supported`): goose can execute local commands. Invocation: `See evidence`.
- **Headless/non-interactive execution** (`native`): goose server and CLI paths support external automation. Invocation: `See evidence`.
- **RPC/app-server protocol** (`native`): The goosed server exposes agent functionality to clients. Invocation: `See evidence`.
- **Agent Skills** (`supported`): Recipes and reusable instructions package workflows for agents. Invocation: `See evidence`.
- **MCP client** (`supported`): goose is MCP-first and can use MCP extensions and apps. Invocation: `See evidence`.
- **Model/provider portability** (`configurable`): goose is designed to work with multiple LLM providers and local models. Invocation: `See evidence`.
- **Subagents/delegation** (`supported`): goose supports delegated/subagent workflows through recipes and summon/delegate primitives. Invocation: `See evidence`.
- **Self-hosted worker/runtime** (`supported`): goose runs locally or on user-managed servers. Invocation: `See evidence`.

## CI or scheduled automation

- **Agent-native file editing** (`supported`): goose can install, execute, edit, and test through agent tools. Invocation: `See evidence`.
- **Agent-native shell execution** (`supported`): goose can execute local commands. Invocation: `See evidence`.
- **Headless/non-interactive execution** (`native`): goose server and CLI paths support external automation. Invocation: `See evidence`.
- **RPC/app-server protocol** (`native`): The goosed server exposes agent functionality to clients. Invocation: `See evidence`.
- **Agent Skills** (`supported`): Recipes and reusable instructions package workflows for agents. Invocation: `See evidence`.
- **MCP client** (`supported`): goose is MCP-first and can use MCP extensions and apps. Invocation: `See evidence`.
- **Model/provider portability** (`configurable`): goose is designed to work with multiple LLM providers and local models. Invocation: `See evidence`.
- **Subagents/delegation** (`supported`): goose supports delegated/subagent workflows through recipes and summon/delegate primitives. Invocation: `See evidence`.
- **Self-hosted worker/runtime** (`supported`): goose runs locally or on user-managed servers. Invocation: `See evidence`.

## Administrator

- **Agent-native file editing** (`configurable`): goose can install, execute, edit, and test through agent tools. Invocation: `See evidence`.
- **Agent-native shell execution** (`configurable`): goose can execute local commands. Invocation: `See evidence`.
- **Headless/non-interactive execution** (`configurable`): goose server and CLI paths support external automation. Invocation: `See evidence`.
- **RPC/app-server protocol** (`configurable`): The goosed server exposes agent functionality to clients. Invocation: `See evidence`.
- **Agent Skills** (`configurable`): Recipes and reusable instructions package workflows for agents. Invocation: `See evidence`.
- **MCP client** (`configurable`): goose is MCP-first and can use MCP extensions and apps. Invocation: `See evidence`.
- **Desktop or web surface** (`configurable`): goose provides an Electron desktop interface. Invocation: `See evidence`.
- **Interactive terminal/TUI** (`configurable`): goose provides a CLI agent interface. Invocation: `See evidence`.
- **Model/provider portability** (`configurable`): goose is designed to work with multiple LLM providers and local models. Invocation: `See evidence`.
- **Subagents/delegation** (`configurable`): goose supports delegated/subagent workflows through recipes and summon/delegate primitives. Invocation: `See evidence`.
- **Self-hosted worker/runtime** (`native`): goose runs locally or on user-managed servers. Invocation: `See evidence`.

## Freshness rule

Treat unavailable or unknown actor access as unsupported until verified. UI-only capability is not agent-callable by implication.
