.PHONY: build sh test dist

name := typecastai-python
version := dev

build:
	@docker build  . -t ${name}:${version} -f ./docker/Dockerfile

sh:
	@docker run --rm -it \
		-v .:/code \
		${name}:${version} \
		bash

test:
	@docker run --rm -it \
		-v .:/code \
		-e typecast_token=${typecast_token} \
		${name}:${version} \
		poetry run pytest -lvs

dist:
	@docker run --rm -it \
		-v .:/code \
		${name}:${version} \
		poetry build
