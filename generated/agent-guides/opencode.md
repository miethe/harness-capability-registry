---
schema_version: 0.1
harness_id: opencode
generated_at: 2026-08-30T21:07:07.656998Z
artifact_kind: harness_capability_guide
---

# OpenCode — Agent Capability Guide

**Vendor:** Anomaly  
**Lifecycle:** active  
**Current version in registry:** 1.18.25  
**Last verified:** 2026-08-30T21:06:52.344015Z

> UI availability does not imply that an in-harness model or an external orchestrator can invoke the capability. Use the actor-specific sections below.

## Human operator

- **CI/GitHub automation** (`supported`): The OpenCode GitHub agent handles issue and pull-request automation. Invocation: `opencode github install, /opencode or /oc PR/issue comment trigger, .github/workflows/opencode.yml`.
- **Hierarchical project instructions** (`configurable`): Repository instruction files and agent definitions shape project behavior. Invocation: `AGENTS.md (project root, walked upward), ~/.config/opencode/AGENTS.md (global), "instructions" field in opencode.json`.
- **Agent-native file editing** (`supported`): The build agent can edit files while the plan agent is read-only by default. Invocation: `edit tool, write tool, apply_patch tool`.
- **Agent-native shell execution** (`supported`): Agents can run commands subject to permission configuration. Invocation: `bash tool`.
- **Headless/non-interactive execution** (`supported`): OpenCode supports non-interactive run and GitHub automation modes. Invocation: `opencode run "<prompt>", opencode serve`.
- **Machine-readable output** (`supported`): Recent releases added JSON transcript export; automation should distinguish transcript export from a stable live event protocol. Invocation: `opencode run --format json, opencode session export --format json`.
- **Agent Skills** (`configurable`): OpenCode discovers Agent Skills and exposes them to the model through a native skill tool. Invocation: `.opencode/skills/<name>/SKILL.md, ~/.config/opencode/skills/<name>/SKILL.md, skill tool (e.g. skill({ name: "git-release" }))`.
- **MCP client** (`configurable`): OpenCode connects to MCP servers and supports OAuth compatibility improvements. Invocation: `"mcp" field in opencode.json (type: local/remote), opencode mcp auth <server-name>, opencode mcp list`.
- **Plugins/extensions** (`configurable`): Plugins extend OpenCode with events, tools, authentication, and custom behavior. Invocation: `.opencode/plugins/ (local files), ~/.config/opencode/plugins/, "plugin" field in opencode.json (npm packages)`.
- **Desktop or web surface** (`native`): OpenCode provides a desktop application and shareable session links. Invocation: `OpenCode Desktop app, opencode web, /share (generates opncd.ai/s/<share-id> link)`.
- **IDE integration** (`native`): OpenCode is available through IDE integration. Invocation: `OpenCode VS Code extension (run `opencode` in the integrated terminal to auto-install, or install "OpenCode" from the Extension Marketplace)`.
- **Interactive terminal/TUI** (`native`): OpenCode provides an interactive terminal UI with build and plan agents. Invocation: `opencode`.
- **Artifacts, diffs, and rich result views** (`native`): Desktop/TUI sessions expose diffs, undo, sharing, and transcript exports. Invocation: `TUI diff viewer ("diff_style" in tui.json), /undo and /redo commands, /details command (tool execution details)`.
- **Model and reasoning controls** (`native`): Model/provider selection is configurable per session and agent. Invocation: `provider.<name>.models.<model>.options.reasoningEffort (opencode.json), opencode run -m provider_id/model_id:variant_name`.
- **Model/provider portability** (`native`): OpenCode is explicitly provider-neutral and supports multiple API providers and subscription-backed authentication paths. Invocation: `"provider" field in opencode.json, opencode run --model / -m <provider_id>/<model_id>`.
- **Parallel/background agents** (`native`): Multiple OpenCode sessions can run in parallel against a project. Invocation: `task tool (invoking a subagent, e.g. the "general" agent), "permission.task" field in opencode.json`.
- **Web search/research** (`supported`): Web access is available through providers, MCP, and plugins rather than one fixed research subsystem. Invocation: `websearch tool, webfetch tool`.
- **Granular permissions and approvals** (`native`): Build and plan agents carry different default permissions, with configurable command and tool access. Invocation: `"permission" field in opencode.json (allow/ask/deny per tool, e.g. permission.bash, permission.edit)`.
- **Resume, fork, and session lineage** (`native`): OpenCode persists sessions and supports session navigation, sharing, undo, and reconnect flows. Invocation: `opencode run --continue / -c, opencode run --session <id> / -s, opencode run --fork`.

