# src/dal/deps.py
from collections.abc import AsyncGenerator
from dal.database import SessionLocal
from sqlalchemy.ext.asyncio import AsyncSession
from dal.database import engine
from sqlalchemy.ext.asyncio import async_sessionmaker

async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session