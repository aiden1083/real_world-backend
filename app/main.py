from fastapi import FastAPI, APIRouter
from app.api.api import api_router

def create_app() -> FastAPI:
    app = FastAPI(title="RealWorld")
    app.include_router(api_router, prefix="/api")

    return app

app = create_app()