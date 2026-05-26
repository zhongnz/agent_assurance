# Contributing

The work in this repository is offered as a contribution to a developing field. Reactions, critiques, extensions, and corrections are welcome through the channels described below.

## What kinds of engagement are useful

**Substantive critique.** The methodology is preliminary and is described as v1.0 of an artifact that will revise as it meets engagement reality. Disagreement with the architectural argument, the necessary-but-insufficient critique of the established disciplines, the threat taxonomy, the design principles, the control matrix's specific controls, the case study's analytical moves, or the reference application's findings is welcome. The methodology improves through testing against serious objection.

**Corrections.** Factual errors, mistaken citations, miscoded mapping-strength labels, broken cross-references, and similar specific corrections are useful and easy to incorporate. The paper has been through three rounds of structured self-review by the author and four rounds of source verification, but external review has not yet occurred and errors remain plausible — a fresh set of eyes typically surfaces things the author has missed.

**Extension proposals.** Additional case studies (other documented agent-security incidents that would benefit from methodology application), additional controls for the matrix (where the OWASP categories or the design principles motivate them), and extensions to non-EU regulatory regimes are areas where the work has acknowledged gaps. Proposals for any of these are welcome.

**Engagement experience.** Application of the methodology to live regulated production deployments produces empirical learning the public-record-only development cannot. Engagement experience that can be shared (with appropriate institutional consent) is the highest-leverage contribution; the methodology depends on it. The templates in `assurance_kit/` and the ten-control subset in `MINIMUM_VIABLE_ASSURANCE.md` (repository root) provide the operational scaffolding most engagement-experience contributions are usefully framed against — what worked, what required adaptation, what the templates missed.

**Editorial feedback.** The paper, case study, and reference application materials are written for serious readers and aim to be precise without being inaccessible. Editorial feedback on places where precision could be improved, terminology could be refined, or argument could be tightened is welcome.

## How to engage

**For substantive comments**, open a GitHub Issue. Issues can reference specific sections of the paper, specific controls in the matrix, or specific findings in the reference application. Threaded discussion in issues is visible to other readers and contributes to the work's collective improvement.

**For corrections to specific text**, opening an issue with the section reference and the proposed correction is the cleanest channel. For larger editorial work, a pull request is welcome but please open an issue first to discuss scope.

**For private feedback**, professional inquiries, or engagement opportunities, the contact mechanism on the author's GitHub profile is the appropriate channel.

**For sensitive disclosures** (security concerns about the methodology itself, regulatory or compliance issues, identification of confidential information that should not be public), please use the channel documented in `SECURITY.md` rather than open issues.

## Issue conventions

Issues benefit from specificity. The most useful issues:

- Reference the specific document and section the issue concerns.
- State the specific concern, correction, or proposal.
- Where possible, propose how the issue might be resolved.

Issues that surface broader methodological disagreements are also welcome, but benefit from being framed as engagement with the work's substantive claims rather than as general commentary.

## Pull request conventions

Pull requests are welcome for:

- Specific text corrections (typo, mistaken citation, broken cross-reference).
- Editorial improvements to existing content.
- Format changes that improve readability without altering substance.

Pull requests for substantive additions (new controls, new case studies, new sections) should be preceded by an issue establishing the scope and the contribution's relationship to the existing work.

The work is licensed under Creative Commons Attribution 4.0 International (CC BY 4.0). Contributions accepted into the repository are licensed under the same terms; by submitting a pull request, you agree to license your contribution under CC BY 4.0.

## What this repository is not

A few things worth being explicit about, given the methodology's domain:

This repository is not a security advisory channel. Security disclosures relating to specific products, services, or vulnerabilities should go to the affected vendor's security response programme, not to this repository. The methodology's case study cites public security disclosures; the repository is not the appropriate venue for new disclosures.

This repository is not a regulatory inquiry channel. Questions about specific regulatory obligations under DORA, the AI Act, or other regimes should go to the relevant supervisor or to qualified legal counsel. The methodology's regulatory anchoring is offered as analytical reference, not as legal advice.

This repository is not a substitute for assurance engagement. The methodology produces assurance-ready evidence; formal attestation requires partnership with a qualified ISAE 3000 or AT-C 205 practitioner. Institutions deploying agents in regulated financial services should not treat the methodology as a substitute for the engagement work the methodology itself acknowledges is required.

## Review and incorporation

Issues and pull requests are reviewed on a rolling basis. The maintainer's response time depends on the volume and substance of incoming engagement; thoughtful issues receive thoughtful replies, and the response should be expected within reasonable bounds rather than within specific service-level commitments.

Substantive contributions accepted into the work are credited in the CHANGELOG entry for the version that incorporates them. Authorship of specific contributions can be acknowledged in the relevant document at the contributor's request.

## Decision policy for methodology disputes

When a contribution proposes a substantive change to the methodology — the architectural argument, the design principles, the threat taxonomy, the control matrix's controls, the regulatory anchoring, or the reference application's structural moves — the maintainer evaluates it against a brief decision protocol. The protocol is informal at present (the project is solo-maintained) and is documented here primarily so contributors know what shape their proposal benefits from taking.

1. **Identify the locus.** Is the proposed change about the paper's architectural argument (§1–§4), the threat taxonomy (§3), specific controls in the matrix (`paper/control_matrix.md`), the case study's analytical moves (`case_studies/echoleak.md`), the reference application's deployment specification or findings, or the assurance kit templates? The locus determines what other parts of the repository the change might propagate into.
2. **Evaluate against the design principles.** Does the change preserve evidence-first, framework-anchored, regulator-legible, composable-and-continuous, and principal-bound (paper §4.2)? Where the change tensions with one principle, the proposal is strengthened by naming the trade-off explicitly rather than eliding it.
3. **Evaluate against the regulatory anchoring.** If the change affects which regulatory articles or standards clauses are cited (AI Act, DORA, ISO/IEC 42001, NIST AI RMF, OWASP Top 10 for Agentic Applications, GDPR), verification against the primary source is expected. The methodology's "regulator-legible" design principle depends on the anchors being accurately labelled.
4. **Consider engagement experience.** Proposals grounded in experience applying the methodology to an actual deployment (with appropriate institutional consent for what is shared publicly) carry particular weight. The methodology is articulated as v1.0 of an artifact that revises as it meets engagement reality; engagement learning is the methodology's intended source of revision pressure.
5. **Decide.**
    - If the proposal is well-grounded and consistent with the methodology's frame, incorporate via PR with the contributor credited in the CHANGELOG entry.
    - If the proposal requires methodology revision rather than a point fix, queue for the next minor version (v0.9 onward) with the relevant ROADMAP.md entry updated.
    - If the proposal represents a different methodology rather than a refinement of this one, decline with reasoning and recommend it as a separate work; engagement on the difference of approach is welcome via Issues.

The maintainer's response is expected to engage the substance of the proposal — agreement or disagreement is welcome, but engagement that names the proposal's specific moves and the reasons for the response is what the contributor benefits from. This is the same standard the work asks of its own arguments.

Formal governance — multi-maintainer review, voting procedures, a code-of-conduct-enforcement committee — will be added if the project's engagement scale grows to require it. See `MAINTAINERS.md` for the current solo-maintainer state and `CODE_OF_CONDUCT.md` for the conduct expectations.
