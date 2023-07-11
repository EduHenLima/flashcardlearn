from fastapi import FastAPI

from app.backend.config import settings
from app.routers.api import router as api_router

app = FastAPI()


@app.get("/vars")
async def info():
    return {
        "APP Name": settings.APP_NAME,
    }


app.include_router(api_router, prefix="/v1")
