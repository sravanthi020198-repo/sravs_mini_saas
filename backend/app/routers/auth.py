from fastapi import APIRouter, HTTPException, Depends
from app.schemas import UserCreate, UserOut
from app.models import User, RoleEnum
from app.db import SessionLocal
from passlib.context import CryptContext
from jose import jwt
import os

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = os.getenv("SECRET_KEY", "supersecret")
ALGORITHM = "HS256"

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

@router.post("/register", response_model=UserOut)
def register(user: UserCreate):
    db = SessionLocal()
    if db.query(User).filter_by(email=user.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    user_obj = User(
        email=user.email,
        password_hash=get_password_hash(user.password),
        role=user.role
    )
    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)
    db.close()
    return user_obj

@router.post("/login")
def login(data: UserCreate):
    db = SessionLocal()
    user = db.query(User).filter_by(email=data.email).first()
    if not user or not verify_password(data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = jwt.encode({"sub": user.email, "role": user.role.value}, SECRET_KEY, algorithm=ALGORITHM)
    db.close()
    return {"access_token": token, "token_type": "bearer"}
