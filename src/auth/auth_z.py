# src/auth/auth_bearer.py

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated

from auth.auth_n import decode_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/")  

TokenData = Annotated[str, Depends(oauth2_scheme)]


def get_current_user(token: TokenData):
    return decode_token(token)



