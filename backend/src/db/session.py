
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker # async engine for DB connections, async session for individual sessions, async sessionmaker to create sessions
from sqlalchemy.orm import declarative_base # define ORM models (tables) as Python classes using the Declarative system declarative_base
from typing import AsyncGenerator # for type hinting of async generator function
from src.core.config import settings

DATABASE_URL = str(settings.DATABASE_URL)

# create engine from DATABASE_URL in .env
engine = create_async_engine(
    DATABASE_URL,
    future=True,
    echo=False,
)

# create session factory for generating new sessions when needed (eg. per request)
AsyncSessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)

# Base class for ORM models to inherit from (declarative base)
Base = declarative_base()

# Dependency to get DB session for request, ensures proper opening/closing of session
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session
