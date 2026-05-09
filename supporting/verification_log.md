# Verification Log — Position Paper v0.8

This log records the primary-source verification performed on the 51 [VERIFY:] / [UNCERTAIN:] markers carried in v0.7. All have been resolved through web verification of primary or directly-corroborating sources. No markers remain in the paper.

## Section 1 — The Shape of the Problem (9 markers, all resolved)

**§1.1 EchoLeak / CVE-2025-32711 / Aim Labs.** Microsoft as CNA confirmed via OpenCVE / NVD record (cveMetadata.assignerOrgId = Microsoft, datePublished 2025-06-11T13:22:38.935Z). Aim Labs of Aim Security confirmed as discloser via aim.security/lp/aim-labs-echoleak-m365 reference in the CVE record and via secondary corroboration (Checkmarx, SOC Prime, Information Security Buzz). Mechanism description refined: exfiltration via reference-style markdown image link auto-fetched through Microsoft Teams proxy permitted by content security policy — confirmed via arXiv paper 2509.10540 (academic case study) and Checkmarx technical writeup.

**§1.1 SpAIware (Rehberger).** 20 September 2024 BSides Vancouver Island disclosure confirmed via Embrace The Red original blog post (timeline section explicitly lists "September, 20 2024: Disclosure at BSides Vancouver Island 2024"). Independent corroboration via The Hacker News, Vulcan Cyber, SC World.

**§1.1 AgentFlayer (Zenity Labs / Bargury, Sharbat).** 6 August 2025 Black Hat USA confirmed via Zenity Labs / PRNewswire press release ("LAS VEGAS, Aug. 6, 2025"). Researchers Michael Bargury (Zenity co-founder/CTO) and Tamir Ishay Sharbat confirmed. Six-platform target list (ChatGPT, Microsoft Copilot Studio, Salesforce Einstein, Google Gemini, Microsoft 365 Copilot, Cursor with Jira MCP) confirmed.

**§1.1 Shadow Escape (Operant AI).** 22 October 2025 confirmed via GlobeNewswire press release and corroborating secondary sources (Cyber Magazine, Manila Times, IT Business Net). Cross-platform across ChatGPT, Claude, Gemini confirmed; framing as "first zero-click agentic attack via MCP" confirmed.

**§1.2 MCP origin and AAIF donation.** 25 November 2024 Anthropic launch confirmed via Anthropic announcement page (anthropic.com/news/model-context-protocol) and corroborating secondary sources (Wikipedia, Pento, Zuplo, mindstudio.ai) — David Soria Parra and Justin Spahr-Summers as creators; SDKs in Python and TypeScript at launch. 9 December 2025 AAIF formation confirmed via Linux Foundation press release. Founding contributions: Anthropic's MCP, Block's goose, OpenAI's AGENTS.md. Platinum members: AWS, Anthropic, Block, Bloomberg, Cloudflare, Google, Microsoft, OpenAI.

**§1.3 ECB SSM Supervisory Priorities 2026-2028.** Published 18 November 2025 confirmed via bankingsupervision.europa.eu primary text. Priority 2 (operational resilience and ICT capabilities) covers AI focus including generative AI applications; commitment to "step up effort to engage with banks on how they use new technologies, and in particular AI" confirmed. The earlier "AI Board Subgroup on Financial Services" framing softened to "institutional engagement signalling sustained supervisory attention" — the phrase appears to refer to the EU AI Board's Subgroup on Financial Services rather than an ECB-internal structure.

**§1.3 BaFin guidance.** 18 December 2025 (German publication) and 30 January 2026 (English) — *Guidance on ICT Risks in the Use of AI at Financial Entities* — verified in earlier rounds. Treats AI systems as a sub-case of network and information systems under DORA Article 3(2); addresses AI strategy, asset inventory, ICT lifecycle integration, and adversarial-input handling.

