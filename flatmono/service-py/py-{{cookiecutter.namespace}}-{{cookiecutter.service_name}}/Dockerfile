FROM {{cookiecutter.registry_dns}}/{{cookiecutter.namespace}}/images/service-py:latest

WORKDIR /svc
COPY . /svc
RUN pipenv sync

ENV PYTHONUNBUFFERED True

CMD exec pipenv run uvicorn scripts.main:app --port $PORT
