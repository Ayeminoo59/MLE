.PHONY: help lint format test

help:
	@echo "Targets:"
	@echo "  make lint    - run ruff lint"
	@echo "  make format  - run ruff formatter"
	@echo "  make test    - run pytest"

lint:
	ruff check .

format:
	ruff format .

test:
	pytest

