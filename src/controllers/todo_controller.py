from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from services import todo_service
from dal.schemas.todo_schema import TodoBase, TodoUpdate
from fastapi.security import OAuth2PasswordRequestForm

from auth import auth_z
user_dependency = Annotated[dict, Depends(auth_z.get_current_user)]

router = APIRouter(prefix="/todos", tags=["todos"])

@router.post("/")
async def create_todo(todo: TodoBase , user: user_dependency):
    return await todo_service.create_todo(todo, user)

@router.get("/")
async def get_all_todos(user: user_dependency):
    return await todo_service.get_all_todos(user)

@router.get("/{todo_id}")
async def get_todo(todo_id: int, user: user_dependency):
    return await todo_service.get_todo_by_id(todo_id, user)

@router.put("/{todo_id}")
async def update_todo(todo_id: int, updated_data: TodoUpdate, user: user_dependency):
    return await todo_service.update_todo(todo_id, updated_data, user)

@router.delete("/{todo_id}")
async def delete_todo(todo_id: int, user: user_dependency):
    return await todo_service.delete_todo(todo_id, user)
