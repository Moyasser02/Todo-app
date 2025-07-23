from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=30, example="johndoe")
    email: EmailStr = Field(..., example="user@example.com")
    full_name: str = Field(..., min_length=1, max_length=50, example="John Doe")
    is_active: bool = Field(default=True, example=True)
    role: str = Field(default="user", example="user")


class UserCreateRequest(UserBase):
    password: str = Field(..., min_length=6, max_length=100, example="securepassword")


class UserLoginRequest(BaseModel):
    username: str = Field(..., min_length=3, max_length=30, example="johndoe")
    password: str = Field(..., min_length=6, max_length=100, example="securepassword")

class UserInDB(UserBase):
    id: int
    hashed_password: str

    class Config:
        orm_mode = True 


class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True  # allows conversion from ORM models to Pydantic
