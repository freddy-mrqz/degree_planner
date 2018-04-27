.PHONY: docker up down

docker:
	docker build -t degree_planner .
up:
	docker-compose up -d
down:
	docker-compose down --remove-orphans
