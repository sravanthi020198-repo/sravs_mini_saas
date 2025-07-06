from pydantic import BaseModel
from enum import Enum

class StatusEnum(str, Enum):
    OPEN = "OPEN"
    TRIAGED = "TRIAGED"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"

class IssueCreate(BaseModel):
    title: str
    description: str
    severity: str

class IssueRead(IssueCreate):
    id: int
    status: StatusEnum
    class Config:
        orm_mode = True
