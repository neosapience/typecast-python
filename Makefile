.PHONY: build up down shell test lint format dist

build:
	docker compose build --progress=plain

up:
	docker compose up -d

down:
	docker compose down

shell:
	docker compose exec typecast-sdk-dev /bin/bash

test:
	docker compose exec typecast-sdk-dev poetry run pytest

lint:
	docker compose exec typecast-sdk-dev poetry run black src --check
	docker compose exec typecast-sdk-dev poetry run mypy src

format:
	docker compose exec typecast-sdk-dev poetry run black src
	docker compose exec typecast-sdk-dev poetry run isort .
	
dist:
	docker compose exec typecast-sdk-dev poetry build
	docker compose exec typecast-sdk-dev poetry publish --build
