from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from dal.models.todo_model import Todos
from fastapi import Depends
from dal.deps import get_db


db: AsyncSession = Depends(get_db)


class TodoRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_todo_by_id(self, todo_id: int):
        return await self.db.get(Todos, todo_id)


    async def get_todos_by_owner(self, owner_id: int):
        result = await self.db.execute(
            select(Todos).filter(Todos.owner_id == owner_id)
        )
        return result.scalars().all()

    async def get_all_todos(self):
        result = await self.db.execute(select(Todos))
        return result.scalars().all()

    async def create_todo(self, todo: Todos):
        self.db.add(todo)
        await self.db.commit()
        await self.db.refresh(todo)
        return todo

    async def update_todo(self, todo: Todos):
        await self.db.commit()
        await self.db.refresh(todo)
        return todo

    async def delete_todo(self, todo: Todos):
        await self.db.delete(todo)
        await self.db.commit()
