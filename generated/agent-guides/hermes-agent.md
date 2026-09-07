---
schema_version: 0.1
harness_id: hermes-agent
generated_at: 2026-09-07T04:43:09.252238Z
artifact_kind: harness_capability_guide
---

# Hermes Agent — Agent Capability Guide

**Vendor:** Nous Research  
**Lifecycle:** active  
**Current version in registry:** 2026.8.31  
**Last verified:** 2026-09-03T11:16:00.695788Z

> UI availability does not imply that an in-harness model or an external orchestrator can invoke the capability. Use the actor-specific sections below.

## Human operator

- **Scheduled tasks** (`configurable`): Hermes includes scheduled and gateway-driven automation paths. Invocation: `cronjob tool (create/list/update/pause/resume/run/remove), /cron add "<cron-expr>" "<prompt>", hermes cron list`.
- **Persistent memory** (`configurable`): Persistent memory and conversation search are first-class parts of Hermes' self-improving agent model. Invocation: `memory tool (add/replace/remove), ~/.hermes/memories/MEMORY.md, config.yaml memory.memory_enabled`.
- **Agent-native file editing** (`supported`): Hermes agents can inspect and edit files through built-in and learned tools. Invocation: `write_file, patch, read_file, search_files`.
- **Agent-native shell execution** (`supported`): Hermes can execute shell commands, including direct `!` command shortcuts in recent releases. Invocation: `!<command>`.
- **Headless/non-interactive execution** (`supported`): Hermes can be invoked through CLI/gateway automation, but the seed does not yet verify a stable event protocol equivalent to Codex app-server. Invocation: `hermes -z "<prompt>", hermes chat -q "<query>" --quiet, hermes serve`.
- **Agent Skills** (`configurable`): Hermes discovers skills progressively and can create or improve them through its learning loop and `/learn` workflow. Invocation: `hermes skills install <name>, /<skill-name>, /learn`.
- **MCP client** (`configurable`): Hermes supports MCP servers and Docker-based MCP commands. Invocation: `hermes mcp add <name> --command <cmd> --args <args>, hermes mcp install <name>, hermes mcp catalog`.
- **Plugins/extensions** (`configurable`): Hermes 0.20 added a desktop plugin SDK and extensibility surfaces. Invocation: `$HERMES_HOME/desktop-plugins/<id>/plugin.js`.
- **Desktop or web surface** (`native`): Hermes 0.20 introduced desktop artifacts, a plugin SDK, and multi-window operation. Invocation: `hermes desktop, hermes dashboard`.
- **Interactive terminal/TUI** (`native`): Hermes provides a CLI/TUI with session resume, interruption, and command shortcuts. Invocation: `hermes`.
- **Artifacts, diffs, and rich result views** (`native`): Desktop artifacts and multiple windows provide richer outputs than plain terminal text. Invocation: `Artifacts pane in hermes desktop, /diff`.
- **Voice interaction** (`native`): Streaming voice supports barge-in and wake words. Invocation: `/voice on|off|tts|status, Ctrl+B (voice.record_key in config.yaml)`.
- **Model/provider portability** (`native`): Hermes supports multiple hosted and local model providers. Invocation: `hermes model, hermes config set model <provider>/<model>`.
- **First-class multi-agent coordination** (`supported`): Mixture-of-Agents is a first-class coordination mode rather than only ad hoc subagent prompting. Invocation: `moa virtual model provider (config.yaml moa presets, select via hermes model)`.
- **Parallel/background agents** (`supported`): Hermes supports background work and Mixture-of-Agents execution. Invocation: `delegate_task(tasks=[...]), delegation.max_concurrent_children config key / DELEGATION_MAX_CONCURRENT_CHILDREN env var`.
- **Subagents/delegation** (`supported`): Hermes can delegate work to specialized agents. Invocation: `delegate_task(goal, context, role="leaf"|"orchestrator", ...)`.
- **Web search/research** (`supported`): Hermes 0.20 added grounded research and citation support. Invocation: `web_search tool, web_extract tool, grounded-citations skill`.
- **Remote/cloud execution** (`native`): Hermes gateways let users interact through messaging channels while work runs on another machine or cloud VM. Invocation: `hermes config set terminal.backend modal|daytona|vercel_sandbox, hermes gateway`.
- **Self-hosted worker/runtime** (`configurable`): Hermes can run on user-owned machines, VPSs, clusters, or serverless infrastructure. Invocation: `hermes config set terminal.backend docker|ssh|singularity`.
- **Granular permissions and approvals** (`native`): Permission modes such as `/yolo` and gateway/tool configuration govern autonomy; use conservative defaults for unattended runs. Invocation: `hermes --yolo, /yolo, approvals.mode in config.yaml (smart|manual|off), approvals.deny glob rules`.
- **Resume, fork, and session lineage** (`native`): Hermes persists and resumes sessions across CLI and gateway surfaces. Invocation: `hermes --resume <session> / -r, hermes --continue [name] / -c, /branch, /fork`.

