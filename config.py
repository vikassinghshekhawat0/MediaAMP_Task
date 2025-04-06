import os

class Config:
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "secret")
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
        f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', 'redis://redis:6379/0')
    CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND', 'redis://redis:6379/0')

class Development(Config): pass
class Staging(Config): pass
class Production(Config): pass

def get_config(env):
    return {"development": Development, "staging": Staging, "production": Production}.get(env, Development)