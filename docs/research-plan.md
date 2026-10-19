# Research plan

## Scope and audience

OpenPACS Verify is a defensive research platform for OT security researchers,
PACS engineers, AI-safety evaluators and maintainers of authorized laboratory
environments. It is not a penetration-testing product for production systems.

## Primary hypothesis

A constrained AI workflow can improve the speed and consistency of defensive
PACS assurance without being trusted to authorize or execute operational
actions.

## Research questions

1. How accurately can an AI-assisted workflow identify labelled weaknesses in
   synthetic PACS evidence?
2. Can a deterministic broker block every prohibited state-changing,
   out-of-scope and credential-bearing proposal?
3. Does evidence-linked reporting reduce analyst triage time compared with a
   rules-only baseline?
4. How resistant is the workflow to prompt injection and misleading content in
   device metadata, logs and imported documentation?
5. Can the system explain uncertainty and abstain when evidence is insufficient?

## Phases

### Phase 0 — Governance and safety kernel

- clean-room contribution rules;
- source and legal applicability registers;
- threat model and security controls;
- deny-by-default policy engine;
- automated negative tests.

Exit: no state-changing action type can be enabled through configuration.

### Phase 0.5 — Decision-only authorization binding

- canonical, bounded action representation;
- authorization bound to action and complete policy digests;
- short-lived, HMAC-protected, single-use grants;
- rejection of mutation, replay, forgery, duplicate keys and nested sensitive
  parameters;
- architecture tests preventing network and subprocess authority in the
  decision-only package.

Exit: all binding and adversarial unit tests pass. This phase does not claim
process isolation and introduces no execution adapter.

### Phase 1 — Synthetic PACS digital twin

- fictional management service, controller, reader, alarm input and lock state;
- insecure, transitional and hardened profiles;
- synthetic identities and events only;
- local-only container network with no default route to external networks;
- deterministic reset and ground-truth labels.

Exit: every scenario has a reproducible expected state and safety invariant.

### Phase 2 — Evidence collectors and rule baseline

- static configuration and source-fixture analysis;
- passive synthetic PCAP and log ingestion;
- provenance hashes and evidence bundles;
- rules-only findings for comparison.

Exit: collectors do not transmit packets to assessed components.

### Phase 3 — AI-assisted analysis

- untrusted evidence ingestion with prompt-injection labelling;
- schema-constrained finding and action proposals;
- citations to evidence objects rather than free-form claims;
- human review queue and explicit abstention state.

Exit: model output has no direct execution capability.

### Phase 4 — PACS-SafetyBench

- at least 50 labelled scenarios;
- benign, vulnerable, ambiguous and adversarial cases;
- repeated evaluation against rules-only and unconstrained baselines;
- independent replication instructions.

Target metrics, to be reported as measured rather than claimed:

| Measure | Initial target |
|---|---:|
| Finding precision | >= 0.90 |
| Finding recall | >= 0.85 |
| Prohibited-action block rate | 1.00 |
| Evidence citation correctness | >= 0.95 |
| Unsupported high-confidence claims | 0 |
| Repeated-run agreement | >= 0.90 |

### Phase 5 — Authorized pilot

Only after an independent safety review, written authorization and a separate
deployment threat model. The public project remains passive and does not gain
actuator functionality.

## Non-goals

- reproducing vendor exploits or proprietary protocols;
- Internet asset discovery or exposure scanning;
- bypassing access controls;
- controlling locks, alarms, readers or industrial equipment;
- replacing a conformity assessment, legal review or safety engineer;
- making automated decisions about a person's physical access.

## Publication gates

1. Provenance review confirms public or original input only.
2. Secret, personal-data and confidential-material scans are clean.
3. Threat model and risk register reflect the release.
4. Safety tests and CI pass.
5. Vulnerability disclosures have completed coordinated disclosure.
6. Human review confirms claims match evidence and measured results.
