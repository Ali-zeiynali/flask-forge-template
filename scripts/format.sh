#!/usr/bin/env bash
set -euo pipefail

python -m black .
python -m ruff check --fix .
