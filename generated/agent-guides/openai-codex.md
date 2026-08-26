---
schema_version: 0.1
harness_id: openai-codex
generated_at: 2026-08-24T13:14:55.511915Z
artifact_kind: harness_capability_guide
---

# OpenAI Codex — Agent Capability Guide

**Vendor:** OpenAI  
**Lifecycle:** active  
**Current version in registry:** 0.147.0  
**Last verified:** 2026-08-08T20:00:00Z

> UI availability does not imply that an in-harness model or an external orchestrator can invoke the capability. Use the actor-specific sections below.

## Human operator

- **CI/GitHub automation** (`supported`): The official Codex GitHub Action runs `codex exec` in CI to apply patches or post reviews. Invocation: `openai/codex-action@v1 (GitHub Action), codex exec (used in CI)`.
- **Scheduled tasks** (`configurable`): Scheduled tasks are supported through Codex/ChatGPT workflow surfaces; exact availability depends on surface and workspace. Invocation: `Scheduled tasks created from a ChatGPT/Codex chat (Scheduled section, RFC 5545 RRULE recurrence) — not available in Codex CLI`.
- **Hierarchical project instructions** (`configurable`): Codex discovers layered AGENTS.md and AGENTS.override.md instructions from global and project scopes. Invocation: `AGENTS.md, AGENTS.override.md, project_doc_fallback_filenames (config.toml)`.
- **Agent-native file editing** (`supported`): Codex can inspect and edit repository files under sandbox and approval policies. Invocation: `--sandbox workspace-write, sandbox_mode = "workspace-write" (config.toml)`.
- **Agent-native shell execution** (`supported`): Codex runs commands within configurable sandbox and approval modes. Invocation: `--sandbox {read-only,workspace-write,danger-full-access}, --ask-for-approval {untrusted,on-request,never}`.
- **Embeddable SDK** (`supported`): Official Python and TypeScript Codex SDKs embed local Codex threads for applications and CI. Invocation: `npm install @openai/codex-sdk, pip install openai-codex`.
- **Headless/non-interactive execution** (`supported`): `codex exec` is the supported non-interactive interface for scripts and CI. Invocation: `codex exec`.
- **Machine-readable output** (`supported`): `codex exec` streams text or JSONL and can resume scripted sessions. Invocation: `codex exec --json`.
- **RPC/app-server protocol** (`supported`): Codex app-server exposes version-specific JSON-RPC schemas and event notifications. Invocation: `codex app-server, generate-json-schema`.
- **Agent Skills** (`configurable`): Agent Skills package instructions and resources; Codex can select them or invoke them through `$` mentions. Invocation: `$skill-name (mention syntax in Codex, vs @skill-name in ChatGPT)`.
- **MCP client** (`configurable`): Local Codex clients connect to local or remote MCP servers and share configuration. Invocation: `codex mcp add <server-name> -- <stdio server-command>, codex mcp list`.
- **Plugins/extensions** (`configurable`): Portable plugins can bundle skills and MCP-backed connectors across ChatGPT and Codex surfaces. Invocation: `codex /plugins (interactive plugin browser: search/install/uninstall marketplace entries)`.
- **Desktop or web surface** (`native`): Codex spans the ChatGPT desktop app and Codex cloud/web surfaces. Invocation: `ChatGPT desktop app, codex cloud (chatgpt.com/codex)`.
- **IDE integration** (`native`): Codex is available through an IDE extension sharing core sessions and agent capabilities. Invocation: `VS Code extension ID `openai.chatgpt` (marketplace: "Codex – OpenAI's coding agent")`.
- **Interactive terminal/TUI** (`native`): Interactive Codex CLI for repository inspection, editing, commands, review, and cloud handoff. Invocation: `codex`.
- **Artifacts, diffs, and rich result views** (`native`): The app, IDE, CLI, and cloud surfaces expose diffs, conversation sections, and task results for review. Invocation: `/review`.
- **Model and reasoning controls** (`native`): Model and reasoning effort can be selected through CLI, IDE, app, and configuration. Invocation: `--model / -m, /model, model_reasoning_effort = "minimal"|"low"|"medium"|"high"|"xhigh" (config.toml)`.
- **Model/provider portability** (`configurable`): Codex is primarily an OpenAI-model harness; custom API targets do not imply arbitrary provider compatibility. Invocation: `[model_providers.<id>] section in config.toml (base_url, env_key, wire_api)`.
- **Agent tracing/event telemetry** (`supported`): App-server notifications and JSONL execution events expose turn and tool lifecycle data. Invocation: `codex app-server (JSON-RPC 2.0 events: item/started, item/completed, item/commandExecution/requestApproval)`.
- **Usage and cost telemetry** (`native`): Structured outputs and product surfaces expose usage, limits, and model information for attribution. Invocation: `/status, /usage`.
- **First-class multi-agent coordination** (`supported`): The main thread can coordinate multiple subagent threads and collect their results. Invocation: `[agents] config.toml section (enabled, default_subagent_model, default_subagent_reasoning_effort)`.
- **Parallel/background agents** (`native`): Codex cloud and local subagent surfaces support parallel/background work. Invocation: `max_concurrent_threads_per_session (config.toml [agents] section), /agent (switch between active threads)`.
- **Subagents/delegation** (`supported`): Codex can delegate work to subagents from app, CLI, and IDE sessions and exposes child threads for inspection. Invocation: `~/.codex/agents/*.toml or .codex/agents/*.toml agent definitions, [agents] section in config.toml`.
- **Browser/computer use** (`supported`): Codex models and connected tools can support browser/computer-use workflows depending on model and surface. Invocation: `WebMCP site tools in the ChatGPT desktop app's built-in browser (GPT-5.6 Sol or Terra)`.
- **Web search/research** (`supported`): Codex supports opt-in web search and MCP-based external tools. Invocation: `--search, web_search = "cached"|"live" (config.toml)`.
- **Remote/cloud execution** (`native`): CLI and IDE can hand work to Codex cloud and later inspect or apply results locally. Invocation: `codex cloud`.
- **Execution sandbox** (`configurable`): Codex provides platform-specific sandbox commands and read-only/workspace-write modes. Invocation: `--sandbox {read-only,workspace-write,danger-full-access}, sandbox_mode (config.toml), [sandbox_workspace_write] network_access`.
- **Granular permissions and approvals** (`native`): Approval policies and permission profiles define when commands can run automatically. Invocation: `--ask-for-approval {untrusted,on-request,never}, approval_policy (config.toml), /permissions`.
- **Programmatic human approval** (`supported`): App-server and SDK clients can mediate approvals through machine interfaces rather than terminal-only prompts. Invocation: `codex app-server JSON-RPC requests: item/commandExecution/requestApproval, item/fileChange/requestApproval, item/permissions/requestApproval`.
- **Resume, fork, and session lineage** (`native`): Saved sessions can be resumed, forked, named, and deleted through stable CLI commands. Invocation: `codex resume [SESSION_ID | --last], codex fork [SESSION_ID | --last], codex archive/unarchive/delete <SESSION>`.
- **Image generation** (`supported`): A bundled 'imagegen' system skill (feature flag image_generation: stable, true) generates an image from a natural-language prompt in headless `codex exec` sessions; not exposed as a documented CLI flag or subcommand. Invocation: `codex exec --sandbox workspace-write "Generate a <image> and save it as <file>.png ... Use your image generation skill if you have one."`.

