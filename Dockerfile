FROM python:3.6
ENV PYTHONUNBUFFERED 1 
ENV C_FORCE_ROOT true

COPY ./requirements.txt /tmp/requirements.txt
COPY ./config /home/docker/config
COPY ./manage.py /home/docker/manage.py
COPY ./src /home/docker/src

RUN pip install -r /tmp/requirements.txt

WORKDIR /home/docker/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
