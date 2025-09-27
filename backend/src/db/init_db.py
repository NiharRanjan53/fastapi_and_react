# src/db/init_db.py
import asyncio
from src.db.session import engine, Base

# Import models so they register with Base.metadata
from src.models import user  # noqa: F401

async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("✅ Tables created")

if __name__ == "__main__":
    asyncio.run(init_models())
