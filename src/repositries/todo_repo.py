from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from dal.models.todo_model import Todos
from dal.deps import get_db


async def get_todo_by_id(todo_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Todos).where(Todos.id == todo_id))
    return result.scalars().first()


async def get_todos_by_owner(owner_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Todos).where(Todos.owner_id == owner_id))
    return result.scalars().all()


async def get_all_todos(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Todos))
    return result.scalars().all()


async def create_todo(todo: Todos, db: AsyncSession = Depends(get_db)):
    db.add(todo)
    await db.commit()
    await db.refresh(todo)
    return todo

async def update_todo(todo: Todos, db: AsyncSession = Depends(get_db)):
    await db.commit()
    await db.refresh(todo)
    return todo

async def delete_todo(todo: Todos, db: AsyncSession = Depends(get_db)):
    await db.delete(todo)
    await db.commit()
