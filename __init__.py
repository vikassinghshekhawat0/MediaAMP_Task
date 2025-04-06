from flask import Flask
from app.config import get_config
from app.db import init_db
from app.routes import register_blueprints
from flask_jwt_extended import JWTManager
import redis
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

jwt = JWTManager()
limiter = Limiter(get_remote_address)


def create_app(env):
    app = Flask(__name__)
    app.config.from_object(get_config(env))
    init_db(app)
    jwt.init_app(app)
    limiter.init_app(app)
    register_blueprints(app)
    app.redis = redis.Redis(host='redis', port=6379, decode_responses=True)
    return app