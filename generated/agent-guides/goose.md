---
schema_version: 0.1
harness_id: goose
generated_at: 2026-09-07T04:43:09.252238Z
artifact_kind: harness_capability_guide
---

# goose — Agent Capability Guide

**Vendor:** Block  
**Lifecycle:** active  
**Current version in registry:** 2.0.0-rc-04-27-0  
**Last verified:** 2026-08-15T20:10:18.746297Z

> UI availability does not imply that an in-harness model or an external orchestrator can invoke the capability. Use the actor-specific sections below.

## Human operator

- **Agent-native file editing** (`supported`): goose can install, execute, edit, and test through agent tools. Invocation: `write, edit, tree (developer extension tools)`.
- **Agent-native shell execution** (`supported`): goose can execute local commands. Invocation: `shell (developer extension tool)`.
- **Headless/non-interactive execution** (`supported`): goose server and CLI paths support external automation. Invocation: `goose run -i <FILE>, goose run -t "<TEXT>", goose run --no-session, goose run --quiet`.
- **RPC/app-server protocol** (`supported`): The goosed server exposes agent functionality to clients. Invocation: `goose acp, goose serve --host <HOST> --port <PORT>`.
- **Agent Skills** (`configurable`): Recipes and reusable instructions package workflows for agents. Invocation: `goose skills list, /skills (interactive slash command)`.
- **MCP client** (`configurable`): goose is MCP-first and can use MCP extensions and apps. Invocation: `goose configure (Configure Providers/Extensions), goose session --with-extension <command>, goose session --with-streamable-http-extension <url>`.
- **Desktop or web surface** (`native`): goose provides an Electron desktop interface. Invocation: `Goose Desktop (Electron app, downloadable per-OS installer)`.
- **Interactive terminal/TUI** (`native`): goose provides a CLI agent interface. Invocation: `goose session, goose`.
- **Model/provider portability** (`native`): goose is designed to work with multiple LLM providers and local models. Invocation: `goose configure (Configure Providers), GOOSE_MODEL env var / config.yaml, goose run --model <MODEL> --provider <PROVIDER>`.
- **Subagents/delegation** (`supported`): goose supports delegated/subagent workflows through recipes and summon/delegate primitives. Invocation: `natural-language delegation request (e.g. "run these in parallel using subagents"), GOOSE_SUBAGENT_MAX_TURNS env var`.
- **Self-hosted worker/runtime** (`configurable`): goose runs locally or on user-managed servers. Invocation: `goose session --container <id>, goose serve (self-hosted ACP server)`.

## In-harness agent

- **Agent-native file editing** (`native`): goose can install, execute, edit, and test through agent tools. Invocation: `write, edit, tree (developer extension tools)`.
- **Agent-native shell execution** (`native`): goose can execute local commands. Invocation: `shell (developer extension tool)`.
- **Agent Skills** (`native`): Recipes and reusable instructions package workflows for agents. Invocation: `goose skills list, /skills (interactive slash command)`.
- **MCP client** (`native`): goose is MCP-first and can use MCP extensions and apps. Invocation: `goose configure (Configure Providers/Extensions), goose session --with-extension <command>, goose session --with-streamable-http-extension <url>`.
- **Model/provider portability** (`supported`): goose is designed to work with multiple LLM providers and local models. Invocation: `goose configure (Configure Providers), GOOSE_MODEL env var / config.yaml, goose run --model <MODEL> --provider <PROVIDER>`.
- **Subagents/delegation** (`native`): goose supports delegated/subagent workflows through recipes and summon/delegate primitives. Invocation: `natural-language delegation request (e.g. "run these in parallel using subagents"), GOOSE_SUBAGENT_MAX_TURNS env var`.

## External agent/orchestrator

- **Agent-native file editing** (`supported`): goose can install, execute, edit, and test through agent tools. Invocation: `write, edit, tree (developer extension tools)`.
- **Agent-native shell execution** (`supported`): goose can execute local commands. Invocation: `shell (developer extension tool)`.
- **Headless/non-interactive execution** (`native`): goose server and CLI paths support external automation. Invocation: `goose run -i <FILE>, goose run -t "<TEXT>", goose run --no-session, goose run --quiet`.
- **RPC/app-server protocol** (`native`): The goosed server exposes agent functionality to clients. Invocation: `goose acp, goose serve --host <HOST> --port <PORT>`.
- **Agent Skills** (`supported`): Recipes and reusable instructions package workflows for agents. Invocation: `goose skills list, /skills (interactive slash command)`.
- **MCP client** (`supported`): goose is MCP-first and can use MCP extensions and apps. Invocation: `goose configure (Configure Providers/Extensions), goose session --with-extension <command>, goose session --with-streamable-http-extension <url>`.
- **Model/provider portability** (`configurable`): goose is designed to work with multiple LLM providers and local models. Invocation: `goose configure (Configure Providers), GOOSE_MODEL env var / config.yaml, goose run --model <MODEL> --provider <PROVIDER>`.
- **Subagents/delegation** (`supported`): goose supports delegated/subagent workflows through recipes and summon/delegate primitives. Invocation: `natural-language delegation request (e.g. "run these in parallel using subagents"), GOOSE_SUBAGENT_MAX_TURNS env var`.
- **Self-hosted worker/runtime** (`supported`): goose runs locally or on user-managed servers. Invocation: `goose session --container <id>, goose serve (self-hosted ACP server)`.

