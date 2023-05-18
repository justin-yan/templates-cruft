FROM {{cookiecutter.registry_dns}}/{{cookiecutter.namespace}}/images/service-py:latest

ENV PYTHONUNBUFFERED True
# https://cloud.google.com/run/docs/issues#home
ENV HOME /home

WORKDIR /svc
COPY . /svc

RUN pipenv sync
CMD exec pipenv run uvicorn scripts.main:app --host 0.0.0.0 --port $PORT
