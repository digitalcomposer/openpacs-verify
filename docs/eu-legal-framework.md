# EU legal and security-framework applicability register

**Review date:** 2026-10-19

**Status:** Initial research assessment; not legal advice or certification.

## Intended use baseline

OpenPACS Verify is currently open research code for synthetic, local,
non-operational environments. It does not decide whether a person may enter a
physical space, operate a real controller, or claim conformity on behalf of a
manufacturer or operator.

Applicability must be reassessed before commercialization, processing personal
data, connection to real OT, autonomous tool execution, use as a safety
component, or deployment by an essential/important entity.

## EU legal register

| Instrument | Current relevance | Project treatment | Reassessment trigger |
|---|---|---|---|
| EU AI Act, Regulation (EU) 2024/1689 as amended | The research workflow may be an AI system when a model integration is provided. Classification depends on intended purpose and deployment. A PACS/critical-infrastructure or regulated-product safety component may change the risk classification. | Document intended purpose and prohibited uses; human oversight; logs; robustness and cybersecurity tests; AI interaction disclosure; risk register. Do not claim high-risk conformity. | Model integration, EU placing on market/putting into service, safety or access decision influence. |
| Cyber Resilience Act, Regulation (EU) 2024/2847 | Non-commercial FOSS is generally outside manufacturer obligations, but commercial supply, stewardship or incorporation can change status. Reporting obligations apply from 11 September 2026; full application is scheduled for 11 December 2027. | Secure development, vulnerability handling, support policy, risk assessment and technical evidence are adopted voluntarily. | Monetization, commercial support, distribution in commercial activity, legal-person stewardship. |
| NIS2, Directive (EU) 2022/2555 and national transpositions | The repository is not itself an essential or important entity. Operators or service providers may have risk-management and incident-reporting duties. | Support risk analysis, incident handling, continuity, supply-chain security, secure development, vulnerability disclosure, cryptography and control-effectiveness evidence. | Deployment by an in-scope operator, managed security provider or supplier. |
| GDPR, Regulation (EU) 2016/679 | Not applicable to synthetic fixtures that cannot identify a person. Real badge identifiers, access events, video, biometrics or model telemetry may be personal data. | Prohibit real personal data publicly; minimisation, purpose limitation, retention, access controls and DPIA screening before any authorized pilot. | Any real person, badge, location, biometric, account or access-event data. |
| Data Act, Regulation (EU) 2023/2854 | Potentially relevant to connected-product data access and contractual use, not to the present local synthetic kernel. | Track as a deployment question; do not ingest product data without authority. | Commercial connected product/service integration. |
| Cybersecurity Act, Regulation (EU) 2019/881 | Certification schemes may provide assurance evidence but this repository is not certified. | Never describe framework mappings as certification. Track relevant EU schemes. | Formal certification or procurement claim. |
| Product Liability Directive (EU) 2024/2853 and national implementation | Could matter if software is supplied as a product and causes damage. | Strong intended-use limits, safety invariants, test evidence and release traceability. | Commercial/public operational release or physical-world integration. |
| Machinery Regulation (EU) 2023/1230 and sector/product rules | Not presently applicable to a research-only synthetic PACS lab; may matter if embedded as a safety component in a regulated product. | No actuator or safety-function integration. | Hardware/product integration. |
| Dual-use and cyber-surveillance export controls | Context- and capability-dependent. A passive assurance tool is lower risk than exploit or intrusion tooling, but classification requires specialist review. | No exploit modules, credential theft, production targeting or surveillance features. | Offensive capability, controlled destination/end user, commercial export. |

## AI Act design file

The following are engineering controls, not a declaration that every listed
obligation legally applies:

| Area | Current artifact | Gap |
|---|---|---|
| Intended purpose and instructions | README, non-goals, policy | User-facing model integration notice |
| Risk management | Threat model and controls matrix | Continuous risk workflow and owners |
| Data governance | Synthetic-only policy and classification | Dataset cards and lineage automation |
| Technical documentation | Architecture, research plan, source ledger | Versioned system/model card |
| Logging and traceability | Structured policy decisions | Integrity-protected evidence journal |
| Transparency | README limitations | Runtime AI disclosure and generated-content metadata where required |
| Human oversight | Review gates | Enforced approval workflow and operator competency criteria |
| Accuracy and robustness | Benchmark targets | Implemented benchmark and uncertainty calibration |
| Cybersecurity | Deny-by-default kernel and threat model | Sandbox, supply-chain provenance, adversarial evaluation |
| Fundamental-rights impact | Avoid real access decisions and personal data | Formal assessment before any real deployment |

## Security and assurance frameworks

These sources are used as complementary lenses; their requirements are not
copied into the repository and no certification is claimed.

| Domain | Frameworks/standards | Intended use |
|---|---|---|
| OT/PACS | NIST SP 800-82 Rev. 3; IEC 62443-3-2, 3-3, 4-1 and 4-2 | Zones/conduits, system risk, component requirements, secure lifecycle |
| AI governance | NIST AI RMF 1.0 and GenAI Profile; ISO/IEC 42001; ISO/IEC 23894 | Govern, map, measure and manage AI risks |
| AI cybersecurity | ENISA multilayer framework; MITRE ATLAS; OWASP guidance for LLM/agentic applications | AI supply chain, prompt injection, unsafe tool use and model abuse |
| Security engineering | NIST CSF 2.0; NIST SSDF SP 800-218; ISO/IEC 27001/27002 | Governance, secure development and operational controls |
| Threat behaviour | MITRE ATT&CK for ICS | Scenario and detection coverage, not proof of vulnerability |
| Application verification | OWASP ASVS | Web/API control verification in synthetic components |
| Product security | CRA essential-requirement mapping and relevant harmonised standards when published | Product lifecycle and vulnerability handling readiness |

## Required legal gates

Before processing non-synthetic evidence or deploying outside loopback:

1. Identify provider, deployer, importer, distributor, manufacturer and operator
   roles.
2. Record jurisdiction, intended purpose, market activity and affected sector.
3. Determine whether AI influences access, biometrics, critical infrastructure,
   safety or a regulated product.
4. Complete personal-data/DPIA screening and confidential-information review.
5. Review CRA product class, open-source/commercial status and reporting duties.
6. Review NIS2 national implementation and operator/supply-chain obligations.
7. Obtain written target authorization and safety-owner approval.
8. Obtain qualified legal advice for the concrete deployment.

## Known uncertainty

EU rules, implementing guidance and harmonised standards continue to evolve.
This register is a dated design input and must be refreshed at every release and
before any operational or commercial use.
