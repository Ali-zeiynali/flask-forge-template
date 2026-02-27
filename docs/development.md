# Development

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env
```

Commands:

- `make run`
- `make test`
- `make lint`
- `make format`
