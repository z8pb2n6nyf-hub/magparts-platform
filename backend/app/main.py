from fastapi import FastAPI

from app.core import settings
from app.core.logging import setup_logging

setup_logging()

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="0.1.0",
    description="Backend API for MagParts Platform",
)


@app.get("/")
async def root():
    return {
        "project": settings.PROJECT_NAME,
        "version": "0.1.0",
        "status": "running",
    }


@app.get("/health")
async def health():
    return {
        "status": "ok",
    }