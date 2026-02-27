$ErrorActionPreference = "Stop"

if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    throw "python is required but was not found in PATH."
}

if (-not (Test-Path ".venv")) {
    python -m venv .venv
}

$venvPython = Join-Path ".venv" "Scripts/python.exe"
if (-not (Test-Path $venvPython)) {
    throw "Virtual environment Python executable not found at $venvPython"
}

$hasPip = & $venvPython -m pip --version 2>$null
if (-not $?) {
    & $venvPython -m ensurepip --upgrade
}

& $venvPython -m pip install --upgrade pip
& $venvPython -m pip install -e ".[dev]"

if (-not (Test-Path ".env")) {
    Copy-Item .env.example .env
    Write-Host "Created .env from .env.example"
}

$appEntrypoint = "flaskforge.wsgi:app"

& $venvPython -m flask --app $appEntrypoint db upgrade
& $venvPython -m flask --app $appEntrypoint forge seed

$createAdmin = Read-Host "Create or update an admin user now? [y/N]"
if ($createAdmin -match '^[Yy]$') {
    $adminEmail = Read-Host "Admin email"
    $adminPassword = Read-Host "Admin password"
    $adminFullName = Read-Host "Admin full name [Administrator]"
    if ([string]::IsNullOrWhiteSpace($adminFullName)) {
        $adminFullName = "Administrator"
    }

    & $venvPython -m flask --app $appEntrypoint forge create-admin `
        --email $adminEmail `
        --password $adminPassword `
        --full-name $adminFullName
}

Write-Host "Bootstrap complete."
Write-Host "Run the app with: .\\.venv\\Scripts\\Activate.ps1; python -m flask --app $appEntrypoint run --debug"
