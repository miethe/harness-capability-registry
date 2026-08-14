from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from hcr.collectors.markdown_changelog import parse_changelog_file  # noqa: E402
from hcr.io import write_json  # noqa: E402
from hcr.versions import release_timeline_key  # noqa: E402
from hcr.normalizers.heuristic import (  # noqa: E402
    classify_category,
    classify_change,
    infer_actors,
    infer_capabilities,
    infer_surfaces,
    is_breaking_or_deprecated,
    is_security_relevant,
)

TODAY = "2026-08-08"
VERIFIED_AT = "2026-08-08T20:00:00Z"


def source(
    id: str,
    name: str,
    url: str,
    harness_ids: list[str],
    *,
    source_type: str,
    purpose: str,
    authority: str = "official_primary",
    official: bool = True,
    collector: dict[str, Any] | None = None,
    cadence: str = "daily",
    enabled: bool = True,
    notes: str | None = None,
) -> dict[str, Any]:
    return {
        "id": id,
        "name": name,
        "url": url,
        "harness_ids": harness_ids,
        "source_type": source_type,
        "purpose": purpose,
        "authority": authority,
        "official": official,
        "enabled": enabled,
        "collector": collector or {"kind": "manual_reference"},
        "refresh": {
            "cadence": cadence,
            "historical_backfill_days": 120,
            "staleness_sla_hours": 24 if cadence in {"hourly", "six_hourly", "daily"} else 168,
        },
        "notes": notes,
    }


sources: list[dict[str, Any]] = [
    # Claude Code
    source(
        "src.claude-code.changelog",
        "Claude Code raw changelog",
        "https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md",
        ["claude-code"],
        source_type="markdown_changelog",
        purpose="release_history",
        collector={"kind": "markdown_changelog", "local_seed_path": "raw/claude-code/CHANGELOG.md", "max_dateless_releases": 110},
        cadence="six_hourly",
    ),
    source(
        "src.claude-code.releases",
        "Claude Code GitHub releases",
        "https://github.com/anthropics/claude-code/releases",
        ["claude-code"],
        source_type="github_releases",
        purpose="release_history",
        collector={"kind": "github_releases", "repo": "anthropics/claude-code"},
        cadence="six_hourly",
        notes="Use GitHub release metadata to enrich dates and immutable tag references; reconcile against the raw changelog.",
    ),
    source("src.claude-code.docs.overview", "Claude Code overview", "https://docs.anthropic.com/en/docs/claude-code/overview", ["claude-code"], source_type="documentation", purpose="capability_reference"),
    source("src.claude-code.docs.headless", "Claude Code programmatic/headless mode", "https://docs.anthropic.com/en/docs/claude-code/headless", ["claude-code"], source_type="documentation", purpose="capability_reference"),
    source("src.claude-code.docs.skills", "Claude Code skills", "https://docs.anthropic.com/en/docs/claude-code/skills", ["claude-code"], source_type="documentation", purpose="capability_reference"),
    source("src.claude-code.docs.hooks", "Claude Code hooks", "https://docs.anthropic.com/en/docs/claude-code/hooks-guide", ["claude-code"], source_type="documentation", purpose="capability_reference"),
    source("src.claude-code.docs.settings", "Claude Code settings and plugins", "https://docs.anthropic.com/en/docs/claude-code/settings", ["claude-code"], source_type="documentation", purpose="capability_reference"),
    source("src.claude-code.docs.sdk", "Claude Agent SDK overview", "https://docs.anthropic.com/en/docs/claude-code/sdk", ["claude-code", "claude-agent-sdk-python", "claude-agent-sdk-typescript"], source_type="documentation", purpose="capability_reference"),
    source("src.claude-code.docs.cli", "Claude Code CLI reference", "https://docs.anthropic.com/en/docs/claude-code/cli-reference", ["claude-code"], source_type="documentation", purpose="capability_reference"),
    # OpenAI Codex
    source("src.codex.releases", "OpenAI Codex GitHub releases", "https://github.com/openai/codex/releases", ["openai-codex"], source_type="github_releases", purpose="release_history", collector={"kind": "github_releases", "repo": "openai/codex"}, cadence="six_hourly"),
    source("src.codex.product-changelog", "ChatGPT and Codex product changelog", "https://developers.openai.com/codex/changelog", ["openai-codex"], source_type="product_changelog", purpose="capability_reference", cadence="daily"),
    source("src.codex.docs.cli", "Codex CLI", "https://developers.openai.com/codex/cli", ["openai-codex"], source_type="documentation", purpose="capability_reference"),
    source("src.codex.docs.noninteractive", "Codex non-interactive mode", "https://developers.openai.com/codex/non-interactive-mode", ["openai-codex"], source_type="documentation", purpose="capability_reference"),
    source("src.codex.docs.commands", "Codex developer commands", "https://developers.openai.com/codex/developer-commands", ["openai-codex"], source_type="documentation", purpose="capability_reference"),
    source("src.codex.docs.app-server", "Codex app server", "https://developers.openai.com/codex/app-server", ["openai-codex", "codex-sdk-python"], source_type="documentation", purpose="capability_reference"),
    source("src.codex.docs.sdk", "Codex SDK", "https://developers.openai.com/codex/codex-sdk", ["openai-codex", "codex-sdk-python", "codex-sdk-typescript"], source_type="documentation", purpose="capability_reference"),
    source("src.codex.docs.skills", "Codex skills and plugins", "https://developers.openai.com/codex/skills-and-plugins", ["openai-codex"], source_type="documentation", purpose="capability_reference"),
    source("src.codex.docs.agents-md", "Codex AGENTS.md instructions", "https://developers.openai.com/codex/agent-configuration/agents-md", ["openai-codex"], source_type="documentation", purpose="capability_reference"),
    source("src.codex.docs.mcp", "Codex MCP", "https://developers.openai.com/codex/mcp", ["openai-codex"], source_type="documentation", purpose="capability_reference"),
    source("src.codex.docs.subagents", "Codex subagents", "https://developers.openai.com/codex/agent-configuration/subagents", ["openai-codex"], source_type="documentation", purpose="capability_reference"),
    source("src.codex.docs.security", "Codex approvals and security", "https://developers.openai.com/codex/agent-approvals-security", ["openai-codex"], source_type="documentation", purpose="capability_reference"),
    source("src.codex.docs.github-action", "Codex GitHub Action", "https://developers.openai.com/codex/github-action", ["openai-codex"], source_type="documentation", purpose="capability_reference"),
    # OpenCode
    source("src.opencode.releases", "OpenCode GitHub releases", "https://github.com/anomalyco/opencode/releases", ["opencode"], source_type="github_releases", purpose="release_history", collector={"kind": "github_releases", "repo": "anomalyco/opencode"}, cadence="six_hourly"),
    source("src.opencode.docs.intro", "OpenCode documentation", "https://opencode.ai/docs/", ["opencode"], source_type="documentation", purpose="capability_reference"),
    source("src.opencode.docs.skills", "OpenCode Agent Skills", "https://opencode.ai/docs/skills/", ["opencode"], source_type="documentation", purpose="capability_reference"),
    source("src.opencode.docs.plugins", "OpenCode plugins", "https://opencode.ai/docs/plugins/", ["opencode"], source_type="documentation", purpose="capability_reference"),
    source("src.opencode.docs.github", "OpenCode GitHub agent", "https://opencode.ai/docs/github/", ["opencode"], source_type="documentation", purpose="capability_reference"),
    source("src.opencode.repo", "OpenCode repository", "https://github.com/anomalyco/opencode", ["opencode"], source_type="repository", purpose="capability_reference"),
    # Hermes
    source("src.hermes.releases", "Hermes Agent GitHub releases", "https://github.com/NousResearch/hermes-agent/releases", ["hermes-agent"], source_type="github_releases", purpose="release_history", collector={"kind": "github_releases", "repo": "NousResearch/hermes-agent"}, cadence="six_hourly"),
    source("src.hermes.repo", "Hermes Agent repository", "https://github.com/NousResearch/hermes-agent", ["hermes-agent"], source_type="repository", purpose="capability_reference"),
    source("src.hermes.docs", "Hermes Agent documentation", "https://hermes-agent.nousresearch.com/", ["hermes-agent"], source_type="documentation", purpose="capability_reference"),
    source("src.hermes.docs.quickstart", "Hermes quickstart", "https://hermes-agent.nousresearch.com/docs/getting-started/quickstart", ["hermes-agent"], source_type="documentation", purpose="capability_reference"),
    source("src.hermes.docs.skills", "Hermes skills", "https://hermes-agent.nousresearch.com/docs/user-guide/features/skills", ["hermes-agent"], source_type="documentation", purpose="capability_reference"),
    source("src.hermes.docs.memory", "Hermes memory", "https://hermes-agent.nousresearch.com/docs/user-guide/features/memory", ["hermes-agent"], source_type="documentation", purpose="capability_reference"),
    source("src.hermes.docs.voice", "Hermes voice", "https://hermes-agent.nousresearch.com/docs/user-guide/features/voice-mode", ["hermes-agent"], source_type="documentation", purpose="capability_reference"),
    # Google Antigravity and Gemini
    source("src.antigravity.changelog", "Antigravity CLI raw changelog", "https://raw.githubusercontent.com/google-antigravity/antigravity-cli/main/CHANGELOG.md", ["antigravity-cli"], source_type="markdown_changelog", purpose="release_history", collector={"kind": "markdown_changelog", "local_seed_path": "raw/antigravity-cli/CHANGELOG.md", "max_dateless_releases": 110}, cadence="six_hourly"),
    source("src.antigravity.releases", "Antigravity CLI GitHub releases", "https://github.com/google-antigravity/antigravity-cli/releases", ["antigravity-cli"], source_type="github_releases", purpose="release_history", collector={"kind": "github_releases", "repo": "google-antigravity/antigravity-cli"}, cadence="six_hourly"),
    source("src.antigravity.repo", "Antigravity CLI repository", "https://github.com/google-antigravity/antigravity-cli", ["antigravity-cli"], source_type="repository", purpose="capability_reference"),
    source("src.antigravity.site", "Google Antigravity", "https://antigravity.google/", ["antigravity-cli"], source_type="product_documentation", purpose="capability_reference"),
    source("src.antigravity.transition-blog", "Google transition from Gemini CLI to Antigravity CLI", "https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/", ["antigravity-cli", "gemini-cli"], source_type="official_announcement", purpose="lifecycle_reference", cadence="weekly"),
    source("src.gemini.releases", "Gemini CLI GitHub releases", "https://github.com/google-gemini/gemini-cli/releases", ["gemini-cli"], source_type="github_releases", purpose="release_history", collector={"kind": "github_releases", "repo": "google-gemini/gemini-cli"}, cadence="daily"),
    source("src.gemini.repo", "Gemini CLI repository", "https://github.com/google-gemini/gemini-cli", ["gemini-cli"], source_type="repository", purpose="capability_reference"),
    source("src.gemini.docs", "Gemini CLI documentation", "https://geminicli.com/docs/", ["gemini-cli"], source_type="documentation", purpose="capability_reference"),
    source("src.gemini.transition", "Gemini CLI transition discussion", "https://github.com/google-gemini/gemini-cli/discussions/27274", ["gemini-cli", "antigravity-cli"], source_type="official_announcement", purpose="lifecycle_reference", cadence="weekly"),
    # Qwen, Goose, Copilot, Pi
    source("src.qwen.releases", "Qwen Code GitHub releases", "https://github.com/QwenLM/qwen-code/releases", ["qwen-code"], source_type="github_releases", purpose="release_history", collector={"kind": "github_releases", "repo": "QwenLM/qwen-code"}, cadence="six_hourly"),
    source("src.qwen.repo", "Qwen Code repository", "https://github.com/QwenLM/qwen-code", ["qwen-code"], source_type="repository", purpose="capability_reference"),
    source("src.qwen.docs", "Qwen Code documentation", "https://qwenlm.github.io/qwen-code-docs/en/users/overview", ["qwen-code"], source_type="documentation", purpose="capability_reference"),
    source("src.goose.releases", "goose GitHub releases", "https://github.com/block/goose/releases", ["goose"], source_type="github_releases", purpose="release_history", collector={"kind": "github_releases", "repo": "block/goose"}, cadence="daily"),
    source("src.goose.repo", "goose repository", "https://github.com/block/goose", ["goose"], source_type="repository", purpose="capability_reference"),
    source("src.goose.docs", "goose documentation", "https://block.github.io/goose/", ["goose"], source_type="documentation", purpose="capability_reference"),
    source("src.copilot-cli.releases", "GitHub Copilot CLI releases", "https://github.com/github/copilot-cli/releases", ["github-copilot-cli"], source_type="github_releases", purpose="release_history", collector={"kind": "github_releases", "repo": "github/copilot-cli"}, cadence="daily"),
    source("src.copilot-cli.docs", "GitHub Copilot CLI documentation", "https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli", ["github-copilot-cli"], source_type="documentation", purpose="capability_reference"),
    source("src.pi.repo", "Pi Agent Harness repository", "https://github.com/earendil-works/pi", ["pi-agent"], source_type="repository", purpose="capability_reference"),
    source("src.pi.releases", "Pi Agent Harness releases", "https://github.com/earendil-works/pi/releases", ["pi-agent"], source_type="github_releases", purpose="release_history", collector={"kind": "github_releases", "repo": "earendil-works/pi"}, cadence="daily"),
    # External official comparison source
    source("src.github-agentic-workflows.engine-matrix", "GitHub Agentic Workflows engine comparison", "https://github.github.com/gh-aw/reference/engines/", ["claude-code", "openai-codex", "gemini-cli", "github-copilot-cli", "pi-agent", "opencode"], source_type="official_secondary_matrix", purpose="comparison_reference", authority="official_secondary", cadence="daily", notes="Useful as a normalized secondary source for GitHub Actions compatibility, not as canonical product capability truth."),
    # Claude Agent SDKs
    source("src.claude-agent-sdk-python.changelog", "Claude Agent SDK Python changelog", "https://raw.githubusercontent.com/anthropics/claude-agent-sdk-python/main/CHANGELOG.md", ["claude-agent-sdk-python"], source_type="markdown_changelog", purpose="release_history", collector={"kind": "markdown_changelog", "local_seed_path": "raw/claude-agent-sdk-python/CHANGELOG.md", "max_dateless_releases": 110}, cadence="six_hourly"),
    source("src.claude-agent-sdk-python.releases", "Claude Agent SDK Python releases", "https://github.com/anthropics/claude-agent-sdk-python/releases", ["claude-agent-sdk-python"], source_type="github_releases", purpose="release_history", collector={"kind": "github_releases", "repo": "anthropics/claude-agent-sdk-python"}, cadence="six_hourly"),
    source("src.claude-agent-sdk-typescript.changelog", "Claude Agent SDK TypeScript changelog", "https://raw.githubusercontent.com/anthropics/claude-agent-sdk-typescript/main/CHANGELOG.md", ["claude-agent-sdk-typescript"], source_type="markdown_changelog", purpose="release_history", collector={"kind": "markdown_changelog", "local_seed_path": "raw/claude-agent-sdk-typescript/CHANGELOG.md", "max_dateless_releases": 110}, cadence="six_hourly"),
    source("src.claude-agent-sdk-typescript.releases", "Claude Agent SDK TypeScript releases", "https://github.com/anthropics/claude-agent-sdk-typescript/releases", ["claude-agent-sdk-typescript"], source_type="github_releases", purpose="release_history", collector={"kind": "github_releases", "repo": "anthropics/claude-agent-sdk-typescript"}, cadence="six_hourly"),
    # Codex SDK and OpenAI Agents SDK
    source("src.codex-sdk-python.releases", "Codex Python SDK releases", "https://pypi.org/project/openai-codex/", ["codex-sdk-python"], source_type="package_registry", purpose="release_history", collector={"kind": "pypi", "package": "openai-codex"}, cadence="six_hourly"),
    source("src.codex-sdk-typescript.releases", "Codex TypeScript SDK releases", "https://www.npmjs.com/package/@openai/codex-sdk", ["codex-sdk-typescript"], source_type="package_registry", purpose="release_history", collector={"kind": "npm", "package": "@openai/codex-sdk"}, cadence="six_hourly"),
    source("src.openai-agents-python.releases", "OpenAI Agents SDK Python releases", "https://github.com/openai/openai-agents-python/releases", ["openai-agents-sdk-python"], source_type="github_releases", purpose="release_history", collector={"kind": "github_releases", "repo": "openai/openai-agents-python"}, cadence="six_hourly"),
    source("src.openai-agents-python.docs", "OpenAI Agents SDK Python docs", "https://openai.github.io/openai-agents-python/", ["openai-agents-sdk-python"], source_type="documentation", purpose="capability_reference"),
    source("src.openai-agents-js.releases", "OpenAI Agents SDK JavaScript releases", "https://github.com/openai/openai-agents-js/releases", ["openai-agents-sdk-js"], source_type="github_releases", purpose="release_history", collector={"kind": "github_releases", "repo": "openai/openai-agents-js"}, cadence="six_hourly"),
    source("src.openai-agents-js.docs", "OpenAI Agents SDK JavaScript docs", "https://openai.github.io/openai-agents-js/", ["openai-agents-sdk-js"], source_type="documentation", purpose="capability_reference"),
    # Provider SDKs
    source("src.openai-python.changelog", "OpenAI Python SDK changelog", "https://raw.githubusercontent.com/openai/openai-python/main/CHANGELOG.md", ["openai-python-sdk"], source_type="markdown_changelog", purpose="release_history", collector={"kind": "markdown_changelog", "local_seed_path": "raw/openai-python/CHANGELOG.md"}, cadence="daily"),
    source("src.openai-node.changelog", "OpenAI Node SDK changelog", "https://raw.githubusercontent.com/openai/openai-node/master/CHANGELOG.md", ["openai-node-sdk"], source_type="markdown_changelog", purpose="release_history", collector={"kind": "markdown_changelog", "local_seed_path": "raw/openai-node/CHANGELOG.md"}, cadence="daily"),
    source("src.anthropic-python.changelog", "Anthropic Python SDK changelog", "https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/CHANGELOG.md", ["anthropic-python-sdk"], source_type="markdown_changelog", purpose="release_history", collector={"kind": "markdown_changelog", "local_seed_path": "raw/anthropic-sdk-python/CHANGELOG.md"}, cadence="daily"),
    source("src.anthropic-typescript.changelog", "Anthropic TypeScript SDK changelog", "https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/CHANGELOG.md", ["anthropic-typescript-sdk"], source_type="markdown_changelog", purpose="release_history", collector={"kind": "markdown_changelog", "local_seed_path": "raw/anthropic-sdk-typescript/CHANGELOG.md"}, cadence="daily"),
]


