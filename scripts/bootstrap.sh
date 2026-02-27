#!/usr/bin/env bash
set -euo pipefail

if ! command -v python >/dev/null 2>&1; then
    echo "python is required but was not found in PATH."
    exit 1
fi

if [ ! -d ".venv" ]; then
    python -m venv .venv
fi

# shellcheck disable=SC1091
source .venv/bin/activate

if ! python -m pip --version >/dev/null 2>&1; then
    python -m ensurepip --upgrade
fi

python -m pip install --upgrade pip
python -m pip install -e ".[dev]"

if [ ! -f ".env" ]; then
    cp .env.example .env
    echo "Created .env from .env.example"
fi

APP_ENTRYPOINT="flaskforge.wsgi:app"

python -m flask --app "$APP_ENTRYPOINT" db upgrade
python -m flask --app "$APP_ENTRYPOINT" forge seed

read -r -p "Create or update an admin user now? [y/N]: " CREATE_ADMIN
if [[ "$CREATE_ADMIN" =~ ^[Yy]$ ]]; then
    read -r -p "Admin email: " ADMIN_EMAIL
    read -r -s -p "Admin password: " ADMIN_PASSWORD
    echo
    read -r -p "Admin full name [Administrator]: " ADMIN_FULL_NAME
    ADMIN_FULL_NAME=${ADMIN_FULL_NAME:-Administrator}

    python -m flask --app "$APP_ENTRYPOINT" forge create-admin \
        --email "$ADMIN_EMAIL" \
        --password "$ADMIN_PASSWORD" \
        --full-name "$ADMIN_FULL_NAME"
fi

echo "Bootstrap complete."
echo "Run the app with: source .venv/bin/activate && python -m flask --app $APP_ENTRYPOINT run --debug"
