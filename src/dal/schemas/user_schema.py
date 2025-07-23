from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=30, example="johndoe")
    email: EmailStr = Field(..., example="user@example.com")
    password: str = Field(..., min_length=6, max_length=100, example="securepassword")
    full_name: str = Field(..., min_length=1, max_length=50, example="John Doe")
    is_active: bool = Field(default=True, example=True)
    role: str = Field(default="user", example="user")

class UserCreate(UserBase):
    id: int = Field(..., ge=1, example=1)  
    username: str = Field(..., min_length=3, max_length=30, example="johndoe")
    email: EmailStr = Field(..., example="user@example.com")
    password: str = Field(..., min_length=6, max_length=100, example="securepassword")
    full_name: str = Field(..., min_length=1, max_length=50, example="John Doe")
    
class UserLogin(UserBase):
    username: str = Field(..., min_length=3, max_length=30, example="johndoe")
    password: str = Field(..., min_length=6, max_length=100, example="securepassword")

class UserOut(UserBase):
    id: int