def harness(
    id: str,
    name: str,
    vendor: str,
    family: str,
    lifecycle: str,
    *,
    current_version: str | None,
    maturity: str,
    priority: str,
    source_ids: list[str],
    repo_url: str | None = None,
    docs_url: str | None = None,
    predecessor: str | None = None,
    successor: str | None = None,
    surfaces: list[str] | None = None,
    auth_modes: list[str] | None = None,
    recommended_when: list[str] | None = None,
    avoid_when: list[str] | None = None,
    dimensions: dict[str, str] | None = None,
    lifecycle_events: list[dict[str, Any]] | None = None,
    notes: str | None = None,
) -> dict[str, Any]:
    return {
        "id": id,
        "name": name,
        "vendor": vendor,
        "family": family,
        "lifecycle": lifecycle,
        "maturity": maturity,
        "tracking_priority": priority,
        "current_version": current_version,
        "version_as_of": TODAY,
        "last_verified_at": VERIFIED_AT,
        "predecessor": predecessor,
        "successor": successor,
        "repo_url": repo_url,
        "docs_url": docs_url,
        "surfaces": surfaces or [],
        "auth_modes": auth_modes or [],
        "source_ids": source_ids,
        "recommended_when": recommended_when or [],
        "avoid_when": avoid_when or [],
        "control_plane_dimensions": dimensions or {},
        "lifecycle_events": lifecycle_events or [],
        "notes": notes,
    }


harnesses: list[dict[str, Any]] = [
    harness(
        "claude-code", "Claude Code", "Anthropic", "agentic_harness", "active",
        current_version="2.1.226", maturity="stable", priority="core",
        source_ids=[item["id"] for item in sources if "claude-code" in item["harness_ids"]],
        repo_url="https://github.com/anthropics/claude-code", docs_url="https://docs.anthropic.com/en/docs/claude-code/overview",
        surfaces=["terminal", "IDE", "desktop", "web", "mobile_remote", "SDK"],
        auth_modes=["Claude subscription", "Anthropic API key", "Amazon Bedrock", "Google Vertex AI", "enterprise gateway"],
        recommended_when=["Long-horizon repository work", "Rich skills/hooks/plugins", "Deep subagent orchestration", "Cross-device or self-hosted execution"],
        avoid_when=["A provider-neutral local harness is mandatory", "The workflow cannot tolerate rapid release churn without pinning"],
        dimensions={"local_execution": "strong", "remote_execution": "strong", "multi_agent": "strong", "structured_automation": "strong", "provider_portability": "moderate", "enterprise_controls": "strong"},
    ),
    harness(
        "openai-codex", "OpenAI Codex", "OpenAI", "agentic_harness", "active",
        current_version="0.147.0", maturity="stable", priority="core",
        source_ids=[item["id"] for item in sources if "openai-codex" in item["harness_ids"]],
        repo_url="https://github.com/openai/codex", docs_url="https://developers.openai.com/codex/cli",
        surfaces=["terminal", "IDE", "desktop", "web/cloud", "SDK", "app-server"],
        auth_modes=["ChatGPT sign-in", "OpenAI API key", "managed workspace"],
        recommended_when=["Codex local plus cloud continuity", "Machine-readable app-server integration", "OpenAI model and plugin ecosystem", "GitHub Action automation"],
        avoid_when=["You require broad model-provider portability inside the same harness"],
        dimensions={"local_execution": "strong", "remote_execution": "strong", "multi_agent": "strong", "structured_automation": "strong", "provider_portability": "limited", "enterprise_controls": "strong"},
    ),
    harness(
        "opencode", "OpenCode", "Anomaly", "agentic_harness", "active",
        current_version="1.18.15", maturity="stable", priority="core",
        source_ids=[item["id"] for item in sources if "opencode" in item["harness_ids"]],
        repo_url="https://github.com/anomalyco/opencode", docs_url="https://opencode.ai/docs/",
        surfaces=["terminal", "desktop", "IDE"], auth_modes=["provider API keys", "GitHub Copilot account", "ChatGPT subscription"],
        recommended_when=["Open-source and multi-provider operation", "Parallel local sessions", "LSP-aware coding", "Portable Agent Skills"],
        avoid_when=["You need a mature enterprise policy plane supplied by the harness vendor"],
        dimensions={"local_execution": "strong", "remote_execution": "moderate", "multi_agent": "moderate", "structured_automation": "moderate", "provider_portability": "strong", "enterprise_controls": "limited"},
    ),
    harness(
        "hermes-agent", "Hermes Agent", "Nous Research", "general_agent_harness", "active",
        current_version="0.20.0", maturity="rapidly_evolving", priority="core",
        source_ids=[item["id"] for item in sources if "hermes-agent" in item["harness_ids"]],
        repo_url="https://github.com/NousResearch/hermes-agent", docs_url="https://hermes-agent.nousresearch.com/",
        surfaces=["terminal/TUI", "desktop", "messaging gateway", "voice"], auth_modes=["Nous Portal", "provider API keys", "self-hosted models"],
        recommended_when=["Persistent personal-agent memory", "Self-improving skill creation", "Voice and messaging gateways", "Provider-neutral general agent workflows"],
        avoid_when=["You need conservative release management without pinning", "You need an enterprise support contract from a major platform vendor"],
        dimensions={"local_execution": "strong", "remote_execution": "strong", "multi_agent": "strong", "structured_automation": "moderate", "provider_portability": "strong", "enterprise_controls": "emerging"},
    ),
    harness(
        "antigravity-cli", "Antigravity CLI", "Google", "agentic_harness", "active",
        current_version="1.1.11", maturity="stable", priority="core",
        source_ids=[item["id"] for item in sources if "antigravity-cli" in item["harness_ids"]],
        repo_url="https://github.com/google-antigravity/antigravity-cli", docs_url="https://antigravity.google/",
        predecessor="gemini-cli", surfaces=["terminal", "Antigravity desktop", "SDK"],
        auth_modes=["Google AI account", "Google Cloud project", "Gemini Enterprise", "Workforce Identity Federation", "Application Default Credentials"],
        recommended_when=["Google Antigravity multi-agent backend", "Background orchestration", "Structured print-mode automation", "Google enterprise identity"],
        avoid_when=["You need compatibility with Gemini CLI behavior without migration testing"],
        dimensions={"local_execution": "strong", "remote_execution": "strong", "multi_agent": "strong", "structured_automation": "strong", "provider_portability": "limited", "enterprise_controls": "strong"},
        lifecycle_events=[{"date": "2026-05-19", "type": "product_launch", "summary": "Google announced Antigravity CLI as the successor terminal experience to Gemini CLI."}],
    ),
    harness(
        "gemini-cli", "Gemini CLI", "Google", "agentic_harness", "legacy",
        current_version="0.56.0-nightly.20260808.gcf22ac7e8", maturity="legacy_for_individuals", priority="historical",
        source_ids=[item["id"] for item in sources if "gemini-cli" in item["harness_ids"]],
        repo_url="https://github.com/google-gemini/gemini-cli", docs_url="https://geminicli.com/docs/", successor="antigravity-cli",
        surfaces=["terminal", "IDE integration"], auth_modes=["API key", "enterprise license", "legacy individual sign-in"],
        recommended_when=["Historical compatibility analysis", "Enterprise or API-key deployments that remain supported"],
        avoid_when=["New individual-user workflows; migrate to Antigravity CLI"],
        dimensions={"local_execution": "strong", "remote_execution": "limited", "multi_agent": "moderate", "structured_automation": "strong", "provider_portability": "limited", "enterprise_controls": "moderate"},
        lifecycle_events=[
            {"date": "2026-05-19", "type": "transition_announced", "summary": "Google announced migration to Antigravity CLI."},
            {"date": "2026-06-18", "type": "individual_service_end", "summary": "Gemini CLI stopped serving free, Google AI Pro, and Google AI Ultra individual accounts; enterprise and API-key paths remained."},
        ],
    ),
    harness(
        "qwen-code", "Qwen Code", "Alibaba / Qwen", "agentic_harness", "active",
        current_version="0.21.8", maturity="stable", priority="secondary",
        source_ids=[item["id"] for item in sources if "qwen-code" in item["harness_ids"]],
        repo_url="https://github.com/QwenLM/qwen-code", docs_url="https://qwenlm.github.io/qwen-code-docs/en/users/overview",
        surfaces=["terminal", "desktop"], auth_modes=["Qwen", "OpenAI-compatible", "Anthropic", "Gemini APIs"],
        recommended_when=["Open-source terminal agent with broad provider support", "Qwen-native workflows"],
        avoid_when=["You need the deepest enterprise governance controls from the harness itself"],
        dimensions={"local_execution": "strong", "remote_execution": "moderate", "multi_agent": "moderate", "structured_automation": "moderate", "provider_portability": "strong", "enterprise_controls": "limited"},
    ),
    harness(
        "goose", "goose", "Block", "general_agent_harness", "active",
        current_version=None, maturity="stable", priority="secondary",
        source_ids=[item["id"] for item in sources if "goose" in item["harness_ids"]],
        repo_url="https://github.com/block/goose", docs_url="https://block.github.io/goose/",
        surfaces=["CLI", "desktop", "server/API"], auth_modes=["multiple provider APIs", "local models"],
        recommended_when=["Open-source extensible agent beyond coding", "MCP-first integrations", "Provider-neutral local operation"],
        avoid_when=["You require a canonical managed cloud execution plane"],
        dimensions={"local_execution": "strong", "remote_execution": "moderate", "multi_agent": "moderate", "structured_automation": "strong", "provider_portability": "strong", "enterprise_controls": "emerging"},
    ),
    harness(
        "github-copilot-cli", "GitHub Copilot CLI", "GitHub", "agentic_harness", "active",
        current_version=None, maturity="stable", priority="secondary",
        source_ids=[item["id"] for item in sources if "github-copilot-cli" in item["harness_ids"]],
        repo_url="https://github.com/github/copilot-cli", docs_url="https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli",
        surfaces=["terminal", "GitHub Agentic Workflows"], auth_modes=["GitHub Copilot entitlement", "GitHub token"],
        recommended_when=["GitHub-native automation", "Broad GitHub Agentic Workflows feature support"],
        avoid_when=["Non-GitHub environments are the primary control plane"],
        dimensions={"local_execution": "strong", "remote_execution": "strong", "multi_agent": "moderate", "structured_automation": "strong", "provider_portability": "moderate", "enterprise_controls": "strong"},
    ),
    harness(
        "pi-agent", "Pi Agent Harness", "Earendil Works", "agentic_harness", "active",
        current_version=None, maturity="experimental_to_stable", priority="discovery",
        source_ids=[item["id"] for item in sources if "pi-agent" in item["harness_ids"]],
        repo_url="https://github.com/earendil-works/pi", docs_url="https://github.com/earendil-works/pi",
        surfaces=["terminal", "library/runtime"], auth_modes=["multiple provider APIs"],
        recommended_when=["Minimal self-extensible harness", "Provider-neutral agent runtime experiments"],
        avoid_when=["You need a fully managed enterprise product"],
        dimensions={"local_execution": "strong", "remote_execution": "limited", "multi_agent": "moderate", "structured_automation": "moderate", "provider_portability": "strong", "enterprise_controls": "limited"},
    ),
    # Agent SDKs
    harness("claude-agent-sdk-python", "Claude Agent SDK — Python", "Anthropic", "agent_sdk", "active", current_version="0.2.134", maturity="stable", priority="core", source_ids=[item["id"] for item in sources if "claude-agent-sdk-python" in item["harness_ids"]], repo_url="https://github.com/anthropics/claude-agent-sdk-python", docs_url="https://docs.anthropic.com/en/docs/claude-code/sdk", surfaces=["Python library", "bundled Claude Code runtime"], auth_modes=["Anthropic API", "Bedrock", "Vertex"], recommended_when=["Embedding the Claude Code agent loop in Python applications"], dimensions={"structured_automation": "strong", "multi_agent": "strong", "provider_portability": "moderate", "enterprise_controls": "strong"}),
    harness("claude-agent-sdk-typescript", "Claude Agent SDK — TypeScript", "Anthropic", "agent_sdk", "active", current_version="0.3.226", maturity="stable", priority="core", source_ids=[item["id"] for item in sources if "claude-agent-sdk-typescript" in item["harness_ids"]], repo_url="https://github.com/anthropics/claude-agent-sdk-typescript", docs_url="https://docs.anthropic.com/en/docs/claude-code/sdk", surfaces=["TypeScript library", "bundled Claude Code runtime"], auth_modes=["Anthropic API", "Bedrock", "Vertex"], recommended_when=["Embedding the Claude Code agent loop in TypeScript applications"], dimensions={"structured_automation": "strong", "multi_agent": "strong", "provider_portability": "moderate", "enterprise_controls": "strong"}),
    harness("codex-sdk-python", "Codex SDK — Python", "OpenAI", "agent_sdk", "active", current_version="0.144.4", maturity="stable", priority="core", source_ids=[item["id"] for item in sources if "codex-sdk-python" in item["harness_ids"]], repo_url="https://github.com/openai/codex", docs_url="https://developers.openai.com/codex/codex-sdk", surfaces=["Python library", "local app-server JSON-RPC"], auth_modes=["ChatGPT sign-in", "OpenAI API key"], recommended_when=["Programmatic control of the local Codex app-server from Python"], dimensions={"structured_automation": "strong", "multi_agent": "strong", "provider_portability": "limited", "enterprise_controls": "strong"}),
    harness("codex-sdk-typescript", "Codex SDK — TypeScript", "OpenAI", "agent_sdk", "active", current_version="0.146.0", maturity="stable", priority="core", source_ids=[item["id"] for item in sources if "codex-sdk-typescript" in item["harness_ids"]], repo_url="https://github.com/openai/codex/tree/main/sdk/typescript", docs_url="https://developers.openai.com/codex/codex-sdk", surfaces=["TypeScript library", "CLI JSONL transport"], auth_modes=["ChatGPT sign-in", "OpenAI API key"], recommended_when=["Embedding local Codex threads in server-side Node.js applications and CI"], avoid_when=["You need the richer JSON-RPC app-server surface exposed by the Python SDK"], dimensions={"structured_automation": "strong", "multi_agent": "moderate", "provider_portability": "limited", "enterprise_controls": "strong"}),
    harness("openai-agents-sdk-python", "OpenAI Agents SDK — Python", "OpenAI", "agent_sdk", "active", current_version="0.14.0", maturity="stable", priority="core", source_ids=[item["id"] for item in sources if "openai-agents-sdk-python" in item["harness_ids"]], repo_url="https://github.com/openai/openai-agents-python", docs_url="https://openai.github.io/openai-agents-python/", surfaces=["Python library"], auth_modes=["OpenAI API", "provider-compatible models"], recommended_when=["Building provider-agnostic multi-agent applications with tracing, guardrails, sessions, and handoffs"], dimensions={"structured_automation": "strong", "multi_agent": "strong", "provider_portability": "strong", "enterprise_controls": "strong"}),
    harness("openai-agents-sdk-js", "OpenAI Agents SDK — JavaScript/TypeScript", "OpenAI", "agent_sdk", "active", current_version="0.14.3", maturity="stable", priority="core", source_ids=[item["id"] for item in sources if "openai-agents-sdk-js" in item["harness_ids"]], repo_url="https://github.com/openai/openai-agents-js", docs_url="https://openai.github.io/openai-agents-js/", surfaces=["JavaScript/TypeScript library"], auth_modes=["OpenAI API", "provider-compatible models"], recommended_when=["Building multi-agent JS/TS applications with tracing, guardrails, sessions, and handoffs"], dimensions={"structured_automation": "strong", "multi_agent": "strong", "provider_portability": "strong", "enterprise_controls": "strong"}),
    # Provider SDKs
    harness("openai-python-sdk", "OpenAI API SDK — Python", "OpenAI", "provider_sdk", "active", current_version="2.53.0", maturity="stable", priority="provider_sdk", source_ids=[item["id"] for item in sources if "openai-python-sdk" in item["harness_ids"]], repo_url="https://github.com/openai/openai-python", docs_url="https://github.com/openai/openai-python", surfaces=["Python library"], auth_modes=["OpenAI API key", "Azure/OpenAI-compatible targets"], recommended_when=["Low-level typed OpenAI API access"], dimensions={"structured_automation": "strong", "multi_agent": "application_defined", "provider_portability": "moderate", "enterprise_controls": "strong"}),
    harness("openai-node-sdk", "OpenAI API SDK — Node", "OpenAI", "provider_sdk", "active", current_version=None, maturity="stable", priority="provider_sdk", source_ids=[item["id"] for item in sources if "openai-node-sdk" in item["harness_ids"]], repo_url="https://github.com/openai/openai-node", docs_url="https://github.com/openai/openai-node", surfaces=["JavaScript/TypeScript library"], auth_modes=["OpenAI API key"], recommended_when=["Low-level typed OpenAI API access from JS/TS"], dimensions={"structured_automation": "strong", "multi_agent": "application_defined", "provider_portability": "moderate", "enterprise_controls": "strong"}),
    harness("anthropic-python-sdk", "Claude API SDK — Python", "Anthropic", "provider_sdk", "active", current_version="0.121.0", maturity="stable", priority="provider_sdk", source_ids=[item["id"] for item in sources if "anthropic-python-sdk" in item["harness_ids"]], repo_url="https://github.com/anthropics/anthropic-sdk-python", docs_url="https://platform.claude.com/docs/en/api/sdks/python", surfaces=["Python library"], auth_modes=["Anthropic API", "AWS", "Vertex"], recommended_when=["Low-level typed Claude API and managed-agent access"], dimensions={"structured_automation": "strong", "multi_agent": "application_defined", "provider_portability": "moderate", "enterprise_controls": "strong"}),
    harness("anthropic-typescript-sdk", "Claude API SDK — TypeScript", "Anthropic", "provider_sdk", "active", current_version="0.115.0", maturity="stable", priority="provider_sdk", source_ids=[item["id"] for item in sources if "anthropic-typescript-sdk" in item["harness_ids"]], repo_url="https://github.com/anthropics/anthropic-sdk-typescript", docs_url="https://platform.claude.com/docs/en/api/sdks/typescript", surfaces=["JavaScript/TypeScript library"], auth_modes=["Anthropic API", "AWS", "Vertex"], recommended_when=["Low-level typed Claude API and managed-agent access from JS/TS"], dimensions={"structured_automation": "strong", "multi_agent": "application_defined", "provider_portability": "moderate", "enterprise_controls": "strong"}),
]

