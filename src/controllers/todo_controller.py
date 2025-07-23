from fastapi import APIRouter, Depends, HTTPException, status
from services import todo_service
from dal.schemas.todo_schema import TodoBase, TodoUpdate


router = APIRouter(prefix="/todos", tags=["todos"])

@router.post("/")
async def create_todo(todo: TodoBase):
    return await todo_service.create_todo(todo)

@router.get("/")
async def get_all_todos():
    return await todo_service.get_all_todos()

@router.get("/{todo_id}")
async def get_todo(todo_id: int):
    return await todo_service.get_todo_by_id(todo_id)

@router.put("/{todo_id}")
async def update_todo(todo_id: int, updated_data: TodoUpdate):
    return await todo_service.update_todo(todo_id, updated_data)

@router.delete("/{todo_id}")
async def delete_todo(todo_id: int):
    return await todo_service.delete_todo(todo_id)
