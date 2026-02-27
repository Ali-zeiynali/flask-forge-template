#!/usr/bin/env bash
set -euo pipefail

PYTHONPATH=src flask --app wsgi:app db upgrade
PYTHONPATH=src flask --app wsgi:app forge seed