# Canonical capability taxonomy. These are comparable concepts, not product marketing labels.
taxonomy: list[dict[str, Any]] = [
    {"id": "interaction.terminal", "name": "Interactive terminal/TUI", "category": "interaction", "definition": "Human-operated conversational terminal interface.", "comparison_question": "Can a human run and steer the harness interactively from a terminal?"},
    {"id": "interaction.ide", "name": "IDE integration", "category": "interaction", "definition": "First-party or supported editor integration.", "comparison_question": "Is the harness available beside the code in an IDE?"},
    {"id": "interaction.desktop_web", "name": "Desktop or web surface", "category": "interaction", "definition": "First-party GUI or browser surface sharing the agent backend or sessions.", "comparison_question": "Can a human manage work through a GUI or browser?"},
    {"id": "execution.file_edit", "name": "Agent-native file editing", "category": "execution", "definition": "The in-harness model can inspect and mutate files through governed tools.", "comparison_question": "Can the model directly edit repository files?"},
    {"id": "execution.shell", "name": "Agent-native shell execution", "category": "execution", "definition": "The in-harness model can invoke shell commands or equivalent execution tools.", "comparison_question": "Can the model run commands?"},
    {"id": "execution.headless", "name": "Headless/non-interactive execution", "category": "execution", "definition": "A supported one-shot or scripted interface without an interactive TUI.", "comparison_question": "Can an external agent or CI runner invoke the harness non-interactively?"},
    {"id": "execution.structured_output", "name": "Machine-readable output", "category": "execution", "definition": "JSON, JSONL, event streams, or schema-constrained result output.", "comparison_question": "Can software reliably parse progress and final results?"},
    {"id": "execution.sdk_embedding", "name": "Embeddable SDK", "category": "execution", "definition": "Supported language SDK exposing the agent loop or harness runtime.", "comparison_question": "Can an application embed/control the harness through a supported SDK?"},
    {"id": "execution.rpc_server", "name": "RPC/app-server protocol", "category": "execution", "definition": "Versioned machine protocol for controlling sessions, turns, and events.", "comparison_question": "Can an orchestrator control the harness through RPC rather than terminal scraping?"},
    {"id": "extensions.mcp_client", "name": "MCP client", "category": "extensions", "definition": "Connects to Model Context Protocol servers for tools or context.", "comparison_question": "Can the harness discover and invoke MCP tools?"},
    {"id": "extensions.skills", "name": "Agent Skills", "category": "extensions", "definition": "Reusable instruction/resource bundles discoverable or invokable by the model.", "comparison_question": "Can reusable skills be installed and used by the agent?"},
    {"id": "extensions.plugins", "name": "Plugins/extensions", "category": "extensions", "definition": "Installable packages that can add tools, skills, hooks, connectors, or UI.", "comparison_question": "Can functionality be packaged and distributed?"},
    {"id": "extensions.hooks", "name": "Lifecycle hooks", "category": "extensions", "definition": "User-defined code or policy at lifecycle events before/after tools, turns, or sessions.", "comparison_question": "Can deterministic automation intercept the agent lifecycle?"},
    {"id": "context.project_instructions", "name": "Hierarchical project instructions", "category": "context_memory", "definition": "Repository- and directory-scoped instruction files loaded automatically.", "comparison_question": "Can projects carry durable, scoped instructions?"},
    {"id": "context.dynamic_injection", "name": "Dynamic context injection", "category": "context_memory", "definition": "Context can be loaded at runtime by hooks, skills, tools, or routing logic.", "comparison_question": "Can context be selected dynamically rather than always preloaded?"},
    {"id": "context.persistent_memory", "name": "Persistent memory", "category": "context_memory", "definition": "Cross-session memory or learned knowledge managed by the harness.", "comparison_question": "Does the harness preserve and retrieve durable memory?"},
    {"id": "sessions.resume_fork", "name": "Resume, fork, and session lineage", "category": "session_state", "definition": "Sessions can be resumed, branched, named, or traced through lineage.", "comparison_question": "Can work continue without rebuilding context?"},
    {"id": "orchestration.subagents", "name": "Subagents/delegation", "category": "orchestration", "definition": "A primary agent can delegate bounded work to child agents.", "comparison_question": "Can the model create or direct subagents?"},
    {"id": "orchestration.parallel_background", "name": "Parallel/background agents", "category": "orchestration", "definition": "Multiple agent tasks can run concurrently or independently in the background.", "comparison_question": "Can long-running work continue without blocking the main session?"},
    {"id": "orchestration.cross_session_messaging", "name": "Cross-session agent messaging", "category": "orchestration", "definition": "Running sessions can discover and send messages to one another.", "comparison_question": "Can separate sessions communicate natively?"},
    {"id": "orchestration.multi_agent_coordination", "name": "First-class multi-agent coordination", "category": "orchestration", "definition": "Coordination primitives beyond simple one-off delegation, such as teams, supervisors, or mixtures.", "comparison_question": "Does the harness provide explicit coordination semantics?"},
    {"id": "runtime.remote_cloud", "name": "Remote/cloud execution", "category": "runtime", "definition": "Tasks or sessions can run remotely and be observed or resumed locally.", "comparison_question": "Can work execute away from the local terminal?"},
    {"id": "runtime.self_hosted", "name": "Self-hosted worker/runtime", "category": "runtime", "definition": "The user can supply machines or containers as governed execution workers.", "comparison_question": "Can remote execution run on user-owned infrastructure?"},
    {"id": "automation.ci", "name": "CI/GitHub automation", "category": "automation", "definition": "Supported integration for CI jobs, pull requests, issues, or repository events.", "comparison_question": "Can the harness run safely in CI?"},
    {"id": "automation.schedules", "name": "Scheduled tasks", "category": "automation", "definition": "The platform can create or run recurring agent tasks.", "comparison_question": "Can agent work be scheduled without a human starting each run?"},
    {"id": "security.sandbox", "name": "Execution sandbox", "category": "security_governance", "definition": "OS/process/filesystem/network isolation for agent actions.", "comparison_question": "Are tool actions isolated from the host?"},
    {"id": "security.permissions", "name": "Granular permissions and approvals", "category": "security_governance", "definition": "Fine-grained allow, deny, prompt, or policy controls for tools and commands.", "comparison_question": "Can operators define what actions require approval?"},
    {"id": "security.enterprise_policy", "name": "Enterprise managed policy", "category": "security_governance", "definition": "Organization-admin controls, managed settings, identity, or policy enforcement.", "comparison_question": "Can administrators centrally govern the harness?"},
    {"id": "observability.usage_cost", "name": "Usage and cost telemetry", "category": "observability", "definition": "Tokens, cache, spend, quotas, or cost signals exposed to humans or software.", "comparison_question": "Can usage and spend be attributed?"},
    {"id": "observability.tracing", "name": "Agent tracing/event telemetry", "category": "observability", "definition": "Structured traces or events for turns, tools, agents, and outcomes.", "comparison_question": "Can executions be observed beyond terminal text?"},
    {"id": "tools.web_research", "name": "Web search/research", "category": "research_tools", "definition": "First-party or supported web search, fetch, grounded research, and citations.", "comparison_question": "Can the agent gather current web evidence?"},
    {"id": "tools.browser_computer", "name": "Browser/computer use", "category": "research_tools", "definition": "The agent can operate a browser or computer UI through supported tools.", "comparison_question": "Can the agent act through graphical applications?"},
    {"id": "interfaces.voice", "name": "Voice interaction", "category": "interfaces", "definition": "Streaming speech input/output and conversational interruption support.", "comparison_question": "Can a human operate the agent by voice?"},
    {"id": "interfaces.artifacts", "name": "Artifacts, diffs, and rich result views", "category": "interfaces", "definition": "Structured visual artifacts, diff inspection, or rich result viewers.", "comparison_question": "Can users inspect results beyond plain text?"},
    {"id": "models.provider_portability", "name": "Model/provider portability", "category": "models_providers", "definition": "Multiple model providers can be selected without replacing the harness.", "comparison_question": "Can the same harness operate across providers?"},
    {"id": "models.reasoning_control", "name": "Model and reasoning controls", "category": "models_providers", "definition": "Model selection, effort, context-window, or routing controls exposed explicitly.", "comparison_question": "Can workflows pin and tune model behavior?"},
    {"id": "evaluation.schema_enforcement", "name": "Output schema enforcement", "category": "evaluation", "definition": "A JSON schema or equivalent can constrain the final output contract.", "comparison_question": "Can downstream automation rely on a validated result shape?"},
    {"id": "governance.human_approval_api", "name": "Programmatic human approval", "category": "security_governance", "definition": "Approval decisions can be intercepted or supplied through a supported API/callback.", "comparison_question": "Can an application mediate risky actions rather than relying on terminal prompts?"},
]

