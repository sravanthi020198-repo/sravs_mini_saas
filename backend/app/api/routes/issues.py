from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.issue import Issue, StatusEnum
from app.schemas.issue import IssueCreate, IssueRead
from app.api.deps import get_current_user, require_role
from app.schemas.user import RoleEnum, TokenData

router = APIRouter()

@router.post("/", response_model=IssueRead)
def create_issue(
    issue: IssueCreate,
    db: Session = Depends(get_db),
    current_user: TokenData = Depends(require_role(RoleEnum.REPORTER))
):
    db_issue = Issue(
        title=issue.title,
        description=issue.description,
        severity=issue.severity,
        reporter_id=current_user.email
    )
    db.add(db_issue)
    db.commit()
    db.refresh(db_issue)
    return db_issue

@router.get("/", response_model=list[IssueRead])
def get_issues(
    db: Session = Depends(get_db),
    current_user: TokenData = Depends(get_current_user)
):
    if current_user.role == RoleEnum.REPORTER:
        return db.query(Issue).filter(Issue.reporter_id == current_user.email).all()
    return db.query(Issue).all()

@router.patch("/{issue_id}", response_model=IssueRead)
def update_issue_status(
    issue_id: int,
    status: StatusEnum,
    db: Session = Depends(get_db),
    current_user: TokenData = Depends(require_role(RoleEnum.MAINTAINER))
):
    issue = db.query(Issue).filter(Issue.id == issue_id).first()
    if not issue:
        raise HTTPException(status_code=404, detail="Issue not found")
    issue.status = status
    db.commit()
    db.refresh(issue)
    return issue