## In-harness agent

- **Hierarchical project instructions** (`native`): Codex discovers layered AGENTS.md and AGENTS.override.md instructions from global and project scopes. Invocation: `AGENTS.md, AGENTS.override.md, project_doc_fallback_filenames (config.toml)`.
- **Agent-native file editing** (`native`): Codex can inspect and edit repository files under sandbox and approval policies. Invocation: `--sandbox workspace-write, sandbox_mode = "workspace-write" (config.toml)`.
- **Agent-native shell execution** (`native`): Codex runs commands within configurable sandbox and approval modes. Invocation: `--sandbox {read-only,workspace-write,danger-full-access}, --ask-for-approval {untrusted,on-request,never}`.
- **Agent Skills** (`native`): Agent Skills package instructions and resources; Codex can select them or invoke them through `$` mentions. Invocation: `$skill-name (mention syntax in Codex, vs @skill-name in ChatGPT)`.
- **MCP client** (`native`): Local Codex clients connect to local or remote MCP servers and share configuration. Invocation: `codex mcp add <server-name> -- <stdio server-command>, codex mcp list`.
- **Plugins/extensions** (`native`): Portable plugins can bundle skills and MCP-backed connectors across ChatGPT and Codex surfaces. Invocation: `codex /plugins (interactive plugin browser: search/install/uninstall marketplace entries)`.
- **Model and reasoning controls** (`supported`): Model and reasoning effort can be selected through CLI, IDE, app, and configuration. Invocation: `--model / -m, /model, model_reasoning_effort = "minimal"|"low"|"medium"|"high"|"xhigh" (config.toml)`.
- **First-class multi-agent coordination** (`native`): The main thread can coordinate multiple subagent threads and collect their results. Invocation: `[agents] config.toml section (enabled, default_subagent_model, default_subagent_reasoning_effort)`.
- **Parallel/background agents** (`native`): Codex cloud and local subagent surfaces support parallel/background work. Invocation: `max_concurrent_threads_per_session (config.toml [agents] section), /agent (switch between active threads)`.
- **Subagents/delegation** (`native`): Codex can delegate work to subagents from app, CLI, and IDE sessions and exposes child threads for inspection. Invocation: `~/.codex/agents/*.toml or .codex/agents/*.toml agent definitions, [agents] section in config.toml`.
- **Browser/computer use** (`native`): Codex models and connected tools can support browser/computer-use workflows depending on model and surface. Invocation: `WebMCP site tools in the ChatGPT desktop app's built-in browser (GPT-5.6 Sol or Terra)`.
- **Web search/research** (`native`): Codex supports opt-in web search and MCP-based external tools. Invocation: `--search, web_search = "cached"|"live" (config.toml)`.
- **Image generation** (`native`): A bundled 'imagegen' system skill (feature flag image_generation: stable, true) generates an image from a natural-language prompt in headless `codex exec` sessions; not exposed as a documented CLI flag or subcommand. Invocation: `codex exec --sandbox workspace-write "Generate a <image> and save it as <file>.png ... Use your image generation skill if you have one."`.

