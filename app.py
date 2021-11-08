from flask import Flask
from flask_restful import Api
from database.db import initialize_db
from resources.RiderResource import RiderResource
from utils.JSONEncoder import MongoEngineJSONEncoder
from authentication.jwt import initialize_jwt
from resources.UserRegistration import UserRegistration
from resources.UserLogin import UserLogin

app = Flask(__name__)  # Creating a FLASK app
app.config['MONGODB_SETTINGS'] = {
    'db': 'app-rest',
    'host': 'mongodb://localhost:27017/app-rest'
}

app.config['JWT_SECRET_KEY'] = 'i-wont-tell-you-this-secret'  # Change this!

initialize_db(app)
jwt = initialize_jwt(app)
app.json_encoder = MongoEngineJSONEncoder
api = Api(app)  # Creating a REST API for the app


# http://localhost:5000/rider
# http://localhost:5000/rider/rider_id
# http://localhost:5000/rider/rider_id?arg=value
api.add_resource(RiderResource,
                 '/rider',
                 '/rider/',
                 '/rider/<string:rider_id>')

# http://localhost:5000/register?email=value&password=value
api.add_resource(UserRegistration, '/register')

# http://localhost:5000/login?email=value&password=value
api.add_resource(UserLogin, '/login')


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == "__main__":
    app.run()  # Runs web app @ http://localhost:5000 by default for me.
