from flask_mongoengine import MongoEngine
from services.RiderService import init_riders

db = MongoEngine()


def initialize_db(app):
    db.init_app(app)  # Create the db
    init_riders()  # Populate it with default riders