## In-harness agent

- **Hierarchical project instructions** (`native`): Repository instruction files and agent definitions shape project behavior. Invocation: `AGENTS.md (project root, walked upward), ~/.config/opencode/AGENTS.md (global), "instructions" field in opencode.json`.
- **Agent-native file editing** (`native`): The build agent can edit files while the plan agent is read-only by default. Invocation: `edit tool, write tool, apply_patch tool`.
- **Agent-native shell execution** (`native`): Agents can run commands subject to permission configuration. Invocation: `bash tool`.
- **Agent Skills** (`native`): OpenCode discovers Agent Skills and exposes them to the model through a native skill tool. Invocation: `.opencode/skills/<name>/SKILL.md, ~/.config/opencode/skills/<name>/SKILL.md, skill tool (e.g. skill({ name: "git-release" }))`.
- **MCP client** (`native`): OpenCode connects to MCP servers and supports OAuth compatibility improvements. Invocation: `"mcp" field in opencode.json (type: local/remote), opencode mcp auth <server-name>, opencode mcp list`.
- **Plugins/extensions** (`native`): Plugins extend OpenCode with events, tools, authentication, and custom behavior. Invocation: `.opencode/plugins/ (local files), ~/.config/opencode/plugins/, "plugin" field in opencode.json (npm packages)`.
- **Model and reasoning controls** (`supported`): Model/provider selection is configurable per session and agent. Invocation: `provider.<name>.models.<model>.options.reasoningEffort (opencode.json), opencode run -m provider_id/model_id:variant_name`.
- **Web search/research** (`native`): Web access is available through providers, MCP, and plugins rather than one fixed research subsystem. Invocation: `websearch tool, webfetch tool`.

## External agent/orchestrator

- **CI/GitHub automation** (`native`): The OpenCode GitHub agent handles issue and pull-request automation. Invocation: `opencode github install, /opencode or /oc PR/issue comment trigger, .github/workflows/opencode.yml`.
- **Hierarchical project instructions** (`supported`): Repository instruction files and agent definitions shape project behavior. Invocation: `AGENTS.md (project root, walked upward), ~/.config/opencode/AGENTS.md (global), "instructions" field in opencode.json`.
- **Agent-native file editing** (`supported`): The build agent can edit files while the plan agent is read-only by default. Invocation: `edit tool, write tool, apply_patch tool`.
- **Agent-native shell execution** (`supported`): Agents can run commands subject to permission configuration. Invocation: `bash tool`.
- **Headless/non-interactive execution** (`native`): OpenCode supports non-interactive run and GitHub automation modes. Invocation: `opencode run "<prompt>", opencode serve`.
- **Machine-readable output** (`supported`): Recent releases added JSON transcript export; automation should distinguish transcript export from a stable live event protocol. Invocation: `opencode run --format json, opencode session export --format json`.
- **Agent Skills** (`supported`): OpenCode discovers Agent Skills and exposes them to the model through a native skill tool. Invocation: `.opencode/skills/<name>/SKILL.md, ~/.config/opencode/skills/<name>/SKILL.md, skill tool (e.g. skill({ name: "git-release" }))`.
- **MCP client** (`supported`): OpenCode connects to MCP servers and supports OAuth compatibility improvements. Invocation: `"mcp" field in opencode.json (type: local/remote), opencode mcp auth <server-name>, opencode mcp list`.
- **Plugins/extensions** (`supported`): Plugins extend OpenCode with events, tools, authentication, and custom behavior. Invocation: `.opencode/plugins/ (local files), ~/.config/opencode/plugins/, "plugin" field in opencode.json (npm packages)`.
- **Model and reasoning controls** (`configurable`): Model/provider selection is configurable per session and agent. Invocation: `provider.<name>.models.<model>.options.reasoningEffort (opencode.json), opencode run -m provider_id/model_id:variant_name`.
- **Model/provider portability** (`configurable`): OpenCode is explicitly provider-neutral and supports multiple API providers and subscription-backed authentication paths. Invocation: `"provider" field in opencode.json, opencode run --model / -m <provider_id>/<model_id>`.
- **Parallel/background agents** (`supported`): Multiple OpenCode sessions can run in parallel against a project. Invocation: `task tool (invoking a subagent, e.g. the "general" agent), "permission.task" field in opencode.json`.
- **Web search/research** (`supported`): Web access is available through providers, MCP, and plugins rather than one fixed research subsystem. Invocation: `websearch tool, webfetch tool`.
- **Granular permissions and approvals** (`supported`): Build and plan agents carry different default permissions, with configurable command and tool access. Invocation: `"permission" field in opencode.json (allow/ask/deny per tool, e.g. permission.bash, permission.edit)`.
- **Resume, fork, and session lineage** (`supported`): OpenCode persists sessions and supports session navigation, sharing, undo, and reconnect flows. Invocation: `opencode run --continue / -c, opencode run --session <id> / -s, opencode run --fork`.

