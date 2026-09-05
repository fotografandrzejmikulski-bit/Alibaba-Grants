# OMEGA-X — 15-Enterprise Pilot Program

## Objective

Validate whether OMEGA-X materially reduces the technical effort and elapsed time required to qualify and execute AWS-to-Alibaba Cloud migration opportunities.

## Cohort design

| Phase | Pilot count | Primary objective |
|---|---:|---|
| M1–2 | 0 external | Platform validation, Alibaba Cloud onboarding, control testing |
| M3–4 | 3 | Early enterprise POCs; establish measurement baseline |
| M5–8 | 7 | Scale repeatability and context reuse |
| M9–12 | 5 | Validate commercial conversion and production-readiness |
| **Total** | **15** | **Enterprise pilot cohort** |

## Pilot selection criteria

Prefer workloads with:

- infrastructure represented through Terraform or equivalent machine-readable configuration,
- clear source architecture ownership,
- a defined target-region requirement,
- permission to run a bounded POC,
- measurable migration effort,
- a realistic production decision within the program period.

## Pilot stages

### 1. Intake
Document workload scope, architecture, dependencies, security requirements, and data-residency constraints.

### 2. Automated assessment
Run ingestion, normalization, architecture mapping, security analysis, and cost-model preparation.

### 3. Human review
A qualified engineer reviews assumptions, findings, generated IaC, and recommended target design.

### 4. Bounded POC
Provision only the resources necessary to validate the critical technical hypotheses.

### 5. Outcome review
Record time saved, engineering effort, validation defects, model consumption, infrastructure cost, and customer decision.

## Conversion criteria

Production conversion requires customer authorization and successful validation of:

- functional requirements,
- security requirements,
- availability/performance requirements,
- cost assumptions,
- data-residency requirements,
- operational ownership.

The program reports negative outcomes as well as successful conversions. This preserves evidentiary integrity.
