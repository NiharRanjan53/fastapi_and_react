from fastapi import FastAPI
from src.core.config import settings
from src.routes import register_routes

def create_app() -> FastAPI:
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

    register_routes(app)

    return  app

app = create_app()