# Executive Summary — Position Paper v0.8

*A 1-2 page orientation to the paper. Companion to the abstract and the cover note; not a substitute for either.*

## Thesis

The paper argues three connected claims. **First**, that autonomous AI agents in regulated financial services constitute a distinct assurance object — distinguished by architectural properties the established disciplines were not constructed to address in combination. **Second**, that model risk management, AI governance, and cybersecurity are individually necessary but jointly insufficient for the assurance task. **Third**, that the synthesis required is articulable as a working methodology, anchored to the AI Act, DORA, ISO/IEC 42001, NIST AI RMF, and OWASP's agent-specific threat taxonomy, calibrated for the second-line risk level where Tier-2 European banks and insurers will need it.

## The argument arc

**§1 — The Shape of the Problem.** Establishes that agents are a distinct assurance object through five architectural properties (non-determinism, capacity for delegated authority, composite tool chains, runtime-constructed reasoning context, semantic attack susceptibility) and characterises the regulated financial-services deployment context that brings supervisory attention.

**§2 — Framework Insufficiency.** Examines model risk management, AI governance, and cybersecurity in turn; locates the precise gap each leaves and shows the gaps are not coextensive. The "necessary but insufficient" framing is developed here.

**§3 — Threat Taxonomy.** Adopts OWASP's *Top 10 for Agentic Applications* as the consensus vocabulary, then analyses five cross-cutting compositional patterns — tool poisoning, identity and privilege abuse, the lethal trifecta, toxic flows, zero-click exfiltration — that the existing disciplines do not natively address. Concludes with the financial-services amplifications that raise the stakes for regulated deployments.

**§4 — Synthesis Framework.** The methodological core. Articulates five design principles (evidence-first, framework-anchored, regulator-legible, composable and continuous, principal-bound) and presents the control matrix structure. Demonstrates with five illustrative controls, each derived from one threat pattern in §3.

**§5 — Illustrative Reference Application.** Applies the methodology to a hypothetical insurance claims-processing agent, showing how the principles translate into concrete control specifications. The application is calibrated as a stress case representative of patterns observable in the market, not a recommended configuration.

**§6 — Regulatory Horizon.** Maps the in-force, in-approach, and in-formation regulatory architecture — the AI Act, DORA, EU national supervisors, the Digital Omnibus uncertainty — and argues the methodology operates regardless of AI Act timing because DORA applies on its own terms.

**§7 — Recommendations.** Operational guidance for regulated firms with agent deployments: inventory, threat-model, adversarially test, build assurance-ready evidence capture, engage with second-line and supervisor audiences early.

**§8 — Closing.** What the paper has done, what it has not done, and the audiences it addresses.

## Where your perspective would be especially useful

**On the "necessary but insufficient" framing (§2).** Does the model risk management critique correctly locate the object-of-assurance shift, or does it underweight what MRM has historically done with non-deterministic models (stress testing, scenario analysis, statistical validation)? Is the AI governance critique fair to ISO/IEC 42001's actual scope? Is the cybersecurity critique correctly located at semantic instruction-following inside authorised workflows and compositions of permitted calls — rather than at the perimeter or per-action access-check level where most cybersecurity critiques of AI try to locate it?

**On the synthesis methodology (§4).** Do the five design principles feel jointly necessary and non-redundant? Does "regulator-legibility as design property" carry weight as a discrete principle, or does it collapse into framework-anchoring? Does the control matrix carry the analytical weight the paper places on it, or read as taxonomy without methodology?

**On the regulatory characterisation (§1.3 and §6).** Is the characterisation of the EU regulatory architecture accurate from your vantage on the policy work? Is the Digital Omnibus uncertainty (proposed deferral to 2 December 2027, trilogue ongoing) handled appropriately? Are the national-supervisor framings (BaFin's December 2025 / January 2026 ICT-AI guidance, ACPR's compass methodology in Beau's October 2025 speech, DNB's *AI bij verzekeraars*, CSSF's Second Thematic Review with BCL) accurate as conveyed?

**On the evidentiary discipline.** The paper introduces an A/B/C/D evidence-grading convention applied to disclosed incidents and source claims; some macroprudential references in §3.3 were generalised because primary-source verification was not feasible within scope. Reactions to the evidentiary handling — both the conventions and the places where the paper acknowledges its limits — would be especially valuable given your work on empirical legal methodology.

## Where the paper acknowledges it does not go

§8.2 makes the boundaries explicit. The paper does not produce empirical validation of the methodology at scale; it does not deliver a turnkey methodology; it does not constitute formal attestation. The framework is preliminary, the control matrix is v1.0, and specific controls will be revised as the methodology meets engagement reality. If your reaction touches on these limits, knowing where they could be tightened — or where they should be drawn differently — would be useful.
