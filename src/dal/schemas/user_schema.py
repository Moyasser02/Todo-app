from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    username: str = Field(...,min_length=3, max_length=30, example="johndoe")
    email: EmailStr = Field(..., example="user@example.com")
    full_name: str = Field(..., min_length=1, max_length=50, example="John Doe")
    is_active: bool = Field(..., default=True, example=True)
    role: str = Field(..., default="user", example="user")