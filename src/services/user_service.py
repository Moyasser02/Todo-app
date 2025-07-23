from sqlalchemy.ext.asyncio import AsyncSession
from dal.schemas.user_schema import UserCreate
from dal.models.user_model import User
from exceptions.exceptions import NoUsersFoundException, UserAlreadyExistsException, UserNotFoundException , InvalidUsernameOrPasswordException
from repositries import user_repo
from auth.password_hasher import PasswordHasher
from dal.deps import get_db
from auth import auth_n

password_hasher = PasswordHasher()

async def register_user(user: UserCreate):
    existing_user = await user_repo.get_user_by_username(user.username)
    if existing_user:
        raise UserAlreadyExistsException()

    new_user = User(
        username=user.username,
        hashed_password=password_hasher.hash_password(user.password),
        full_name=user.full_name,
        email=user.email
    )
    return await user_repo.create_user(new_user)
   
async def login_user(username: str, password: str):
    user = await get_user_by_username(username)
    if not user or not auth_n.verify_password(password, user.hashed_password):
        raise InvalidUsernameOrPasswordException()
    token = auth_n.create_access_token(username=user.username, user_id=user.id)
    return {"access_token": token, "token_type": "bearer"}

async def get_user_by_username(username: str):
    user = await user_repo.get_user_by_username(username)
    if not user:
        raise UserNotFoundException()
    return user

async def get_user_by_id(user_id: int):
    user = await user_repo.get_user_by_id(user_id)
    if not user:
        raise UserNotFoundException()
    return user

async def get_all_users():
     users = await user_repo.get_all_users()
     if not users:
         raise NoUsersFoundException()
     return users