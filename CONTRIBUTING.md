# Contributing

Thanks for contributing to Flask Forge Template.

Repository: https://github.com/Ali-zeiynali/flask-forge-template

## Development setup

### macOS / Linux

```bash
bash scripts/bootstrap.sh
```

### Windows PowerShell

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\bootstrap.ps1
```

## Run checks before opening a PR

```bash
bash scripts/lint.sh
bash scripts/test.sh
```

## Pull request expectations

- Keep changes focused and reviewable.
- Add or update tests for behavior changes.
- Update docs for setup/runtime/API changes.
- Update `CHANGELOG.md` for user-visible changes.
- Ensure CI is green.
