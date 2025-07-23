from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from dal.models.user_model import User
from dal.deps import get_db

async def get_user_by_username(username: str , db: AsyncSession = next(get_db())):
    result = db.execute(select(User).where(User.username == username))
    return result.scalars().first()

async def get_user_by_id(user_id: int , db: AsyncSession = next(get_db())):

    result = db.execute(select(User).where(User.id == user_id))
    return result.scalars().first()

async def get_all_users(db: AsyncSession = next(get_db())):
    result = db.execute(select(User))
    return result.scalars().all()
    

async def create_user(user: User, db: AsyncSession = next(get_db())):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
