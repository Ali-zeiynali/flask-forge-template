run:
	PYTHONPATH=src flask --app wsgi:app run --debug

test:
	PYTHONPATH=src pytest

lint:
	ruff check .

format:
	black .