from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import auth, issues, dashboard

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/auth")
app.include_router(issues.router, prefix="/api/issues")
app.include_router(dashboard.router, prefix="/api/dashboard")

@app.get("/")
def read_root():
    return {"status": "Mini SaaS Tracker Running"}

## backend/app/models/user.py
from sqlalchemy import Column, Integer, String, Enum
from app.db.base import Base
import enum

class RoleEnum(str, enum.Enum):
    ADMIN = "ADMIN"
    MAINTAINER = "MAINTAINER"
    REPORTER = "REPORTER"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(Enum(RoleEnum), default=RoleEnum.REPORTER)
