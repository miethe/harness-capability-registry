---
schema_version: 0.1
harness_id: claude-code
generated_at: 2026-08-08T20:00:00Z
artifact_kind: harness_capability_guide
---

# Claude Code — Agent Capability Guide

**Vendor:** Anthropic  
**Lifecycle:** active  
**Current version in registry:** 2.1.226  
**Last verified:** 2026-08-08T20:00:00Z

> UI availability does not imply that an in-harness model or an external orchestrator can invoke the capability. Use the actor-specific sections below.

## Human operator

- **CI/GitHub automation** (`supported`): Headless mode and the Agent SDK support CI, batch, and scripted workflows. Invocation: `See evidence`.
- **Scheduled tasks** (`configurable`): Workflow and scheduled-task primitives are present, but coverage is less mature than headless execution. Invocation: `See evidence`.
- **Dynamic context injection** (`configurable`): Skills, hooks, and MCP tools can inject context only when relevant. Invocation: `See evidence`.
- **Hierarchical project instructions** (`configurable`): CLAUDE.md and scoped configuration provide durable project instructions. Invocation: `See evidence`.
- **Persistent memory** (`configurable`): Auto memory and project memory preserve selected knowledge across sessions. Invocation: `See evidence`.
- **Output schema enforcement** (`supported`): Headless and SDK flows can request structured output contracts for downstream automation. Invocation: `See evidence`.
- **Agent-native file editing** (`supported`): Claude can read and edit repository files through native tools. Invocation: `See evidence`.
- **Agent-native shell execution** (`supported`): Claude can run shell commands with configurable permission modes and sandbox controls. Invocation: `Bash tool`.
- **Embeddable SDK** (`supported`): The Claude Agent SDK exposes the same agent loop, tools, and context management as Claude Code in Python and TypeScript. Invocation: `See evidence`.
- **Headless/non-interactive execution** (`supported`): `claude -p` provides supported non-interactive execution for scripts and CI; `--bare` disables ambient project customization for reproducibility. Invocation: `claude -p, claude -p --bare`.
- **Machine-readable output** (`supported`): Headless execution supports machine-readable JSON and streaming event output. Invocation: `--output-format json, --output-format stream-json`.
- **Agent Skills** (`configurable`): SKILL.md bundles can be selected by Claude or invoked explicitly; Claude Code extends the Agent Skills standard with invocation controls and subagent execution. Invocation: `/skill-name, .claude/skills/*/SKILL.md`.
- **Lifecycle hooks** (`configurable`): Hooks execute code at lifecycle events to inject context, enforce policy, format files, or notify humans. Invocation: `PreToolUse, PostToolUse, Stop, SessionStart`.
- **MCP client** (`configurable`): Claude Code connects to local and remote MCP servers and supports OAuth-backed tools. Invocation: `.mcp.json, plugin MCP servers`.
- **Plugins/extensions** (`configurable`): Plugins distribute skills, agents, hooks, and MCP servers through project/user configuration and marketplaces. Invocation: `plugin install, settings.json`.
- **Desktop or web surface** (`native`): Claude Code sessions are available through desktop and browser surfaces and can attach through Remote Control. Invocation: `See evidence`.
- **IDE integration** (`native`): First-party IDE integration, including VS Code surfaces tracked in the changelog. Invocation: `See evidence`.
- **Interactive terminal/TUI** (`native`): Interactive terminal agent with slash commands, session controls, and tool approvals. Invocation: `claude`.
- **Artifacts, diffs, and rich result views** (`native`): IDE, desktop, web, attachments, diffs, and review flows provide rich result inspection beyond terminal text. Invocation: `See evidence`.
- **Model and reasoning controls** (`native`): Model selection, fast mode, context-window enforcement, and subagent model selection are configurable. Invocation: `See evidence`.
- **Model/provider portability** (`configurable`): Claude Code supports Anthropic-hosted Claude plus Bedrock, Vertex AI, and enterprise gateways, but remains Claude-model-centric. Invocation: `See evidence`.
- **Agent tracing/event telemetry** (`supported`): Headless/SDK event streams and hook events provide structured execution telemetry. Invocation: `See evidence`.
- **Usage and cost telemetry** (`native`): Usage, token, budget, spend-limit, and model-usage signals are exposed in CLI/SDK paths. Invocation: `See evidence`.
- **Cross-session agent messaging** (`supported`): Running sessions can discover one another with ListAgents and exchange messages with SendMessage across machines. Invocation: `ListAgents, SendMessage`.
- **First-class multi-agent coordination** (`supported`): Agent teams, nested subagents, and cross-session messaging provide explicit coordination primitives. Invocation: `See evidence`.
- **Parallel/background agents** (`supported`): Subagents and forked skills can run in the background with concurrency and spawn-depth controls. Invocation: `See evidence`.
- **Subagents/delegation** (`supported`): Claude can delegate work to defined or dynamic subagents with separate prompts and tool restrictions. Invocation: `See evidence`.
- **Browser/computer use** (`supported`): Claude-in-Chrome and browser/MCP integrations provide browser interaction. Invocation: `See evidence`.
- **Web search/research** (`native`): Built-in deep research is manually invoked; web access can also be supplied through MCP and browser tools. Invocation: `/deep-research`.
- **Remote/cloud execution** (`native`): Remote Control and cloud sessions let work continue across terminal, web, desktop, and mobile surfaces. Invocation: `See evidence`.
- **Self-hosted worker/runtime** (`configurable`): `claude self-hosted-runner` registers user-owned machines or containers as execution environments for web/mobile/desktop sessions. Invocation: `claude self-hosted-runner`.
- **Execution sandbox** (`configurable`): Filesystem and network sandbox controls constrain tool execution, including credential masking and TLS termination options. Invocation: `See evidence`.
- **Granular permissions and approvals** (`native`): Permission modes, allow/deny rules, workspace trust, and approval hooks govern agent actions. Invocation: `See evidence`.
- **Programmatic human approval** (`supported`): SDK permission callbacks and hooks let an embedding application mediate tool use programmatically. Invocation: `See evidence`.
- **Resume, fork, and session lineage** (`native`): Sessions can be resumed, continued, renamed, forked, and moved between local/cloud contexts. Invocation: `--resume, --continue, /resume`.

