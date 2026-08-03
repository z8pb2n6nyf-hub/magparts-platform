from fastapi import FastAPI

app = FastAPI(
    title="MagParts API",
    version="0.1.0",
    description="Backend API for MagParts Platform",
)


@app.get("/")
async def root():
    return {
        "project": "MagParts",
        "version": "0.1.0",
        "status": "running",
    }


@app.get("/health")
async def health():
    return {
        "status": "ok"
    }
