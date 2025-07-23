from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from services.user_service import UserService
from dal.schemas.user_schema import UserCreateRequest, UserLoginRequest, UserResponse
from dal.deps import get_db

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/register")
async def register(user: UserCreateRequest, db: AsyncSession = Depends(get_db)):
    service = UserService(db)
    return await service.register_user(user)

@router.post("/login")
async def login(user: UserLoginRequest, db: AsyncSession = Depends(get_db)):
    service = UserService(db)
    return await service.login_user(user.username, user.password)

@router.get("/{user_id}")
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    service = UserService(db)
    return await service.get_user_by_id(user_id)

@router.get("/")
async def get_all_users(db: AsyncSession = Depends(get_db)):
    service = UserService(db)
    return await service.get_all_users()