## In-harness agent

- **Scheduled tasks** (`supported`): Workflow and scheduled-task primitives are present, but coverage is less mature than headless execution. Invocation: `See evidence`.
- **Dynamic context injection** (`native`): Skills, hooks, and MCP tools can inject context only when relevant. Invocation: `See evidence`.
- **Hierarchical project instructions** (`native`): CLAUDE.md and scoped configuration provide durable project instructions. Invocation: `See evidence`.
- **Persistent memory** (`native`): Auto memory and project memory preserve selected knowledge across sessions. Invocation: `See evidence`.
- **Agent-native file editing** (`native`): Claude can read and edit repository files through native tools. Invocation: `See evidence`.
- **Agent-native shell execution** (`native`): Claude can run shell commands with configurable permission modes and sandbox controls. Invocation: `Bash tool`.
- **Agent Skills** (`native`): SKILL.md bundles can be selected by Claude or invoked explicitly; Claude Code extends the Agent Skills standard with invocation controls and subagent execution. Invocation: `/skill-name, .claude/skills/*/SKILL.md`.
- **MCP client** (`native`): Claude Code connects to local and remote MCP servers and supports OAuth-backed tools. Invocation: `.mcp.json, plugin MCP servers`.
- **Plugins/extensions** (`native`): Plugins distribute skills, agents, hooks, and MCP servers through project/user configuration and marketplaces. Invocation: `plugin install, settings.json`.
- **Model and reasoning controls** (`supported`): Model selection, fast mode, context-window enforcement, and subagent model selection are configurable. Invocation: `See evidence`.
- **Cross-session agent messaging** (`native`): Running sessions can discover one another with ListAgents and exchange messages with SendMessage across machines. Invocation: `ListAgents, SendMessage`.
- **First-class multi-agent coordination** (`native`): Agent teams, nested subagents, and cross-session messaging provide explicit coordination primitives. Invocation: `See evidence`.
- **Parallel/background agents** (`native`): Subagents and forked skills can run in the background with concurrency and spawn-depth controls. Invocation: `See evidence`.
- **Subagents/delegation** (`native`): Claude can delegate work to defined or dynamic subagents with separate prompts and tool restrictions. Invocation: `See evidence`.
- **Browser/computer use** (`native`): Claude-in-Chrome and browser/MCP integrations provide browser interaction. Invocation: `See evidence`.

