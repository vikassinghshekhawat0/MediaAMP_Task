from app.db import db
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Index
from sqlalchemy.orm import relationship
from datetime import datetime

class User(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    role = Column(String, default='user')

class TaskManager(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    status = Column(String, default='active')
    user_id = Column(Integer, ForeignKey('user.id'))
    created_at = Column(DateTime, default=datetime.utcnow)
    user = relationship('User', backref='tasks')

class TaskLogger(db.Model):
    id = Column(Integer, primary_key=True)
    task_id = Column(Integer, ForeignKey('task_manager.id', ondelete='CASCADE'))
    date = Column(DateTime, default=datetime.utcnow, index=True)
    task = relationship('TaskManager')

class AuditLog(db.Model):
    id = Column(Integer, primary_key=True)
    task_id = Column(Integer, ForeignKey('task_manager.id'))
    status = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)