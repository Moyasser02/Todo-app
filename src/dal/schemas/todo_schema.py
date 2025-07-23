from pydantic import BaseModel, EmailStr, Field
from typing import Optional
class TodoBase(BaseModel):
    title: str = Field(..., example="Buy groceries",min_length=1, max_length=30)
    description: str = Field(..., min_length=1, max_length=100)
    completed: bool = Field(default=False)
    priority: int = Field(default=5, gt=0, lt=11)  
    owner_id: int = Field(..., example=1) 

class TodoUpdate(BaseModel):
    title: Optional[str] = Field(None, example="Buy groceries", min_length=1, max_length=30)
    description: Optional[str] = Field(None, min_length=1, max_length=100)
    completed: Optional[bool] = Field(None)
    priority: Optional[int] = Field(None, gt=0, lt=11)
    
