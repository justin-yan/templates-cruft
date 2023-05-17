from fastapi import FastAPI

from {{cookiecutter.namespace}}.{{cookiecutter.service_name}}.ports.api.health import health_router

def create_app() -> FastAPI:
    app = FastAPI()

    ########
    ## Route Specification
    ########
    app.include_router(health_router)

    return app