SOURCE_URL = {item["id"]: item["url"] for item in sources}


def cap(
    harness_id: str,
    capability_id: str,
    summary: str,
    *,
    source_id: str,
    status: str = "stable",
    confidence: str = "verified_official",
    actors: dict[str, str] | None = None,
    surfaces: list[str] | None = None,
    invocation: list[str] | None = None,
    minimum_version: str | None = None,
    limitations: list[str] | None = None,
    requires_human: bool = False,
    claim: str | None = None,
) -> dict[str, Any]:
    return {
        "id": f"impl.{harness_id}.{capability_id}",
        "harness_id": harness_id,
        "capability_id": capability_id,
        "status": status,
        "summary": summary,
        "actor_access": actors or {
            "human_operator": "supported",
            "in_harness_agent": "supported",
            "external_orchestrator": "unknown",
            "ci_runner": "unknown",
            "administrator": "configurable",
        },
        "requires_human_mediation": requires_human,
        "surfaces": surfaces or [],
        "invocation": invocation or [],
        "minimum_version": minimum_version,
        "current_version_verified": next((item.get("current_version") for item in harnesses if item["id"] == harness_id), None),
        "limitations": limitations or [],
        "confidence": confidence,
        "verified_at": VERIFIED_AT,
        "evidence": [
            {
                "source_id": source_id,
                "url": SOURCE_URL[source_id],
                "claim": claim or summary,
                "version": minimum_version,
                "verified_at": VERIFIED_AT,
            }
        ],
    }


HUMAN_UI = {"human_operator": "native", "in_harness_agent": "unavailable", "external_orchestrator": "unavailable", "ci_runner": "unavailable", "administrator": "configurable"}
AGENT_TOOL = {"human_operator": "supported", "in_harness_agent": "native", "external_orchestrator": "supported", "ci_runner": "supported", "administrator": "configurable"}
HEADLESS = {"human_operator": "supported", "in_harness_agent": "unavailable", "external_orchestrator": "native", "ci_runner": "native", "administrator": "configurable"}
EXTENSION = {"human_operator": "configurable", "in_harness_agent": "native", "external_orchestrator": "supported", "ci_runner": "supported", "administrator": "configurable"}
ADMIN = {"human_operator": "mediated", "in_harness_agent": "mediated", "external_orchestrator": "mediated", "ci_runner": "mediated", "administrator": "native"}
SDK = {"human_operator": "supported", "in_harness_agent": "unavailable", "external_orchestrator": "native", "ci_runner": "native", "administrator": "configurable"}

capabilities: list[dict[str, Any]] = []

def add(*items: dict[str, Any]) -> None:
    capabilities.extend(items)

# Claude Code
add(
    cap("claude-code", "interaction.terminal", "Interactive terminal agent with slash commands, session controls, and tool approvals.", source_id="src.claude-code.docs.overview", actors=HUMAN_UI, surfaces=["terminal"], invocation=["claude"]),
    cap("claude-code", "interaction.ide", "First-party IDE integration, including VS Code surfaces tracked in the changelog.", source_id="src.claude-code.docs.overview", actors=HUMAN_UI, surfaces=["VS Code", "IDE"]),
    cap("claude-code", "interaction.desktop_web", "Claude Code sessions are available through desktop and browser surfaces and can attach through Remote Control.", source_id="src.claude-code.docs.overview", actors=HUMAN_UI, surfaces=["desktop", "web", "mobile"]),
    cap("claude-code", "execution.file_edit", "Claude can read and edit repository files through native tools.", source_id="src.claude-code.docs.overview", actors=AGENT_TOOL, surfaces=["terminal", "IDE", "SDK"]),
    cap("claude-code", "execution.shell", "Claude can run shell commands with configurable permission modes and sandbox controls.", source_id="src.claude-code.docs.cli", actors=AGENT_TOOL, surfaces=["terminal", "SDK"], invocation=["Bash tool"]),
    cap("claude-code", "execution.headless", "`claude -p` provides supported non-interactive execution for scripts and CI; `--bare` disables ambient project customization for reproducibility.", source_id="src.claude-code.docs.headless", actors=HEADLESS, surfaces=["CLI", "stdin/stdout"], invocation=["claude -p", "claude -p --bare"]),
    cap("claude-code", "execution.structured_output", "Headless execution supports machine-readable JSON and streaming event output.", source_id="src.claude-code.docs.headless", actors=HEADLESS, surfaces=["CLI", "JSON", "stream JSON"], invocation=["--output-format json", "--output-format stream-json"]),
    cap("claude-code", "execution.sdk_embedding", "The Claude Agent SDK exposes the same agent loop, tools, and context management as Claude Code in Python and TypeScript.", source_id="src.claude-code.docs.sdk", actors=SDK, surfaces=["Python SDK", "TypeScript SDK"]),
    cap("claude-code", "extensions.mcp_client", "Claude Code connects to local and remote MCP servers and supports OAuth-backed tools.", source_id="src.claude-code.docs.settings", actors=EXTENSION, surfaces=["terminal", "SDK", "plugins"], invocation=[".mcp.json", "plugin MCP servers"]),
    cap("claude-code", "extensions.skills", "SKILL.md bundles can be selected by Claude or invoked explicitly; Claude Code extends the Agent Skills standard with invocation controls and subagent execution.", source_id="src.claude-code.docs.skills", actors=EXTENSION, surfaces=["terminal", "plugins"], invocation=["/skill-name", ".claude/skills/*/SKILL.md"]),
    cap("claude-code", "extensions.plugins", "Plugins distribute skills, agents, hooks, and MCP servers through project/user configuration and marketplaces.", source_id="src.claude-code.docs.settings", actors=EXTENSION, surfaces=["marketplaces", "archive source"], invocation=["plugin install", "settings.json"]),
    cap("claude-code", "extensions.hooks", "Hooks execute code at lifecycle events to inject context, enforce policy, format files, or notify humans.", source_id="src.claude-code.docs.hooks", actors={"human_operator": "configurable", "in_harness_agent": "mediated", "external_orchestrator": "supported", "ci_runner": "supported", "administrator": "configurable"}, surfaces=["settings", "agents", "skills"], invocation=["PreToolUse", "PostToolUse", "Stop", "SessionStart"]),
    cap("claude-code", "context.project_instructions", "CLAUDE.md and scoped configuration provide durable project instructions.", source_id="src.claude-code.docs.skills", actors=EXTENSION, surfaces=["project", "user", "managed"]),
    cap("claude-code", "context.dynamic_injection", "Skills, hooks, and MCP tools can inject context only when relevant.", source_id="src.claude-code.docs.skills", actors=EXTENSION, surfaces=["skills", "hooks", "MCP"]),
    cap("claude-code", "context.persistent_memory", "Auto memory and project memory preserve selected knowledge across sessions.", source_id="src.claude-code.docs.headless", actors={"human_operator": "configurable", "in_harness_agent": "native", "external_orchestrator": "supported", "ci_runner": "mediated", "administrator": "configurable"}, surfaces=["auto memory", "CLAUDE.md"], limitations=["Bare mode intentionally skips auto memory and CLAUDE.md."]),
    cap("claude-code", "sessions.resume_fork", "Sessions can be resumed, continued, renamed, forked, and moved between local/cloud contexts.", source_id="src.claude-code.docs.cli", actors={"human_operator": "native", "in_harness_agent": "mediated", "external_orchestrator": "supported", "ci_runner": "supported", "administrator": "configurable"}, surfaces=["CLI", "Remote Control"], invocation=["--resume", "--continue", "/resume"]),
    cap("claude-code", "orchestration.subagents", "Claude can delegate work to defined or dynamic subagents with separate prompts and tool restrictions.", source_id="src.claude-code.docs.skills", actors={"human_operator": "supported", "in_harness_agent": "native", "external_orchestrator": "supported", "ci_runner": "supported", "administrator": "configurable"}, surfaces=["agents", "skills", "SDK"]),
    cap("claude-code", "orchestration.parallel_background", "Subagents and forked skills can run in the background with concurrency and spawn-depth controls.", source_id="src.claude-code.changelog", actors={"human_operator": "supported", "in_harness_agent": "native", "external_orchestrator": "supported", "ci_runner": "supported", "administrator": "configurable"}, surfaces=["terminal", "SDK"], minimum_version="2.1.218"),
    cap("claude-code", "orchestration.cross_session_messaging", "Running sessions can discover one another with ListAgents and exchange messages with SendMessage across machines.", source_id="src.claude-code.changelog", actors={"human_operator": "supported", "in_harness_agent": "native", "external_orchestrator": "supported", "ci_runner": "supported", "administrator": "configurable"}, surfaces=["local sessions", "Remote Control"], invocation=["ListAgents", "SendMessage"], minimum_version="2.1.224"),
    cap("claude-code", "orchestration.multi_agent_coordination", "Agent teams, nested subagents, and cross-session messaging provide explicit coordination primitives.", source_id="src.claude-code.changelog", actors={"human_operator": "supported", "in_harness_agent": "native", "external_orchestrator": "supported", "ci_runner": "supported", "administrator": "configurable"}, surfaces=["agents", "teams", "sessions"], status="experimental", minimum_version="2.1.219"),
    cap("claude-code", "runtime.remote_cloud", "Remote Control and cloud sessions let work continue across terminal, web, desktop, and mobile surfaces.", source_id="src.claude-code.changelog", actors={"human_operator": "native", "in_harness_agent": "mediated", "external_orchestrator": "supported", "ci_runner": "supported", "administrator": "configurable"}, surfaces=["Remote Control", "web", "desktop", "mobile"]),
    cap("claude-code", "runtime.self_hosted", "`claude self-hosted-runner` registers user-owned machines or containers as execution environments for web/mobile/desktop sessions.", source_id="src.claude-code.changelog", actors={"human_operator": "configurable", "in_harness_agent": "mediated", "external_orchestrator": "supported", "ci_runner": "supported", "administrator": "native"}, surfaces=["self-hosted worker"], invocation=["claude self-hosted-runner"], minimum_version="2.1.224"),
    cap("claude-code", "automation.ci", "Headless mode and the Agent SDK support CI, batch, and scripted workflows.", source_id="src.claude-code.docs.headless", actors=HEADLESS, surfaces=["CI", "shell pipelines"]),
    cap("claude-code", "automation.schedules", "Workflow and scheduled-task primitives are present, but coverage is less mature than headless execution.", source_id="src.claude-code.changelog", actors={"human_operator": "configurable", "in_harness_agent": "supported", "external_orchestrator": "supported", "ci_runner": "native", "administrator": "configurable"}, status="experimental", confidence="inferred_high", surfaces=["workflows", "scheduled tasks"], limitations=["Verify exact schedule semantics for the pinned version before relying on them."]),
    cap("claude-code", "security.sandbox", "Filesystem and network sandbox controls constrain tool execution, including credential masking and TLS termination options.", source_id="src.claude-code.changelog", actors={"human_operator": "configurable", "in_harness_agent": "mediated", "external_orchestrator": "supported", "ci_runner": "supported", "administrator": "native"}, surfaces=["filesystem sandbox", "network sandbox"], minimum_version="2.1.224"),
    cap("claude-code", "security.permissions", "Permission modes, allow/deny rules, workspace trust, and approval hooks govern agent actions.", source_id="src.claude-code.docs.cli", actors={"human_operator": "native", "in_harness_agent": "mediated", "external_orchestrator": "supported", "ci_runner": "supported", "administrator": "native"}, surfaces=["CLI flags", "settings", "hooks"]),
    cap("claude-code", "security.enterprise_policy", "Managed settings and organization policies govern marketplaces, permissions, telemetry, and environment behavior.", source_id="src.claude-code.docs.settings", actors=ADMIN, surfaces=["managed settings", "MDM", "organization gateway"]),
    cap("claude-code", "observability.usage_cost", "Usage, token, budget, spend-limit, and model-usage signals are exposed in CLI/SDK paths.", source_id="src.claude-code.changelog", actors={"human_operator": "native", "in_harness_agent": "mediated", "external_orchestrator": "supported", "ci_runner": "supported", "administrator": "native"}, surfaces=["status", "SDK result", "gateway"]),
    cap("claude-code", "observability.tracing", "Headless/SDK event streams and hook events provide structured execution telemetry.", source_id="src.claude-code.docs.sdk", actors=SDK, surfaces=["SDK messages", "stream JSON", "hooks"]),
    cap("claude-code", "tools.web_research", "Built-in deep research is manually invoked; web access can also be supplied through MCP and browser tools.", source_id="src.claude-code.changelog", actors={"human_operator": "native", "in_harness_agent": "mediated", "external_orchestrator": "supported", "ci_runner": "supported", "administrator": "configurable"}, surfaces=["/deep-research", "MCP"], invocation=["/deep-research"], minimum_version="2.1.218", limitations=["The changelog explicitly states Claude does not autonomously start /deep-research."]),
    cap("claude-code", "tools.browser_computer", "Claude-in-Chrome and browser/MCP integrations provide browser interaction.", source_id="src.claude-code.changelog", actors=AGENT_TOOL, surfaces=["Chrome", "MCP"], status="experimental"),
    cap("claude-code", "interfaces.artifacts", "IDE, desktop, web, attachments, diffs, and review flows provide rich result inspection beyond terminal text.", source_id="src.claude-code.changelog", actors=HUMAN_UI, surfaces=["IDE", "web", "desktop", "attachments"]),
    cap("claude-code", "models.provider_portability", "Claude Code supports Anthropic-hosted Claude plus Bedrock, Vertex AI, and enterprise gateways, but remains Claude-model-centric.", source_id="src.claude-code.docs.cli", actors={"human_operator": "configurable", "in_harness_agent": "mediated", "external_orchestrator": "configurable", "ci_runner": "configurable", "administrator": "native"}, surfaces=["Anthropic", "Bedrock", "Vertex", "gateway"], limitations=["This is deployment-provider portability, not arbitrary model-provider portability."]),
    cap("claude-code", "models.reasoning_control", "Model selection, fast mode, context-window enforcement, and subagent model selection are configurable.", source_id="src.claude-code.changelog", actors={"human_operator": "native", "in_harness_agent": "supported", "external_orchestrator": "configurable", "ci_runner": "configurable", "administrator": "native"}, surfaces=["/model", "settings", "SDK"]),
    cap("claude-code", "evaluation.schema_enforcement", "Headless and SDK flows can request structured output contracts for downstream automation.", source_id="src.claude-code.docs.headless", actors=HEADLESS, surfaces=["CLI", "SDK"], confidence="inferred_high"),
    cap("claude-code", "governance.human_approval_api", "SDK permission callbacks and hooks let an embedding application mediate tool use programmatically.", source_id="src.claude-code.docs.sdk", actors={"human_operator": "supported", "in_harness_agent": "mediated", "external_orchestrator": "native", "ci_runner": "supported", "administrator": "configurable"}, surfaces=["SDK callbacks", "hooks"]),
)