**§1.3 DNB *AI bij verzekeraars*.** Published 27 March 2025 (English title: *AI at Insurers: opportunities and risks*) confirmed via Stibbe and Lexology technical analyses. 36-insurer 2024 survey, 15 reporting AI use in fraud detection / claim-amount estimation. SAFEST principles framework (predecessor 2019 joint with AFM) identified as foundation.

**§1.3 ACPR Beau speech.** 27 October 2025 Lisbon "A compass to guide us toward intelligent AI supervision" + December 2025 *Archives de philosophie du droit* Tome 66 article — verified in earlier rounds. Four-criterion methodology: appropriate data management, performance, stability, explainability.

**§1.3 EIOPA Opinion BoS-25-360.** Published 6 August 2025, *Opinion on AI Governance and Risk Management* — verified via direct PDF retrieval (88342342-a17f-... reference). Six-area structure (fairness and ethics, data governance, documentation, transparency and explainability, human oversight, accuracy/robustness/cybersecurity) under IDD, Solvency II, DORA, Commission Delegated Regulations 2015/35 and 2017/2358.

**§1.3 DNB statistic.** 15 of 36 insurers reporting AI use in fraud detection and claim-amount estimation — confirmed via Stibbe / Lexology coverage of the DNB publication.

**§1.3 CBEST 2014 / TIBER-EU May 2018.** CBEST established 2014 by Bank of England with PRA, FCA, and FMID supervisory community confirmed via Bank of England implementation guide. TIBER-EU developed jointly by ECB and EU national central banks, approved by Governing Council of the ECB and published in May 2018 confirmed via ECB *What is TIBER-EU?* page.

**§1.4 SR 11-7 / SR 26-2 reproducibility framing.** Reframed to align with the SR 26-2 supersession (verified in earlier round: 17 April 2026 joint Federal Reserve / OCC / FDIC issuance, explicit exclusion of generative AI and agentic AI). Updated text speaks of MRM as a discipline whose object of assurance is models whose inputs, assumptions, outputs, and validation samples can be specified at validation time, contrasting with agent execution paths conditioned on probabilistic inferences.

**§1.4 AI Act Article 12.** Exact text confirmed via multiple primary-source mirrors (artificialintelligenceact.eu, ai-act-service-desk.ec.europa.eu, euaiact.com): "High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system... appropriate to the intended purpose of the system." Article 26(6) six-month minimum retention confirmed; cross-reference to Article 19 (10-year documentation retention) noted.

## Section 2 — Framework Insufficiency (5 markers, all resolved)

**§2.1 PRA SS1/23.** Published 17 May 2023 as part of PS6/23, effective 17 May 2024 — confirmed via Bank of England primary text (bankofengland.co.uk/prudential-regulation/publication/2023/may/model-risk-management-principles-for-banks). UK-incorporated banks, building societies, PRA-designated investment firms with internal model approval; expectations relevant to model financial reporting purposes.

**§2.2 ISO/IEC 42001:2023.** Published December 2023 — confirmed via multiple corroborating sources (ISO official site, Microsoft Learn, KPMG, Deloitte, Accorian).

**§2.2 NIST AI RMF 1.0 / NIST AI 600-1.** AI RMF 1.0 published January 2023; AI 600-1 (Generative AI Profile) published July 2024 — confirmed via Modulos Docs and Kiteworks technical analyses.

**§2.3 ISO/IEC 27001:2022 / NIST CSF 2.0.** ISO 27001:2022 (October 2022 revision, 93 controls across 4 themes); NIST CSF 2.0 (released 26 February 2024, six core functions including "Govern") — confirmed via HITRUST, Secureframe, Cyber Compliance Authority comparative analyses.

**§2.4 NIST SP 800-207 / MCP June 2025 spec.** NIST SP 800-207 (Zero Trust Architecture) published August 2020 — confirmed via NIST CSRC primary site. MCP 18 June 2025 spec major changes confirmed: OAuth 2.0 Resource Server classification (RFC 9728 Protected Resource Metadata), mandatory Resource Indicators (RFC 8707), "Streamable HTTP" replacing SSE — verified via modelcontextprotocol.io, Auth0 technical analysis, ForgeCode, Aaron Parecki blog post.

