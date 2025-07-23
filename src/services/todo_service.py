from sqlalchemy.ext.asyncio import AsyncSession
from dal.schemas.todo_schema import TodoBase
from dal.models.todo_model import Todos
from exceptions.exceptions import TodoNotFoundException, NoTodosFoundException
from repositries import todo_repo
from auth import auth_z
from exceptions import exceptions
from typing_extensions import Annotated
from fastapi import Depends

user_dependency = Annotated[dict, Depends(auth_z.get_current_user)]


async def create_todo(todo_data: TodoBase , user : user_dependency):
    if not user:
        raise exceptions.AuthenticationException("User not authenticated")
    
    new_todo = Todos(
        title=todo_data.title,
        description=todo_data.description,
        completed=todo_data.completed,
        priority=todo_data.priority,
        owner_id=user.get("id", None) 
    )
    return await todo_repo.create_todo(new_todo)

async def get_all_todos(user: user_dependency):
    todos = await todo_repo.get_all_todos(user.get("id", None))
    if not todos:
        raise NoTodosFoundException()
    return todos

async def get_todo_by_id(todo_id: int, user: user_dependency):
    todo = await todo_repo.get_todo_by_id(todo_id, user.get("id", None))
    if not todo:
        raise TodoNotFoundException()
    return todo

async def update_todo(todo_id: int, todo_data: TodoBase, user: user_dependency):
    existing_todo = await get_todo_by_id(todo_id, user)
    existing_todo.title = todo_data.title
    existing_todo.description = todo_data.description
    existing_todo.completed = todo_data.completed
    existing_todo.priority = todo_data.priority
    existing_todo.owner_id = todo_data.owner_id
    return await todo_repo.update_todo(existing_todo)

async def delete_todo(todo_id: int):
    todo = await get_todo_by_id(todo_id)
    return await todo_repo.delete_todo(todo)