# OpenAI Codex
add(
    cap("openai-codex", "interaction.terminal", "Interactive Codex CLI for repository inspection, editing, commands, review, and cloud handoff.", source_id="src.codex.docs.cli", actors=HUMAN_UI, surfaces=["terminal"], invocation=["codex"]),
    cap("openai-codex", "interaction.ide", "Codex is available through an IDE extension sharing core sessions and agent capabilities.", source_id="src.codex.docs.cli", actors=HUMAN_UI, surfaces=["IDE extension"]),
    cap("openai-codex", "interaction.desktop_web", "Codex spans the ChatGPT desktop app and Codex cloud/web surfaces.", source_id="src.codex.docs.cli", actors=HUMAN_UI, surfaces=["desktop", "web/cloud"]),
    cap("openai-codex", "execution.file_edit", "Codex can inspect and edit repository files under sandbox and approval policies.", source_id="src.codex.docs.cli", actors=AGENT_TOOL, surfaces=["CLI", "IDE", "cloud"]),
    cap("openai-codex", "execution.shell", "Codex runs commands within configurable sandbox and approval modes.", source_id="src.codex.docs.security", actors=AGENT_TOOL, surfaces=["CLI", "cloud"]),
    cap("openai-codex", "execution.headless", "`codex exec` is the supported non-interactive interface for scripts and CI.", source_id="src.codex.docs.noninteractive", actors=HEADLESS, surfaces=["CLI", "stdin/stdout"], invocation=["codex exec"]),
    cap("openai-codex", "execution.structured_output", "`codex exec` streams text or JSONL and can resume scripted sessions.", source_id="src.codex.docs.commands", actors=HEADLESS, surfaces=["JSONL", "stdout"], invocation=["codex exec --json"]),
    cap("openai-codex", "execution.sdk_embedding", "Official Python and TypeScript Codex SDKs embed local Codex threads for applications and CI.", source_id="src.codex.docs.sdk", actors=SDK, surfaces=["Python SDK", "TypeScript SDK"]),
    cap("openai-codex", "execution.rpc_server", "Codex app-server exposes version-specific JSON-RPC schemas and event notifications.", source_id="src.codex.docs.app-server", actors=SDK, surfaces=["JSON-RPC"], invocation=["codex app-server", "generate-json-schema"]),
    cap("openai-codex", "extensions.mcp_client", "Local Codex clients connect to local or remote MCP servers and share configuration.", source_id="src.codex.docs.mcp", actors=EXTENSION, surfaces=["CLI", "desktop", "IDE"]),
    cap("openai-codex", "extensions.skills", "Agent Skills package instructions and resources; Codex can select them or invoke them through `$` mentions.", source_id="src.codex.docs.skills", actors=EXTENSION, surfaces=["CLI", "desktop", "plugins"]),
    cap("openai-codex", "extensions.plugins", "Portable plugins can bundle skills and MCP-backed connectors across ChatGPT and Codex surfaces.", source_id="src.codex.docs.skills", actors=EXTENSION, surfaces=["CLI", "desktop", "plugin directory"], minimum_version="0.147.0"),
    cap("openai-codex", "context.project_instructions", "Codex discovers layered AGENTS.md and AGENTS.override.md instructions from global and project scopes.", source_id="src.codex.docs.agents-md", actors=EXTENSION, surfaces=["global", "repository", "directory"]),
    cap("openai-codex", "sessions.resume_fork", "Saved sessions can be resumed, forked, named, and deleted through stable CLI commands.", source_id="src.codex.docs.commands", actors={"human_operator": "native", "in_harness_agent": "mediated", "external_orchestrator": "supported", "ci_runner": "supported", "administrator": "configurable"}, surfaces=["CLI", "app-server"]),
    cap("openai-codex", "orchestration.subagents", "Codex can delegate work to subagents from app, CLI, and IDE sessions and exposes child threads for inspection.", source_id="src.codex.docs.subagents", actors={"human_operator": "supported", "in_harness_agent": "native", "external_orchestrator": "supported", "ci_runner": "supported", "administrator": "configurable"}, surfaces=["app", "CLI", "IDE"]),
    cap("openai-codex", "orchestration.parallel_background", "Codex cloud and local subagent surfaces support parallel/background work.", source_id="src.codex.docs.subagents", actors={"human_operator": "native", "in_harness_agent": "native", "external_orchestrator": "supported", "ci_runner": "supported", "administrator": "configurable"}, surfaces=["cloud", "app", "CLI"]),
    cap("openai-codex", "orchestration.multi_agent_coordination", "The main thread can coordinate multiple subagent threads and collect their results.", source_id="src.codex.docs.subagents", actors={"human_operator": "supported", "in_harness_agent": "native", "external_orchestrator": "supported", "ci_runner": "supported", "administrator": "configurable"}, surfaces=["app", "CLI", "IDE"]),
    cap("openai-codex", "runtime.remote_cloud", "CLI and IDE can hand work to Codex cloud and later inspect or apply results locally.", source_id="src.codex.docs.cli", actors={"human_operator": "native", "in_harness_agent": "mediated", "external_orchestrator": "supported", "ci_runner": "supported", "administrator": "configurable"}, surfaces=["Codex cloud", "CLI", "IDE"]),
    cap("openai-codex", "automation.ci", "The official Codex GitHub Action runs `codex exec` in CI to apply patches or post reviews.", source_id="src.codex.docs.github-action", actors=HEADLESS, surfaces=["GitHub Actions", "CI"]),
    cap("openai-codex", "automation.schedules", "Scheduled tasks are supported through Codex/ChatGPT workflow surfaces; exact availability depends on surface and workspace.", source_id="src.codex.product-changelog", actors={"human_operator": "configurable", "in_harness_agent": "mediated", "external_orchestrator": "supported", "ci_runner": "native", "administrator": "configurable"}, status="experimental", confidence="inferred_high", surfaces=["desktop", "cloud", "CI"], limitations=["Verify workspace/surface availability before relying on it."]),
    cap("openai-codex", "security.sandbox", "Codex provides platform-specific sandbox commands and read-only/workspace-write modes.", source_id="src.codex.docs.security", actors={"human_operator": "configurable", "in_harness_agent": "mediated", "external_orchestrator": "supported", "ci_runner": "supported", "administrator": "native"}, surfaces=["macOS", "Linux", "Windows"]),
    cap("openai-codex", "security.permissions", "Approval policies and permission profiles define when commands can run automatically.", source_id="src.codex.docs.security", actors={"human_operator": "native", "in_harness_agent": "mediated", "external_orchestrator": "supported", "ci_runner": "supported", "administrator": "native"}, surfaces=["CLI", "config.toml", "requirements.toml"]),
    cap("openai-codex", "security.enterprise_policy", "Managed workspace roles, permissions, retention, residency, and authentication policies apply to Codex surfaces.", source_id="src.codex.docs.security", actors=ADMIN, surfaces=["managed ChatGPT workspace", "API organization"]),
    cap("openai-codex", "observability.usage_cost", "Structured outputs and product surfaces expose usage, limits, and model information for attribution.", source_id="src.codex.docs.commands", actors={"human_operator": "native", "in_harness_agent": "mediated", "external_orchestrator": "supported", "ci_runner": "supported", "administrator": "native"}, surfaces=["CLI", "JSONL", "workspace"]),
    cap("openai-codex", "observability.tracing", "App-server notifications and JSONL execution events expose turn and tool lifecycle data.", source_id="src.codex.docs.app-server", actors=SDK, surfaces=["JSON-RPC", "JSONL"]),
    cap("openai-codex", "tools.web_research", "Codex supports opt-in web search and MCP-based external tools.", source_id="src.codex.docs.mcp", actors=AGENT_TOOL, surfaces=["web search", "MCP"]),
    cap("openai-codex", "tools.browser_computer", "Codex models and connected tools can support browser/computer-use workflows depending on model and surface.", source_id="src.codex.product-changelog", actors=AGENT_TOOL, surfaces=["desktop", "web", "MCP"], status="experimental", limitations=["Capability depends on the selected model and enabled tools."]),
    cap("openai-codex", "interfaces.artifacts", "The app, IDE, CLI, and cloud surfaces expose diffs, conversation sections, and task results for review.", source_id="src.codex.docs.cli", actors=HUMAN_UI, surfaces=["app", "IDE", "cloud", "CLI"]),
    cap("openai-codex", "models.provider_portability", "Codex is primarily an OpenAI-model harness; custom API targets do not imply arbitrary provider compatibility.", source_id="src.codex.docs.security", actors={"human_operator": "configurable", "in_harness_agent": "unavailable", "external_orchestrator": "configurable", "ci_runner": "configurable", "administrator": "configurable"}, status="limited", confidence="verified_official", surfaces=["OpenAI", "Bedrock-backed paths"], limitations=["Treat as limited rather than provider-neutral."]),
    cap("openai-codex", "models.reasoning_control", "Model and reasoning effort can be selected through CLI, IDE, app, and configuration.", source_id="src.codex.product-changelog", actors={"human_operator": "native", "in_harness_agent": "supported", "external_orchestrator": "configurable", "ci_runner": "configurable", "administrator": "native"}, surfaces=["/model", "--model", "config.toml"]),
    cap("openai-codex", "governance.human_approval_api", "App-server and SDK clients can mediate approvals through machine interfaces rather than terminal-only prompts.", source_id="src.codex.docs.app-server", actors={"human_operator": "supported", "in_harness_agent": "mediated", "external_orchestrator": "native", "ci_runner": "supported", "administrator": "configurable"}, surfaces=["JSON-RPC", "SDK"]),
)

# OpenCode
add(
    cap("opencode", "interaction.terminal", "OpenCode provides an interactive terminal UI with build and plan agents.", source_id="src.opencode.repo", actors=HUMAN_UI, surfaces=["terminal"], invocation=["opencode"]),
    cap("opencode", "interaction.ide", "OpenCode is available through IDE integration.", source_id="src.opencode.docs.intro", actors=HUMAN_UI, surfaces=["IDE extension"]),
    cap("opencode", "interaction.desktop_web", "OpenCode provides a desktop application and shareable session links.", source_id="src.opencode.docs.intro", actors=HUMAN_UI, surfaces=["desktop", "shared web session"]),
    cap("opencode", "execution.file_edit", "The build agent can edit files while the plan agent is read-only by default.", source_id="src.opencode.repo", actors=AGENT_TOOL, surfaces=["terminal", "desktop", "IDE"]),
    cap("opencode", "execution.shell", "Agents can run commands subject to permission configuration.", source_id="src.opencode.repo", actors=AGENT_TOOL, surfaces=["terminal"]),
    cap("opencode", "execution.headless", "OpenCode supports non-interactive run and GitHub automation modes.", source_id="src.opencode.docs.github", actors=HEADLESS, surfaces=["CLI", "GitHub Actions"], confidence="inferred_high"),
    cap("opencode", "execution.structured_output", "Recent releases added JSON transcript export; automation should distinguish transcript export from a stable live event protocol.", source_id="src.opencode.releases", actors={"human_operator": "supported", "in_harness_agent": "unavailable", "external_orchestrator": "supported", "ci_runner": "supported", "administrator": "configurable"}, surfaces=["JSON transcript"], minimum_version="1.18.15", limitations=["Seed evidence verifies transcript export, not full parity with Codex/Antigravity streaming event protocols."]),
    cap("opencode", "extensions.mcp_client", "OpenCode connects to MCP servers and supports OAuth compatibility improvements.", source_id="src.opencode.releases", actors=EXTENSION, surfaces=["terminal", "desktop"]),
    cap("opencode", "extensions.skills", "OpenCode discovers Agent Skills and exposes them to the model through a native skill tool.", source_id="src.opencode.docs.skills", actors=EXTENSION, surfaces=["SKILL.md", "skill tool"]),
    cap("opencode", "extensions.plugins", "Plugins extend OpenCode with events, tools, authentication, and custom behavior.", source_id="src.opencode.docs.plugins", actors=EXTENSION, surfaces=["plugins"]),
    cap("opencode", "context.project_instructions", "Repository instruction files and agent definitions shape project behavior.", source_id="src.opencode.repo", actors=EXTENSION, surfaces=["AGENTS.md", "agent config"], confidence="inferred_high"),
    cap("opencode", "sessions.resume_fork", "OpenCode persists sessions and supports session navigation, sharing, undo, and reconnect flows.", source_id="src.opencode.docs.intro", actors={"human_operator": "native", "in_harness_agent": "mediated", "external_orchestrator": "supported", "ci_runner": "supported", "administrator": "configurable"}, surfaces=["terminal", "desktop", "share links"]),
    cap("opencode", "orchestration.parallel_background", "Multiple OpenCode sessions can run in parallel against a project.", source_id="src.opencode.docs.intro", actors={"human_operator": "native", "in_harness_agent": "mediated", "external_orchestrator": "supported", "ci_runner": "supported", "administrator": "configurable"}, surfaces=["multi-session"]),
    cap("opencode", "automation.ci", "The OpenCode GitHub agent handles issue and pull-request automation.", source_id="src.opencode.docs.github", actors=HEADLESS, surfaces=["GitHub Actions", "issues", "pull requests"]),
    cap("opencode", "security.permissions", "Build and plan agents carry different default permissions, with configurable command and tool access.", source_id="src.opencode.repo", actors={"human_operator": "native", "in_harness_agent": "mediated", "external_orchestrator": "supported", "ci_runner": "supported", "administrator": "configurable"}, surfaces=["agent definitions", "permission config"]),
    cap("opencode", "tools.web_research", "Web access is available through providers, MCP, and plugins rather than one fixed research subsystem.", source_id="src.opencode.docs.plugins", actors=AGENT_TOOL, surfaces=["MCP", "plugins"], confidence="inferred_high"),
    cap("opencode", "interfaces.artifacts", "Desktop/TUI sessions expose diffs, undo, sharing, and transcript exports.", source_id="src.opencode.docs.intro", actors=HUMAN_UI, surfaces=["desktop", "TUI", "share links"]),
    cap("opencode", "models.provider_portability", "OpenCode is explicitly provider-neutral and supports multiple API providers and subscription-backed authentication paths.", source_id="src.opencode.docs.intro", actors={"human_operator": "native", "in_harness_agent": "mediated", "external_orchestrator": "configurable", "ci_runner": "configurable", "administrator": "configurable"}, surfaces=["multiple providers"]),
    cap("opencode", "models.reasoning_control", "Model/provider selection is configurable per session and agent.", source_id="src.opencode.docs.intro", actors={"human_operator": "native", "in_harness_agent": "supported", "external_orchestrator": "configurable", "ci_runner": "configurable", "administrator": "configurable"}, surfaces=["provider config", "model selector"]),
)

