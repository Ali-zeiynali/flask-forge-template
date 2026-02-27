#!/usr/bin/env bash
set -euo pipefail

PYTHONPATH=src python -m pytest
PYTHONPATH=src python -m pytest --cov=src --cov-report=term-missing
