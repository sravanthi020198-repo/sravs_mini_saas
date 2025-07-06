from apscheduler.schedulers.background import BackgroundScheduler
from datetime import date
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.issue import StatusEnum, Issue
from app.models.stats import DailyStats
import logging

logging.basicConfig(level=logging.INFO)
scheduler = BackgroundScheduler()

def aggregate_issue_stats():
    db: Session = SessionLocal()
    try:
        today = date.today()
        open_count = db.query(Issue).filter(Issue.status == StatusEnum.OPEN).count()
        triaged_count = db.query(Issue).filter(Issue.status == StatusEnum.TRIAGED).count()
        in_progress_count = db.query(Issue).filter(Issue.status == StatusEnum.IN_PROGRESS).count()
        done_count = db.query(Issue).filter(Issue.status == StatusEnum.DONE).count()

        stats = DailyStats(
            date=today,
            open_count=open_count,
            triaged_count=triaged_count,
            in_progress_count=in_progress_count,
            done_count=done_count
        )
        db.merge(stats)
        db.commit()
        logging.info("Daily stats updated.")
    finally:
        db.close()

scheduler.add_job(aggregate_issue_stats, 'interval', minutes=30)
scheduler.start()
