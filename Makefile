.ONESHELL:
SHELL := /bin/bash

.SILENT:

%:
	@:

DEFAULT_GOAL := help
.PHONY: help
help:
	awk 'BEGIN {FS = ":.*?## "} /^[%a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.PHONY: install
install: ## Create poetry environment and install all dependencies
	poetry install

.PHONY: update
update: ## Create poetry environment and install all dependencies
	poetry update

.PHONY: style-check
style-check: ## Run style checks.
	printf "Style Checking with Flake8, Black and Isort\n"
	poetry run black --config pyproject.toml --check .
	poetry run flake8 --config pyproject.toml --exclude research/ .
	poetry run isort --check-only --diff .

.PHONY: static-check
static-check: ## Run strict typing checks.
	printf "Static Checking with Mypy\n"
	poetry run mypy paper_rock_scissors --config-file pyproject.toml

.PHONY: restyle
restyle: ## Run black and isort linter
	poetry run black --config pyproject.toml .
	poetry run isort --atomic .

.PHONY: test
test:
	poetry run coverage run --rcfile ./pyproject.toml -m pytest ./tests
	poetry run coverage report --fail-under 80

.PHONY: play
play:
	poetry run python paper_rock_scissors/main.py

.PHONY: clean
clean: ## Clean unnecessary files and folders
	@find ./ -type d -name '__pycache__' -exec rm -rf {} +;
	@find ./ -type d -name '.pytest_cache' -exec rm -rf {} +;
	@find ./ -type d -name '.prometheus' -exec rm -rf {} +;
	@find ./ -type d -name '.mypy_cache' -exec rm -rf {} +;
	@find ./ -type d -name 'htmlcov' -exec rm -rf {} +;
	@find ./ -name '.coverage' -exec rm -f {} \;
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '*.pyi' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
