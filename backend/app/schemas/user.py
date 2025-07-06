from pydantic import BaseModel, EmailStr
from enum import Enum

class RoleEnum(str, Enum):
    ADMIN = "ADMIN"
    MAINTAINER = "MAINTAINER"
    REPORTER = "REPORTER"

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str
    role: RoleEnum = RoleEnum.REPORTER

class UserRead(UserBase):
    id: int
    role: RoleEnum
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: EmailStr = None
    role: RoleEnum = None
