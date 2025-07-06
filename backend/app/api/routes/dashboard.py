from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import date
from app.db.session import get_db
from app.models.stats import DailyStats

router = APIRouter()

@router.get("/stats")
def get_today_stats(db: Session = Depends(get_db)):
    today = date.today()
    stats = db.query(DailyStats).filter(DailyStats.date == today).first()
    if not stats:
        return {
            "open": 0,
            "triaged": 0,
            "in_progress": 0,
            "done": 0
        }
    return {
        "open": stats.open_count,
        "triaged": stats.triaged_count,
        "in_progress": stats.in_progress_count,
        "done": stats.done_count
    }
