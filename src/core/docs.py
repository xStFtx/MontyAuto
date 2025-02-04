from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Automation Enterprise API",
    description="Enterprise-grade automation platform",
    version="1.0.0",
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc"
)

class HealthCheck(BaseModel):
    status: str
    version: str
    database: bool

@app.get("/health", response_model=HealthCheck)
async def health_check():
    return {
        "status": "ok",
        "version": "1.0.0",
        "database": True
    } 