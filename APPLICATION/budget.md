# OMEGA-X — Grant Budget Framework

The original project brief planned a USD 120,000 annual credit envelope divided as follows: ECS/GPU 72,000; AnalyticDB/OSS 24,000; networking/security 24,000. This repository retains those numbers as a **planning scenario**, not as a guaranteed approved allocation.

## Scenario A — original planning envelope

| Category | Annual planning envelope | Purpose |
|---|---:|---|
| ECS / GPU compute | $72,000 | isolated migration sandboxes, model-support workloads, bounded POC execution |
| Data / context infrastructure | $24,000 | audit history, semantic retrieval, object storage, context infrastructure |
| Network / security | $24,000 | API/gateway, load balancing, perimeter controls, pilot traffic |
| **Total** | **$120,000** | planning ceiling |

## Budget principles

1. Spend follows pilot volume and measured utilization rather than a flat monthly assumption.
2. Production-like resources are introduced only when justified by a pilot stage.
3. Idle infrastructure is scaled down or terminated where operationally safe.
4. Each pilot receives a cost-attribution record.
5. Model consumption is tracked separately from compute, storage, network, and security resources because Model Studio has distinct billing mechanisms.

## Model / token capacity

The original proposal modeled 2 billion Model Studio tokens as approximately 166 million tokens per month. That monthly average is **not** used as a contractual or operational entitlement in the revised application.

Current Alibaba Cloud documentation describes multiple Model Studio mechanisms, including Credits-based Token Plan products, Resource Plans, Savings Plans, and pay-as-you-go inference. Actual consumption depends on model, token usage, thinking mode, tool calls, and cache behavior.

The implementation therefore uses a workload-based model:

**AI cost per migration = model calls × input/output usage profile × applicable model pricing − eligible cache/reuse savings**

Actual values will be measured from console usage data after the chosen account, region, models, and billing mechanism are confirmed.

## Allocation governance

At program start establish a monthly budget review covering:

- compute utilization,
- storage utilization,
- network utilization,
- model inference usage,
- context/cache efficiency,
- pilot-level unit cost,
- forecast versus approved allocation.

Any material variance should trigger architecture, workload, or pilot-scope review.

## Approval rule

No budget figure in this repository should be interpreted as an Alibaba Cloud award. The approved amount, eligible services, duration, region, quota, and expiration are governed by the then-current program terms and any written approval supplied to the applicant.
