from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Text
from sqlalchemy.orm import relationship
from app.db.base import Base
import enum

class StatusEnum(str, enum.Enum):
    OPEN = "OPEN"
    TRIAGED = "TRIAGED"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"

class Issue(Base):
    __tablename__ = "issues"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(Text)
    severity = Column(String)
    status = Column(Enum(StatusEnum), default=StatusEnum.OPEN)
    reporter_id = Column(Integer, ForeignKey("users.id"))
    reporter = relationship("User")
