# OMEGA-X — Threat Model

## High-value assets

- customer infrastructure descriptors,
- customer credentials and access tokens,
- generated Infrastructure-as-Code,
- audit/evidence records,
- model context containing customer architecture,
- cloud resources created for pilots,
- grant-funded compute and model capacity.

## Threats and mitigations

| Threat | Risk | Mitigation |
|---|---|---|
| Prompt injection in infrastructure metadata | malicious model behavior | treat input as data; sanitization; policy boundary |
| Secret leakage | credential compromise | secret scanning/redaction; deny secrets in model context |
| Hallucinated IaC | unsafe or broken infrastructure | deterministic validation + human review |
| Privilege escalation | unauthorized cloud actions | least privilege; separate deployment identities |
| Runaway agent loop | cost/API burn | call/time/retry/state budgets |
| Supply-chain manipulation | compromised artifacts | hashes, version pinning, provenance |
| Cross-region data movement | residency violation | explicit region policy + transfer gate |
| Destructive deployment | customer outage/data loss | approval gate + change review |
| Audit tampering | loss of trust/evidence | append-only or immutable audit storage where practical |
| Data exfiltration through tools | confidentiality loss | allowlisted tools, scoped credentials, tool-call logging |

## Security acceptance test

Before external pilot execution, demonstrate at minimum:

1. injection-resilient handling of representative malicious configuration strings,
2. secret-redaction tests,
3. forbidden-action tests,
4. loop termination tests,
5. cross-region transfer denial tests,
6. artifact-integrity tests,
7. human approval enforcement tests.