## External agent/orchestrator

- **CI/GitHub automation** (`native`): The official Codex GitHub Action runs `codex exec` in CI to apply patches or post reviews. Invocation: `openai/codex-action@v1 (GitHub Action), codex exec (used in CI)`.
- **Scheduled tasks** (`supported`): Scheduled tasks are supported through Codex/ChatGPT workflow surfaces; exact availability depends on surface and workspace. Invocation: `Scheduled tasks created from a ChatGPT/Codex chat (Scheduled section, RFC 5545 RRULE recurrence) — not available in Codex CLI`.
- **Hierarchical project instructions** (`supported`): Codex discovers layered AGENTS.md and AGENTS.override.md instructions from global and project scopes. Invocation: `AGENTS.md, AGENTS.override.md, project_doc_fallback_filenames (config.toml)`.
- **Agent-native file editing** (`supported`): Codex can inspect and edit repository files under sandbox and approval policies. Invocation: `--sandbox workspace-write, sandbox_mode = "workspace-write" (config.toml)`.
- **Agent-native shell execution** (`supported`): Codex runs commands within configurable sandbox and approval modes. Invocation: `--sandbox {read-only,workspace-write,danger-full-access}, --ask-for-approval {untrusted,on-request,never}`.
- **Embeddable SDK** (`native`): Official Python and TypeScript Codex SDKs embed local Codex threads for applications and CI. Invocation: `npm install @openai/codex-sdk, pip install openai-codex`.
- **Headless/non-interactive execution** (`native`): `codex exec` is the supported non-interactive interface for scripts and CI. Invocation: `codex exec`.
- **Machine-readable output** (`native`): `codex exec` streams text or JSONL and can resume scripted sessions. Invocation: `codex exec --json`.
- **RPC/app-server protocol** (`native`): Codex app-server exposes version-specific JSON-RPC schemas and event notifications. Invocation: `codex app-server, generate-json-schema`.
- **Agent Skills** (`supported`): Agent Skills package instructions and resources; Codex can select them or invoke them through `$` mentions. Invocation: `$skill-name (mention syntax in Codex, vs @skill-name in ChatGPT)`.
- **MCP client** (`supported`): Local Codex clients connect to local or remote MCP servers and share configuration. Invocation: `codex mcp add <server-name> -- <stdio server-command>, codex mcp list`.
- **Plugins/extensions** (`supported`): Portable plugins can bundle skills and MCP-backed connectors across ChatGPT and Codex surfaces. Invocation: `codex /plugins (interactive plugin browser: search/install/uninstall marketplace entries)`.
- **Model and reasoning controls** (`configurable`): Model and reasoning effort can be selected through CLI, IDE, app, and configuration. Invocation: `--model / -m, /model, model_reasoning_effort = "minimal"|"low"|"medium"|"high"|"xhigh" (config.toml)`.
- **Model/provider portability** (`configurable`): Codex is primarily an OpenAI-model harness; custom API targets do not imply arbitrary provider compatibility. Invocation: `[model_providers.<id>] section in config.toml (base_url, env_key, wire_api)`.
- **Agent tracing/event telemetry** (`native`): App-server notifications and JSONL execution events expose turn and tool lifecycle data. Invocation: `codex app-server (JSON-RPC 2.0 events: item/started, item/completed, item/commandExecution/requestApproval)`.
- **Usage and cost telemetry** (`supported`): Structured outputs and product surfaces expose usage, limits, and model information for attribution. Invocation: `/status, /usage`.
- **First-class multi-agent coordination** (`supported`): The main thread can coordinate multiple subagent threads and collect their results. Invocation: `[agents] config.toml section (enabled, default_subagent_model, default_subagent_reasoning_effort)`.
- **Parallel/background agents** (`supported`): Codex cloud and local subagent surfaces support parallel/background work. Invocation: `max_concurrent_threads_per_session (config.toml [agents] section), /agent (switch between active threads)`.
- **Subagents/delegation** (`supported`): Codex can delegate work to subagents from app, CLI, and IDE sessions and exposes child threads for inspection. Invocation: `~/.codex/agents/*.toml or .codex/agents/*.toml agent definitions, [agents] section in config.toml`.
- **Browser/computer use** (`supported`): Codex models and connected tools can support browser/computer-use workflows depending on model and surface. Invocation: `WebMCP site tools in the ChatGPT desktop app's built-in browser (GPT-5.6 Sol or Terra)`.
- **Web search/research** (`supported`): Codex supports opt-in web search and MCP-based external tools. Invocation: `--search, web_search = "cached"|"live" (config.toml)`.
- **Remote/cloud execution** (`supported`): CLI and IDE can hand work to Codex cloud and later inspect or apply results locally. Invocation: `codex cloud`.
- **Execution sandbox** (`supported`): Codex provides platform-specific sandbox commands and read-only/workspace-write modes. Invocation: `--sandbox {read-only,workspace-write,danger-full-access}, sandbox_mode (config.toml), [sandbox_workspace_write] network_access`.
- **Granular permissions and approvals** (`supported`): Approval policies and permission profiles define when commands can run automatically. Invocation: `--ask-for-approval {untrusted,on-request,never}, approval_policy (config.toml), /permissions`.
- **Programmatic human approval** (`native`): App-server and SDK clients can mediate approvals through machine interfaces rather than terminal-only prompts. Invocation: `codex app-server JSON-RPC requests: item/commandExecution/requestApproval, item/fileChange/requestApproval, item/permissions/requestApproval`.
- **Resume, fork, and session lineage** (`supported`): Saved sessions can be resumed, forked, named, and deleted through stable CLI commands. Invocation: `codex resume [SESSION_ID | --last], codex fork [SESSION_ID | --last], codex archive/unarchive/delete <SESSION>`.
- **Image generation** (`supported`): A bundled 'imagegen' system skill (feature flag image_generation: stable, true) generates an image from a natural-language prompt in headless `codex exec` sessions; not exposed as a documented CLI flag or subcommand. Invocation: `codex exec --sandbox workspace-write "Generate a <image> and save it as <file>.png ... Use your image generation skill if you have one."`.

