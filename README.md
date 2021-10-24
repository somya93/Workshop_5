# Workshop 5

In this workshop, we'll be introducing how to build an API.

## Prerequisites

1. Install [Postman](https://www.postman.com/) - you don't need to create an account.

Postman is an awesome development tool to test our REST APIs.

2. Install [MongoDB Compass](https://www.mongodb.com/try/download/compass) - you don't need to create an account.

MongoDB Compass provides a simple GUI to view all MongoDB objects, which helps test whether our API works.

## New Dependencies
Make sure to have these dependencies added to your project interpreter in PyCharm.

1. [Flask](https://flask.palletsprojects.com/en/1.1.x/)
2. [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/)
3. [flask-mongoengine](https://docs.mongoengine.org/projects/flask-mongoengine/en/latest/)

<b> Flask </b> is a framework that allows us to easily setup a web server with Python. It's a bit minimalistic, so to make it work better for our needs we add Flask-RESTful, which introduces a lot of helpful methods to handle creating a REST API. Flask-mongoengine is the same as the mongoengine we've used previously; it just adds a little more code to integrate mongoengine with our Flask app.

## New Folder Structure

You'll notice that we have some new folders: database, models, resources, services, and utils. 

The database folder has the code we used previously to set up the connection with the MongoDB database.

The models folder stores all the schemas for our MongoDB documents.

The resources folder contains all our Flask-RESTful resources, which act as an interface between HTTP requests and services.

The services folder contains code for our "services." Here, we have our business logic that can be called up by our Flask-RESTful resources.

The utils folder contains any miscellaneous code we use in our app.

## New app.py
We initialize our Flask web-server in app.py by creating a Flask app and passing on our MongoDB info.

```
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'REST_API',
    'host': 'mongodb://localhost:27017/REST_API'
}

initialize_db(app)
```


### JSONEncoder
Flask, by default, has trouble changing MongoDB documents to JSON. Most of our HTTP requests return JSON, so that is a problem. To solve this issue, we provide Flask with our own custom JSONEncoder (found in the utils folder).

In app.py
```
from utils.JSONEncoder import MongoEngineJSONEncoder
...
app.json_encoder = MongoEngineJSONEncoder
```

## Flask RESTful Resources

In Flask-RESTful, resources are basically HTTP controllers. Here, we define what the server does for HTTP requests.

```
class RiderResource(Resource):
    def get(self, rider_id=None):
        response = get_rider(rider_id)
        return make_response(convertToHTMLString(response), 200, headers)

    def post(self):
        args = post_parser.parse_args()
        response = create_rider(args.name, args.premium)
        return make_response(convertToHTMLString(response), 200, headers)

    def patch(self, rider_id=None):
        if rider_id is not None:
            args = patch_parser.parse_args()
            response = update_rider(rider_id, args.premium)
            return make_response(convertToHTMLString(response), 200, headers)
        return 400
```

You'll see that each method corresponds to a certain HTTP request. Here, we have defined behavior for GET, POST, and PATCH.

## Routing 
By default, Flask supports routing with '@' decorators
```
@app.route('/')
def hello_world():
    return 'Hello World!'
```

This means that our server will return 'Hello World!' whenever we make an GET call on localhost:5000/

However, this form of routing can get a little messy for larger apps and Flask-RESTful uses a different kind of routing.

```
api = Api(app)
api.add_resource(RiderResource,
                 '/rider',
                 '/rider/',
                 '/rider/<string:rider_id>')
```

Here, we are passing our Flask app into a Flask-RESTful constructor to convert it into a Flask-RESTful API.

Flask-RESTful allows us to create routes in this way. We pass in our Flask-RESTful resource along with any API paths it should support. In our case, our app supports two paths. One ends with /rider and the other allows the requester to append a rider_id (e.g. /rider/asd23sd34) to target a rider with that specific ID.

It will then use our specified Resource to handle the different HTTP calls at those endpoints.

Technically, you can mix these two kinds of routing, but I highly recommend you stick to the Flask-RESTful routing format.

## Services

Our services encapsulate our business logic. In this project, our services mainly deal with handling changes to the database.

## Adding more endpoints
I highly recommend you follow the pattern I established as you add more features to your server. For example, if I were to create a User entity that can be modified through HTTP calls, I would create a User MongoEngine document in the models folder, a UserResource Flask-RESTful resource in the resources folder, and a UserService service in the services folder. Then you need to add the appropriate routing in app.py

It would look something like this
```
api.add_resource(Users, '/users')
```