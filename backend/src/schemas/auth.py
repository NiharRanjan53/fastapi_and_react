from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=7, max_length=15)

class UserData(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=7, max_length=15)
    firstname: str = Field(..., min_length=1, max_length=50)
    lastname: str = Field(..., min_length=1, max_length=50)
    age: Optional[int] = Field(None, ge=0, le=120)
    contact_number: Optional[str] = Field(None, min_length=7, max_length=15)
    is_active: Optional[bool] = True
  

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    firstname: str
    lastname: str
    age: Optional[int]
    contact_number: Optional[str]
    is_active: bool

    class Config:  # Config class to enable ORM mode for SQLAlchemy compatibility
        orm_mode = True 