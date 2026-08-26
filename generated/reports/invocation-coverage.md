# Invocation Coverage Report

Generated for registry state: 2026-08-24T13:14:55.511915Z

**coverage: (235, 237)**

PARTIAL — not every capability has a resolved invocation token or a recorded not-applicable reason.

| Harness | Resolved | Not applicable | Unreviewed |
|---|---:|---:|---:|
| Antigravity CLI | 27 | 0 | 1 |
| Claude API SDK — Python | 3 | 0 | 0 |
| Claude API SDK — TypeScript | 3 | 0 | 0 |
| Claude Agent SDK — Python | 9 | 0 | 0 |
| Claude Agent SDK — TypeScript | 9 | 0 | 0 |
| Claude Code | 34 | 2 | 0 |
| Codex SDK — Python | 5 | 0 | 1 |
| Codex SDK — TypeScript | 4 | 0 | 0 |
| Gemini CLI | 13 | 0 | 0 |
| GitHub Copilot CLI | 4 | 0 | 0 |
| Hermes Agent | 21 | 0 | 0 |
| OpenAI API SDK — Node | 3 | 0 | 0 |
| OpenAI API SDK — Python | 3 | 0 | 0 |
| OpenAI Agents SDK — JavaScript/TypeScript | 10 | 0 | 0 |
| OpenAI Agents SDK — Python | 10 | 0 | 0 |
| OpenAI Codex | 32 | 0 | 0 |
| OpenCode | 19 | 0 | 0 |
| Pi Agent Harness | 5 | 0 | 0 |
| Qwen Code | 8 | 0 | 0 |
| goose | 11 | 0 | 0 |

## Unreviewed capability_ids

- runtime.remote_cloud [antigravity-cli]
- execution.structured_output [codex-sdk-python]

## Interpretation

An empty `invocation` array is no longer ambiguous: `invocation_status` distinguishes a confirmed not-applicable capability from one nobody has reviewed yet. Silent truncation — a report that skips what it has no evidence for — is the defect this report exists to prevent; the unreviewed list above is never elided.