## CI or scheduled automation

- **CI/GitHub automation** (`native`): The OpenCode GitHub agent handles issue and pull-request automation. Invocation: `opencode github install, /opencode or /oc PR/issue comment trigger, .github/workflows/opencode.yml`.
- **Hierarchical project instructions** (`supported`): Repository instruction files and agent definitions shape project behavior. Invocation: `AGENTS.md (project root, walked upward), ~/.config/opencode/AGENTS.md (global), "instructions" field in opencode.json`.
- **Agent-native file editing** (`supported`): The build agent can edit files while the plan agent is read-only by default. Invocation: `edit tool, write tool, apply_patch tool`.
- **Agent-native shell execution** (`supported`): Agents can run commands subject to permission configuration. Invocation: `bash tool`.
- **Headless/non-interactive execution** (`native`): OpenCode supports non-interactive run and GitHub automation modes. Invocation: `opencode run "<prompt>", opencode serve`.
- **Machine-readable output** (`supported`): Recent releases added JSON transcript export; automation should distinguish transcript export from a stable live event protocol. Invocation: `opencode run --format json, opencode session export --format json`.
- **Agent Skills** (`supported`): OpenCode discovers Agent Skills and exposes them to the model through a native skill tool. Invocation: `.opencode/skills/<name>/SKILL.md, ~/.config/opencode/skills/<name>/SKILL.md, skill tool (e.g. skill({ name: "git-release" }))`.
- **MCP client** (`supported`): OpenCode connects to MCP servers and supports OAuth compatibility improvements. Invocation: `"mcp" field in opencode.json (type: local/remote), opencode mcp auth <server-name>, opencode mcp list`.
- **Plugins/extensions** (`supported`): Plugins extend OpenCode with events, tools, authentication, and custom behavior. Invocation: `.opencode/plugins/ (local files), ~/.config/opencode/plugins/, "plugin" field in opencode.json (npm packages)`.
- **Model and reasoning controls** (`configurable`): Model/provider selection is configurable per session and agent. Invocation: `provider.<name>.models.<model>.options.reasoningEffort (opencode.json), opencode run -m provider_id/model_id:variant_name`.
- **Model/provider portability** (`configurable`): OpenCode is explicitly provider-neutral and supports multiple API providers and subscription-backed authentication paths. Invocation: `"provider" field in opencode.json, opencode run --model / -m <provider_id>/<model_id>`.
- **Parallel/background agents** (`supported`): Multiple OpenCode sessions can run in parallel against a project. Invocation: `task tool (invoking a subagent, e.g. the "general" agent), "permission.task" field in opencode.json`.
- **Web search/research** (`supported`): Web access is available through providers, MCP, and plugins rather than one fixed research subsystem. Invocation: `websearch tool, webfetch tool`.
- **Granular permissions and approvals** (`supported`): Build and plan agents carry different default permissions, with configurable command and tool access. Invocation: `"permission" field in opencode.json (allow/ask/deny per tool, e.g. permission.bash, permission.edit)`.
- **Resume, fork, and session lineage** (`supported`): OpenCode persists sessions and supports session navigation, sharing, undo, and reconnect flows. Invocation: `opencode run --continue / -c, opencode run --session <id> / -s, opencode run --fork`.

