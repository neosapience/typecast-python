.PHONY: build sh test dist

name := typecast-python
version := dev

build:
	@docker build  . -t ${name}:${version} -f ./docker/Dockerfile

sh:
	@docker run --rm -it \
		-v .:/code \
		typecast-python:dev \
		bash

test:
	@docker run --rm -it \
		-v .:/code \
		-e typecast_token=${typecast_token} \
		typecast-python:dev \
		poetry run pytest -lvs

dist:
	@docker run --rm -it \
		-v .:/code \
		typecast-python:dev \
		poetry build