## External agent/orchestrator

- **CI/GitHub automation** (`native`): Headless mode and the Agent SDK support CI, batch, and scripted workflows. Invocation: `See evidence`.
- **Scheduled tasks** (`supported`): Workflow and scheduled-task primitives are present, but coverage is less mature than headless execution. Invocation: `See evidence`.
- **Dynamic context injection** (`supported`): Skills, hooks, and MCP tools can inject context only when relevant. Invocation: `See evidence`.
- **Hierarchical project instructions** (`supported`): CLAUDE.md and scoped configuration provide durable project instructions. Invocation: `See evidence`.
- **Persistent memory** (`supported`): Auto memory and project memory preserve selected knowledge across sessions. Invocation: `See evidence`.
- **Output schema enforcement** (`native`): Headless and SDK flows can request structured output contracts for downstream automation. Invocation: `See evidence`.
- **Agent-native file editing** (`supported`): Claude can read and edit repository files through native tools. Invocation: `See evidence`.
- **Agent-native shell execution** (`supported`): Claude can run shell commands with configurable permission modes and sandbox controls. Invocation: `Bash tool`.
- **Embeddable SDK** (`native`): The Claude Agent SDK exposes the same agent loop, tools, and context management as Claude Code in Python and TypeScript. Invocation: `See evidence`.
- **Headless/non-interactive execution** (`native`): `claude -p` provides supported non-interactive execution for scripts and CI; `--bare` disables ambient project customization for reproducibility. Invocation: `claude -p, claude -p --bare`.
- **Machine-readable output** (`native`): Headless execution supports machine-readable JSON and streaming event output. Invocation: `--output-format json, --output-format stream-json`.
- **Agent Skills** (`supported`): SKILL.md bundles can be selected by Claude or invoked explicitly; Claude Code extends the Agent Skills standard with invocation controls and subagent execution. Invocation: `/skill-name, .claude/skills/*/SKILL.md`.
- **Lifecycle hooks** (`supported`): Hooks execute code at lifecycle events to inject context, enforce policy, format files, or notify humans. Invocation: `PreToolUse, PostToolUse, Stop, SessionStart`.
- **MCP client** (`supported`): Claude Code connects to local and remote MCP servers and supports OAuth-backed tools. Invocation: `.mcp.json, plugin MCP servers`.
- **Plugins/extensions** (`supported`): Plugins distribute skills, agents, hooks, and MCP servers through project/user configuration and marketplaces. Invocation: `plugin install, settings.json`.
- **Model and reasoning controls** (`configurable`): Model selection, fast mode, context-window enforcement, and subagent model selection are configurable. Invocation: `See evidence`.
- **Model/provider portability** (`configurable`): Claude Code supports Anthropic-hosted Claude plus Bedrock, Vertex AI, and enterprise gateways, but remains Claude-model-centric. Invocation: `See evidence`.
- **Agent tracing/event telemetry** (`native`): Headless/SDK event streams and hook events provide structured execution telemetry. Invocation: `See evidence`.
- **Usage and cost telemetry** (`supported`): Usage, token, budget, spend-limit, and model-usage signals are exposed in CLI/SDK paths. Invocation: `See evidence`.
- **Cross-session agent messaging** (`supported`): Running sessions can discover one another with ListAgents and exchange messages with SendMessage across machines. Invocation: `ListAgents, SendMessage`.
- **First-class multi-agent coordination** (`supported`): Agent teams, nested subagents, and cross-session messaging provide explicit coordination primitives. Invocation: `See evidence`.
- **Parallel/background agents** (`supported`): Subagents and forked skills can run in the background with concurrency and spawn-depth controls. Invocation: `See evidence`.
- **Subagents/delegation** (`supported`): Claude can delegate work to defined or dynamic subagents with separate prompts and tool restrictions. Invocation: `See evidence`.
- **Browser/computer use** (`supported`): Claude-in-Chrome and browser/MCP integrations provide browser interaction. Invocation: `See evidence`.
- **Web search/research** (`supported`): Built-in deep research is manually invoked; web access can also be supplied through MCP and browser tools. Invocation: `/deep-research`.
- **Remote/cloud execution** (`supported`): Remote Control and cloud sessions let work continue across terminal, web, desktop, and mobile surfaces. Invocation: `See evidence`.
- **Self-hosted worker/runtime** (`supported`): `claude self-hosted-runner` registers user-owned machines or containers as execution environments for web/mobile/desktop sessions. Invocation: `claude self-hosted-runner`.
- **Execution sandbox** (`supported`): Filesystem and network sandbox controls constrain tool execution, including credential masking and TLS termination options. Invocation: `See evidence`.
- **Granular permissions and approvals** (`supported`): Permission modes, allow/deny rules, workspace trust, and approval hooks govern agent actions. Invocation: `See evidence`.
- **Programmatic human approval** (`native`): SDK permission callbacks and hooks let an embedding application mediate tool use programmatically. Invocation: `See evidence`.
- **Resume, fork, and session lineage** (`supported`): Sessions can be resumed, continued, renamed, forked, and moved between local/cloud contexts. Invocation: `--resume, --continue, /resume`.

