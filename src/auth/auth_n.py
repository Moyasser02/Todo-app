# src/auth/auth_handler.py
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from auth.password_hasher import PasswordHasher
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from dal.models.user_model import User
from config.environment import get_environment
from typing import Optional
from exceptions.exceptions import  PasswordVerificationException , TokenInvalidException , UserNotFoundException , InvalidUsernameOrPasswordException
from typing import Dict
environment = get_environment()


SECRET_KEY = environment.SECRET_KEY
ALGORITHM = environment.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = environment.ACCESS_TOKEN_EXPIRE_MINUTES

password_hasher = PasswordHasher()


def create_access_token(username: str, user_id: int, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = {"sub": username, "id": user_id}
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def decode_token(token: str) -> Dict[str, int]:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        user_id: int = payload.get("id")
        if not username or not user_id:
            raise UserNotFoundException()
        return {"username": username, "id": user_id}
    except JWTError:
        raise TokenInvalidException()

def verify_password(plain_password: str, hashed_password: str) -> bool:
    try:
        return password_hasher.verify(plain_password, hashed_password)
    except Exception:
        raise PasswordVerificationException()


def authenticate_user(db: Session, username: str, password: str) -> User:
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.hashed_password):
        raise InvalidUsernameOrPasswordException()
    return user
