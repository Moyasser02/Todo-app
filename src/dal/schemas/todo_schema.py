from pydantic import BaseModel, EmailStr, Field

class TodoBase(BaseModel):
    title: str = Field(..., example="Buy groceries",min_length=1, max_length=30)
    description: str = Field(..., min_length=1, max_length=100)
    completed: bool = Field(default=False)
    priority: int = Field(default=5, gt=0, lt=11)  # Default priority is 5
    owner_id: int = Field(..., example=1)  # Foreign key to associate with User