## Section 3 — Threat Taxonomy (17 markers, all resolved)

**§3.1 OWASP Top 10 for Agentic Applications.** Released 9 December 2025 at the London Agentic Security Summit (during Black Hat Europe 2025) — confirmed via OWASP GenAI Security Project primary site (genai.owasp.org/2025/12/09/owasp-top-10-for-agentic-applications-the-benchmark-for-agentic-security-in-the-age-of-autonomous-ai/) and corroborating secondary sources (Palo Alto Networks, Promptfoo, Practical-DevSecOps, Straiker, Giskard). 100+ contributors with Distinguished Expert Review Board including representatives from NIST, Alan Turing Institute, Microsoft AI Red Team, AWS, Cisco/CAMLIS, Oracle Cloud, CoSAI, Zenity. Categories ASI01-ASI10 confirmed.

**§3.2.1 MCPTox.** arXiv:2508.14925 (August 2025); AAAI 2026 proceedings publication confirmed in earlier round.

**§3.2.2 General Analysis Supabase/Cursor.** 6 July 2025 disclosure confirmed; Simon Willison blog post and Supabase security team published response confirmed as corroboration.

**§3.2.2 MCP June 2025 spec.** 18 June 2025 revision confirmed (see §2.4 above).

**§3.2.2 Asana incident.** Discovered 4 June 2025; server taken offline 5 June; restored 17 June 2025; ~1,000 customers affected; tenant-isolation logic flaw — confirmed via Pomerium ("Approximately 1,000 customers were potentially exposed between June 5 and June 17, 2025"), BleepingComputer ("a spokesperson has told us the incident impacts roughly 1,000 customers"), UpGuard, Adversa AI, Quilr AI.

**§3.2.3 Lethal trifecta attribution.** Coined by Simon Willison in blog post 16 June 2025 ("The lethal trifecta for AI agents: private data, untrusted content, and external communication") — confirmed via simonwillison.net primary source and corroborating secondary references (Lou Franco, Constellation Foundation, Oso Security, HiddenLayer, Xavor).

**§3.2.3 EchoLeak / AgentFlayer.** Both verified above.

**§3.2.3 Invariant Labs GitHub MCP disclosure.** 26 May 2025 — verified in earlier round; GitHub incident response timeline corroborated.

**§3.2.4 Snyk × Invariant.** 24 June 2025 — verified in earlier round.

**§3.2.5 Shadow Escape / Month of AI Bugs.** Shadow Escape verified above. Month of AI Bugs (Johann Rehberger) August 2025 confirmed via Embrace The Red announcement, Simon Willison's "Summer of Johann" coverage, monthofaibugs.com landing page, and 39c3 conference talk announcement. 20+ daily disclosures across ChatGPT, Codex, Anthropic MCPs, Cursor, Amp, Devin, OpenHands, Claude Code, GitHub Copilot, and Google Jules.

**§3.3 GDPR Articles 33/34.** 72-hour notification to supervisory authority (Art. 33) and communication to data subject (Art. 34) — verified.

**§3.3 AI Act Annex III.** Section 5(b) creditworthiness assessment and credit scoring; Section 5(c) life-and-health insurance pricing and risk assessment — verified.

**§3.3 FSB report.** *The Financial Stability Implications of Artificial Intelligence*, published 14 November 2024 — confirmed via fsb.org primary site and BIS executive summary mirror. Vulnerabilities: third-party dependencies and service-provider concentration, market correlations, cyber risks, model risk and data quality and governance.

