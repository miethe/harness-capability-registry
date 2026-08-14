---
schema_version: 0.1
id: hci.aos-integration.v0.1
type: specification
artifact_kind: architecture_decision_record
title: Harness Capability Intelligence Integration with Agentic OS
project: Agentic Operating System
domain: harness_capability_intelligence
status: proposed_integration
owner: Nick Miethe
created_at: 2026-08-08
updated_at: 2026-08-08
system_of_record: MeatyWiki
current_location: specs/04_AOS_Integration.md
related_systems:
  - Intent and I-BOM
  - IntentTree
  - Agent Postures
  - SkillMeat
  - Execution Engine
  - CCDash
  - MeatyWiki
  - Agentic Control Plane
  - Governance and Evaluation
source_context:
  - Agentic OS seed specs
  - Harness Capability Registry implementation
intended_use: Defines ownership and writeback boundaries across the AOS portfolio.
next_action: Register HarnessBOM as a SkillMeat artifact type and expose routing queries to the control plane.
review_cadence: quarterly
confidentiality: personal
tags:
  - aos-integration
  - control-plane
  - skillmeat
---

# AOS Integration

## 1. Classification

| Dimension | Decision |
|---|---|
| Canonical layer | Agentic Control Plane Routing Layer |
| Supporting layers | SkillMeat, Execution, CCDash, MeatyWiki, Governance |
| Owning project | Agentic Control Plane, with HCR as a distinct subsystem/repository |
| Primary artifact | HarnessBOM |
| Default agent posture | Researcher → Architect → Critic → Operator |
| Domain | Implementation and research; enterprise/personal shared foundation |

HCR should **not** be collapsed into SkillMeat or CCDash. It is a specialized capability-intelligence subsystem that publishes artifacts to both.

## 2. Intent and I-BOM

An execution intent should declare capability requirements rather than naming a preferred harness too early.

```yaml
harness_requirements:
  required:
    - execution.headless
    - execution.structured_output
    - security.sandbox
  preferred:
    - extensions.skills
    - runtime.self_hosted
  actor: external_orchestrator
  environment: mac_studio
  approval_policy: on_request
```

The I-BOM should capture:

- Installed harness versions
- Available subscriptions/API keys
- Platform/OS constraints
- Required data-access boundaries
- Approved model providers
- Repository or client policy
- Historical task evidence from CCDash

## 3. IntentTree

HCR contributes reusable tasks:

- Verify installed/current harness version
- Resolve required capabilities
- Identify actor-access mismatches
- Select invocation surface
- Generate harness-specific workflow implementation
- Test critical capability assumptions
- Promote validated routing evidence

A product release that affects an active workflow should create an IntentTree impact-review node rather than silently changing execution.

## 4. Agent Postures

Recommended posture chain:

1. **Researcher** gathers official source evidence.
2. **Architect** maps vendor-specific behavior to the canonical taxonomy.
3. **Critic** challenges actor reachability, parity, and negative claims.
4. **Operator** applies approved registry changes and regenerates artifacts.
5. **Red Team** reviews security- and permission-boundary changes.

## 5. SkillMeat

Register new artifact types:

```yaml
artifact_types:
  harnessbom:
    purpose: Portable evidence-backed capability and release bundle for one harness.
  harness_agent_guide:
    purpose: Compact actor-aware runtime guide for agent routing.
  harness_adapter:
    purpose: Versioned invocation, parsing, permission, and validation adapter.
  capability_eval:
    purpose: Runtime test proving a capability on a version/environment.
```

A SkillBOM can then declare:

```yaml
runtime_requirements:
  harness_id: claude-code
  version: ">=2.1.224"
  required_capabilities:
    - orchestration.cross_session_messaging
    - runtime.self_hosted
  harness_guide: generated/agent-guides/claude-code.json
```

## 6. Execution Engine

The Execution Engine owns scheduled collection and review workflows. It should select the smallest adequate update path:

- Release collection only
- Documentation drift audit
- One-harness impact review
- Full historical backfill
- Runtime validation against an installed environment

## 7. CCDash

HCR says what a product claims to support. CCDash records what actually worked in Nick's environments.

Join keys:

- `harness_id`
- `harness_version`
- `capability_id`
- `skillbom_id`
- `execution_environment_id`
- `approval_mode`

CCDash can then distinguish:

- Officially supported and runtime validated
- Officially supported but failing locally
- Undocumented but observed
- Deprecated but still used
- Higher rework/cost on one harness despite nominal feature parity

Performance evidence must not overwrite official capability evidence; it augments selection confidence.

## 8. MeatyWiki

Write back:

- Product-lineage decisions
- Capability-taxonomy rationale
- Source conflict notes
- Migration guidance
- Major security or governance changes
- Why a harness was preferred for a class of work

Do not duplicate the full release ledger in MeatyWiki. Link to the registry and preserve the reasoning.

## 9. Agentic Control Plane

The control plane consumes agent guides and HarnessBOMs to answer:

- Which harness can satisfy the active task for the acting agent?
- Is the capability direct, mediated, experimental, or unknown?
- Which invocation interface is least brittle?
- Does the installed version meet the minimum?
- Is a human approval path required?
- Has CCDash shown this path works in the current environment?
- Is a product transition changing the default route?

Selection order:

1. Hard capability and policy constraints
2. Actor reachability
3. Installed/version availability
4. Runtime evidence
5. Cost/latency preference
6. User preference

## 10. Governance and Evaluation

Human review is mandatory for:

- Changes that reduce sandbox or approval boundaries
- Credential/auth changes
- Deprecation/removal of a capability used by active SkillBOMs
- Product transitions
- Negative claims (`unavailable`)
- New provider/data-access pathways

The governance layer should maintain approved source tiers, curator identities, and promotion rules.

## 11. Writebacks

| Event | Writeback |
|---|---|
| New release | HCR ledger; optional CCDash informational event |
| New capability candidate | HCR review queue; IntentTree task |
| Verified current capability | HarnessBOM + SkillMeat guide |
| Runtime pass/fail | CCDash capability evidence |
| Product transition | MeatyWiki decision + control-plane route update |
| Workflow broken by release | CCDash incident + SkillBOM version constraint |
| Reusable adapter improvement | SkillMeat harness adapter |

## 12. Decision

Adopt HCR as a standalone subsystem that publishes governed capability artifacts to SkillMeat and routing views to the Agentic Control Plane. Preserve release evidence independently from execution telemetry and conceptual memory.
