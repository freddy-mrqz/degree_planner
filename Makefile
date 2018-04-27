.PHONY: docker up down

CONTAINER=degree_planner

docker:
	docker build -t degree_planner .
up:
	docker-compose up -d
down:
	docker-compose down --remove-orphans
logs:
	docker logs $(CONTAINER)

