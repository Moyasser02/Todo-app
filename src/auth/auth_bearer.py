# src/auth/auth_bearer.py

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated

from src.auth.auth_handler import decode_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")  # tokenUrl must match your login route

TokenData = Annotated[dict, Depends(oauth2_scheme)]


def get_current_user(token: TokenData):
    return decode_token(token)



