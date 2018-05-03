.PHONY: build up up_d up_build up_build_d down logs exec shell 

CONTAINER=degree_planner

build:
	docker build -t degree_planner .
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
exec:
	docker exec -i -t degree_planner /bin/bash
shell:
	docker exec -i -t degree_planner python manage.py shell_plus
reset: down up_build
	@echo "Restarting..."
