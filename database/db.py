from flask_mongoengine import MongoEngine
from services.RiderService import init_riders
from services.UserService import init_users

db = MongoEngine()


def initialize_db(app):
    db.init_app(app)  # Create the db
    init_users()  # Populate it with default users
    init_riders()  # Populate it with default riders
