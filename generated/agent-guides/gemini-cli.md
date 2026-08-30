---
schema_version: 0.1
harness_id: gemini-cli
generated_at: 2026-08-30T21:07:07.656998Z
artifact_kind: harness_capability_guide
---

# Gemini CLI — Agent Capability Guide

**Vendor:** Google  
**Lifecycle:** legacy  
**Current version in registry:** 0.59.0-nightly.20260830.g0bd1d4397  
**Last verified:** 2026-08-30T21:06:52.344015Z

> UI availability does not imply that an in-harness model or an external orchestrator can invoke the capability. Use the actor-specific sections below.

## Human operator

- **Agent-native file editing** (`supported`): Gemini CLI agents can inspect and modify repository files. Invocation: `write_file tool, replace tool, edit tool`.
- **Agent-native shell execution** (`supported`): Gemini CLI agents can run shell tools under configured policies. Invocation: `run_shell_command tool`.
- **Headless/non-interactive execution** (`supported`): Gemini CLI exposes headless mode for scripts and automation. Invocation: `-p, --prompt`.
- **Machine-readable output** (`supported`): Headless mode supports structured JSON output. Invocation: `--output-format json, --output-format jsonl`.
- **Agent Skills** (`configurable`): Agent Skills were supported and ported to Antigravity CLI. Invocation: `.gemini/skills/ directory, ~/.gemini/skills/ directory, activate_skill tool`.
- **Lifecycle hooks** (`configurable`): Gemini CLI supports lifecycle hooks. Invocation: `hooks key in settings.json (e.g. BeforeTool, AfterTool, SessionStart events)`.
- **MCP client** (`configurable`): Gemini CLI supports MCP servers. Invocation: `mcpServers key in settings.json, gemini mcp add`.
- **Plugins/extensions** (`configurable`): Gemini CLI extensions were supported and became Antigravity plugins in the successor product. Invocation: `gemini extensions install <repo-url>, /extensions list`.
- **Interactive terminal/TUI** (`native`): Gemini CLI provides an interactive terminal agent. Invocation: `gemini`.
- **Model and reasoning controls** (`native`): Model selection and plan-mode workflows are configurable. Invocation: `--model flag, /model command, thinkingBudget in modelConfigs.customAliases[].modelConfig.generateContentConfig`.
- **Subagents/delegation** (`supported`): Subagents were supported and ported to Antigravity CLI. Invocation: `/agents command, @<subagent_name> syntax, agents.overrides in settings.json`.
- **Granular permissions and approvals** (`native`): Gemini CLI provides approval and policy controls for tools. Invocation: `--approval-mode <default|auto_edit|yolo|plan>, --yolo, policy engine (policyPaths, .toml policy files)`.
- **Image generation** (`experimental`): gemini-cli has no built-in image-synthesis command out of the box; image generation is reached either by installing the community 'nanobanana' extension (extensions.plugins) or by routing a prompt to an image-capable model via -m (e.g. gemini-3.1-flash-image) — neither path is documented as a first-class gemini-cli feature. Invocation: `gemini extensions install https://github.com/gemini-cli-extensions/nanobanana  (then) /generate <prompt>, gemini -p "<prompt>" -m gemini-3.1-flash-image --yolo -o text  (undocumented, AOS-observed model-routing path)`.

## In-harness agent

- **Agent-native file editing** (`native`): Gemini CLI agents can inspect and modify repository files. Invocation: `write_file tool, replace tool, edit tool`.
- **Agent-native shell execution** (`native`): Gemini CLI agents can run shell tools under configured policies. Invocation: `run_shell_command tool`.
- **Agent Skills** (`native`): Agent Skills were supported and ported to Antigravity CLI. Invocation: `.gemini/skills/ directory, ~/.gemini/skills/ directory, activate_skill tool`.
- **MCP client** (`native`): Gemini CLI supports MCP servers. Invocation: `mcpServers key in settings.json, gemini mcp add`.
- **Plugins/extensions** (`native`): Gemini CLI extensions were supported and became Antigravity plugins in the successor product. Invocation: `gemini extensions install <repo-url>, /extensions list`.
- **Model and reasoning controls** (`supported`): Model selection and plan-mode workflows are configurable. Invocation: `--model flag, /model command, thinkingBudget in modelConfigs.customAliases[].modelConfig.generateContentConfig`.
- **Subagents/delegation** (`native`): Subagents were supported and ported to Antigravity CLI. Invocation: `/agents command, @<subagent_name> syntax, agents.overrides in settings.json`.

