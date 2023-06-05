from pydantic import BaseSettings


class Config(BaseSettings):
    app_name: str = "{{cookiecutter.service_name}}"
    version: str = "0.0.1"
    environment: str = "dev"
    ######
    ## Custom Config Below
    ######
