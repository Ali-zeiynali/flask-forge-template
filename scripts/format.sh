#!/usr/bin/env bash
set -euo pipefail

black .
ruff check --fix .
