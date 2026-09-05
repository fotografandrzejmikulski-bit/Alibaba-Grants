# OMEGA-X — Grant Budget Framework

The original proposal planned a USD 120,000 annual credit envelope divided as follows: ECS/GPU 72,000; AnalyticDB/OSS 24,000; networking/security 24,000. fileciteturn0file0L51-L61

This repository retains those planning numbers as a **scenario**, not as a guaranteed approved allocation.

## Scenario A — original planning envelope

| Category | Annual planning envelope | Purpose |
|---|---:|---|
| ECS / GPU compute | $72,000 | isolated migration sandboxes, model-support workloads, POC execution |
| Data / context infrastructure | $24,000 | audit history, vector/semantic retrieval, object storage, context infrastructure |
| Network / security | $24,000 | gateway, load balancing, protection, traffic and pilot perimeter |
| **Total** | **$120,000** | planning ceiling |

## Budget principles

1. Spend follows pilot volume rather than a flat monthly assumption.
2. Production-like resources are introduced only when justified by a pilot.
3. Idle infrastructure is scaled down or terminated.
4. Each pilot receives a cost attribution record.
5. Model consumption is monitored separately from general cloud infrastructure because Alibaba Cloud documents separate billing mechanisms for Model Studio inference and compute resources. citeturn380136search14turn380136search15

## Token / model capacity

The proposal originally modeled 2 billion Model Studio tokens as approximately 166 million tokens per month. fileciteturn0file0L53-L60

For the revised application, this monthly average should **not** be used as a contractual consumption assumption. Current Model Studio documentation includes multiple billing and plan mechanisms, including Credits-based Token Plan products and pay-as-you-go model inference. Pricing also depends on model and cache usage. citeturn380136search1turn380136search8turn380136search14

## Allocation governance

At program start establish a monthly budget review covering:

- compute utilization,
- storage utilization,
- network utilization,
- model inference usage,
- cache efficiency,
- pilot-level unit cost,
- forecast versus approved allocation.

Any material variance should trigger architecture or pilot-scope review.
