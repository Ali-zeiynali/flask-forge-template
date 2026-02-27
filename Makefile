PYTHONPATH=src

run:
	$(PYTHONPATH) flask --app wsgi:app run --debug

test:
	$(PYTHONPATH) pytest

lint:
	ruff check .
	black --check .

format:
	black .
	ruff check --fix .