## In-harness agent

- **Scheduled tasks** (`supported`): Hermes includes scheduled and gateway-driven automation paths. Invocation: `cronjob tool (create/list/update/pause/resume/run/remove), /cron add "<cron-expr>" "<prompt>", hermes cron list`.
- **Persistent memory** (`native`): Persistent memory and conversation search are first-class parts of Hermes' self-improving agent model. Invocation: `memory tool (add/replace/remove), ~/.hermes/memories/MEMORY.md, config.yaml memory.memory_enabled`.
- **Agent-native file editing** (`native`): Hermes agents can inspect and edit files through built-in and learned tools. Invocation: `write_file, patch, read_file, search_files`.
- **Agent-native shell execution** (`native`): Hermes can execute shell commands, including direct `!` command shortcuts in recent releases. Invocation: `!<command>`.
- **Agent Skills** (`native`): Hermes discovers skills progressively and can create or improve them through its learning loop and `/learn` workflow. Invocation: `hermes skills install <name>, /<skill-name>, /learn`.
- **MCP client** (`native`): Hermes supports MCP servers and Docker-based MCP commands. Invocation: `hermes mcp add <name> --command <cmd> --args <args>, hermes mcp install <name>, hermes mcp catalog`.
- **Plugins/extensions** (`native`): Hermes 0.20 added a desktop plugin SDK and extensibility surfaces. Invocation: `$HERMES_HOME/desktop-plugins/<id>/plugin.js`.
- **Model/provider portability** (`supported`): Hermes supports multiple hosted and local model providers. Invocation: `hermes model, hermes config set model <provider>/<model>`.
- **First-class multi-agent coordination** (`native`): Mixture-of-Agents is a first-class coordination mode rather than only ad hoc subagent prompting. Invocation: `moa virtual model provider (config.yaml moa presets, select via hermes model)`.
- **Parallel/background agents** (`native`): Hermes supports background work and Mixture-of-Agents execution. Invocation: `delegate_task(tasks=[...]), delegation.max_concurrent_children config key / DELEGATION_MAX_CONCURRENT_CHILDREN env var`.
- **Subagents/delegation** (`native`): Hermes can delegate work to specialized agents. Invocation: `delegate_task(goal, context, role="leaf"|"orchestrator", ...)`.
- **Web search/research** (`native`): Hermes 0.20 added grounded research and citation support. Invocation: `web_search tool, web_extract tool, grounded-citations skill`.

## External agent/orchestrator

