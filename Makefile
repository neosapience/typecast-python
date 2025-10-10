.PHONY: help install test test-integration lint format check clean build dist publish
.PHONY: docker-build docker-up docker-down docker-shell docker-test
.DEFAULT_GOAL := help

# Colors for output
BLUE := \033[0;34m
GREEN := \033[0;32m
YELLOW := \033[0;33m
NC := \033[0m # No Color

help: ## Show this help message
	@echo "$(BLUE)Typecast Python SDK - Available Commands$(NC)"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  $(GREEN)%-20s$(NC) %s\n", $$1, $$2}'
	@echo ""

# Local Development Commands
install: ## Install dependencies with uv
	uv sync --all-extras

test: ## Run all tests (skip integration tests without API key)
	uv run pytest tests/ -v

test-integration: ## Run all tests including integration tests (requires API key)
	uv run pytest tests/ -v --run-integration

test-watch: ## Run tests in watch mode
	uv run pytest-watch tests/

lint: ## Run all linters (ruff check + mypy)
	uv run ruff check src/ tests/ examples/
	uv run mypy src/

format: ## Format code with ruff
	uv run ruff format src/ tests/ examples/
	uv run ruff check --fix src/ tests/ examples/

check: lint test ## Run linters and tests

clean: ## Clean up build artifacts and cache
	rm -rf dist/ build/ *.egg-info .pytest_cache .mypy_cache .ruff_cache
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete

build: clean ## Build distribution packages
	uv build

publish: build ## Publish to PyPI (requires credentials)
	uv publish

publish-test: build ## Publish to TestPyPI
	uv publish --publish-url https://test.pypi.org/legacy/

# Docker Commands
docker-build: ## Build Docker image
	docker compose build --progress=plain

docker-up: ## Start Docker container in background
	docker compose up -d

docker-down: ## Stop Docker container
	docker compose down

docker-shell: ## Open shell in Docker container
	docker compose exec typecast-dev /bin/bash

docker-test: ## Run tests in Docker
	docker compose exec typecast-dev uv run pytest tests/ -v

docker-lint: ## Run linters in Docker
	docker compose exec typecast-dev uv run ruff check src/ tests/ examples/

docker-format: ## Format code in Docker
	docker compose exec typecast-dev uv run ruff format src/ tests/ examples/

# CI/CD Commands (for CircleCI)
ci-install: ## Install dependencies for CI
	pip install uv
	uv sync --frozen --all-extras

ci-lint: ## Run linters in CI
	uv run ruff check src/ tests/ examples/ --output-format=github
	uv run mypy src/ --junit-xml=test-reports/mypy.xml

ci-test: ## Run tests in CI with coverage
	uv run pytest tests/ -v --junitxml=test-reports/pytest.xml --cov=src/typecast --cov-report=xml --cov-report=html

ci-build: ## Build package in CI
	uv build
	ls -lh dist/

# Development helpers
dev-setup: ## Setup development environment
	@echo "$(BLUE)Setting up development environment...$(NC)"
	uv sync --all-extras
	@echo "$(GREEN)✓ Dependencies installed$(NC)"
	@echo "$(YELLOW)Don't forget to copy .env.example to .env and add your API key!$(NC)"

version: ## Show current version
	@grep '^version = ' pyproject.toml | cut -d'"' -f2