**§3.3 Other macroprudential references.** BoE FPC, ECB FSR, IMF GFSR, BIS publications consolidated to forms supported by available evidence (see §6.3 below for the BoE FPC verification). Specific paper references (BIS Papers 154, ECB FSR May 2024 Leitner et al., IMF GFSR October 2024 Chapter 3, Lopez-Lira NBER WP 34054) generalised in body text to avoid claiming specific details I have not independently confirmed; the substantive claim — that concentration and correlation are flagged macroprudential concerns — is well-supported.

## Section 4 — Synthesis Framework (10 markers, all resolved)

**§4.1 GDPR Article 25.** Data protection by design and by default — verified.

**§4.1 ISAE 3000 (Revised) / AT-C 205.** ISAE 3000 (Revised) issued by IAASB; AT-C 205 issued by AICPA — verified in earlier rounds; both structure assurance engagements around evidence-based reasonable or limited assurance.

**§4.2 Cross-walking references.** CSA CCM (Cloud Controls Matrix); NIST SP 800-53 mapping to ISO/IEC 27001 (CSRC OLIR catalog reference 154 verified); CIS Controls cross-walks to NIST CSF and ISO 27001 — all verified as established cross-walking lineage.

**§4.2 CBEST/TIBER-EU/DORA TLPT articles.** CBEST 2014, TIBER-EU May 2018 verified above. DORA Articles 24-27 (testing programme, basic requirements, advanced TLPT) confirmed.

**§4.3 NIST SP 800-207.** August 2020 — verified.

**§4.3 AI Act Articles 14/15.** Article 14 (human oversight) and Article 15 (accuracy, robustness and cybersecurity) — confirmed.

**§4.3 DORA Articles 9/17/18/28.** Article 9 (protection and prevention); Articles 17-18 (ICT-related incident management process and incident classification); Article 28 (general principles for ICT third-party risk management) — confirmed.

**§4.3 ISO 42001 Annex A.6.2 / NIST AI RMF Manage 2.** ISO 42001 Annex A controls including third-party relationships clause; NIST AI RMF Manage function 2 (managing risks from third-party AI systems and resources) — confirmed.

**§4.2/§4.3 Control matrix references.** The full control matrix is now presented as a companion document (`paper/control_matrix.md`) covering 26 controls across all ten OWASP Top 10 for Agentic Applications categories, the five cross-cutting threat patterns, and additional governance and evidence-capture areas. Earlier paper revisions referenced the matrix as forthcoming; v1.0 of the matrix is now in the repository.

## Section 5 — Illustrative Reference Application (4 markers, all resolved)

**§5.1 EIOPA digitalisation.** Resolved via EIOPA Opinion BoS-25-360 reference plus DNB 15-of-36 statistic.

**§5.2 LangGraph.** LangChain Inc.-maintained open-source orchestration framework for long-running stateful agents; MIT-licensed; used in production by Klarna, Replit, Elastic, Uber, J.P. Morgan; 600+ integrations; "low-level orchestration framework" framing confirmed via official LangChain documentation, GitHub README, and AWS Prescriptive Guidance.

**§5.2 UNCERTAIN admission about deployment configuration.** Retained as plain prose acknowledged limitation rather than as bracketed marker; the substantive caveat that the configuration is plausible-as-representative rather than directly observed at any specific institution is preserved.

**§5.4 DORA Article 17.** ICT-related incident management process — covering detection, classification, response, recovery, and post-incident review — confirmed.

## Section 6 — Regulatory Horizon (5 markers, all resolved)

**§6.1 AI Act timing / Digital Omnibus.** Original timeline confirmed: into force 1 August 2024; prohibited practices applicable from 2 February 2025; GPAI obligations from 2 August 2025; high-risk obligations from 2 August 2026 (in original text). Digital Omnibus on AI proposal (COM(2025) 836) of 19 November 2025 confirmed via European Commission digital-strategy site, IAPP, Sidley Austin, Skadden, Morrison Foerster, Jones Day, DLA Piper, PwC, European Parliament Legislative Train Schedule. Deferral to 2 December 2027 (Annex III stand-alone high-risk) and 2 August 2028 (Annex I product-embedded high-risk) linked to availability of standards/Commission tools. Council position 13 March 2026; Parliament IMCO/LIBE joint report on file 2025/0359(COD) early 2026. Trilogue 28 April 2026 ended without agreement; provisional agreement reached in the early hours of 7 May 2026, confirming the deferred dates (Council of the EU press release 7 May 2026; Bird & Bird, IAPP, DLA Piper, Hogan Lovells, Timelex, Ropes & Gray, A&O Shearman, NicFab convergent on the substantive content). Formal adoption pending; legal-linguistic revision and Council/Parliament endorsement targeted before 2 August 2026.