# Hermes Agent
add(
    cap("hermes-agent", "interaction.terminal", "Hermes provides a CLI/TUI with session resume, interruption, and command shortcuts.", source_id="src.hermes.docs.quickstart", actors=HUMAN_UI, surfaces=["CLI", "TUI"], invocation=["hermes"]),
    cap("hermes-agent", "interaction.desktop_web", "Hermes 0.20 introduced desktop artifacts, a plugin SDK, and multi-window operation.", source_id="src.hermes.releases", actors=HUMAN_UI, surfaces=["desktop", "artifacts"], minimum_version="0.20.0"),
    cap("hermes-agent", "execution.file_edit", "Hermes agents can inspect and edit files through built-in and learned tools.", source_id="src.hermes.repo", actors=AGENT_TOOL, surfaces=["CLI", "desktop"]),
    cap("hermes-agent", "execution.shell", "Hermes can execute shell commands, including direct `!` command shortcuts in recent releases.", source_id="src.hermes.releases", actors=AGENT_TOOL, surfaces=["CLI"], invocation=["!<command>"], minimum_version="0.20.0"),
    cap("hermes-agent", "execution.headless", "Hermes can be invoked through CLI/gateway automation, but the seed does not yet verify a stable event protocol equivalent to Codex app-server.", source_id="src.hermes.docs.quickstart", actors=HEADLESS, surfaces=["CLI", "gateway"], confidence="inferred_high"),
    cap("hermes-agent", "extensions.mcp_client", "Hermes supports MCP servers and Docker-based MCP commands.", source_id="src.hermes.releases", actors=EXTENSION, surfaces=["MCP", "Docker"]),
    cap("hermes-agent", "extensions.skills", "Hermes discovers skills progressively and can create or improve them through its learning loop and `/learn` workflow.", source_id="src.hermes.docs.skills", actors=EXTENSION, surfaces=["skills catalog", "/learn"]),
    cap("hermes-agent", "extensions.plugins", "Hermes 0.20 added a desktop plugin SDK and extensibility surfaces.", source_id="src.hermes.releases", actors=EXTENSION, surfaces=["desktop plugin SDK"], minimum_version="0.20.0"),
    cap("hermes-agent", "context.persistent_memory", "Persistent memory and conversation search are first-class parts of Hermes' self-improving agent model.", source_id="src.hermes.docs.memory", actors={"human_operator": "configurable", "in_harness_agent": "native", "external_orchestrator": "supported", "ci_runner": "mediated", "administrator": "configurable"}, surfaces=["memory", "conversation history"]),
    cap("hermes-agent", "sessions.resume_fork", "Hermes persists and resumes sessions across CLI and gateway surfaces.", source_id="src.hermes.docs.quickstart", actors={"human_operator": "native", "in_harness_agent": "mediated", "external_orchestrator": "supported", "ci_runner": "supported", "administrator": "configurable"}, surfaces=["CLI", "gateway"]),
    cap("hermes-agent", "orchestration.subagents", "Hermes can delegate work to specialized agents.", source_id="src.hermes.releases", actors={"human_operator": "supported", "in_harness_agent": "native", "external_orchestrator": "supported", "ci_runner": "supported", "administrator": "configurable"}, surfaces=["CLI", "gateway"]),
    cap("hermes-agent", "orchestration.parallel_background", "Hermes supports background work and Mixture-of-Agents execution.", source_id="src.hermes.releases", actors={"human_operator": "supported", "in_harness_agent": "native", "external_orchestrator": "supported", "ci_runner": "supported", "administrator": "configurable"}, surfaces=["background tasks", "Mixture-of-Agents"], minimum_version="0.18.0"),
    cap("hermes-agent", "orchestration.multi_agent_coordination", "Mixture-of-Agents is a first-class coordination mode rather than only ad hoc subagent prompting.", source_id="src.hermes.releases", actors={"human_operator": "supported", "in_harness_agent": "native", "external_orchestrator": "supported", "ci_runner": "supported", "administrator": "configurable"}, surfaces=["Mixture-of-Agents"], minimum_version="0.18.0"),
    cap("hermes-agent", "runtime.remote_cloud", "Hermes gateways let users interact through messaging channels while work runs on another machine or cloud VM.", source_id="src.hermes.repo", actors={"human_operator": "native", "in_harness_agent": "mediated", "external_orchestrator": "supported", "ci_runner": "supported", "administrator": "configurable"}, surfaces=["Telegram/gateway", "cloud VM"]),
    cap("hermes-agent", "runtime.self_hosted", "Hermes can run on user-owned machines, VPSs, clusters, or serverless infrastructure.", source_id="src.hermes.repo", actors={"human_operator": "configurable", "in_harness_agent": "mediated", "external_orchestrator": "supported", "ci_runner": "supported", "administrator": "native"}, surfaces=["local", "VPS", "cluster", "serverless"]),
    cap("hermes-agent", "automation.schedules", "Hermes includes scheduled and gateway-driven automation paths.", source_id="src.hermes.repo", actors={"human_operator": "configurable", "in_harness_agent": "supported", "external_orchestrator": "supported", "ci_runner": "native", "administrator": "configurable"}, confidence="inferred_high", surfaces=["gateway", "scheduler"]),
    cap("hermes-agent", "security.permissions", "Permission modes such as `/yolo` and gateway/tool configuration govern autonomy; use conservative defaults for unattended runs.", source_id="src.hermes.releases", actors={"human_operator": "native", "in_harness_agent": "mediated", "external_orchestrator": "supported", "ci_runner": "supported", "administrator": "configurable"}, surfaces=["CLI permission modes"], limitations=["The security model needs deeper comparative review before enterprise promotion."]),
    cap("hermes-agent", "tools.web_research", "Hermes 0.20 added grounded research and citation support.", source_id="src.hermes.releases", actors=AGENT_TOOL, surfaces=["research tools", "citations"], minimum_version="0.20.0"),
    cap("hermes-agent", "interfaces.voice", "Streaming voice supports barge-in and wake words.", source_id="src.hermes.docs.voice", actors={"human_operator": "native", "in_harness_agent": "mediated", "external_orchestrator": "supported", "ci_runner": "unavailable", "administrator": "configurable"}, surfaces=["voice"], minimum_version="0.20.0"),
    cap("hermes-agent", "interfaces.artifacts", "Desktop artifacts and multiple windows provide richer outputs than plain terminal text.", source_id="src.hermes.releases", actors=HUMAN_UI, surfaces=["desktop artifacts"], minimum_version="0.20.0"),
    cap("hermes-agent", "models.provider_portability", "Hermes supports multiple hosted and local model providers.", source_id="src.hermes.repo", actors={"human_operator": "native", "in_harness_agent": "supported", "external_orchestrator": "configurable", "ci_runner": "configurable", "administrator": "configurable"}, surfaces=["hosted APIs", "local models"]),
)

# Antigravity CLI
add(
    cap("antigravity-cli", "interaction.terminal", "Terminal-first interface to Antigravity agents with slash commands, Vim mode, and artifact views.", source_id="src.antigravity.changelog", actors=HUMAN_UI, surfaces=["terminal"], invocation=["agy"]),
    cap("antigravity-cli", "interaction.desktop_web", "Antigravity CLI shares a backend with the Antigravity desktop command center.", source_id="src.antigravity.site", actors=HUMAN_UI, surfaces=["desktop", "projects"]),
    cap("antigravity-cli", "execution.file_edit", "Antigravity agents understand codebases and edit files under permission controls.", source_id="src.antigravity.site", actors=AGENT_TOOL, surfaces=["terminal", "desktop"]),
    cap("antigravity-cli", "execution.shell", "Agents execute shell commands, and users can issue direct commands from the CLI.", source_id="src.antigravity.changelog", actors=AGENT_TOOL, surfaces=["terminal"]),
    cap("antigravity-cli", "execution.headless", "Print mode provides non-interactive execution and direct read-only slash-command queries.", source_id="src.antigravity.changelog", actors=HEADLESS, surfaces=["CLI", "print mode"], invocation=["agy -p"]),
    cap("antigravity-cli", "execution.structured_output", "Print mode emits text, JSON, or typed NDJSON `stream-json`, including tool and subagent metadata.", source_id="src.antigravity.changelog", actors=HEADLESS, surfaces=["JSON", "stream-json"], invocation=["--output-format json", "--output-format stream-json"], minimum_version="1.1.8"),
    cap("antigravity-cli", "execution.sdk_embedding", "The Antigravity SDK provides programmatic access to the same platform capabilities.", source_id="src.antigravity.site", actors=SDK, surfaces=["Antigravity SDK"]),
    cap("antigravity-cli", "extensions.mcp_client", "Antigravity CLI supports MCP tools, progress reporting, OAuth, and admin controls.", source_id="src.antigravity.changelog", actors=EXTENSION, surfaces=["MCP"]),
    cap("antigravity-cli", "extensions.skills", "Agent Skills can be discovered and expanded in interactive and headless print modes.", source_id="src.antigravity.changelog", actors=EXTENSION, surfaces=["skills", "print mode"], minimum_version="1.1.9"),
    cap("antigravity-cli", "extensions.plugins", "Plugins package customizations and share enablement with Antigravity configuration.", source_id="src.antigravity.changelog", actors=EXTENSION, surfaces=["plugins"]),
    cap("antigravity-cli", "extensions.hooks", "Hooks run before/after invocations and at stop points with explicit ordering.", source_id="src.antigravity.changelog", actors={"human_operator": "configurable", "in_harness_agent": "mediated", "external_orchestrator": "supported", "ci_runner": "supported", "administrator": "native"}, surfaces=["hooks.json"], invocation=["PostInvocation", "Stop", "PostToolUse"]),
    cap("antigravity-cli", "context.project_instructions", "Custom agents can be defined in Markdown with frontmatter controlling role, inheritance, and command policy.", source_id="src.antigravity.changelog", actors=EXTENSION, surfaces=["agent.md"], minimum_version="1.1.6"),
    cap("antigravity-cli", "sessions.resume_fork", "Conversations are persistent, can be forked, and warn about concurrent access.", source_id="src.antigravity.changelog", actors={"human_operator": "native", "in_harness_agent": "mediated", "external_orchestrator": "supported", "ci_runner": "supported", "administrator": "configurable"}, surfaces=["CLI", "desktop"], invocation=["/fork"]),
    cap("antigravity-cli", "orchestration.subagents", "Custom and dynamic subagents are first-class and expose child conversation metadata in structured output.", source_id="src.antigravity.changelog", actors={"human_operator": "supported", "in_harness_agent": "native", "external_orchestrator": "supported", "ci_runner": "supported", "administrator": "configurable"}, surfaces=["subagents", "stream-json"], minimum_version="1.1.6"),
    cap("antigravity-cli", "orchestration.parallel_background", "Antigravity orchestrates multiple agents and background tasks without blocking the terminal.", source_id="src.antigravity.transition-blog", actors={"human_operator": "native", "in_harness_agent": "native", "external_orchestrator": "supported", "ci_runner": "supported", "administrator": "configurable"}, surfaces=["background subagents", "desktop command center"]),
    cap("antigravity-cli", "orchestration.multi_agent_coordination", "The Antigravity backend provides explicit multi-agent orchestration and coordinator/subagent state.", source_id="src.antigravity.site", actors={"human_operator": "native", "in_harness_agent": "native", "external_orchestrator": "supported", "ci_runner": "supported", "administrator": "configurable"}, surfaces=["projects", "subagents"]),
    cap("antigravity-cli", "runtime.remote_cloud", "CLI and desktop share a unified Antigravity backend for background and multi-workspace work.", source_id="src.antigravity.site", actors={"human_operator": "native", "in_harness_agent": "mediated", "external_orchestrator": "supported", "ci_runner": "supported", "administrator": "native"}, surfaces=["Antigravity backend", "desktop"]),
    cap("antigravity-cli", "automation.schedules", "Antigravity projects support scheduled messages/tasks.", source_id="src.antigravity.site", actors={"human_operator": "configurable", "in_harness_agent": "supported", "external_orchestrator": "supported", "ci_runner": "native", "administrator": "configurable"}, surfaces=["scheduled messages"]),
    cap("antigravity-cli", "security.sandbox", "Terminal execution uses filesystem/network sandboxing and records blocked network requests.", source_id="src.antigravity.changelog", actors={"human_operator": "configurable", "in_harness_agent": "mediated", "external_orchestrator": "supported", "ci_runner": "supported", "administrator": "native"}, surfaces=["sandbox"]),
    cap("antigravity-cli", "security.permissions", "Permission modes, allowlists, project/user settings, and strict review modes govern commands.", source_id="src.antigravity.changelog", actors={"human_operator": "native", "in_harness_agent": "mediated", "external_orchestrator": "supported", "ci_runner": "supported", "administrator": "native"}, surfaces=["settings.json", "allowlists"]),
    cap("antigravity-cli", "security.enterprise_policy", "Business sign-in, WIF, ADC, regional inference, and organization admin controls are supported.", source_id="src.antigravity.changelog", actors=ADMIN, surfaces=["Gemini Enterprise", "Google Cloud", "WIF"], minimum_version="1.1.10"),
    cap("antigravity-cli", "observability.usage_cost", "Structured output includes token/cache usage; read-only print commands expose usage, quota, credits, model, and effort without an agent turn.", source_id="src.antigravity.changelog", actors={"human_operator": "native", "in_harness_agent": "mediated", "external_orchestrator": "native", "ci_runner": "native", "administrator": "native"}, surfaces=["JSON", "stream-json", "/usage", "/quota"]),
    cap("antigravity-cli", "observability.tracing", "Typed step, tool, subagent, and terminal result events form a machine-consumable execution trace.", source_id="src.antigravity.changelog", actors=SDK, surfaces=["stream-json"], minimum_version="1.1.8"),
    cap("antigravity-cli", "tools.web_research", "Antigravity supports research through tools and connected MCP knowledge sources.", source_id="src.antigravity.site", actors=AGENT_TOOL, surfaces=["web", "MCP"]),
    cap("antigravity-cli", "tools.browser_computer", "Built-in Chrome DevTools MCP and Antigravity integrations support browser workflows.", source_id="src.antigravity.changelog", actors=AGENT_TOOL, surfaces=["Chrome DevTools MCP"]),
    cap("antigravity-cli", "interfaces.artifacts", "Artifact views, diffs, images, comments, and rich desktop panels support result review.", source_id="src.antigravity.changelog", actors=HUMAN_UI, surfaces=["artifact viewer", "diff viewer", "desktop"]),
    cap("antigravity-cli", "models.reasoning_control", "Model and reasoning effort are selectable interactively and through headless flags.", source_id="src.antigravity.changelog", actors={"human_operator": "native", "in_harness_agent": "supported", "external_orchestrator": "configurable", "ci_runner": "configurable", "administrator": "native"}, surfaces=["/model", "/effort", "--model", "--effort"]),
    cap("antigravity-cli", "evaluation.schema_enforcement", "`--json-schema` constrains the final structured result in JSON and stream-json modes.", source_id="src.antigravity.changelog", actors=HEADLESS, surfaces=["print mode"], invocation=["--json-schema"], minimum_version="1.1.8"),
)