- **Scheduled tasks** (`supported`): Hermes includes scheduled and gateway-driven automation paths. Invocation: `cronjob tool (create/list/update/pause/resume/run/remove), /cron add "<cron-expr>" "<prompt>", hermes cron list`.
- **Persistent memory** (`supported`): Persistent memory and conversation search are first-class parts of Hermes' self-improving agent model. Invocation: `memory tool (add/replace/remove), ~/.hermes/memories/MEMORY.md, config.yaml memory.memory_enabled`.
- **Agent-native file editing** (`supported`): Hermes agents can inspect and edit files through built-in and learned tools. Invocation: `write_file, patch, read_file, search_files`.
- **Agent-native shell execution** (`supported`): Hermes can execute shell commands, including direct `!` command shortcuts in recent releases. Invocation: `!<command>`.
- **Headless/non-interactive execution** (`native`): Hermes can be invoked through CLI/gateway automation, but the seed does not yet verify a stable event protocol equivalent to Codex app-server. Invocation: `hermes -z "<prompt>", hermes chat -q "<query>" --quiet, hermes serve`.
- **Agent Skills** (`supported`): Hermes discovers skills progressively and can create or improve them through its learning loop and `/learn` workflow. Invocation: `hermes skills install <name>, /<skill-name>, /learn`.
- **MCP client** (`supported`): Hermes supports MCP servers and Docker-based MCP commands. Invocation: `hermes mcp add <name> --command <cmd> --args <args>, hermes mcp install <name>, hermes mcp catalog`.
- **Plugins/extensions** (`supported`): Hermes 0.20 added a desktop plugin SDK and extensibility surfaces. Invocation: `$HERMES_HOME/desktop-plugins/<id>/plugin.js`.
- **Voice interaction** (`supported`): Streaming voice supports barge-in and wake words. Invocation: `/voice on|off|tts|status, Ctrl+B (voice.record_key in config.yaml)`.
- **Model/provider portability** (`configurable`): Hermes supports multiple hosted and local model providers. Invocation: `hermes model, hermes config set model <provider>/<model>`.
- **First-class multi-agent coordination** (`supported`): Mixture-of-Agents is a first-class coordination mode rather than only ad hoc subagent prompting. Invocation: `moa virtual model provider (config.yaml moa presets, select via hermes model)`.
- **Parallel/background agents** (`supported`): Hermes supports background work and Mixture-of-Agents execution. Invocation: `delegate_task(tasks=[...]), delegation.max_concurrent_children config key / DELEGATION_MAX_CONCURRENT_CHILDREN env var`.
- **Subagents/delegation** (`supported`): Hermes can delegate work to specialized agents. Invocation: `delegate_task(goal, context, role="leaf"|"orchestrator", ...)`.
- **Web search/research** (`supported`): Hermes 0.20 added grounded research and citation support. Invocation: `web_search tool, web_extract tool, grounded-citations skill`.
- **Remote/cloud execution** (`supported`): Hermes gateways let users interact through messaging channels while work runs on another machine or cloud VM. Invocation: `hermes config set terminal.backend modal|daytona|vercel_sandbox, hermes gateway`.
- **Self-hosted worker/runtime** (`supported`): Hermes can run on user-owned machines, VPSs, clusters, or serverless infrastructure. Invocation: `hermes config set terminal.backend docker|ssh|singularity`.
- **Granular permissions and approvals** (`supported`): Permission modes such as `/yolo` and gateway/tool configuration govern autonomy; use conservative defaults for unattended runs. Invocation: `hermes --yolo, /yolo, approvals.mode in config.yaml (smart|manual|off), approvals.deny glob rules`.
- **Resume, fork, and session lineage** (`supported`): Hermes persists and resumes sessions across CLI and gateway surfaces. Invocation: `hermes --resume <session> / -r, hermes --continue [name] / -c, /branch, /fork`.

## CI or scheduled automation

