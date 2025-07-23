from fastapi import APIRouter, Depends, HTTPException, status
from services import todo_service
from dal.schemas.todo_schema import TodoBase, TodoUpdate
from dal.schemas.user_schema import UserInDB
from sqlalchemy.ext.asyncio import AsyncSession
from dal.deps import get_db
from auth.auth_z import get_current_user

router = APIRouter(prefix="/todos", tags=["todos"])

@router.post("/")
async def create_todo(
    todo: TodoBase,
    db: AsyncSession = Depends(get_db),
    current_user: UserInDB = Depends(get_current_user)  
):
    return await todo_service.create_todo(todo, db, current_user.id)

@router.get("/")
async def get_all_todos(
    db: AsyncSession = Depends(get_db),
    current_user: UserInDB = Depends(get_current_user)  
):
    return await todo_service.get_all_todos(db, current_user.id)

@router.get("/{todo_id}")
async def get_todo(
    todo_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: UserInDB = Depends(get_current_user)  
):
    return await todo_service.get_todo_by_id(todo_id, db, current_user.id)

@router.put("/{todo_id}")
async def update_todo(
    todo_id: int,
    updated_data: TodoUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: UserInDB = Depends(get_current_user)  
):
    return await todo_service.update_todo(todo_id, updated_data, db, current_user.id)

@router.delete("/{todo_id}")
async def delete_todo(
    todo_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: UserInDB = Depends(get_current_user)
):
    return await todo_service.delete_todo(todo_id, db, current_user.id)
