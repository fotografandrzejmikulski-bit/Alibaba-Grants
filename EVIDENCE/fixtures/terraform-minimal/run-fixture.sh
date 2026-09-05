#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

python3 validate_schema.py
python3 validator.py
python3 - <<'PY'
import hashlib
from pathlib import Path
root = Path('.')
files = [
    Path('aws/main.tf'),
    Path('expected-target-artifact.json'),
    Path('expected-target-mapping.md'),
    Path('validation-result.json'),
    Path('runbook.md'),
    Path('validator.py'),
    Path('validate_schema.py'),
]
for p in files:
    print(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p}")
PY
