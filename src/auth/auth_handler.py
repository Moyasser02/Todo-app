# src/auth/auth_handler.py

from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from src.dal.models.user_model import User
from src.config.environment import get_environment

environment = get_environment()

SECRET_KEY = environment.SECRET_KEY
ALGORITHM = environment.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = environment.ACCESS_TOKEN_EXPIRE_MINUTES

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def create_access_token(username: str, user_id: int, expires_delta: timedelta | None = None):
    to_encode = {"sub": username, "id": user_id}
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt_context.verify(plain_password, hashed_password)


def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.hashed_password):
        return False
    return user


def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        user_id: int = payload.get("id")
        if username is None or user_id is None:
            raise credentials_exception()
        return {"username": username, "id": user_id}
    except JWTError:
        raise credentials_exception()


def credentials_exception():
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid authentication credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
