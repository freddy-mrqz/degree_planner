.PHONY: docker docker_local up up_d down logs

CONTAINER=degree_planner

docker:
	docker build -t degree_planner .
docker_local:
	docker build -t degree_planner_local -f Dockerfile.local .
up:
	docker-compose up
up_build:
	docker-compose up --build
up_build_d:
	docker-compose up -d --build
up_d:
	docker-compose up -d	
down:
	docker-compose down --remove-orphans
logs:
	docker logs $(CONTAINER)
exec_local:
	docker run --rm -i -t degree_planner_local /bin/bash
exec:
	docker run --rm -i -t degree_planner /bin/bash
reset: down up_build
	@echo "Restarting..."