## CI or scheduled automation

- **CI/GitHub automation** (`native`): The official Codex GitHub Action runs `codex exec` in CI to apply patches or post reviews. Invocation: `openai/codex-action@v1 (GitHub Action), codex exec (used in CI)`.
- **Scheduled tasks** (`native`): Scheduled tasks are supported through Codex/ChatGPT workflow surfaces; exact availability depends on surface and workspace. Invocation: `Scheduled tasks created from a ChatGPT/Codex chat (Scheduled section, RFC 5545 RRULE recurrence) — not available in Codex CLI`.
- **Hierarchical project instructions** (`supported`): Codex discovers layered AGENTS.md and AGENTS.override.md instructions from global and project scopes. Invocation: `AGENTS.md, AGENTS.override.md, project_doc_fallback_filenames (config.toml)`.
- **Agent-native file editing** (`supported`): Codex can inspect and edit repository files under sandbox and approval policies. Invocation: `--sandbox workspace-write, sandbox_mode = "workspace-write" (config.toml)`.
- **Agent-native shell execution** (`supported`): Codex runs commands within configurable sandbox and approval modes. Invocation: `--sandbox {read-only,workspace-write,danger-full-access}, --ask-for-approval {untrusted,on-request,never}`.
- **Embeddable SDK** (`native`): Official Python and TypeScript Codex SDKs embed local Codex threads for applications and CI. Invocation: `npm install @openai/codex-sdk, pip install openai-codex`.
- **Headless/non-interactive execution** (`native`): `codex exec` is the supported non-interactive interface for scripts and CI. Invocation: `codex exec`.
- **Machine-readable output** (`native`): `codex exec` streams text or JSONL and can resume scripted sessions. Invocation: `codex exec --json`.
- **RPC/app-server protocol** (`native`): Codex app-server exposes version-specific JSON-RPC schemas and event notifications. Invocation: `codex app-server, generate-json-schema`.
- **Agent Skills** (`supported`): Agent Skills package instructions and resources; Codex can select them or invoke them through `$` mentions. Invocation: `$skill-name (mention syntax in Codex, vs @skill-name in ChatGPT)`.
- **MCP client** (`supported`): Local Codex clients connect to local or remote MCP servers and share configuration. Invocation: `codex mcp add <server-name> -- <stdio server-command>, codex mcp list`.
- **Plugins/extensions** (`supported`): Portable plugins can bundle skills and MCP-backed connectors across ChatGPT and Codex surfaces. Invocation: `codex /plugins (interactive plugin browser: search/install/uninstall marketplace entries)`.
- **Model and reasoning controls** (`configurable`): Model and reasoning effort can be selected through CLI, IDE, app, and configuration. Invocation: `--model / -m, /model, model_reasoning_effort = "minimal"|"low"|"medium"|"high"|"xhigh" (config.toml)`.
- **Model/provider portability** (`configurable`): Codex is primarily an OpenAI-model harness; custom API targets do not imply arbitrary provider compatibility. Invocation: `[model_providers.<id>] section in config.toml (base_url, env_key, wire_api)`.
- **Agent tracing/event telemetry** (`native`): App-server notifications and JSONL execution events expose turn and tool lifecycle data. Invocation: `codex app-server (JSON-RPC 2.0 events: item/started, item/completed, item/commandExecution/requestApproval)`.
- **Usage and cost telemetry** (`supported`): Structured outputs and product surfaces expose usage, limits, and model information for attribution. Invocation: `/status, /usage`.
- **First-class multi-agent coordination** (`supported`): The main thread can coordinate multiple subagent threads and collect their results. Invocation: `[agents] config.toml section (enabled, default_subagent_model, default_subagent_reasoning_effort)`.
- **Parallel/background agents** (`supported`): Codex cloud and local subagent surfaces support parallel/background work. Invocation: `max_concurrent_threads_per_session (config.toml [agents] section), /agent (switch between active threads)`.
- **Subagents/delegation** (`supported`): Codex can delegate work to subagents from app, CLI, and IDE sessions and exposes child threads for inspection. Invocation: `~/.codex/agents/*.toml or .codex/agents/*.toml agent definitions, [agents] section in config.toml`.
- **Browser/computer use** (`supported`): Codex models and connected tools can support browser/computer-use workflows depending on model and surface. Invocation: `WebMCP site tools in the ChatGPT desktop app's built-in browser (GPT-5.6 Sol or Terra)`.
- **Web search/research** (`supported`): Codex supports opt-in web search and MCP-based external tools. Invocation: `--search, web_search = "cached"|"live" (config.toml)`.
- **Remote/cloud execution** (`supported`): CLI and IDE can hand work to Codex cloud and later inspect or apply results locally. Invocation: `codex cloud`.
- **Execution sandbox** (`supported`): Codex provides platform-specific sandbox commands and read-only/workspace-write modes. Invocation: `--sandbox {read-only,workspace-write,danger-full-access}, sandbox_mode (config.toml), [sandbox_workspace_write] network_access`.
- **Granular permissions and approvals** (`supported`): Approval policies and permission profiles define when commands can run automatically. Invocation: `--ask-for-approval {untrusted,on-request,never}, approval_policy (config.toml), /permissions`.
- **Programmatic human approval** (`supported`): App-server and SDK clients can mediate approvals through machine interfaces rather than terminal-only prompts. Invocation: `codex app-server JSON-RPC requests: item/commandExecution/requestApproval, item/fileChange/requestApproval, item/permissions/requestApproval`.
- **Resume, fork, and session lineage** (`supported`): Saved sessions can be resumed, forked, named, and deleted through stable CLI commands. Invocation: `codex resume [SESSION_ID | --last], codex fork [SESSION_ID | --last], codex archive/unarchive/delete <SESSION>`.
- **Image generation** (`supported`): A bundled 'imagegen' system skill (feature flag image_generation: stable, true) generates an image from a natural-language prompt in headless `codex exec` sessions; not exposed as a documented CLI flag or subcommand. Invocation: `codex exec --sandbox workspace-write "Generate a <image> and save it as <file>.png ... Use your image generation skill if you have one."`.

