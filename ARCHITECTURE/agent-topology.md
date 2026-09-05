# OMEGA-X — Agent Topology

## Coordinator

Responsibilities:

- create bounded task plans,
- maintain workflow state,
- enforce execution budgets,
- dispatch specialist tasks,
- collect evidence,
- stop workflows that exceed policy limits.

The Coordinator must not directly authorize production deployment.

## Architect Agent

Input:

- normalized AWS resource graph,
- workload requirements,
- availability requirements,
- residency constraints,
- target Alibaba Cloud service catalog.

Output:

- target architecture,
- service mappings,
- dependency risks,
- unresolved assumptions.

## Developer Agent

Input:

- approved target architecture,
- source IaC,
- organization templates.

Output:

- translated IaC,
- configuration changes,
- test artifacts.

All generated artifacts are subject to deterministic validation.

## Security Agent

Checks:

- identity and access configuration,
- public exposure,
- network boundaries,
- encryption requirements,
- secret-handling assumptions,
- data-residency rules,
- configured organizational policies.

The Security Agent produces findings; legal interpretation remains outside the agent's scope.

## Deterministic validator

The validator is intentionally separate from the model agents. It performs machine-verifiable checks such as syntax validation, schema validation, policy evaluation, artifact hashing, and execution-budget checks.

## Human approval

The following actions require an explicit approval boundary:

- production deployment,
- destructive infrastructure changes,
- transfer of customer data outside approved boundaries,
- credential or access-policy changes,
- release of customer artifacts to external parties.

## Failure handling

A failed validation should produce a structured failure record. The system may return to a bounded repair loop, subject to retry and token/call budgets. Repeated failure terminates the workflow and escalates to human review.
