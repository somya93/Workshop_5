from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from jwt import exceptions as jwt_exception

from database.db import initialize_db
from utils.JSONEncoder import MongoEngineJSONEncoder
from resources.Users import Users
from resources.Sessions import Sessions
from resources.Riders import Riders
from resources.Trips import Trips

app = Flask(__name__)  # Creating a FLASK app
app.config['MONGODB_SETTINGS'] = {
    'db': 'app-rest',
    'host': 'mongodb://localhost:27017/app-rest'
}

app.config['JWT_SECRET_KEY'] = 'i-wont-tell-you-this-secret'  # Change this!
app.config['PROPAGATE_EXCEPTIONS'] = True

initialize_db(app)
jwt = JWTManager(app)
app.json_encoder = MongoEngineJSONEncoder
api = Api(app)  # Creating a REST API for the app


# http://localhost:5000/register?email=value&password=value
api.add_resource(Users, '/users')

# http://localhost:5000/login?email=value&password=value
api.add_resource(Sessions, '/sessions')

# http://localhost:5000/rider
# http://localhost:5000/rider/rider_id
# http://localhost:5000/rider/rider_id?arg=value
api.add_resource(Riders,
                 '/riders',
                 '/riders/',
                 '/riders/<string:rider_id>')

# http://localhost:5000/rider/rider_id/trip?arg=value
api.add_resource(Trips,
                 '/riders/<string:rider_id>/trips')


@app.route('/')
def hello_world():
    raise jwt_exception.ExpiredSignatureError
    # return make_response(jsonify(api='rideshare', version='0.0.1', date='2021-11-08'), 200)


if __name__ == "__main__":
    app.run()  # Runs web app @ http://localhost:5000 by default for me.
