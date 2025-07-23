from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from dal.models.user_model import User
from fastapi import Depends
from dal.deps import get_db


db: AsyncSession = Depends(get_db)


class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_user_by_username(self, username: str):
        result = await self.db.execute(
            select(User).filter(User.username == username)
    )
        return result.scalars().first()

    async def get_user_by_id(self, user_id: int):
        return await self.db.get(User, user_id)

    async def get_all_users(self):
        result = await self.db.execute(
            select(User)
        )
        return result.scalars().all()

    async def create_user(self, user: User):
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user
