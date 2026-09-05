#!/usr/bin/env python3
"""Dependency-free structural validator for the fixture target artifact."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ARTIFACT = ROOT / "expected-target-artifact.json"


def fail(message: str) -> int:
    print(f"FAIL: {message}", file=sys.stderr)
    return 1


def main() -> int:
    try:
        obj = json.loads(ARTIFACT.read_text(encoding="utf-8"))
    except Exception as exc:  # pragma: no cover
        return fail(f"invalid JSON: {exc}")

    required = {"schema_version", "fixture", "source", "target", "resources", "controls", "assumptions"}
    missing = required - obj.keys()
    if missing:
        return fail(f"missing keys: {sorted(missing)}")
    if obj["fixture"] != "terraform-minimal":
        return fail("fixture identifier mismatch")
    if obj["source"].get("provider") != "aws":
        return fail("source provider must be aws")
    if obj["target"].get("provider") != "alibaba-cloud":
        return fail("target provider must be alibaba-cloud")
    if obj["controls"].get("deployment_allowed") is not False:
        return fail("deployment must remain blocked for fixture evidence")
    if obj["controls"].get("human_approval_required") is not True:
        return fail("human approval gate must remain enabled")
    if len(obj["resources"]) < 1:
        return fail("no resources in target artifact")

    for item in obj["resources"]:
        for key in ("source_address", "source_type", "target_service", "mapping_status", "confidence", "notes"):
            if key not in item:
                return fail(f"resource missing {key}")
    print("PASS: target artifact structural validation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
