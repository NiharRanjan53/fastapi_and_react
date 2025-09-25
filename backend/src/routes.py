from fastapi import FastAPI
from src.api.v1.home import routes as home_v1
from src.api.v1.auth import routes as auth_v1


def register_routes(app: FastAPI):
    app.include_router(home_v1.router, prefix="/api/v1", tags=["home"])
    app.include_router(auth_v1.router, prefix="/api/v1", tags=["auth"])


    