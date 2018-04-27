FROM python:3.6

ENV PYTHONUNBUFFERED 1 

COPY requirements.txt /home/docker/requirements.txt
COPY docker-entrypoint.sh /docker-entrypoint.sh
COPY scripts/ /home/docker/scripts

RUN pip install -r /home/docker/requirements.txt

WORKDIR /home/docker/degree_planner/

ENTRYPOINT ["./docker-entrypoint.sh"]
