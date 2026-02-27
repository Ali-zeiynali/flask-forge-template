#!/usr/bin/env bash
set -euo pipefail

python -m flask --app flaskforge.wsgi:app db upgrade
python -m flask --app flaskforge.wsgi:app forge seed
