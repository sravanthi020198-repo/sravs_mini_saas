from celery import Celery
from sqlalchemy import func
from datetime import datetime
from app.db import SessionLocal
from app.models import Issue, IssueStatus, DailyStats

celery = Celery(__name__, broker="redis://redis:6379/0")

@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # every 30 min
    sender.add_periodic_task(1800.0, aggregate_issue_counts.s(), name="aggregate every 30 min")

@celery.task
def aggregate_issue_counts():
    db = SessionLocal()
    today = datetime.utcnow().date()
    for status in IssueStatus:
        count = db.query(Issue).filter(Issue.status == status).count()
        stat = DailyStats(date=today, status=status, count=count)
        db.add(stat)
    db.commit()
    db.close()
