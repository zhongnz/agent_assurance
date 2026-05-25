# Contributing

The work in this repository is offered as a contribution to a developing field. Reactions, critiques, extensions, and corrections are welcome through the channels described below.

## What kinds of engagement are useful

**Substantive critique.** The methodology is preliminary and is described as v1.0 of an artifact that will revise as it meets engagement reality. Disagreement with the architectural argument, the necessary-but-insufficient critique of the established disciplines, the threat taxonomy, the design principles, the control matrix's specific controls, the case study's analytical moves, or the reference application's findings is welcome. The methodology improves through testing against serious objection.

**Corrections.** Factual errors, mistaken citations, miscoded mapping-strength labels, broken cross-references, and similar specific corrections are useful and easy to incorporate. The paper has been through three rounds of peer review and four rounds of source verification, but errors remain plausible.

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