## CI or scheduled automation

- **CI/GitHub automation** (`native`): Headless mode and the Agent SDK support CI, batch, and scripted workflows. Invocation: `See evidence`.
- **Scheduled tasks** (`native`): Workflow and scheduled-task primitives are present, but coverage is less mature than headless execution. Invocation: `See evidence`.
- **Dynamic context injection** (`supported`): Skills, hooks, and MCP tools can inject context only when relevant. Invocation: `See evidence`.
- **Hierarchical project instructions** (`supported`): CLAUDE.md and scoped configuration provide durable project instructions. Invocation: `See evidence`.
- **Output schema enforcement** (`native`): Headless and SDK flows can request structured output contracts for downstream automation. Invocation: `See evidence`.
- **Agent-native file editing** (`supported`): Claude can read and edit repository files through native tools. Invocation: `See evidence`.
- **Agent-native shell execution** (`supported`): Claude can run shell commands with configurable permission modes and sandbox controls. Invocation: `Bash tool`.
- **Embeddable SDK** (`native`): The Claude Agent SDK exposes the same agent loop, tools, and context management as Claude Code in Python and TypeScript. Invocation: `See evidence`.
- **Headless/non-interactive execution** (`native`): `claude -p` provides supported non-interactive execution for scripts and CI; `--bare` disables ambient project customization for reproducibility. Invocation: `claude -p, claude -p --bare`.
- **Machine-readable output** (`native`): Headless execution supports machine-readable JSON and streaming event output. Invocation: `--output-format json, --output-format stream-json`.
- **Agent Skills** (`supported`): SKILL.md bundles can be selected by Claude or invoked explicitly; Claude Code extends the Agent Skills standard with invocation controls and subagent execution. Invocation: `/skill-name, .claude/skills/*/SKILL.md`.
- **Lifecycle hooks** (`supported`): Hooks execute code at lifecycle events to inject context, enforce policy, format files, or notify humans. Invocation: `PreToolUse, PostToolUse, Stop, SessionStart`.
- **MCP client** (`supported`): Claude Code connects to local and remote MCP servers and supports OAuth-backed tools. Invocation: `.mcp.json, plugin MCP servers`.
- **Plugins/extensions** (`supported`): Plugins distribute skills, agents, hooks, and MCP servers through project/user configuration and marketplaces. Invocation: `plugin install, settings.json`.
- **Model and reasoning controls** (`configurable`): Model selection, fast mode, context-window enforcement, and subagent model selection are configurable. Invocation: `See evidence`.
- **Model/provider portability** (`configurable`): Claude Code supports Anthropic-hosted Claude plus Bedrock, Vertex AI, and enterprise gateways, but remains Claude-model-centric. Invocation: `See evidence`.
- **Agent tracing/event telemetry** (`native`): Headless/SDK event streams and hook events provide structured execution telemetry. Invocation: `See evidence`.
- **Usage and cost telemetry** (`supported`): Usage, token, budget, spend-limit, and model-usage signals are exposed in CLI/SDK paths. Invocation: `See evidence`.
- **Cross-session agent messaging** (`supported`): Running sessions can discover one another with ListAgents and exchange messages with SendMessage across machines. Invocation: `ListAgents, SendMessage`.
- **First-class multi-agent coordination** (`supported`): Agent teams, nested subagents, and cross-session messaging provide explicit coordination primitives. Invocation: `See evidence`.
- **Parallel/background agents** (`supported`): Subagents and forked skills can run in the background with concurrency and spawn-depth controls. Invocation: `See evidence`.
- **Subagents/delegation** (`supported`): Claude can delegate work to defined or dynamic subagents with separate prompts and tool restrictions. Invocation: `See evidence`.
- **Browser/computer use** (`supported`): Claude-in-Chrome and browser/MCP integrations provide browser interaction. Invocation: `See evidence`.
- **Web search/research** (`supported`): Built-in deep research is manually invoked; web access can also be supplied through MCP and browser tools. Invocation: `/deep-research`.
- **Remote/cloud execution** (`supported`): Remote Control and cloud sessions let work continue across terminal, web, desktop, and mobile surfaces. Invocation: `See evidence`.
- **Self-hosted worker/runtime** (`supported`): `claude self-hosted-runner` registers user-owned machines or containers as execution environments for web/mobile/desktop sessions. Invocation: `claude self-hosted-runner`.
- **Execution sandbox** (`supported`): Filesystem and network sandbox controls constrain tool execution, including credential masking and TLS termination options. Invocation: `See evidence`.
- **Granular permissions and approvals** (`supported`): Permission modes, allow/deny rules, workspace trust, and approval hooks govern agent actions. Invocation: `See evidence`.
- **Programmatic human approval** (`supported`): SDK permission callbacks and hooks let an embedding application mediate tool use programmatically. Invocation: `See evidence`.
- **Resume, fork, and session lineage** (`supported`): Sessions can be resumed, continued, renamed, forked, and moved between local/cloud contexts. Invocation: `--resume, --continue, /resume`.

