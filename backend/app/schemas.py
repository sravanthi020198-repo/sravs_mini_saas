from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional
import enum

class RoleEnum(str, enum.Enum):
    ADMIN = 'ADMIN'
    MAINTAINER = 'MAINTAINER'
    REPORTER = 'REPORTER'

class IssueStatus(str, enum.Enum):
    OPEN = 'OPEN'
    TRIAGED = 'TRIAGED'
    IN_PROGRESS = 'IN_PROGRESS'
    DONE = 'DONE'

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    role: RoleEnum = RoleEnum.REPORTER

class UserOut(BaseModel):
    id: int
    email: EmailStr
    role: RoleEnum
    class Config(ConfigDict):
        from_attributes = True

class IssueCreate(BaseModel):
    title: str
    description: str
    severity: str

class IssueOut(BaseModel):
    id: int
    title: str
    description: str
    severity: str
    status: IssueStatus
    creator_id: int
    file_path: Optional[str] = None
    class Config(ConfigDict):
        from_attributes = True
