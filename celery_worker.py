from celery import Celery
from app import create_app
from app.db import db
from app.models import TaskManager, TaskLogger
from datetime import date

celery = Celery(__name__)
celery.conf.update(create_app("development").config)

@celery.task
def daily_task_loader():
    today = date.today()
    tasks = TaskManager.query.filter_by(status='active').all()
    for t in tasks:
        if not TaskLogger.query.filter_by(task_id=t.id, date=today).first():
            db.session.add(TaskLogger(task_id=t.id, date=today))
    db.session.commit()