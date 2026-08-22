---
schema_version: 0.1
harness_id: opencode
generated_at: 2026-08-22T13:02:17.406799Z
artifact_kind: harness_capability_guide
---

# OpenCode — Agent Capability Guide

**Vendor:** Anomaly  
**Lifecycle:** active  
**Current version in registry:** 1.18.21  
**Last verified:** 2026-08-22T13:02:05.018986Z

> UI availability does not imply that an in-harness model or an external orchestrator can invoke the capability. Use the actor-specific sections below.

## Human operator

- **CI/GitHub automation** (`supported`): The OpenCode GitHub agent handles issue and pull-request automation. Invocation: `See evidence`.
- **Hierarchical project instructions** (`configurable`): Repository instruction files and agent definitions shape project behavior. Invocation: `See evidence`.
- **Agent-native file editing** (`supported`): The build agent can edit files while the plan agent is read-only by default. Invocation: `See evidence`.
- **Agent-native shell execution** (`supported`): Agents can run commands subject to permission configuration. Invocation: `See evidence`.
- **Headless/non-interactive execution** (`supported`): OpenCode supports non-interactive run and GitHub automation modes. Invocation: `See evidence`.
- **Machine-readable output** (`supported`): Recent releases added JSON transcript export; automation should distinguish transcript export from a stable live event protocol. Invocation: `See evidence`.
- **Agent Skills** (`configurable`): OpenCode discovers Agent Skills and exposes them to the model through a native skill tool. Invocation: `See evidence`.
- **MCP client** (`configurable`): OpenCode connects to MCP servers and supports OAuth compatibility improvements. Invocation: `See evidence`.
- **Plugins/extensions** (`configurable`): Plugins extend OpenCode with events, tools, authentication, and custom behavior. Invocation: `See evidence`.
- **Desktop or web surface** (`native`): OpenCode provides a desktop application and shareable session links. Invocation: `See evidence`.
- **IDE integration** (`native`): OpenCode is available through IDE integration. Invocation: `See evidence`.
- **Interactive terminal/TUI** (`native`): OpenCode provides an interactive terminal UI with build and plan agents. Invocation: `opencode`.
- **Artifacts, diffs, and rich result views** (`native`): Desktop/TUI sessions expose diffs, undo, sharing, and transcript exports. Invocation: `See evidence`.
- **Model and reasoning controls** (`native`): Model/provider selection is configurable per session and agent. Invocation: `See evidence`.
- **Model/provider portability** (`native`): OpenCode is explicitly provider-neutral and supports multiple API providers and subscription-backed authentication paths. Invocation: `See evidence`.
- **Parallel/background agents** (`native`): Multiple OpenCode sessions can run in parallel against a project. Invocation: `See evidence`.
- **Web search/research** (`supported`): Web access is available through providers, MCP, and plugins rather than one fixed research subsystem. Invocation: `See evidence`.
- **Granular permissions and approvals** (`native`): Build and plan agents carry different default permissions, with configurable command and tool access. Invocation: `See evidence`.
- **Resume, fork, and session lineage** (`native`): OpenCode persists sessions and supports session navigation, sharing, undo, and reconnect flows. Invocation: `See evidence`.

## In-harness agent

- **Hierarchical project instructions** (`native`): Repository instruction files and agent definitions shape project behavior. Invocation: `See evidence`.
- **Agent-native file editing** (`native`): The build agent can edit files while the plan agent is read-only by default. Invocation: `See evidence`.
- **Agent-native shell execution** (`native`): Agents can run commands subject to permission configuration. Invocation: `See evidence`.
- **Agent Skills** (`native`): OpenCode discovers Agent Skills and exposes them to the model through a native skill tool. Invocation: `See evidence`.
- **MCP client** (`native`): OpenCode connects to MCP servers and supports OAuth compatibility improvements. Invocation: `See evidence`.
- **Plugins/extensions** (`native`): Plugins extend OpenCode with events, tools, authentication, and custom behavior. Invocation: `See evidence`.
- **Model and reasoning controls** (`supported`): Model/provider selection is configurable per session and agent. Invocation: `See evidence`.
- **Web search/research** (`native`): Web access is available through providers, MCP, and plugins rather than one fixed research subsystem. Invocation: `See evidence`.

## External agent/orchestrator

- **CI/GitHub automation** (`native`): The OpenCode GitHub agent handles issue and pull-request automation. Invocation: `See evidence`.
- **Hierarchical project instructions** (`supported`): Repository instruction files and agent definitions shape project behavior. Invocation: `See evidence`.
- **Agent-native file editing** (`supported`): The build agent can edit files while the plan agent is read-only by default. Invocation: `See evidence`.
- **Agent-native shell execution** (`supported`): Agents can run commands subject to permission configuration. Invocation: `See evidence`.
- **Headless/non-interactive execution** (`native`): OpenCode supports non-interactive run and GitHub automation modes. Invocation: `See evidence`.
- **Machine-readable output** (`supported`): Recent releases added JSON transcript export; automation should distinguish transcript export from a stable live event protocol. Invocation: `See evidence`.
- **Agent Skills** (`supported`): OpenCode discovers Agent Skills and exposes them to the model through a native skill tool. Invocation: `See evidence`.
- **MCP client** (`supported`): OpenCode connects to MCP servers and supports OAuth compatibility improvements. Invocation: `See evidence`.
- **Plugins/extensions** (`supported`): Plugins extend OpenCode with events, tools, authentication, and custom behavior. Invocation: `See evidence`.
- **Model and reasoning controls** (`configurable`): Model/provider selection is configurable per session and agent. Invocation: `See evidence`.
- **Model/provider portability** (`configurable`): OpenCode is explicitly provider-neutral and supports multiple API providers and subscription-backed authentication paths. Invocation: `See evidence`.
- **Parallel/background agents** (`supported`): Multiple OpenCode sessions can run in parallel against a project. Invocation: `See evidence`.
- **Web search/research** (`supported`): Web access is available through providers, MCP, and plugins rather than one fixed research subsystem. Invocation: `See evidence`.
- **Granular permissions and approvals** (`supported`): Build and plan agents carry different default permissions, with configurable command and tool access. Invocation: `See evidence`.
- **Resume, fork, and session lineage** (`supported`): OpenCode persists sessions and supports session navigation, sharing, undo, and reconnect flows. Invocation: `See evidence`.

