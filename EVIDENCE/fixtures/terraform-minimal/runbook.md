# Fixture Validation Runbook

## Objective

Create a reproducible, non-production demonstration of the OMEGA-X source-to-target workflow using the included Terraform fixture.

## Procedure

1. Pin the Terraform CLI version used for the test.
2. Parse `aws/main.tf` without applying infrastructure.
3. Record the discovered resource addresses and source-region metadata.
4. Generate or review `expected-target-artifact.json`.
5. Validate JSON schema and migration policy checks.
6. Run a secret scan over generated artifacts.
7. Confirm the deployment gate remains blocked for fixture-level evidence.
8. Record timestamp, tool versions, commit SHA, result, and operator.

## Evidence classification

Running this procedure locally can establish **E1/E2 artifact-level evidence** depending on reproducibility. It does not establish Alibaba Cloud production capability, customer traction, or measured percentage improvements.

## Required records

- Git commit SHA
- Terraform version
- validator version
- execution timestamp
- stdout/stderr or summarized result
- generated artifact checksum
- operator identity
