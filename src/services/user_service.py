from sqlalchemy.ext.asyncio import AsyncSession
from dal.schemas.user_schema import UserCreateRequest, UserLoginRequest, UserResponse
from dal.models.user_model import User
from exceptions.exceptions import (
    NoUsersFoundException,
    UserAlreadyExistsException,
    UserNotFoundException,
    InvalidUsernameOrPasswordException
)
from repositries.user_repo import UserRepository
from auth.password_hasher import PasswordHasher
from auth import auth_n

class UserService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.user_repo = UserRepository(db)
        self.password_hasher = PasswordHasher()

    async def register_user(self, user: UserCreateRequest) -> UserResponse:
        existing_user = await self.user_repo.get_user_by_username(user.username)
        if existing_user:
            raise UserAlreadyExistsException()

        new_user = User(
            username=user.username,
            hashed_password=self.password_hasher.hash_password(user.password),
            full_name=user.full_name,
            email=user.email
        )
        return await self.user_repo.create_user(new_user)

    async def login_user(self, username: str, password: str) -> dict:
        user = await self.user_repo.get_user_by_username(username)
        if not user or not auth_n.verify_password(password, user.hashed_password):
            raise InvalidUsernameOrPasswordException()

        access_token = auth_n.create_access_token(user.username, user.id)
        refresh_token = auth_n.create_refresh_token(user.username, user.id)
        return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}

    async def get_user_by_username(self, username: str) -> User:
        user = await self.user_repo.get_user_by_username(username)
        if not user:
            raise UserNotFoundException()
        return user

    async def get_user_by_id(self, user_id: int) -> User:
        user = await self.user_repo.get_user_by_id(user_id)
        if not user:
            raise UserNotFoundException()
        return user

    async def get_all_users(self) -> list[User]:
        users = await self.user_repo.get_all_users()
        if not users:
            raise NoUsersFoundException()
        return users
