# backend/src/core/config.py
from pydantic_settings import BaseSettings
from pydantic import AnyUrl
from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str
    VERSION: str
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    DATABASE_URL: AnyUrl
    BACKEND_CORS_ORIGINS: List[str] = []  # parsed from comma-separated string

    class Config:
        env_file = ".env"   # Pydantic will auto-read .env

settings = Settings()
