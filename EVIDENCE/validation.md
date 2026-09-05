# OMEGA-X — Validation Plan

## Validation layers

### Unit validation

Validate parsers, canonical resource models, service-mapping rules, policy rules, hashing, loop detection, budget enforcement, and report generation independently.

### Fixture validation

Maintain representative AWS/Terraform fixtures covering:

- compute,
- managed database,
- object storage,
- VPC/networking,
- IAM,
- load balancing,
- common security controls,
- multi-tier applications.

### Golden-output validation

For deterministic translation rules, preserve expected target-resource structures and compare generated output with tolerance for non-semantic ordering differences.

### Model evaluation

Measure:

- correct service mapping,
- IaC compilation/syntax success,
- policy-finding precision/recall where ground truth exists,
- hallucination rate,
- unnecessary resource creation,
- repair-loop frequency,
- total model consumption.

### Human review

A qualified engineer signs off pilot outputs before infrastructure promotion.

## Release gates

A release cannot be promoted when:

- critical validator tests fail,
- security-gating tests fail,
- execution can exceed configured budget limits,
- generated artifacts are not traceable to a source input and model/version metadata,
- audit records are incomplete.

## Pilot benchmark

For each pilot maintain a paired comparison where feasible:

**baseline workflow** vs **OMEGA-X workflow**

with the same scope, source artifacts, and review requirements.

Record elapsed time and human effort separately. This prevents model-speed improvements from being confused with reductions in total project effort.
