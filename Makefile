run:
	PYTHONPATH=src python -m flask --app wsgi:app run --debug

test:
	PYTHONPATH=src python -m pytest

coverage:
	PYTHONPATH=src python -m pytest --cov=src --cov-report=term-missing

lint:
	python -m ruff check .
	python -m black --check .

format:
	python -m black .
	python -m ruff check --fix .

audit:
	python -m bandit -r src
	python -m pip_audit

seed:
	PYTHONPATH=src python -m flask --app wsgi:app forge seed