## External agent/orchestrator

- **Agent-native file editing** (`supported`): Gemini CLI agents can inspect and modify repository files. Invocation: `write_file tool, replace tool, edit tool`.
- **Agent-native shell execution** (`supported`): Gemini CLI agents can run shell tools under configured policies. Invocation: `run_shell_command tool`.
- **Headless/non-interactive execution** (`native`): Gemini CLI exposes headless mode for scripts and automation. Invocation: `-p, --prompt`.
- **Machine-readable output** (`native`): Headless mode supports structured JSON output. Invocation: `--output-format json, --output-format jsonl`.
- **Agent Skills** (`supported`): Agent Skills were supported and ported to Antigravity CLI. Invocation: `.gemini/skills/ directory, ~/.gemini/skills/ directory, activate_skill tool`.
- **Lifecycle hooks** (`supported`): Gemini CLI supports lifecycle hooks. Invocation: `hooks key in settings.json (e.g. BeforeTool, AfterTool, SessionStart events)`.
- **MCP client** (`supported`): Gemini CLI supports MCP servers. Invocation: `mcpServers key in settings.json, gemini mcp add`.
- **Plugins/extensions** (`supported`): Gemini CLI extensions were supported and became Antigravity plugins in the successor product. Invocation: `gemini extensions install <repo-url>, /extensions list`.
- **Model and reasoning controls** (`configurable`): Model selection and plan-mode workflows are configurable. Invocation: `--model flag, /model command, thinkingBudget in modelConfigs.customAliases[].modelConfig.generateContentConfig`.
- **Subagents/delegation** (`supported`): Subagents were supported and ported to Antigravity CLI. Invocation: `/agents command, @<subagent_name> syntax, agents.overrides in settings.json`.
- **Granular permissions and approvals** (`supported`): Gemini CLI provides approval and policy controls for tools. Invocation: `--approval-mode <default|auto_edit|yolo|plan>, --yolo, policy engine (policyPaths, .toml policy files)`.
- **Image generation** (`experimental`): gemini-cli has no built-in image-synthesis command out of the box; image generation is reached either by installing the community 'nanobanana' extension (extensions.plugins) or by routing a prompt to an image-capable model via -m (e.g. gemini-3.1-flash-image) — neither path is documented as a first-class gemini-cli feature. Invocation: `gemini extensions install https://github.com/gemini-cli-extensions/nanobanana  (then) /generate <prompt>, gemini -p "<prompt>" -m gemini-3.1-flash-image --yolo -o text  (undocumented, AOS-observed model-routing path)`.

## CI or scheduled automation