- **Scheduled tasks** (`native`): Hermes includes scheduled and gateway-driven automation paths. Invocation: `cronjob tool (create/list/update/pause/resume/run/remove), /cron add "<cron-expr>" "<prompt>", hermes cron list`.
- **Agent-native file editing** (`supported`): Hermes agents can inspect and edit files through built-in and learned tools. Invocation: `write_file, patch, read_file, search_files`.
- **Agent-native shell execution** (`supported`): Hermes can execute shell commands, including direct `!` command shortcuts in recent releases. Invocation: `!<command>`.
- **Headless/non-interactive execution** (`native`): Hermes can be invoked through CLI/gateway automation, but the seed does not yet verify a stable event protocol equivalent to Codex app-server. Invocation: `hermes -z "<prompt>", hermes chat -q "<query>" --quiet, hermes serve`.
- **Agent Skills** (`supported`): Hermes discovers skills progressively and can create or improve them through its learning loop and `/learn` workflow. Invocation: `hermes skills install <name>, /<skill-name>, /learn`.
- **MCP client** (`supported`): Hermes supports MCP servers and Docker-based MCP commands. Invocation: `hermes mcp add <name> --command <cmd> --args <args>, hermes mcp install <name>, hermes mcp catalog`.
- **Plugins/extensions** (`supported`): Hermes 0.20 added a desktop plugin SDK and extensibility surfaces. Invocation: `$HERMES_HOME/desktop-plugins/<id>/plugin.js`.
- **Model/provider portability** (`configurable`): Hermes supports multiple hosted and local model providers. Invocation: `hermes model, hermes config set model <provider>/<model>`.
- **First-class multi-agent coordination** (`supported`): Mixture-of-Agents is a first-class coordination mode rather than only ad hoc subagent prompting. Invocation: `moa virtual model provider (config.yaml moa presets, select via hermes model)`.
- **Parallel/background agents** (`supported`): Hermes supports background work and Mixture-of-Agents execution. Invocation: `delegate_task(tasks=[...]), delegation.max_concurrent_children config key / DELEGATION_MAX_CONCURRENT_CHILDREN env var`.
- **Subagents/delegation** (`supported`): Hermes can delegate work to specialized agents. Invocation: `delegate_task(goal, context, role="leaf"|"orchestrator", ...)`.
- **Web search/research** (`supported`): Hermes 0.20 added grounded research and citation support. Invocation: `web_search tool, web_extract tool, grounded-citations skill`.
- **Remote/cloud execution** (`supported`): Hermes gateways let users interact through messaging channels while work runs on another machine or cloud VM. Invocation: `hermes config set terminal.backend modal|daytona|vercel_sandbox, hermes gateway`.
- **Self-hosted worker/runtime** (`supported`): Hermes can run on user-owned machines, VPSs, clusters, or serverless infrastructure. Invocation: `hermes config set terminal.backend docker|ssh|singularity`.
- **Granular permissions and approvals** (`supported`): Permission modes such as `/yolo` and gateway/tool configuration govern autonomy; use conservative defaults for unattended runs. Invocation: `hermes --yolo, /yolo, approvals.mode in config.yaml (smart|manual|off), approvals.deny glob rules`.
- **Resume, fork, and session lineage** (`supported`): Hermes persists and resumes sessions across CLI and gateway surfaces. Invocation: `hermes --resume <session> / -r, hermes --continue [name] / -c, /branch, /fork`.

## Administrator

