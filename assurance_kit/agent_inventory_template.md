# Agent Inventory

*Template for the institution-wide inventory of agent deployments. The inventory is the 30-day artifact in §7 of the position paper's recommendations: every agent the institution operates, with the fields needed for downstream methodology work.*

## How to use

For each agent deployment, complete a row in the table below. The fields are the minimum that the threat register, gap analysis, and supervisory-engagement work downstream of the inventory require. Add columns where the institution's internal GRC, model-risk, or audit infrastructure requires additional fields (e.g., model-risk tier, business owner, third-line audit owner, geographic scope).

The inventory is a living artifact. Material change to any field — new tool, change to principal model, change to auto-approval threshold, foundation-model upgrade, change of accountable executive — triggers re-assessment per the methodology's *composable and continuous* design principle.

## Inventory

| Agent ID | Business function | Foundation model | Orchestration framework | Tool count / sensitive-data-tool count | Principal model | Authority surface | Volume / consequence | Oversight regime | Accountable executive | Last review date |
|---|---|---|---|---|---|---|---|---|---|---|
| [e.g., CLM-AGT-01] | [e.g., Insurance claims processing] | [e.g., Claude / Anthropic API] | [e.g., LangGraph] | [e.g., 7 / 3] | [e.g., single service account `claims_agent`] | [e.g., auto-approve <€2,500; route to adjuster otherwise] | [e.g., low tens of thousands / month] | [e.g., quarterly second-line; no real-time human-in-the-loop below auto-approval] | [e.g., CRO] | [YYYY-MM-DD] |
| | | | | | | | | | | |

## Field definitions

**Agent ID.** Institution-internal identifier, unique per deployed agent. Stable across deployment lifecycle.

**Business function.** The business activity the agent supports (claims processing, fraud detection, customer-service triage, internal operations, etc.). One-line description.

**Foundation model.** The model the agent's reasoning runs on; API identifier and provider. Where multiple models are used (e.g., a routing model plus a primary reasoning model), name each.

**Orchestration framework.** The agent framework managing tool invocation, state, and reasoning steps (LangGraph, custom, etc.). Note the framework's version pinning policy.

**Tool count / sensitive-data-tool count.** Two numbers: total count of tools the agent can invoke, and count of those tools that access sensitive data. Detailed tool inventory belongs in the deployment specification, not the inventory entry.

**Principal model.** Whether the agent operates under a single service account, propagates the requesting principal's identity, or uses a hybrid model. The principal model is the methodology's primary identity-and-authority concern (LT-01, IA-01).

**Authority surface.** What the agent is authorised to do without further human approval. Where there is an auto-approval threshold, name it. Where there are escalation thresholds, name them.

**Volume / consequence.** Approximate monthly invocation volume; consequence class (irreversible payments / reversible recommendations / advisory only). Volume informs threat-register severity; consequence informs residual-risk acceptance.

**Oversight regime.** Where the agent sits in the three-lines-of-defence structure; what second-line and third-line review cadence applies.

**Accountable executive.** The named individual accountable for the deployment's risk posture (typically CRO, CIO, or designated officer per institutional structure).

**Last review date.** Last completion date for a full assessment cycle (deployment specification + threat register + gap analysis + findings + residual-risk acceptance).

## See also

- `deployment_specification_template.md` — per-agent detailed specification downstream of the inventory
- `paper/full.md` §7 — recommendations covering the 30/90/180-day cadence the inventory supports
- `paper/control_matrix.md` GP-01 — the matrix control for deployment authorisation, which the inventory feeds