**§6.1 GPAI applicability.** 2 August 2025 — confirmed.

**§6.3 DNB.** *AI bij verzekeraars: kansen en risico's* / English *AI at Insurers: opportunities and risks*, March 2025 — see §1.3 verification above.

**§6.3 CSSF Second Thematic Review.** *Second thematic review on the use of Artificial Intelligence in the Luxembourg financial sector*, published 16 May 2025 jointly with Banque centrale du Luxembourg (BCL). Survey June-August 2024, 461 institutions surveyed, 86% response rate, 402 use cases identified — confirmed via CSSF primary publication page (cssf.lu) and BCL press release.

**§6.3 ECB SSM Priorities 2026-2028.** Published 18 November 2025 — see §1.3 above.

**§6.3 BoE FPC.** *Financial Stability in Focus: AI in the financial system*, published 9 April 2025 — confirmed via Global Regulation Tomorrow, A&O Shearman, Bank of England written evidence to Treasury Committee. Four areas: greater use of AI in banks' and insurers' core financial decision-making, greater use of AI in financial markets, operational risks in relation to AI service providers, changing external cyber threat environment.

**§6.3 BIS publications.** Generalised to forms supported by available evidence (BIS Working Papers and FSI Insights series on regulating AI in the financial sector) rather than claiming specific publication identifiers I have not independently confirmed.

**§6.5 CBEST/TIBER-EU.** See §1.3 verification above.

## Section 7 — Recommendations (1 marker, resolved)

**§7 AgentDojo.** Active and current as of late 2025/early 2026 — confirmed via NeurIPS 2024 publication (arXiv:2406.13352, Debenedetti et al., ETH Zurich SPY Lab); GitHub repository at ethz-spylab/agentdojo with leaderboard at agentdojo.spylab.ai; UK and US AI Safety Institute extension as part of joint red-teaming exercise (per UK Government BEIS Inspect Evals integration documentation). Continues to be cited as comparative benchmark in active research literature through 2025/early 2026.

## Items still pending direct primary-source verification before publication

— None as of v0.8. All 51 markers from v0.7 resolved.

## Verification methodology

The verification was performed through targeted web searches against primary or directly-corroborating secondary sources. For dated publications (CVE records, regulatory documents, academic papers), date and identifier verification used the issuing authority's primary site or an authoritative mirror (NIST CSRC, ECB, EIOPA PDF, BaFin German/English releases, OWASP project pages, vendor security advisories, NeurIPS and arXiv records). For attribution claims (e.g. "Simon Willison coined the term lethal trifecta"), verification used the original blog post or speech text, supplemented by independent corroboration. For incident timelines, verification cross-referenced disclosing-firm announcements with vendor responses and independent security reporting. For institutional positions and timelines (Digital Omnibus on AI, trilogue process), verification used multiple law-firm and policy-tracker analyses convergent on the same dates and substantive content.

Where independent primary verification of a specific publication identifier was not feasible within the verification scope, the body text was generalised to forms supported by the available evidence rather than claiming specific details I had not confirmed (notably: BIS Papers 154, IMF GFSR Chapter 3 specifics, ECB FSR Leitner et al., Lopez-Lira NBER WP 34054). The substantive claim — that concentration and correlation are flagged macroprudential concerns — remains supported by the FSB report and the broader regulatory record.
