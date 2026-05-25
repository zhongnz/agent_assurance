# Evidence Capture Checklist

*Runtime evidence-capture requirements for after-the-fact reconstruction of agent invocations. Operationalises the methodology's *evidence-first* design principle and the v1.0 control matrix's AT-01 (Runtime evidence capture), AT-02 (Evidence-capture privacy controls), and AT-03 (Evidence-store reconstruction queryability) controls. Cross-references GDPR Article 25 (data protection by design).*

## Per-invocation capture (AT-01)

For each agent invocation, the runtime evidence record should contain:

- [ ] **The assembled prompt the model received** — including system instructions, user query, retrieved context (with per-document source metadata), and any intermediate reasoning outputs included in the final context.
- [ ] **The retrieval set** — the documents pulled into context for this invocation, with per-document source identifier, indexing timestamp, and content fingerprint.
- [ ] **Tool definitions available at the moment of invocation** — including tool name, parameter schema, and metadata hash against the approved-tool registry (cross-reference TP-01).
- [ ] **Model reasoning trace** — where the model exposes reasoning steps (e.g., scratchpad outputs, intermediate plan), capture the trace.
- [ ] **Tool calls selected** — name, parameter values, ordering.
- [ ] **Tool outputs returned** — verbatim returns from each tool call, with timestamps.
- [ ] **The model's response in raw form** — before any rendering-layer redaction or post-processing.
- [ ] **The final action(s) taken** — what the agent ultimately did (recommendation produced, payment instruction submitted, escalation routed, etc.).
- [ ] **Egress requests** — where the agent's action produces an outbound network request, the full URL and destination domain, with the linkage to the invocation that triggered it.

## Per-session aggregation

- [ ] **Session ID** linking invocations within a single user session or workflow.
- [ ] **Principal identifier** — the requesting principal (user identity or service-account context).
- [ ] **Timestamp range** covering the session.

## Privacy controls (AT-02)

- [ ] **Data minimisation.** The capture infrastructure does not retain fields beyond what reconstruction requires.
- [ ] **Access control.** Role-based access; review cadence documented; access events logged.
- [ ] **Encryption.** In transit and at rest; key-management process documented.
- [ ] **Retention governance.** Retention period set per applicable obligation — minimum 6 months for AI Act Article 26(6) high-risk systems, longer per institutional policy; deletion process auditable.
- [ ] **Privacy-impact assessment.** Completed for the capture infrastructure; reviewed on material change.
- [ ] **Sensitive-content redaction or exclusion by design.** Personal data, customer secrets, privileged communications redactable or excludable; the redaction policy reviewed under GDPR Article 25.

## Reconstruction queryability (AT-03)

The capture must support the following query types within defined latency criteria. The defined latency depends on the institution's incident-response expectations.

- [ ] **Given a session ID** — return all invocations and their evidence records within latency criterion [X minutes].
- [ ] **Given an output** — return the invocation that produced it and the contextual evidence within [X minutes].
- [ ] **Given a network anomaly (timestamp + destination)** — return the invocation(s) whose egress requests match the anomaly within [X minutes].
- [ ] **Given a malicious input pattern (signature or content excerpt)** — return invocations whose retrieval set or assembled prompt matched the pattern within [X minutes].

## Audit and review

- [ ] **Per-deployment evidence-capture architecture specification** maintained and version-tagged.
- [ ] **Reconstruction-query test suite** exists and is run [quarterly / semi-annually / annually].
- [ ] **Access-control review** completed [quarterly / semi-annually / annually].
- [ ] **Retention-policy audit** completed [annually].
- [ ] **Privacy-impact assessment refresh** completed [per material change or annually, whichever first].

## See also

- `paper/control_matrix.md` AT-01 / AT-02 / AT-03 — the matrix controls this checklist operationalises
- `paper/full.md` §5 — runtime context-capture detail in the reference deployment's specification
- `reference_application/findings/ia_01_01_principal_propagation.md` — worked example showing evidence requirements in context
- `supervisory_engagement_pack_template.md` — the pack the evidence-capture inventory feeds
