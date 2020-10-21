from flask import Flask
from flask_restful import Api
from database.db import initialize_db
from resources.Questions import Questions
from utils.JSONEncoder import MongoEngineJSONEncoder

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'workshop4',
    'host': 'mongodb://localhost:27017/workshop4'
}

initialize_db(app)
app.json_encoder = MongoEngineJSONEncoder
api = Api(app)
api.add_resource(Questions,
                 '/questions',
                 '/questions/<string:q_id>')

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
