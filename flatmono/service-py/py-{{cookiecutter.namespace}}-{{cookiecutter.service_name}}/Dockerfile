FROM {{cookiecutter.registry_dns}}/{{cookiecutter.namespace}}/images/service-py:latest

WORKDIR /svc

COPY . /svc

RUN pipenv sync

EXPOSE 8000

CMD ["pipenv", "run" , "uvicorn", "scripts.main:app", "--host", "0.0.0.0", "--port", "8000"]