- **Agent-native file editing** (`supported`): Gemini CLI agents can inspect and modify repository files. Invocation: `write_file tool, replace tool, edit tool`.
- **Agent-native shell execution** (`supported`): Gemini CLI agents can run shell tools under configured policies. Invocation: `run_shell_command tool`.
- **Headless/non-interactive execution** (`native`): Gemini CLI exposes headless mode for scripts and automation. Invocation: `-p, --prompt`.
- **Machine-readable output** (`native`): Headless mode supports structured JSON output. Invocation: `--output-format json, --output-format jsonl`.
- **Agent Skills** (`supported`): Agent Skills were supported and ported to Antigravity CLI. Invocation: `.gemini/skills/ directory, ~/.gemini/skills/ directory, activate_skill tool`.
- **Lifecycle hooks** (`supported`): Gemini CLI supports lifecycle hooks. Invocation: `hooks key in settings.json (e.g. BeforeTool, AfterTool, SessionStart events)`.
- **MCP client** (`supported`): Gemini CLI supports MCP servers. Invocation: `mcpServers key in settings.json, gemini mcp add`.
- **Plugins/extensions** (`supported`): Gemini CLI extensions were supported and became Antigravity plugins in the successor product. Invocation: `gemini extensions install <repo-url>, /extensions list`.
- **Model and reasoning controls** (`configurable`): Model selection and plan-mode workflows are configurable. Invocation: `--model flag, /model command, thinkingBudget in modelConfigs.customAliases[].modelConfig.generateContentConfig`.
- **Subagents/delegation** (`supported`): Subagents were supported and ported to Antigravity CLI. Invocation: `/agents command, @<subagent_name> syntax, agents.overrides in settings.json`.
- **Granular permissions and approvals** (`supported`): Gemini CLI provides approval and policy controls for tools. Invocation: `--approval-mode <default|auto_edit|yolo|plan>, --yolo, policy engine (policyPaths, .toml policy files)`.

## Administrator

- **Agent-native file editing** (`configurable`): Gemini CLI agents can inspect and modify repository files. Invocation: `write_file tool, replace tool, edit tool`.
- **Agent-native shell execution** (`configurable`): Gemini CLI agents can run shell tools under configured policies. Invocation: `run_shell_command tool`.
- **Headless/non-interactive execution** (`configurable`): Gemini CLI exposes headless mode for scripts and automation. Invocation: `-p, --prompt`.
- **Machine-readable output** (`configurable`): Headless mode supports structured JSON output. Invocation: `--output-format json, --output-format jsonl`.
- **Agent Skills** (`configurable`): Agent Skills were supported and ported to Antigravity CLI. Invocation: `.gemini/skills/ directory, ~/.gemini/skills/ directory, activate_skill tool`.
- **Lifecycle hooks** (`configurable`): Gemini CLI supports lifecycle hooks. Invocation: `hooks key in settings.json (e.g. BeforeTool, AfterTool, SessionStart events)`.
- **MCP client** (`configurable`): Gemini CLI supports MCP servers. Invocation: `mcpServers key in settings.json, gemini mcp add`.
- **Plugins/extensions** (`configurable`): Gemini CLI extensions were supported and became Antigravity plugins in the successor product. Invocation: `gemini extensions install <repo-url>, /extensions list`.
- **Interactive terminal/TUI** (`configurable`): Gemini CLI provides an interactive terminal agent. Invocation: `gemini`.
- **Model and reasoning controls** (`configurable`): Model selection and plan-mode workflows are configurable. Invocation: `--model flag, /model command, thinkingBudget in modelConfigs.customAliases[].modelConfig.generateContentConfig`.
- **Subagents/delegation** (`configurable`): Subagents were supported and ported to Antigravity CLI. Invocation: `/agents command, @<subagent_name> syntax, agents.overrides in settings.json`.
- **Granular permissions and approvals** (`configurable`): Gemini CLI provides approval and policy controls for tools. Invocation: `--approval-mode <default|auto_edit|yolo|plan>, --yolo, policy engine (policyPaths, .toml policy files)`.
- **Image generation** (`configurable`): gemini-cli has no built-in image-synthesis command out of the box; image generation is reached either by installing the community 'nanobanana' extension (extensions.plugins) or by routing a prompt to an image-capable model via -m (e.g. gemini-3.1-flash-image) — neither path is documented as a first-class gemini-cli feature. Invocation: `gemini extensions install https://github.com/gemini-cli-extensions/nanobanana  (then) /generate <prompt>, gemini -p "<prompt>" -m gemini-3.1-flash-image --yolo -o text  (undocumented, AOS-observed model-routing path)`.

## Freshness rule

Treat unavailable or unknown actor access as unsupported until verified. UI-only capability is not agent-callable by implication.
