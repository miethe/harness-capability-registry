from __future__ import annotations

import re
from typing import Iterable

CHANGE_PREFIXES = (
    ("added", ("add", "added", "introduc", "new ")),
    ("fixed", ("fix", "fixed", "resolve", "patch")),
    ("improved", ("improv", "optimiz", "enhanc", "speed")),
    ("deprecated", ("deprecat",)),
    ("removed", ("remove", "removed", "drop ")),
    ("changed", ("change", "changed", "update", "renam", "migrat")),
)

CATEGORY_KEYWORDS: dict[str, tuple[str, ...]] = {
    "execution": ("headless", "non-interactive", "print mode", "exec ", "shell", "bash", "command"),
    "orchestration": ("subagent", "multi-agent", "delegate", "background agent", "agent team", "sendmessage"),
    "extensions": ("skill", "plugin", "extension", "mcp", "hook", "marketplace", "connector"),
    "context_memory": ("memory", "context", "compact", "instruction", "agents.md", "claude.md", "resume"),
    "session_state": ("session", "conversation", "fork", "resume", "teleport", "remote control"),
    "security_governance": ("permission", "sandbox", "allowlist", "deny", "credential", "oauth", "policy", "trust"),
    "observability": ("telemetry", "usage", "token", "trace", "log", "metrics", "cost", "spend"),
    "interfaces": ("tui", "vscode", "ide", "desktop", "web", "mobile", "voice", "artifact", "diff"),
    "models_providers": ("model", "bedrock", "vertex", "provider", "reasoning effort", "api key"),
    "automation": ("ci", "github action", "schedule", "workflow", "webhook", "cron"),
    "research_tools": ("research", "web search", "web-search", "citation", "browser", "chrome"),
    "distribution_runtime": ("self-hosted", "runner", "container", "install", "update", "platform"),
}

CAPABILITY_KEYWORDS: dict[str, tuple[str, ...]] = {
    "execution.headless": ("headless", "non-interactive", "print mode", "codex exec", " -p "),
    "execution.structured_output": ("jsonl", "stream-json", "output-format", "json schema", "structured output"),
    "execution.sdk_embedding": ("agent sdk", "codex sdk", "python sdk", "typescript sdk", "app-server"),
    "extensions.mcp_client": ("mcp server", "mcp tool", "mcp oauth", "model context protocol"),
    "extensions.skills": ("skill", "skill.md", "agent skills"),
    "extensions.plugins": ("plugin", "marketplace", "extension"),
    "extensions.hooks": ("hook", "pretooluse", "posttooluse", "postinvocation"),
    "orchestration.subagents": ("subagent", "delegate"),
    "orchestration.parallel_background": ("background agent", "parallel agent", "multi-agent", "agent team"),
    "orchestration.cross_session_messaging": ("sendmessage", "cross-session", "listagents"),
    "context.project_instructions": ("agents.md", "claude.md", "project instruction"),
    "context.persistent_memory": ("persistent memory", "memory", "learn"),
    "sessions.resume_fork": ("resume", "fork", "conversation history"),
    "runtime.remote_cloud": ("remote control", "cloud session", "cloud task", "teleport"),
    "runtime.self_hosted": ("self-hosted", "self hosted", "runner"),
    "security.sandbox": ("sandbox",),
    "security.permissions": ("permission", "allowlist", "denylist", "approval"),
    "security.enterprise_policy": ("managed setting", "admin control", "enterprise", "organization policy"),
    "automation.ci": ("ci", "github action", "pipeline"),
    "automation.schedules": ("schedule", "scheduled task", "cron"),
    "tools.web_research": ("deep-research", "web search", "citation", "grounded research"),
    "tools.browser_computer": ("browser", "chrome", "computer use"),
    "interfaces.voice": ("voice", "wake word", "barge-in"),
    "interfaces.artifacts": ("artifact", "diff view", "viewer"),
    "observability.usage_cost": ("usage", "token accounting", "cost", "spend", "credits"),
}

SURFACE_KEYWORDS: dict[str, tuple[str, ...]] = {
    "terminal_interactive": ("tui", "terminal", "slash command", "/"),
    "terminal_headless": ("headless", "non-interactive", "print mode", "jsonl", "stream-json"),
    "ide": ("vscode", "ide", "jetbrains"),
    "desktop": ("desktop",),
    "web": ("web", "browser"),
    "mobile": ("mobile",),
    "sdk": ("sdk", "app-server", "json-rpc"),
    "ci": ("ci", "github action", "pipeline"),
    "remote": ("remote control", "cloud session", "self-hosted"),
}

ACTOR_KEYWORDS: dict[str, tuple[str, ...]] = {
    "human_operator": ("prompt", "picker", "tui", "slash command", "desktop", "ide", "user"),
    "in_harness_agent": ("tool", "subagent", "claude can", "agent can", "automatically"),
    "external_orchestrator": ("headless", "sdk", "json-rpc", "api", "non-interactive", "stream-json"),
    "ci_runner": ("ci", "github action", "pipeline", "headless"),
    "administrator": ("managed setting", "admin", "enterprise", "policy", "organization"),
}

SECURITY_TERMS = ("security", "vulnerability", "bypass", "credential", "injection", "escape", "cve", "allowlist")
BREAKING_TERMS = ("breaking", "removed", "no longer", "renamed", "migration required", "deprecated")


def compact_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def classify_change(text: str) -> str:
    lowered = compact_text(text).lower()
    for kind, prefixes in CHANGE_PREFIXES:
        if any(lowered.startswith(prefix) for prefix in prefixes):
            return kind
    return "changed"


def classify_category(text: str) -> str:
    lowered = text.lower()
    scores = {category: sum(1 for word in words if word in lowered) for category, words in CATEGORY_KEYWORDS.items()}
    category, score = max(scores.items(), key=lambda item: item[1])
    return category if score else "other"


def infer_capabilities(text: str) -> list[str]:
    lowered = text.lower()
    return [capability for capability, words in CAPABILITY_KEYWORDS.items() if any(word in lowered for word in words)]


def infer_surfaces(text: str) -> list[str]:
    lowered = text.lower()
    values = [surface for surface, words in SURFACE_KEYWORDS.items() if any(word in lowered for word in words)]
    return values or ["unspecified"]


def infer_actors(text: str) -> list[str]:
    lowered = text.lower()
    values = [actor for actor, words in ACTOR_KEYWORDS.items() if any(word in lowered for word in words)]
    return values or ["unspecified"]


def is_security_relevant(text: str) -> bool:
    lowered = text.lower()
    return any(term in lowered for term in SECURITY_TERMS)


def is_breaking_or_deprecated(text: str) -> bool:
    lowered = text.lower()
    return any(term in lowered for term in BREAKING_TERMS)


def normalize_bullets(lines: Iterable[str]) -> list[str]:
    bullets: list[str] = []
    current: list[str] = []
    for raw in lines:
        line = raw.rstrip()
        match = re.match(r"^\s*[-*+]\s+(.*)$", line)
        if match:
            if current:
                bullets.append(compact_text(" ".join(current)))
            current = [match.group(1)]
        elif current and (line.startswith("  ") or line.startswith("\t")):
            current.append(line.strip())
        elif current and not line.strip():
            bullets.append(compact_text(" ".join(current)))
            current = []
    if current:
        bullets.append(compact_text(" ".join(current)))
    return bullets
