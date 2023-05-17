from fastapi import APIRouter

health_router = APIRouter(prefix="/health")

class HealthCheck:
    @health_router.get("/")
    def health_check(self):
        return {"status": "OK"}
