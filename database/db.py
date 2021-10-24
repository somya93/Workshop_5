from flask_mongoengine import MongoEngine
from services.RiderService import init_riders

db = MongoEngine()


def initialize_db(app):
    db.init_app(app)
    init_riders()


def fetch_engine():
    return db
