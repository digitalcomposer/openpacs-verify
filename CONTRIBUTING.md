# Contributing

Contributions are welcome when they preserve the project's defensive,
vendor-neutral and synthetic-only scope.

## Clean-room declaration

By contributing, you confirm that the contribution:

1. is your original work or is used under a compatible license;
2. does not contain confidential, NDA, employer, customer or personal data;
3. does not reproduce proprietary firmware, protocols, code, diagrams, schemas,
   screenshots, credentials or unpublished vulnerabilities;
4. was developed without testing an unauthorized system;
5. records material public sources in `docs/source-ledger.md`;
6. may be distributed under Apache-2.0.

If employment or another agreement may assign your work to a third party,
obtain written permission before contributing.

## Changes that will not be accepted

- real-world exploit modules or production target discovery;
- Internet scanning or exposure fingerprints;
- credential extraction or default-password collections;
- actuator, relay, lock, alarm or door-control operations;
- safeguards that can be disabled through normal configuration;
- claims of legal compliance, certification or vendor endorsement;
- real access-control data or realistic secrets.

## Development workflow

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
```

Pull requests should state:

- intended defensive outcome;
- affected assets/trust boundaries;
- tests added, especially negative safety tests;
- provenance of external inputs;
- threat-model and legal-register impact;
- residual risk.

Security-relevant changes require review by a maintainer other than the author
once the project has multiple maintainers.