- **Scheduled tasks** (`configurable`): Hermes includes scheduled and gateway-driven automation paths. Invocation: `cronjob tool (create/list/update/pause/resume/run/remove), /cron add "<cron-expr>" "<prompt>", hermes cron list`.
- **Persistent memory** (`configurable`): Persistent memory and conversation search are first-class parts of Hermes' self-improving agent model. Invocation: `memory tool (add/replace/remove), ~/.hermes/memories/MEMORY.md, config.yaml memory.memory_enabled`.
- **Agent-native file editing** (`configurable`): Hermes agents can inspect and edit files through built-in and learned tools. Invocation: `write_file, patch, read_file, search_files`.
- **Agent-native shell execution** (`configurable`): Hermes can execute shell commands, including direct `!` command shortcuts in recent releases. Invocation: `!<command>`.
- **Headless/non-interactive execution** (`configurable`): Hermes can be invoked through CLI/gateway automation, but the seed does not yet verify a stable event protocol equivalent to Codex app-server. Invocation: `hermes -z "<prompt>", hermes chat -q "<query>" --quiet, hermes serve`.
- **Agent Skills** (`configurable`): Hermes discovers skills progressively and can create or improve them through its learning loop and `/learn` workflow. Invocation: `hermes skills install <name>, /<skill-name>, /learn`.
- **MCP client** (`configurable`): Hermes supports MCP servers and Docker-based MCP commands. Invocation: `hermes mcp add <name> --command <cmd> --args <args>, hermes mcp install <name>, hermes mcp catalog`.
- **Plugins/extensions** (`configurable`): Hermes 0.20 added a desktop plugin SDK and extensibility surfaces. Invocation: `$HERMES_HOME/desktop-plugins/<id>/plugin.js`.
- **Desktop or web surface** (`configurable`): Hermes 0.20 introduced desktop artifacts, a plugin SDK, and multi-window operation. Invocation: `hermes desktop, hermes dashboard`.
- **Interactive terminal/TUI** (`configurable`): Hermes provides a CLI/TUI with session resume, interruption, and command shortcuts. Invocation: `hermes`.
- **Artifacts, diffs, and rich result views** (`configurable`): Desktop artifacts and multiple windows provide richer outputs than plain terminal text. Invocation: `Artifacts pane in hermes desktop, /diff`.
- **Voice interaction** (`configurable`): Streaming voice supports barge-in and wake words. Invocation: `/voice on|off|tts|status, Ctrl+B (voice.record_key in config.yaml)`.
- **Model/provider portability** (`configurable`): Hermes supports multiple hosted and local model providers. Invocation: `hermes model, hermes config set model <provider>/<model>`.
- **First-class multi-agent coordination** (`configurable`): Mixture-of-Agents is a first-class coordination mode rather than only ad hoc subagent prompting. Invocation: `moa virtual model provider (config.yaml moa presets, select via hermes model)`.
- **Parallel/background agents** (`configurable`): Hermes supports background work and Mixture-of-Agents execution. Invocation: `delegate_task(tasks=[...]), delegation.max_concurrent_children config key / DELEGATION_MAX_CONCURRENT_CHILDREN env var`.
- **Subagents/delegation** (`configurable`): Hermes can delegate work to specialized agents. Invocation: `delegate_task(goal, context, role="leaf"|"orchestrator", ...)`.
- **Web search/research** (`configurable`): Hermes 0.20 added grounded research and citation support. Invocation: `web_search tool, web_extract tool, grounded-citations skill`.
- **Remote/cloud execution** (`configurable`): Hermes gateways let users interact through messaging channels while work runs on another machine or cloud VM. Invocation: `hermes config set terminal.backend modal|daytona|vercel_sandbox, hermes gateway`.
- **Self-hosted worker/runtime** (`native`): Hermes can run on user-owned machines, VPSs, clusters, or serverless infrastructure. Invocation: `hermes config set terminal.backend docker|ssh|singularity`.
- **Granular permissions and approvals** (`configurable`): Permission modes such as `/yolo` and gateway/tool configuration govern autonomy; use conservative defaults for unattended runs. Invocation: `hermes --yolo, /yolo, approvals.mode in config.yaml (smart|manual|off), approvals.deny glob rules`.
- **Resume, fork, and session lineage** (`configurable`): Hermes persists and resumes sessions across CLI and gateway surfaces. Invocation: `hermes --resume <session> / -r, hermes --continue [name] / -c, /branch, /fork`.

## Freshness rule

Treat unavailable or unknown actor access as unsupported until verified. UI-only capability is not agent-callable by implication.
