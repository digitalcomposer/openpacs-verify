# Security architecture

## Status

Phase 0.5 architecture. The policy kernel, canonical action envelope and
decision-only grant broker are implemented. Process isolation, the OS sandbox,
tool adapters, evidence pipeline, AI planner and digital twin remain planned.

## System context

```text
Synthetic evidence --> Evidence normalizer --> AI analysis planner
       |                                           |
       v                                           v
  Evidence store <------------------------ Finding proposals
                                                   |
                                                   v
Human reviewer --> Signed lab authorization --> Isolated execution broker
                                                   |
                                      canonical action + policy binding
                                                   v
                                        Policy decision point
                                                   |
                                   allow passive operation only
                                                   v
                                        Read-only tool adapter
                                                   |
                                                   v
                                      Local synthetic digital twin
```

There is intentionally no path from the AI planner to an actuator. A future
digital twin may simulate physical state internally, but the public tool adapter
will not expose an actuator operation. The currently implemented
`DecisionBroker` issues and consumes HMAC-protected grants in memory only. It
does not yet run as a separate process and therefore is not an isolation
boundary.

## Assets

- safety policy and authorization records;
- synthetic scenario ground truth;
- evidence objects and integrity hashes;
- findings, confidence and reviewer decisions;
- model prompts, responses and evaluation results;
- build and release provenance.

## Actors

- authorized researcher;
- project maintainer/reviewer;
- untrusted AI model or model service;
- untrusted evidence producer;
- synthetic PACS components;
- CI and dependency providers;
- potential malicious contributor.

## Trust boundaries

1. Imported evidence to the evidence normalizer.
2. Local project to any external model provider.
3. AI output to deterministic policy decision point.
4. Policy decision point to read-only tool adapter.
5. Host to isolated synthetic lab network.
6. Contributor code to protected release pipeline.

## Security invariants

- AI output is data, never executable code.
- No shell command is constructed from model output.
- Targets are explicit IP literals and must belong to the current authorization.
- The public default policy permits loopback only.
- State-changing actions cannot be enabled by editing policy data.
- Authorization is bound to canonical action and policy digests, expires and is
  single-use.
- Mutation, forgery, replay and ambiguous duplicate JSON keys fail closed.
- Missing policy, invalid evidence, ambiguity and timeout fail closed.
- Logs exclude secrets, PINs, badge identifiers and raw personal data.
- Findings must identify evidence and uncertainty.

## Data classification

| Class | Examples | Public repository |
|---|---|---|
| Public | source code, public citations, synthetic fixtures | Allowed |
| Internal | unpublished roadmap, draft reviews | Avoid; private workspace only |
| Confidential | customer topology, vendor NDA material | Prohibited |
| Personal/access data | badge IDs, PINs, access events | Prohibited; synthetic substitutes only |
| Secrets | tokens, passwords, signing keys | Prohibited |

## Quality attributes

- **Safety:** no route to real physical actuation.
- **Security:** least privilege, isolation, integrity and auditable decisions.
- **Reliability:** deterministic authorization and reproducible scenarios.
- **Explainability:** evidence and reason codes accompany each conclusion.
- **Privacy:** synthetic data and minimised telemetry by default.
- **Maintainability:** small typed policy core and versioned control mappings.

## Open architecture questions

- Which local model and hosted-model interfaces should be supported first?
- Which operating system should receive the first independently verified
  sandbox backend? Cross-platform equivalence must not be assumed.
- What evidence format best supports independent verification and redaction?
- Which PACS behaviours can be represented without resembling a proprietary
  protocol or creating a reusable offensive capability?