## CI or scheduled automation

- **CI/GitHub automation** (`native`): The OpenCode GitHub agent handles issue and pull-request automation. Invocation: `See evidence`.
- **Hierarchical project instructions** (`supported`): Repository instruction files and agent definitions shape project behavior. Invocation: `See evidence`.
- **Agent-native file editing** (`supported`): The build agent can edit files while the plan agent is read-only by default. Invocation: `See evidence`.
- **Agent-native shell execution** (`supported`): Agents can run commands subject to permission configuration. Invocation: `See evidence`.
- **Headless/non-interactive execution** (`native`): OpenCode supports non-interactive run and GitHub automation modes. Invocation: `See evidence`.
- **Machine-readable output** (`supported`): Recent releases added JSON transcript export; automation should distinguish transcript export from a stable live event protocol. Invocation: `See evidence`.
- **Agent Skills** (`supported`): OpenCode discovers Agent Skills and exposes them to the model through a native skill tool. Invocation: `See evidence`.
- **MCP client** (`supported`): OpenCode connects to MCP servers and supports OAuth compatibility improvements. Invocation: `See evidence`.
- **Plugins/extensions** (`supported`): Plugins extend OpenCode with events, tools, authentication, and custom behavior. Invocation: `See evidence`.
- **Model and reasoning controls** (`configurable`): Model/provider selection is configurable per session and agent. Invocation: `See evidence`.
- **Model/provider portability** (`configurable`): OpenCode is explicitly provider-neutral and supports multiple API providers and subscription-backed authentication paths. Invocation: `See evidence`.
- **Parallel/background agents** (`supported`): Multiple OpenCode sessions can run in parallel against a project. Invocation: `See evidence`.
- **Web search/research** (`supported`): Web access is available through providers, MCP, and plugins rather than one fixed research subsystem. Invocation: `See evidence`.
- **Granular permissions and approvals** (`supported`): Build and plan agents carry different default permissions, with configurable command and tool access. Invocation: `See evidence`.
- **Resume, fork, and session lineage** (`supported`): OpenCode persists sessions and supports session navigation, sharing, undo, and reconnect flows. Invocation: `See evidence`.

## Administrator

- **CI/GitHub automation** (`configurable`): The OpenCode GitHub agent handles issue and pull-request automation. Invocation: `See evidence`.
- **Hierarchical project instructions** (`configurable`): Repository instruction files and agent definitions shape project behavior. Invocation: `See evidence`.
- **Agent-native file editing** (`configurable`): The build agent can edit files while the plan agent is read-only by default. Invocation: `See evidence`.
- **Agent-native shell execution** (`configurable`): Agents can run commands subject to permission configuration. Invocation: `See evidence`.
- **Headless/non-interactive execution** (`configurable`): OpenCode supports non-interactive run and GitHub automation modes. Invocation: `See evidence`.
- **Machine-readable output** (`configurable`): Recent releases added JSON transcript export; automation should distinguish transcript export from a stable live event protocol. Invocation: `See evidence`.
- **Agent Skills** (`configurable`): OpenCode discovers Agent Skills and exposes them to the model through a native skill tool. Invocation: `See evidence`.
- **MCP client** (`configurable`): OpenCode connects to MCP servers and supports OAuth compatibility improvements. Invocation: `See evidence`.
- **Plugins/extensions** (`configurable`): Plugins extend OpenCode with events, tools, authentication, and custom behavior. Invocation: `See evidence`.
- **Desktop or web surface** (`configurable`): OpenCode provides a desktop application and shareable session links. Invocation: `See evidence`.
- **IDE integration** (`configurable`): OpenCode is available through IDE integration. Invocation: `See evidence`.
- **Interactive terminal/TUI** (`configurable`): OpenCode provides an interactive terminal UI with build and plan agents. Invocation: `opencode`.
- **Artifacts, diffs, and rich result views** (`configurable`): Desktop/TUI sessions expose diffs, undo, sharing, and transcript exports. Invocation: `See evidence`.
- **Model and reasoning controls** (`configurable`): Model/provider selection is configurable per session and agent. Invocation: `See evidence`.
- **Model/provider portability** (`configurable`): OpenCode is explicitly provider-neutral and supports multiple API providers and subscription-backed authentication paths. Invocation: `See evidence`.
- **Parallel/background agents** (`configurable`): Multiple OpenCode sessions can run in parallel against a project. Invocation: `See evidence`.
- **Web search/research** (`configurable`): Web access is available through providers, MCP, and plugins rather than one fixed research subsystem. Invocation: `See evidence`.
- **Granular permissions and approvals** (`configurable`): Build and plan agents carry different default permissions, with configurable command and tool access. Invocation: `See evidence`.
- **Resume, fork, and session lineage** (`configurable`): OpenCode persists sessions and supports session navigation, sharing, undo, and reconnect flows. Invocation: `See evidence`.

## Freshness rule

Treat unavailable or unknown actor access as unsupported until verified. UI-only capability is not agent-callable by implication.
