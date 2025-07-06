from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from app.models import Issue, IssueStatus, User, RoleEnum
from app.schemas import IssueCreate, IssueOut
from app.db import SessionLocal
from jose import jwt, JWTError
from typing import List
import os

router = APIRouter()
SECRET_KEY = os.getenv("SECRET_KEY", "supersecret")
ALGORITHM = "HS256"
UPLOAD_DIR = os.getenv("FILE_UPLOAD_PATH", "./uploads")

def get_current_user(token: str = Depends(lambda: None)):
    from fastapi import Request
    def extract_token(request: Request):
        auth = request.headers.get("Authorization")
        if auth and auth.startswith("Bearer "):
            return auth.split(" ")[1]
        return None
    return extract_token

def require_role(required_roles: List[RoleEnum]):
    def decorator(user: User = Depends(get_current_user)):
        if user.role not in required_roles:
            raise HTTPException(status_code=403, detail="Not enough permissions")
        return user
    return decorator

@router.post("/", response_model=IssueOut)
def create_issue(
    title: str = Form(...),
    description: str = Form(...),
    severity: str = Form(...),
    file: UploadFile = File(None),
    token: str = Depends(get_current_user)
):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_email = payload['sub']
        db = SessionLocal()
        user = db.query(User).filter_by(email=user_email).first()
        if not user:
            raise HTTPException(status_code=401, detail="Invalid user")
        file_path = None
        if file:
            filename = f"{user.id}_{file.filename}"
            file_location = os.path.join(UPLOAD_DIR, filename)
            with open(file_location, "wb") as f:
                f.write(file.file.read())
            file_path = filename
        issue = Issue(
            title=title,
            description=description,
            severity=severity,
            creator_id=user.id,
            file_path=file_path
        )
        db.add(issue)
        db.commit()
        db.refresh(issue)
        db.close()
        return issue
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

# Add more routers for update, list with RBAC, etc.
