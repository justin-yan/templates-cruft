from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from functools import lru_cache

from {{cookiecutter.namespace}}.{{cookiecutter.service_name}}.infrastructure.config import Config
from {{cookiecutter.namespace}}.{{cookiecutter.service_name}}.ports.api.health import health_router

def create_app() -> FastAPI:
    app = FastAPI()
    config = Config()

    ########
    ## Route Specification
    ########
    app.include_router(health_router)


    @lru_cache()
    def custom_openapi():
        return get_openapi(
            title=config.app_name,
            version=config.version,
            description=config.environment,
            routes=app.routes,
        )
    app.openapi = custom_openapi

    return app