# Gemini CLI (historical profile)
add(
    cap("gemini-cli", "interaction.terminal", "Gemini CLI provides an interactive terminal agent.", source_id="src.gemini.repo", actors=HUMAN_UI, surfaces=["terminal"]),
    cap("gemini-cli", "execution.file_edit", "Gemini CLI agents can inspect and modify repository files.", source_id="src.gemini.repo", actors=AGENT_TOOL, surfaces=["terminal"]),
    cap("gemini-cli", "execution.shell", "Gemini CLI agents can run shell tools under configured policies.", source_id="src.gemini.repo", actors=AGENT_TOOL, surfaces=["terminal"]),
    cap("gemini-cli", "execution.headless", "Gemini CLI exposes headless mode for scripts and automation.", source_id="src.gemini.docs", actors=HEADLESS, surfaces=["CLI"]),
    cap("gemini-cli", "execution.structured_output", "Headless mode supports structured JSON output.", source_id="src.gemini.docs", actors=HEADLESS, surfaces=["JSON"]),
    cap("gemini-cli", "extensions.mcp_client", "Gemini CLI supports MCP servers.", source_id="src.gemini.docs", actors=EXTENSION, surfaces=["MCP"]),
    cap("gemini-cli", "extensions.skills", "Agent Skills were supported and ported to Antigravity CLI.", source_id="src.gemini.transition", actors=EXTENSION, surfaces=["skills"]),
    cap("gemini-cli", "extensions.plugins", "Gemini CLI extensions were supported and became Antigravity plugins in the successor product.", source_id="src.gemini.transition", actors=EXTENSION, surfaces=["extensions"], status="deprecated"),
    cap("gemini-cli", "extensions.hooks", "Gemini CLI supports lifecycle hooks.", source_id="src.gemini.docs", actors={"human_operator": "configurable", "in_harness_agent": "mediated", "external_orchestrator": "supported", "ci_runner": "supported", "administrator": "configurable"}, surfaces=["hooks"]),
    cap("gemini-cli", "orchestration.subagents", "Subagents were supported and ported to Antigravity CLI.", source_id="src.gemini.transition", actors={"human_operator": "supported", "in_harness_agent": "native", "external_orchestrator": "supported", "ci_runner": "supported", "administrator": "configurable"}, surfaces=["subagents"]),
    cap("gemini-cli", "security.permissions", "Gemini CLI provides approval and policy controls for tools.", source_id="src.gemini.docs", actors={"human_operator": "native", "in_harness_agent": "mediated", "external_orchestrator": "supported", "ci_runner": "supported", "administrator": "configurable"}, surfaces=["CLI", "settings"]),
    cap("gemini-cli", "models.reasoning_control", "Model selection and plan-mode workflows are configurable.", source_id="src.gemini.docs", actors={"human_operator": "native", "in_harness_agent": "supported", "external_orchestrator": "configurable", "ci_runner": "configurable", "administrator": "configurable"}, surfaces=["model config", "plan mode"]),
)

# Qwen Code
add(
    cap("qwen-code", "interaction.terminal", "Qwen Code is an open-source terminal coding agent.", source_id="src.qwen.repo", actors=HUMAN_UI, surfaces=["terminal"]),
    cap("qwen-code", "interaction.desktop_web", "Qwen Code provides an official desktop application.", source_id="src.qwen.repo", actors=HUMAN_UI, surfaces=["desktop"]),
    cap("qwen-code", "execution.file_edit", "Qwen Code can inspect and edit repository files.", source_id="src.qwen.repo", actors=AGENT_TOOL, surfaces=["terminal", "desktop"]),
    cap("qwen-code", "execution.shell", "Qwen Code can run shell commands.", source_id="src.qwen.repo", actors=AGENT_TOOL, surfaces=["terminal"]),
    cap("qwen-code", "extensions.mcp_client", "Qwen Code supports MCP-style external tools.", source_id="src.qwen.docs", actors=EXTENSION, surfaces=["MCP"], confidence="inferred_high"),
    cap("qwen-code", "extensions.skills", "Qwen Code follows the modern coding-harness skill/instruction model.", source_id="src.qwen.docs", actors=EXTENSION, surfaces=["skills"], confidence="inferred_high"),
    cap("qwen-code", "sessions.resume_fork", "Sessions persist across interactive use.", source_id="src.qwen.docs", actors={"human_operator": "native", "in_harness_agent": "mediated", "external_orchestrator": "supported", "ci_runner": "supported", "administrator": "configurable"}, surfaces=["terminal", "desktop"], confidence="inferred_high"),
    cap("qwen-code", "models.provider_portability", "Qwen Code supports OpenAI, Anthropic, Gemini, and Qwen APIs.", source_id="src.qwen.repo", actors={"human_operator": "native", "in_harness_agent": "supported", "external_orchestrator": "configurable", "ci_runner": "configurable", "administrator": "configurable"}, surfaces=["multiple providers"]),
)

# Goose
add(
    cap("goose", "interaction.terminal", "goose provides a CLI agent interface.", source_id="src.goose.repo", actors=HUMAN_UI, surfaces=["CLI"]),
    cap("goose", "interaction.desktop_web", "goose provides an Electron desktop interface.", source_id="src.goose.repo", actors=HUMAN_UI, surfaces=["desktop"]),
    cap("goose", "execution.file_edit", "goose can install, execute, edit, and test through agent tools.", source_id="src.goose.repo", actors=AGENT_TOOL, surfaces=["CLI", "desktop"]),
    cap("goose", "execution.shell", "goose can execute local commands.", source_id="src.goose.repo", actors=AGENT_TOOL, surfaces=["CLI", "desktop"]),
    cap("goose", "execution.headless", "goose server and CLI paths support external automation.", source_id="src.goose.docs", actors=HEADLESS, surfaces=["CLI", "goosed server"], confidence="inferred_high"),
    cap("goose", "execution.rpc_server", "The goosed server exposes agent functionality to clients.", source_id="src.goose.docs", actors=SDK, surfaces=["goosed server"], confidence="inferred_high"),
    cap("goose", "extensions.mcp_client", "goose is MCP-first and can use MCP extensions and apps.", source_id="src.goose.repo", actors=EXTENSION, surfaces=["MCP extensions", "MCP apps"]),
    cap("goose", "extensions.skills", "Recipes and reusable instructions package workflows for agents.", source_id="src.goose.docs", actors=EXTENSION, surfaces=["recipes"], confidence="inferred_high"),
    cap("goose", "orchestration.subagents", "goose supports delegated/subagent workflows through recipes and summon/delegate primitives.", source_id="src.goose.repo", actors={"human_operator": "supported", "in_harness_agent": "native", "external_orchestrator": "supported", "ci_runner": "supported", "administrator": "configurable"}, surfaces=["delegate", "summon"], confidence="inferred_high"),
    cap("goose", "runtime.self_hosted", "goose runs locally or on user-managed servers.", source_id="src.goose.repo", actors={"human_operator": "configurable", "in_harness_agent": "mediated", "external_orchestrator": "supported", "ci_runner": "supported", "administrator": "native"}, surfaces=["local", "server"]),
    cap("goose", "models.provider_portability", "goose is designed to work with multiple LLM providers and local models.", source_id="src.goose.repo", actors={"human_operator": "native", "in_harness_agent": "supported", "external_orchestrator": "configurable", "ci_runner": "configurable", "administrator": "configurable"}, surfaces=["multiple providers", "local inference"]),
)

# Copilot CLI and Pi discovery profiles
add(
    cap("github-copilot-cli", "interaction.terminal", "GitHub Copilot CLI provides an interactive terminal agent.", source_id="src.copilot-cli.docs", actors=HUMAN_UI, surfaces=["terminal"]),
    cap("github-copilot-cli", "execution.headless", "Copilot CLI is the default engine in GitHub Agentic Workflows and supports unattended workflow execution.", source_id="src.github-agentic-workflows.engine-matrix", actors=HEADLESS, surfaces=["GitHub Actions"]),
    cap("github-copilot-cli", "automation.ci", "GitHub Agentic Workflows provides first-class Copilot engine support with custom agents and continuation controls.", source_id="src.github-agentic-workflows.engine-matrix", actors=HEADLESS, surfaces=["GitHub Actions", "Agentic Workflows"]),
    cap("github-copilot-cli", "security.enterprise_policy", "GitHub organization controls and workflow permissions govern Copilot use.", source_id="src.copilot-cli.docs", actors=ADMIN, surfaces=["GitHub organization"]),
    cap("pi-agent", "interaction.terminal", "Pi includes an interactive coding-agent CLI.", source_id="src.pi.repo", actors=HUMAN_UI, surfaces=["terminal"]),
    cap("pi-agent", "execution.sdk_embedding", "Pi includes an agent core runtime and unified LLM API packages.", source_id="src.pi.repo", actors=SDK, surfaces=["TypeScript packages"]),
    cap("pi-agent", "extensions.skills", "Pi skills are compatible with Claude Code and Codex-style skill bundles.", source_id="src.pi.repo", actors=EXTENSION, surfaces=["skills"]),
    cap("pi-agent", "extensions.plugins", "Pi supports installable extensions.", source_id="src.github-agentic-workflows.engine-matrix", actors=EXTENSION, surfaces=["npm extensions"]),
    cap("pi-agent", "models.provider_portability", "Pi includes a unified multi-provider LLM API.", source_id="src.pi.repo", actors={"human_operator": "native", "in_harness_agent": "supported", "external_orchestrator": "configurable", "ci_runner": "configurable", "administrator": "configurable"}, surfaces=["multiple providers"]),
)

# SDK capability templates
for sdk_id, source_id, language in [
    ("claude-agent-sdk-python", "src.claude-code.docs.sdk", "Python"),
    ("claude-agent-sdk-typescript", "src.claude-code.docs.sdk", "TypeScript"),
]:
    add(
        cap(sdk_id, "execution.sdk_embedding", f"{language} API embeds the Claude Code agent loop, tools, and context management.", source_id=source_id, actors=SDK, surfaces=[f"{language} library"]),
        cap(sdk_id, "execution.structured_output", "Typed message streams expose assistant, tool, task, usage, and terminal-result events.", source_id=source_id, actors=SDK, surfaces=["typed events"]),
        cap(sdk_id, "extensions.mcp_client", "SDK applications can configure MCP servers and SDK-defined MCP tools.", source_id=source_id, actors=SDK, surfaces=["MCP"]),
        cap(sdk_id, "extensions.hooks", "Lifecycle hooks and permission callbacks are available to embedding applications.", source_id=source_id, actors=SDK, surfaces=["callbacks", "hooks"]),
        cap(sdk_id, "orchestration.subagents", "SDK applications can use Claude Code subagents and background tasks.", source_id=source_id, actors=SDK, surfaces=["subagents"]),
        cap(sdk_id, "sessions.resume_fork", "SDK session IDs and stores support resume and session lifecycle management.", source_id=source_id, actors=SDK, surfaces=["session store"]),
        cap(sdk_id, "security.permissions", "Allowed tools, permission modes, and callbacks govern actions.", source_id=source_id, actors=SDK, surfaces=["options", "callbacks"]),
        cap(sdk_id, "observability.tracing", "Typed result and task events provide execution telemetry.", source_id=source_id, actors=SDK, surfaces=["event stream"]),
        cap(sdk_id, "governance.human_approval_api", "Embedding applications can implement human/tool approval callbacks.", source_id=source_id, actors=SDK, surfaces=["permission callback"]),
    )

add(
    cap("codex-sdk-python", "execution.sdk_embedding", "Python SDK controls the local Codex app-server over JSON-RPC and bundles a pinned runtime.", source_id="src.codex.docs.sdk", actors=SDK, surfaces=["Python library"]),
    cap("codex-sdk-python", "execution.rpc_server", "The SDK consumes Codex app-server JSON-RPC methods and version-specific schemas.", source_id="src.codex.docs.app-server", actors=SDK, surfaces=["JSON-RPC"]),
    cap("codex-sdk-python", "execution.structured_output", "Typed notifications and generated schemas expose machine-readable turn events.", source_id="src.codex.docs.app-server", actors=SDK, surfaces=["events", "JSON Schema"]),
    cap("codex-sdk-python", "sessions.resume_fork", "SDK clients control Codex threads and turns.", source_id="src.codex.docs.sdk", actors=SDK, surfaces=["threads"]),
    cap("codex-sdk-python", "security.sandbox", "Python SDK thread and turn calls expose Codex sandbox presets such as read-only and workspace-write.", source_id="src.codex.docs.sdk", actors=SDK, surfaces=["Python API", "sandbox presets"]),
    cap("codex-sdk-python", "governance.human_approval_api", "SDK/app-server clients can participate in approval flows and return decisions through the machine protocol.", source_id="src.codex.docs.app-server", actors=SDK, surfaces=["JSON-RPC"]),
)

add(
    cap("codex-sdk-typescript", "execution.sdk_embedding", "The server-side TypeScript SDK starts, continues, and resumes local Codex threads.", source_id="src.codex.docs.sdk", actors=SDK, surfaces=["TypeScript library", "Node.js 18+"]),
    cap("codex-sdk-typescript", "execution.structured_output", "The TypeScript SDK exchanges JSONL events with the bundled/local Codex CLI for machine-readable progress.", source_id="src.codex.docs.sdk", actors=SDK, surfaces=["JSONL event stream"]),
    cap("codex-sdk-typescript", "sessions.resume_fork", "Applications can continue the same thread or resume a prior thread by ID.", source_id="src.codex.docs.sdk", actors=SDK, surfaces=["threads"]),
    cap("codex-sdk-typescript", "security.sandbox", "Thread options inherit Codex sandbox and approval controls available through the underlying CLI.", source_id="src.codex.docs.sdk", actors=SDK, surfaces=["thread options"], confidence="inferred_high", limitations=["The TypeScript surface may lag CLI/app-server options; verify per release before relying on parity."]),
)

