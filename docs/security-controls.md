# Security controls matrix

Framework mappings express design intent, not certification.

| Control | Threat addressed | Implementation | Verification | Status |
|---|---|---|---|---|
| SC-01 No AI-to-actuator path | TM-01, TM-02 | Declarative `Action`; no executable callback | Unit and architecture tests | Partial |
| SC-02 Deny by default | TM-02, TM-10 | Explicit action, operation and network allow-lists | Negative unit tests | Implemented |
| SC-03 Immutable state-change prohibition | TM-03 | Unsafe kinds rejected even if policy lists them | Policy-construction tests | Implemented |
| SC-04 Target anti-rebinding | TM-02, TM-04 | IP literals only | Hostname denial test | Implemented |
| SC-05 Synthetic-only public data | TM-06, TM-09 | Contribution and repository policy | Review and secret/PII scanning | Process |
| SC-06 Evidence provenance | TM-05, TM-11 | Source ledger; planned evidence IDs/hashes | Finding-schema tests | Partial |
| SC-07 Human oversight | TM-05, TM-11 | Review gates and abstention requirement | Release checklist | Planned |
| SC-08 Audit integrity | TM-05, TM-12 | Structured decisions; signed records planned | Tamper tests | Partial |
| SC-09 Resource isolation | TM-07, TM-10 | Local sandbox/no external route planned | Network and limit tests | Planned |
| SC-10 Supply-chain security | TM-08 | Standard-library core; read-only CI permission | Dependency and workflow review | Partial |
| SC-11 Sensitive input rejection | TM-06 | Denied parameter names; synthetic data policy | Unit tests | Partial |
| SC-12 Coordinated disclosure | Downstream harm | `SECURITY.md` intake and publication gates | Tabletop exercise | Process |

## Framework coverage

- **EU AI Act:** risk management, data governance, technical documentation,
  records, transparency, human oversight, accuracy, robustness and cybersecurity
  are treated as design objectives where applicable.
- **NIST AI RMF:** Govern, Map, Measure and Manage artifacts are represented by
  the governance documents, threat model, benchmark plan and risk treatments.
- **ENISA AI cybersecurity framework:** baseline cybersecurity, AI-specific
  threats and sector-specific OT risks are modelled separately.
- **IEC 62443 concepts:** zones/conduits, least privilege, secure development,
  verification, vulnerability and patch handling guide the lab design.
- **NIST SP 800-82:** OT reliability, safety, architecture and risk-management
  constraints guide the passive-by-default approach.
- **MITRE ATT&CK for ICS:** future scenarios will map behaviour to techniques,
  but mappings will not be treated as proof of exploitability.
- **CRA:** secure-by-design development, vulnerability handling, documentation
  and support-lifecycle evidence are incorporated proactively.
- **NIS2:** risk analysis, incident handling, continuity, supply-chain security,
  secure development, disclosure, cryptography and effectiveness testing inform
  operator-facing controls.

## Control ownership

Until maintainers are formally assigned, the repository owner is accountable
for all controls and release gates. No control is considered independently
assured.
