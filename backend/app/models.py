from sqlalchemy import Column, Integer, String, ForeignKey, Enum, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db import Base
import enum

class RoleEnum(str, enum.Enum):
    ADMIN = 'ADMIN'
    MAINTAINER = 'MAINTAINER'
    REPORTER = 'REPORTER'

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=True)
    role = Column(Enum(RoleEnum), nullable=False, default=RoleEnum.REPORTER)
    issues = relationship("Issue", back_populates="creator")

class IssueStatus(str, enum.Enum):
    OPEN = 'OPEN'
    TRIAGED = 'TRIAGED'
    IN_PROGRESS = 'IN_PROGRESS'
    DONE = 'DONE'

class Issue(Base):
    __tablename__ = 'issues'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    file_path = Column(String, nullable=True)
    severity = Column(String, nullable=False)
    status = Column(Enum(IssueStatus), default=IssueStatus.OPEN)
    creator_id = Column(Integer, ForeignKey("users.id"))
    creator = relationship("User", back_populates="issues")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

class DailyStats(Base):
    __tablename__ = 'daily_stats'
    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, nullable=False)
    status = Column(Enum(IssueStatus), nullable=False)
    count = Column(Integer, default=0)
