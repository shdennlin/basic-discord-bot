PROJECT_NAME=discord-bot
IMAGE_NAME=discord-bot
VERSION=latest
DOCKER_FILE=./Dockerfile
COMPOSE_FILE=./docker-compose.yaml

.PHONY: build
build:
	docker build -t ${IMAGE_NAME}:${VERSION} ${Dockerfile} .

.PHONY: run
run: build
	docker-compose -p ${PROJECT_NAME} -f ${COMPOSE_FILE} up -d

.PHONY: down
down:
	docker-compose -p ${PROJECT_NAME} -f ${COMPOSE_FILE} down
