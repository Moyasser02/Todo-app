# create_tables.py
import asyncio
from dal.database import engine
from dal.models.todo_model import Base as TodoBase
from dal.models.user_model import Base as UserBase

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(TodoBase.metadata.create_all)
        await conn.run_sync(UserBase.metadata.create_all)

if __name__ == "__main__":
    asyncio.run(create_tables())
