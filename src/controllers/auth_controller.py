from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from auth.auth_n import decode_token, create_access_token
from typing import Dict
from pydantic import BaseModel
from exceptions.exceptions import TokenInvalidException

router = APIRouter()

class RefreshRequest(BaseModel):
    refresh_token: str

@router.post("/refresh")
async def refresh_token(payload: RefreshRequest):
    try:
        token_data = decode_token(payload.refresh_token)

        # Optional: check "type" is refresh
        if token_data.get("type") != "refresh":
            raise TokenInvalidException()

        new_access_token = create_access_token(token_data["username"], token_data["id"])
        return {"access_token": new_access_token}
    except Exception:
        raise TokenInvalidException()