## Administrator

- **CI/GitHub automation** (`configurable`): Headless mode and the Agent SDK support CI, batch, and scripted workflows. Invocation: `See evidence`.
- **Scheduled tasks** (`configurable`): Workflow and scheduled-task primitives are present, but coverage is less mature than headless execution. Invocation: `See evidence`.
- **Dynamic context injection** (`configurable`): Skills, hooks, and MCP tools can inject context only when relevant. Invocation: `See evidence`.
- **Hierarchical project instructions** (`configurable`): CLAUDE.md and scoped configuration provide durable project instructions. Invocation: `See evidence`.
- **Persistent memory** (`configurable`): Auto memory and project memory preserve selected knowledge across sessions. Invocation: `See evidence`.
- **Output schema enforcement** (`configurable`): Headless and SDK flows can request structured output contracts for downstream automation. Invocation: `See evidence`.
- **Agent-native file editing** (`configurable`): Claude can read and edit repository files through native tools. Invocation: `See evidence`.
- **Agent-native shell execution** (`configurable`): Claude can run shell commands with configurable permission modes and sandbox controls. Invocation: `Bash tool`.
- **Embeddable SDK** (`configurable`): The Claude Agent SDK exposes the same agent loop, tools, and context management as Claude Code in Python and TypeScript. Invocation: `See evidence`.
- **Headless/non-interactive execution** (`configurable`): `claude -p` provides supported non-interactive execution for scripts and CI; `--bare` disables ambient project customization for reproducibility. Invocation: `claude -p, claude -p --bare`.
- **Machine-readable output** (`configurable`): Headless execution supports machine-readable JSON and streaming event output. Invocation: `--output-format json, --output-format stream-json`.
- **Agent Skills** (`configurable`): SKILL.md bundles can be selected by Claude or invoked explicitly; Claude Code extends the Agent Skills standard with invocation controls and subagent execution. Invocation: `/skill-name, .claude/skills/*/SKILL.md`.
- **Lifecycle hooks** (`configurable`): Hooks execute code at lifecycle events to inject context, enforce policy, format files, or notify humans. Invocation: `PreToolUse, PostToolUse, Stop, SessionStart`.
- **MCP client** (`configurable`): Claude Code connects to local and remote MCP servers and supports OAuth-backed tools. Invocation: `.mcp.json, plugin MCP servers`.
- **Plugins/extensions** (`configurable`): Plugins distribute skills, agents, hooks, and MCP servers through project/user configuration and marketplaces. Invocation: `plugin install, settings.json`.
- **Desktop or web surface** (`configurable`): Claude Code sessions are available through desktop and browser surfaces and can attach through Remote Control. Invocation: `See evidence`.
- **IDE integration** (`configurable`): First-party IDE integration, including VS Code surfaces tracked in the changelog. Invocation: `See evidence`.
- **Interactive terminal/TUI** (`configurable`): Interactive terminal agent with slash commands, session controls, and tool approvals. Invocation: `claude`.
- **Artifacts, diffs, and rich result views** (`configurable`): IDE, desktop, web, attachments, diffs, and review flows provide rich result inspection beyond terminal text. Invocation: `See evidence`.
- **Model and reasoning controls** (`native`): Model selection, fast mode, context-window enforcement, and subagent model selection are configurable. Invocation: `See evidence`.
- **Model/provider portability** (`native`): Claude Code supports Anthropic-hosted Claude plus Bedrock, Vertex AI, and enterprise gateways, but remains Claude-model-centric. Invocation: `See evidence`.
- **Agent tracing/event telemetry** (`configurable`): Headless/SDK event streams and hook events provide structured execution telemetry. Invocation: `See evidence`.
- **Usage and cost telemetry** (`native`): Usage, token, budget, spend-limit, and model-usage signals are exposed in CLI/SDK paths. Invocation: `See evidence`.
- **Cross-session agent messaging** (`configurable`): Running sessions can discover one another with ListAgents and exchange messages with SendMessage across machines. Invocation: `ListAgents, SendMessage`.
- **First-class multi-agent coordination** (`configurable`): Agent teams, nested subagents, and cross-session messaging provide explicit coordination primitives. Invocation: `See evidence`.
- **Parallel/background agents** (`configurable`): Subagents and forked skills can run in the background with concurrency and spawn-depth controls. Invocation: `See evidence`.
- **Subagents/delegation** (`configurable`): Claude can delegate work to defined or dynamic subagents with separate prompts and tool restrictions. Invocation: `See evidence`.
- **Browser/computer use** (`configurable`): Claude-in-Chrome and browser/MCP integrations provide browser interaction. Invocation: `See evidence`.
- **Web search/research** (`configurable`): Built-in deep research is manually invoked; web access can also be supplied through MCP and browser tools. Invocation: `/deep-research`.
- **Remote/cloud execution** (`configurable`): Remote Control and cloud sessions let work continue across terminal, web, desktop, and mobile surfaces. Invocation: `See evidence`.
- **Self-hosted worker/runtime** (`native`): `claude self-hosted-runner` registers user-owned machines or containers as execution environments for web/mobile/desktop sessions. Invocation: `claude self-hosted-runner`.
- **Enterprise managed policy** (`native`): Managed settings and organization policies govern marketplaces, permissions, telemetry, and environment behavior. Invocation: `See evidence`.
- **Execution sandbox** (`native`): Filesystem and network sandbox controls constrain tool execution, including credential masking and TLS termination options. Invocation: `See evidence`.
- **Granular permissions and approvals** (`native`): Permission modes, allow/deny rules, workspace trust, and approval hooks govern agent actions. Invocation: `See evidence`.
- **Programmatic human approval** (`configurable`): SDK permission callbacks and hooks let an embedding application mediate tool use programmatically. Invocation: `See evidence`.
- **Resume, fork, and session lineage** (`configurable`): Sessions can be resumed, continued, renamed, forked, and moved between local/cloud contexts. Invocation: `--resume, --continue, /resume`.

## Freshness rule

Treat unavailable or unknown actor access as unsupported until verified. UI-only capability is not agent-callable by implication.
