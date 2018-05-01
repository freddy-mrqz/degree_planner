FROM python:3.6
ENV PYTHONUNBUFFERED 1 
ENV C_FORCE_ROOT true

COPY ./scripts/ /scripts
COPY ./src /src
RUN pip install -r /src/requirements.txt

CMD ["gunicorn", "config.wsgi", "-b", "0.0.0.0:8000"]
