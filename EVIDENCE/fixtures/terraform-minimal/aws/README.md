# Alpha 0.4 Terraform Fixture

This fixture is intentionally provider-shaped but uses placeholder values. It is a **test artifact**, not a production deployment package.

Expected use:

1. Parse the Terraform configuration without contacting AWS.
2. Build a canonical resource graph.
3. Identify `aws_instance` and `aws_db_instance` resources.
4. Produce a target mapping proposal.
5. Run deterministic schema/policy validation on the generated target artifact.

The `ami` and database credentials are non-functional placeholders. No cloud credentials are required to inspect this fixture.
