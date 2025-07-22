from fastapi import APIRouter, Depends, HTTPException, status
from services import  user_service
from dal.deps import get_db
from dal.models.user_model import User
from dal.schemas.user_schema import UserCreate , UserBase ,UserOut , UserLogin
from exceptions.exceptions import UserNotFoundException, NoUsersFoundException



router = APIRouter(prefix="/users", tags=["users"])

@router.post("/register")
async def register(user: UserCreate):
   return await user_service.register_user(user)

@router.post("/login")
async def login(user: UserLogin):
    return await user_service.login_user(user.username, user.password)

@router.get("/{user_id}")
async def get_user(user_id: int):
    return await user_service.get_user_by_id(user_id)

@router.get("/")
async def get_all_users():
    return await user_service.get_all_users()
  