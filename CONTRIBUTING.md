# Contributing

Thanks for contributing.

## Development Setup

1. Create a virtual environment.
2. Install dependencies.
3. Copy environment variables.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env
```

## Run Locally

```bash
make run
```

## Quality Checks

```bash
make lint
make format
make test
```

## Commit Guidelines

- Use clear, imperative commit messages.
- Keep commits focused and small.
- Update tests and documentation with changes.
- Update `CHANGELOG.md` for user-visible changes.

## Pull Request Guidelines

- Fill out the PR template.
- Ensure CI is green.
- Describe intent, scope, and test evidence.
