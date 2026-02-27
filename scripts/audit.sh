#!/usr/bin/env bash
set -euo pipefail

python -m bandit -r src
python -m pip_audit
