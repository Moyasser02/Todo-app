from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from dal.models.user_model import User

async def get_user_by_username(username: str, db: AsyncSession):
    result = await db.execute(select(User).where(User.username == username))
    return result.scalars().first()

async def get_user_by_id(user_id: int, db: AsyncSession):
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalars().first()

async def get_all_users(db: AsyncSession):
    result = await db.execute(select(User))
    return result.scalars().all()

async def create_user(user: User, db: AsyncSession):
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user