## Administrator

- **CI/GitHub automation** (`configurable`): The OpenCode GitHub agent handles issue and pull-request automation. Invocation: `opencode github install, /opencode or /oc PR/issue comment trigger, .github/workflows/opencode.yml`.
- **Hierarchical project instructions** (`configurable`): Repository instruction files and agent definitions shape project behavior. Invocation: `AGENTS.md (project root, walked upward), ~/.config/opencode/AGENTS.md (global), "instructions" field in opencode.json`.
- **Agent-native file editing** (`configurable`): The build agent can edit files while the plan agent is read-only by default. Invocation: `edit tool, write tool, apply_patch tool`.
- **Agent-native shell execution** (`configurable`): Agents can run commands subject to permission configuration. Invocation: `bash tool`.
- **Headless/non-interactive execution** (`configurable`): OpenCode supports non-interactive run and GitHub automation modes. Invocation: `opencode run "<prompt>", opencode serve`.
- **Machine-readable output** (`configurable`): Recent releases added JSON transcript export; automation should distinguish transcript export from a stable live event protocol. Invocation: `opencode run --format json, opencode session export --format json`.
- **Agent Skills** (`configurable`): OpenCode discovers Agent Skills and exposes them to the model through a native skill tool. Invocation: `.opencode/skills/<name>/SKILL.md, ~/.config/opencode/skills/<name>/SKILL.md, skill tool (e.g. skill({ name: "git-release" }))`.
- **MCP client** (`configurable`): OpenCode connects to MCP servers and supports OAuth compatibility improvements. Invocation: `"mcp" field in opencode.json (type: local/remote), opencode mcp auth <server-name>, opencode mcp list`.
- **Plugins/extensions** (`configurable`): Plugins extend OpenCode with events, tools, authentication, and custom behavior. Invocation: `.opencode/plugins/ (local files), ~/.config/opencode/plugins/, "plugin" field in opencode.json (npm packages)`.
- **Desktop or web surface** (`configurable`): OpenCode provides a desktop application and shareable session links. Invocation: `OpenCode Desktop app, opencode web, /share (generates opncd.ai/s/<share-id> link)`.
- **IDE integration** (`configurable`): OpenCode is available through IDE integration. Invocation: `OpenCode VS Code extension (run `opencode` in the integrated terminal to auto-install, or install "OpenCode" from the Extension Marketplace)`.
- **Interactive terminal/TUI** (`configurable`): OpenCode provides an interactive terminal UI with build and plan agents. Invocation: `opencode`.
- **Artifacts, diffs, and rich result views** (`configurable`): Desktop/TUI sessions expose diffs, undo, sharing, and transcript exports. Invocation: `TUI diff viewer ("diff_style" in tui.json), /undo and /redo commands, /details command (tool execution details)`.
- **Model and reasoning controls** (`configurable`): Model/provider selection is configurable per session and agent. Invocation: `provider.<name>.models.<model>.options.reasoningEffort (opencode.json), opencode run -m provider_id/model_id:variant_name`.
- **Model/provider portability** (`configurable`): OpenCode is explicitly provider-neutral and supports multiple API providers and subscription-backed authentication paths. Invocation: `"provider" field in opencode.json, opencode run --model / -m <provider_id>/<model_id>`.
- **Parallel/background agents** (`configurable`): Multiple OpenCode sessions can run in parallel against a project. Invocation: `task tool (invoking a subagent, e.g. the "general" agent), "permission.task" field in opencode.json`.
- **Web search/research** (`configurable`): Web access is available through providers, MCP, and plugins rather than one fixed research subsystem. Invocation: `websearch tool, webfetch tool`.
- **Granular permissions and approvals** (`configurable`): Build and plan agents carry different default permissions, with configurable command and tool access. Invocation: `"permission" field in opencode.json (allow/ask/deny per tool, e.g. permission.bash, permission.edit)`.
- **Resume, fork, and session lineage** (`configurable`): OpenCode persists sessions and supports session navigation, sharing, undo, and reconnect flows. Invocation: `opencode run --continue / -c, opencode run --session <id> / -s, opencode run --fork`.

## Freshness rule

Treat unavailable or unknown actor access as unsupported until verified. UI-only capability is not agent-callable by implication.
