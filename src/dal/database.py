from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from contextlib import asynccontextmanager

from config.environment import get_environment


environment = get_environment()

SQLALCHEMY_DATABASE_URL = environment.DATABASE_URL

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

Base = declarative_base()

@asynccontextmanager
async def get_db():
    async with SessionLocal() as session:
        yield session


