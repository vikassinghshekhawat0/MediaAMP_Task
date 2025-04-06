from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import OperationalError
import time

db = SQLAlchemy()

def init_db(app):
    retries, delay = 5, 2
    for _ in range(retries):
        try:
            db.init_app(app)
            with app.app_context():
                db.create_all()
            break
        except OperationalError:
            time.sleep(delay)