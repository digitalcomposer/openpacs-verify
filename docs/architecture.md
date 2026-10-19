# Security architecture

## Status

Initial target architecture. Components beyond the policy kernel are planned,
not implemented.

## System context

```text
Synthetic evidence --> Evidence normalizer --> AI analysis planner
       |                                           |
       v                                           v
  Evidence store <------------------------ Finding proposals
                                                   |
                                                   v
Human reviewer --> Signed lab authorization --> Policy decision point
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
will not expose an actuator operation.

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
- Which sandbox gives the clearest cross-platform network isolation guarantee?
- What evidence format best supports independent verification and redaction?
- Which PACS behaviours can be represented without resembling a proprietary
  protocol or creating a reusable offensive capability?
