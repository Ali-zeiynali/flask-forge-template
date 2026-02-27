# Testing and Quality

## Test suite

```bash
PYTHONPATH=src python -m pytest
```

## Coverage

```bash
PYTHONPATH=src python -m pytest --cov=src --cov-report=term-missing
```

## Lint and format

```bash
python -m ruff check .
python -m black --check .
python -m black .
python -m ruff check --fix .
```

## Security checks

```bash
python -m bandit -r src
python -m pip_audit
```