for sdk_id, source_id, language in [
    ("openai-agents-sdk-python", "src.openai-agents-python.docs", "Python"),
    ("openai-agents-sdk-js", "src.openai-agents-js.docs", "JavaScript/TypeScript"),
]:
    add(
        cap(sdk_id, "execution.sdk_embedding", f"{language} framework for building agent applications.", source_id=source_id, actors=SDK, surfaces=[f"{language} library"]),
        cap(sdk_id, "execution.structured_output", "Typed agent results and structured outputs support downstream automation.", source_id=source_id, actors=SDK, surfaces=["typed results"]),
        cap(sdk_id, "extensions.mcp_client", "Agents can connect to MCP servers and expose MCP-backed tools.", source_id=source_id, actors=SDK, surfaces=["MCP"]),
        cap(sdk_id, "orchestration.subagents", "Handoffs and agents-as-tools compose multi-agent workflows.", source_id=source_id, actors=SDK, surfaces=["handoffs", "agents as tools"]),
        cap(sdk_id, "orchestration.multi_agent_coordination", "Supervisor/handoff patterns are first-class in the SDK.", source_id=source_id, actors=SDK, surfaces=["handoffs", "routing"]),
        cap(sdk_id, "context.persistent_memory", "Sessions persist conversation state across agent runs.", source_id=source_id, actors=SDK, surfaces=["sessions"]),
        cap(sdk_id, "security.permissions", "Guardrails and tool policies validate inputs, outputs, and actions.", source_id=source_id, actors=SDK, surfaces=["guardrails"]),
        cap(sdk_id, "observability.tracing", "Built-in tracing records agents, generations, tools, handoffs, and guardrails.", source_id=source_id, actors=SDK, surfaces=["tracing"]),
        cap(sdk_id, "models.provider_portability", "The SDK supports OpenAI APIs and provider-compatible model adapters.", source_id=source_id, actors=SDK, surfaces=["model adapters"]),
        cap(sdk_id, "governance.human_approval_api", "Tool approval/guardrail patterns can be implemented in application code.", source_id=source_id, actors=SDK, surfaces=["callbacks", "guardrails"], confidence="inferred_high"),
    )

# Provider SDKs: track API-surface changes without pretending they are full harnesses.
for sdk_id, source_id, language, provider in [
    ("openai-python-sdk", "src.openai-python.changelog", "Python", "OpenAI"),
    ("openai-node-sdk", "src.openai-node.changelog", "JavaScript/TypeScript", "OpenAI"),
    ("anthropic-python-sdk", "src.anthropic-python.changelog", "Python", "Anthropic"),
    ("anthropic-typescript-sdk", "src.anthropic-typescript.changelog", "JavaScript/TypeScript", "Anthropic"),
]:
    add(
        cap(sdk_id, "execution.sdk_embedding", f"Typed {language} access to the {provider} API.", source_id=source_id, actors=SDK, surfaces=[f"{language} library"]),
        cap(sdk_id, "execution.structured_output", "Streaming and typed response objects support machine-readable application logic.", source_id=source_id, actors=SDK, surfaces=["streaming", "typed API objects"]),
        cap(sdk_id, "models.reasoning_control", "Model and API feature parameters are exposed as generated typed interfaces.", source_id=source_id, actors=SDK, surfaces=["API parameters"]),
    )


def manual_release(
    harness_id: str,
    version: str,
    source_id: str,
    published_at: str | None,
    bullets: list[str],
    *,
    channel: str = "stable",
    title: str | None = None,
) -> dict[str, Any]:
    changes = []
    for index, bullet in enumerate(bullets, 1):
        changes.append({
            "id": f"chg.{harness_id}.{version}.{index:03d}",
            "kind": classify_change(bullet),
            "summary": bullet,
            "category": classify_category(bullet),
            "surfaces": infer_surfaces(bullet),
            "actors": infer_actors(bullet),
            "capability_refs": infer_capabilities(bullet),
            "security_relevant": is_security_relevant(bullet),
            "breaking_or_deprecated": is_breaking_or_deprecated(bullet),
            "normalization": {"method": "human_curated_seed_v1", "confidence": "verified_official", "review_status": "approved"},
        })
    return {
        "id": f"rel.{harness_id}.{version}",
        "harness_id": harness_id,
        "version": version,
        "channel": channel,
        "published_at": published_at,
        "date_precision": "day" if published_at else "unknown",
        "retrieved_at": VERIFIED_AT,
        "source_id": source_id,
        "source_url": SOURCE_URL[source_id],
        "raw_snapshot_path": None,
        "raw_sha256": None,
        "title": title or f"{harness_id} {version}",
        "notes_excerpt": bullets[0] if bullets else "No notes supplied.",
        "change_count": len(changes),
        "flags": {
            "security": any(item["security_relevant"] for item in changes),
            "breaking": any(item["breaking_or_deprecated"] for item in changes),
            "deprecation": any(item["kind"] == "deprecated" for item in changes),
        },
        "changes": changes,
        "provenance": {"authority": "official_primary", "ingestion": "human_curated_seed", "immutable": False},
    }


def parse_seed(path: str, harness_id: str, source_id: str, *, max_sections: int | None = None, since: str | None = None) -> list[dict[str, Any]]:
    releases = parse_changelog_file(
        ROOT / path,
        harness_id=harness_id,
        source_id=source_id,
        source_url=SOURCE_URL[source_id],
        raw_path=path,
    )
    if since:
        releases = [item for item in releases if item.get("published_at") and item["published_at"][:10] >= since]
    if max_sections is not None:
        releases = releases[:max_sections]
    return releases


releases: list[dict[str, Any]] = []
releases.extend(parse_seed("raw/claude-code/CHANGELOG.md", "claude-code", "src.claude-code.changelog", max_sections=110))
releases.extend(parse_seed("raw/antigravity-cli/CHANGELOG.md", "antigravity-cli", "src.antigravity.changelog"))
releases.extend(parse_seed("raw/claude-agent-sdk-python/CHANGELOG.md", "claude-agent-sdk-python", "src.claude-agent-sdk-python.changelog", max_sections=110))
releases.extend(parse_seed("raw/claude-agent-sdk-typescript/CHANGELOG.md", "claude-agent-sdk-typescript", "src.claude-agent-sdk-typescript.changelog", max_sections=110))
releases.extend(parse_seed("raw/openai-python/CHANGELOG.md", "openai-python-sdk", "src.openai-python.changelog", since="2026-05-01"))
releases.extend(parse_seed("raw/openai-node/CHANGELOG.md", "openai-node-sdk", "src.openai-node.changelog", since="2026-05-01"))
releases.extend(parse_seed("raw/anthropic-sdk-python/CHANGELOG.md", "anthropic-python-sdk", "src.anthropic-python.changelog", since="2026-05-01"))
releases.extend(parse_seed("raw/anthropic-sdk-typescript/CHANGELOG.md", "anthropic-typescript-sdk", "src.anthropic-typescript.changelog", since="2026-05-01"))

# Curated recent releases for projects whose authoritative history is GitHub Release bodies rather than a raw changelog.
releases.extend([
    manual_release(
        "openai-codex", "0.147.0", "src.codex.releases", "2026-08-07T00:00:00Z",
        [
            "Added portable Agent Plugins across Codex surfaces.",
            "Added persistent conversation sections and improved long-running thread organization.",
            "Added `--approve-for-me` for explicit approval delegation in supported flows.",
            "Added skill imports and support for the MCP 2026-07-28 specification.",
            "Expanded Amazon Bedrock capabilities and fixed security issues.",
            "Removed the deprecated `codex exec --full-auto` path in favor of explicit sandbox and approval settings.",
        ],
    ),
    manual_release("openai-codex", "0.146.1", "src.codex.releases", None, ["Maintenance release with reliability and compatibility fixes."], title="Codex 0.146.1"),
    manual_release(
        "opencode", "1.18.15", "src.opencode.releases", "2026-08-07T00:00:00Z",
        ["Added JSON transcript export.", "Expanded locale support.", "Fixed transcript chronology and ordering issues."],
    ),
    manual_release(
        "opencode", "1.18.8", "src.opencode.releases", "2026-07-28T00:00:00Z",
        ["Improved MCP and OAuth compatibility.", "Improved session reconnect behavior."],
    ),
    manual_release(
        "hermes-agent", "0.20.0", "src.hermes.releases", "2026-08-03T00:00:00Z",
        [
            "Added streaming voice with barge-in and wake words.",
            "Added A2A 1.0 support and signed webhooks.",
            "Added grounded research and citations.",
            "Added desktop artifacts, a plugin SDK, and multiple windows.",
            "Added CLI commands including `!`, `/init`, `/diff`, `/context`, and `/focus`.",
        ],
    ),
    manual_release("hermes-agent", "0.19.1", "src.hermes.releases", None, ["Maintenance and reliability update."], title="Hermes Agent 0.19.1"),
    manual_release("hermes-agent", "0.19.0", "src.hermes.releases", None, ["Major feature release preceding 0.20.0."], title="Hermes Agent 0.19.0"),
    manual_release("hermes-agent", "0.18.2", "src.hermes.releases", None, ["Maintenance and reliability update."], title="Hermes Agent 0.18.2"),
    manual_release("hermes-agent", "0.18.1", "src.hermes.releases", None, ["Maintenance and reliability update."], title="Hermes Agent 0.18.1"),
    manual_release("hermes-agent", "0.18.0", "src.hermes.releases", "2026-07-01T00:00:00Z", ["Added Mixture-of-Agents as a first-class orchestration capability.", "Completed a broad priority and reliability clean-up."], title="Hermes Agent 0.18.0"),
    manual_release("hermes-agent", "0.17.0", "src.hermes.releases", "2026-06-19T00:00:00Z", ["Major Hermes Agent feature release."], title="Hermes Agent 0.17.0"),
    manual_release("hermes-agent", "0.16.0", "src.hermes.releases", "2026-06-05T00:00:00Z", ["Major Hermes Agent feature release."], title="Hermes Agent 0.16.0"),
    manual_release("hermes-agent", "0.15.2", "src.hermes.releases", None, ["Maintenance release following 0.15.1."], title="Hermes Agent 0.15.2"),
    manual_release("hermes-agent", "0.15.1", "src.hermes.releases", "2026-05-29T00:00:00Z", ["Expanded the skills catalog and MCP Docker commands.", "Added `/yolo` permission mode and memory-context improvements.", "Improved dashboard and gateway reliability."], title="Hermes Agent 0.15.1"),
    manual_release("qwen-code", "0.21.8", "src.qwen.releases", "2026-08-08T00:00:00Z", ["Published Qwen Code 0.21.8 with the latest stable fixes and contributions."], title="Qwen Code 0.21.8"),
    manual_release("qwen-code", "0.21.7", "src.qwen.releases", "2026-08-07T00:00:00Z", ["Published Qwen Code 0.21.7."], title="Qwen Code 0.21.7"),
    manual_release("codex-sdk-python", "0.144.4", "src.codex-sdk-python.releases", "2026-07-17T00:00:00Z", ["Published the stable OpenAI Codex Python SDK with thread execution, progress streaming, and workspace-access controls."], title="OpenAI Codex Python SDK 0.144.4"),
    manual_release("codex-sdk-typescript", "0.146.0", "src.codex-sdk-typescript.releases", "2026-07-29T00:00:00Z", ["Published the Codex TypeScript SDK for embedding local Codex threads through a JSONL CLI transport."], title="OpenAI Codex TypeScript SDK 0.146.0"),
    manual_release("openai-agents-sdk-python", "0.14.0", "src.openai-agents-python.releases", "2026-08-06T00:00:00Z", ["Added Programmatic Tool Calling support as a significant new Responses feature area."], title="OpenAI Agents SDK Python 0.14.0"),
    manual_release("openai-agents-sdk-js", "0.14.3", "src.openai-agents-js.releases", "2026-08-06T00:00:00Z", ["Published OpenAI Agents SDK JavaScript/TypeScript 0.14.3."], title="OpenAI Agents SDK JS 0.14.3"),
])

# De-duplicate release IDs, preferring curated entries over parsed entries with the same id.
release_index: dict[str, dict[str, Any]] = {}
for item in releases:
    release_index[item["id"]] = item
releases = sorted(release_index.values(), key=release_timeline_key, reverse=True)

# Reconcile materialized current versions from the highest release in the seed ledger.
release_versions: dict[str, list[dict[str, Any]]] = {}
for item in releases:
    release_versions.setdefault(item["harness_id"], []).append(item)
for item in harnesses:
    candidates = release_versions.get(item["id"], [])
    if candidates:
        latest = max(candidates, key=lambda release: release_timeline_key(release)[1])
        item["current_version"] = latest["version"]
        item["version_as_of"] = (latest.get("published_at") or VERIFIED_AT)[:10]

meta = {
    "schema_version": "0.1",
    "registry_id": "hcr.agentic-harness-capabilities",
    "name": "Harness Capability Registry",
    "artifact_unit": "HarnessBOM",
    "description": "Evidence-backed release ledger and actor-aware capability graph for agentic harnesses and SDKs.",
    "created_at": VERIFIED_AT,
    "updated_at": VERIFIED_AT,
    "historical_window_target_days": 120,
    "seed_scope": {
        "core_harnesses": ["claude-code", "openai-codex", "opencode", "hermes-agent", "antigravity-cli"],
        "historical_or_secondary_harnesses": ["gemini-cli", "qwen-code", "goose", "github-copilot-cli", "pi-agent"],
        "agent_sdks": ["claude-agent-sdk-python", "claude-agent-sdk-typescript", "codex-sdk-python", "codex-sdk-typescript", "openai-agents-sdk-python", "openai-agents-sdk-js"],
        "provider_sdks": ["openai-python-sdk", "openai-node-sdk", "anthropic-python-sdk", "anthropic-typescript-sdk"],
    },
    "quality_policy": {
        "primary_evidence": "Official changelog, release feed, repository, or product documentation.",
        "secondary_evidence": "Official cross-vendor compatibility matrices may support but not replace primary evidence.",
        "unknown_rule": "Missing evidence is represented as unknown, never inferred as unavailable.",
        "ui_rule": "Human UI availability never implies in-harness or external-agent reachability.",
        "promotion_rule": "Heuristically extracted release changes remain candidates until reviewed or corroborated by official docs.",
    },
}

write_json(ROOT / "registry" / "registry-meta.json", meta)
write_json(ROOT / "registry" / "sources.json", sources)
write_json(ROOT / "registry" / "harnesses.json", harnesses)
write_json(ROOT / "registry" / "taxonomy.json", taxonomy)
write_json(ROOT / "registry" / "capabilities.json", capabilities)
write_json(ROOT / "registry" / "releases.json", releases)
print(f"Wrote {len(sources)} sources, {len(harnesses)} tracks, {len(taxonomy)} taxonomy nodes, {len(capabilities)} capability implementations, and {len(releases)} releases.")