## CI or scheduled automation

- **Agent-native file editing** (`supported`): goose can install, execute, edit, and test through agent tools. Invocation: `write, edit, tree (developer extension tools)`.
- **Agent-native shell execution** (`supported`): goose can execute local commands. Invocation: `shell (developer extension tool)`.
- **Headless/non-interactive execution** (`native`): goose server and CLI paths support external automation. Invocation: `goose run -i <FILE>, goose run -t "<TEXT>", goose run --no-session, goose run --quiet`.
- **RPC/app-server protocol** (`native`): The goosed server exposes agent functionality to clients. Invocation: `goose acp, goose serve --host <HOST> --port <PORT>`.
- **Agent Skills** (`supported`): Recipes and reusable instructions package workflows for agents. Invocation: `goose skills list, /skills (interactive slash command)`.
- **MCP client** (`supported`): goose is MCP-first and can use MCP extensions and apps. Invocation: `goose configure (Configure Providers/Extensions), goose session --with-extension <command>, goose session --with-streamable-http-extension <url>`.
- **Model/provider portability** (`configurable`): goose is designed to work with multiple LLM providers and local models. Invocation: `goose configure (Configure Providers), GOOSE_MODEL env var / config.yaml, goose run --model <MODEL> --provider <PROVIDER>`.
- **Subagents/delegation** (`supported`): goose supports delegated/subagent workflows through recipes and summon/delegate primitives. Invocation: `natural-language delegation request (e.g. "run these in parallel using subagents"), GOOSE_SUBAGENT_MAX_TURNS env var`.
- **Self-hosted worker/runtime** (`supported`): goose runs locally or on user-managed servers. Invocation: `goose session --container <id>, goose serve (self-hosted ACP server)`.

## Administrator

- **Agent-native file editing** (`configurable`): goose can install, execute, edit, and test through agent tools. Invocation: `write, edit, tree (developer extension tools)`.
- **Agent-native shell execution** (`configurable`): goose can execute local commands. Invocation: `shell (developer extension tool)`.
- **Headless/non-interactive execution** (`configurable`): goose server and CLI paths support external automation. Invocation: `goose run -i <FILE>, goose run -t "<TEXT>", goose run --no-session, goose run --quiet`.
- **RPC/app-server protocol** (`configurable`): The goosed server exposes agent functionality to clients. Invocation: `goose acp, goose serve --host <HOST> --port <PORT>`.
- **Agent Skills** (`configurable`): Recipes and reusable instructions package workflows for agents. Invocation: `goose skills list, /skills (interactive slash command)`.
- **MCP client** (`configurable`): goose is MCP-first and can use MCP extensions and apps. Invocation: `goose configure (Configure Providers/Extensions), goose session --with-extension <command>, goose session --with-streamable-http-extension <url>`.
- **Desktop or web surface** (`configurable`): goose provides an Electron desktop interface. Invocation: `Goose Desktop (Electron app, downloadable per-OS installer)`.
- **Interactive terminal/TUI** (`configurable`): goose provides a CLI agent interface. Invocation: `goose session, goose`.
- **Model/provider portability** (`configurable`): goose is designed to work with multiple LLM providers and local models. Invocation: `goose configure (Configure Providers), GOOSE_MODEL env var / config.yaml, goose run --model <MODEL> --provider <PROVIDER>`.
- **Subagents/delegation** (`configurable`): goose supports delegated/subagent workflows through recipes and summon/delegate primitives. Invocation: `natural-language delegation request (e.g. "run these in parallel using subagents"), GOOSE_SUBAGENT_MAX_TURNS env var`.
- **Self-hosted worker/runtime** (`native`): goose runs locally or on user-managed servers. Invocation: `goose session --container <id>, goose serve (self-hosted ACP server)`.

## Freshness rule

Treat unavailable or unknown actor access as unsupported until verified. UI-only capability is not agent-callable by implication.
