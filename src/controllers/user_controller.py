from fastapi import APIRouter, Depends
from services import user_service
from dal.deps import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from dal.schemas.user_schema import UserCreate, UserLogin
from exceptions.exceptions import InvalidUsernameOrPasswordException
from auth import auth_n
from fastapi.security import OAuth2PasswordRequestForm
from typing_extensions import Annotated

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/register")
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await user_service.register_user(user, db)

@router.post("/login")
async def login(user: UserLogin, db: AsyncSession = Depends(get_db)):
    return await user_service.login_user(user.username, user.password, db)

@router.get("/{user_id}")
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    return await user_service.get_user_by_id(user_id, db)

@router.get("/")
async def get_all_users(db: AsyncSession = Depends(get_db)):
    return await user_service.get_all_users(db)

@router.post("/auth")
async def authenticate(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: AsyncSession = Depends(get_db),
):
    user = await user_service.get_user_by_username(form_data.username, db)
    if not user or not auth_n.authenticate_user(user, form_data.password):
        raise InvalidUsernameOrPasswordException()
    token = auth_n.create_access_token(username=user.username, user_id=user.id)
    return {"access_token": token, "token_type": "bearer"}
