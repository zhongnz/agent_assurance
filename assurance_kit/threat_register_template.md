# Threat Register — [Agent ID]

*Structured threat enumeration against the deployment specified in `deployment_specification.md`. Organised by OWASP Top 10 for Agentic Applications categories as the consensus ground-truth taxonomy, supplemented by the cross-cutting threat patterns from §3.2 of the position paper. Mirrors the structure of `reference_application/threat_register.md`.*

## Conventions

Severity classifications follow a four-tier scale: *Critical* (high likelihood of exploitation, high consequence, no compensating controls in current configuration); *High* (moderate likelihood of exploitation or high consequence with insufficient compensating controls); *Medium* (lower likelihood of exploitation, or sufficient compensating controls reducing residual risk); *Low* (theoretical exposure with sufficient mitigation in current configuration). Mark threats as *Not present* or *Not applicable* where the configuration does not exhibit the underlying exposure.

For each threat, the entry below has four fields: configuration exposure (how the deployment exhibits the threat), compensating controls in current configuration, evidence requirements (what runtime evidence would be needed to detect, verify, or refute), and recommended controls (which matrix controls address the gap).

The §3.2 patterns of *tool poisoning* and *identity and privilege abuse* are treated within the matching ASI categories (ASI04 and ASI03 respectively) rather than as standalone cross-cutting sections — their content overlaps the ASI categories materially. *Memory and context poisoning* is treated under ASI06 only and is not duplicated as a cross-cutting section. *Lethal trifecta*, *toxic flows*, and *zero-click exfiltration* are treated as standalone cross-cutting sections.

## OWASP Top 10 for Agentic Applications

### ASI01: Agent Goal Hijack — [severity]

**Threat.** [How the deployment exhibits this threat.]

**Configuration exposure.** [Specifics about the deployment's exposure.]

**Compensating controls in current configuration.** [What's in place.]

**Evidence requirements.** [What runtime data would establish presence, absence, or severity.]

**Recommended controls.** [Matrix controls; e.g., LT-01, ZC-01, AT-01.]

### ASI02: Tool Misuse — [severity]

[...]

### ASI03: Identity & Privilege Abuse — [severity]

[...]

### ASI04: Agentic Supply Chain Vulnerabilities — [severity]

[...]

### ASI05: Unexpected Code Execution — [severity OR Not present]

[The v1.0 control matrix does not include controls anchored to ASI05; document explicitly whether the deployment's tool inventory enables code execution and what controls (if any) gate it. For deployments where the agent does not generate, modify, or run code, the threat is typically Not present.]

### ASI06: Memory & Context Poisoning — [severity]

[...]

### ASI07: Insecure Inter-Agent Communication — [severity OR Not applicable]

[For single-agent deployments, mark Not applicable explicitly and note that cross-deployment shared-infrastructure concerns belong under TF-02 (cross-deployment flow review) and CF-01 (failure-domain isolation) rather than under IC-01.]

### ASI08: Cascading Failures — [severity]

[...]

### ASI09: Human-Agent Trust Exploitation — [severity]

[...]

### ASI10: Rogue Agents — [severity]

[...]

## Cross-cutting threat patterns

### Lethal trifecta — [severity]

[Describe the trifecta's presence in this deployment: sensitive data access, untrusted input exposure, egress channel. Note whether the egress channel has external destinations or is internal-only — this materially shapes severity. Reference LT-01.]

### Toxic flows — [severity]

[Describe compositional paths from untrusted-input sources through privileged-data access to egress, identified in the tool inventory. Reference TF-01.]

### Zero-click exfiltration — [severity]

[Describe whether the deployment processes content asynchronously without a human-in-the-loop at the moment of action, and the residual risk that creates. Reference ZC-01.]

## Out-of-OWASP-taxonomy operational concerns

### Resource overload — [severity]

[Document operational-resilience concerns adjacent to the OWASP taxonomy. Reference RO-01.]

## Aggregate severity assessment

[Total counts across all sections above — ASI categories, cross-cutting patterns, and out-of-OWASP-taxonomy operational concerns combined: X Critical / X High / X Medium / X Low / X Not present / X Not applicable. Brief commentary on whether the aggregate reflects a stress-case configuration, a conservative one, or somewhere between. Where useful, split the count into ASI-section subtotals and cross-cutting-section subtotals.]

## Evidence-requirements summary

[Consolidated list of evidence captures the methodology's evidence-first principle requires across the threats above. Cross-reference `evidence_capture_checklist.md` for the operational specification.]

## See also

- `gap_analysis_template.md` — control-by-control evaluation against this threat register
- `paper/full.md` §3.2 — cross-cutting threat patterns documentation
- `paper/control_matrix.md` — the v1.0 control matrix
- `reference_application/threat_register.md` — worked example
