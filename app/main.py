from fastapi import FastAPI
from app.routers.api import router as api_router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(api_router, prefix="/v1")