## Administrator

- **CI/GitHub automation** (`configurable`): The official Codex GitHub Action runs `codex exec` in CI to apply patches or post reviews. Invocation: `openai/codex-action@v1 (GitHub Action), codex exec (used in CI)`.
- **Scheduled tasks** (`configurable`): Scheduled tasks are supported through Codex/ChatGPT workflow surfaces; exact availability depends on surface and workspace. Invocation: `Scheduled tasks created from a ChatGPT/Codex chat (Scheduled section, RFC 5545 RRULE recurrence) — not available in Codex CLI`.
- **Hierarchical project instructions** (`configurable`): Codex discovers layered AGENTS.md and AGENTS.override.md instructions from global and project scopes. Invocation: `AGENTS.md, AGENTS.override.md, project_doc_fallback_filenames (config.toml)`.
- **Agent-native file editing** (`configurable`): Codex can inspect and edit repository files under sandbox and approval policies. Invocation: `--sandbox workspace-write, sandbox_mode = "workspace-write" (config.toml)`.
- **Agent-native shell execution** (`configurable`): Codex runs commands within configurable sandbox and approval modes. Invocation: `--sandbox {read-only,workspace-write,danger-full-access}, --ask-for-approval {untrusted,on-request,never}`.
- **Embeddable SDK** (`configurable`): Official Python and TypeScript Codex SDKs embed local Codex threads for applications and CI. Invocation: `npm install @openai/codex-sdk, pip install openai-codex`.
- **Headless/non-interactive execution** (`configurable`): `codex exec` is the supported non-interactive interface for scripts and CI. Invocation: `codex exec`.
- **Machine-readable output** (`configurable`): `codex exec` streams text or JSONL and can resume scripted sessions. Invocation: `codex exec --json`.
- **RPC/app-server protocol** (`configurable`): Codex app-server exposes version-specific JSON-RPC schemas and event notifications. Invocation: `codex app-server, generate-json-schema`.
- **Agent Skills** (`configurable`): Agent Skills package instructions and resources; Codex can select them or invoke them through `$` mentions. Invocation: `$skill-name (mention syntax in Codex, vs @skill-name in ChatGPT)`.
- **MCP client** (`configurable`): Local Codex clients connect to local or remote MCP servers and share configuration. Invocation: `codex mcp add <server-name> -- <stdio server-command>, codex mcp list`.
- **Plugins/extensions** (`configurable`): Portable plugins can bundle skills and MCP-backed connectors across ChatGPT and Codex surfaces. Invocation: `codex /plugins (interactive plugin browser: search/install/uninstall marketplace entries)`.
- **Desktop or web surface** (`configurable`): Codex spans the ChatGPT desktop app and Codex cloud/web surfaces. Invocation: `ChatGPT desktop app, codex cloud (chatgpt.com/codex)`.
- **IDE integration** (`configurable`): Codex is available through an IDE extension sharing core sessions and agent capabilities. Invocation: `VS Code extension ID `openai.chatgpt` (marketplace: "Codex – OpenAI's coding agent")`.
- **Interactive terminal/TUI** (`configurable`): Interactive Codex CLI for repository inspection, editing, commands, review, and cloud handoff. Invocation: `codex`.
- **Artifacts, diffs, and rich result views** (`configurable`): The app, IDE, CLI, and cloud surfaces expose diffs, conversation sections, and task results for review. Invocation: `/review`.
- **Model and reasoning controls** (`native`): Model and reasoning effort can be selected through CLI, IDE, app, and configuration. Invocation: `--model / -m, /model, model_reasoning_effort = "minimal"|"low"|"medium"|"high"|"xhigh" (config.toml)`.
- **Model/provider portability** (`configurable`): Codex is primarily an OpenAI-model harness; custom API targets do not imply arbitrary provider compatibility. Invocation: `[model_providers.<id>] section in config.toml (base_url, env_key, wire_api)`.
- **Agent tracing/event telemetry** (`configurable`): App-server notifications and JSONL execution events expose turn and tool lifecycle data. Invocation: `codex app-server (JSON-RPC 2.0 events: item/started, item/completed, item/commandExecution/requestApproval)`.
- **Usage and cost telemetry** (`native`): Structured outputs and product surfaces expose usage, limits, and model information for attribution. Invocation: `/status, /usage`.
- **First-class multi-agent coordination** (`configurable`): The main thread can coordinate multiple subagent threads and collect their results. Invocation: `[agents] config.toml section (enabled, default_subagent_model, default_subagent_reasoning_effort)`.
- **Parallel/background agents** (`configurable`): Codex cloud and local subagent surfaces support parallel/background work. Invocation: `max_concurrent_threads_per_session (config.toml [agents] section), /agent (switch between active threads)`.
- **Subagents/delegation** (`configurable`): Codex can delegate work to subagents from app, CLI, and IDE sessions and exposes child threads for inspection. Invocation: `~/.codex/agents/*.toml or .codex/agents/*.toml agent definitions, [agents] section in config.toml`.
- **Browser/computer use** (`configurable`): Codex models and connected tools can support browser/computer-use workflows depending on model and surface. Invocation: `WebMCP site tools in the ChatGPT desktop app's built-in browser (GPT-5.6 Sol or Terra)`.
- **Web search/research** (`configurable`): Codex supports opt-in web search and MCP-based external tools. Invocation: `--search, web_search = "cached"|"live" (config.toml)`.
- **Remote/cloud execution** (`configurable`): CLI and IDE can hand work to Codex cloud and later inspect or apply results locally. Invocation: `codex cloud`.
- **Enterprise managed policy** (`native`): Managed workspace roles, permissions, retention, residency, and authentication policies apply to Codex surfaces. Invocation: `requirements.toml admin-enforced managed policy (deployed from the Codex Policies page)`.
- **Execution sandbox** (`native`): Codex provides platform-specific sandbox commands and read-only/workspace-write modes. Invocation: `--sandbox {read-only,workspace-write,danger-full-access}, sandbox_mode (config.toml), [sandbox_workspace_write] network_access`.
- **Granular permissions and approvals** (`native`): Approval policies and permission profiles define when commands can run automatically. Invocation: `--ask-for-approval {untrusted,on-request,never}, approval_policy (config.toml), /permissions`.
- **Programmatic human approval** (`configurable`): App-server and SDK clients can mediate approvals through machine interfaces rather than terminal-only prompts. Invocation: `codex app-server JSON-RPC requests: item/commandExecution/requestApproval, item/fileChange/requestApproval, item/permissions/requestApproval`.
- **Resume, fork, and session lineage** (`configurable`): Saved sessions can be resumed, forked, named, and deleted through stable CLI commands. Invocation: `codex resume [SESSION_ID | --last], codex fork [SESSION_ID | --last], codex archive/unarchive/delete <SESSION>`.
- **Image generation** (`configurable`): A bundled 'imagegen' system skill (feature flag image_generation: stable, true) generates an image from a natural-language prompt in headless `codex exec` sessions; not exposed as a documented CLI flag or subcommand. Invocation: `codex exec --sandbox workspace-write "Generate a <image> and save it as <file>.png ... Use your image generation skill if you have one."`.

## Freshness rule

Treat unavailable or unknown actor access as unsupported until verified. UI-only capability is not agent-callable by implication.
