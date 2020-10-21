# Workshop 4

In this workshop, we'll be extending our previous project into a API.

## Prerequisites

1. Install [Postman](https://www.postman.com/) - you may need to create an account

Postman is an awesome development tool to test our REST APIs.

## New Dependencies
Make sure to have these dependencies added to your project interpreter in PyCharm.

1. [Flask](https://flask.palletsprojects.com/en/1.1.x/)
2. [Flask-RESTful](https://flask-rescful.readthedocs.io/en/latest/)
3. [flask-mongoengine](https://docs.mongoengine.org/projects/flask-mongoengine/en/latest/)

<b> Flask </b> is a framework that allows us to easily setup a web server with Python. It's a bit minimalistic, so to make it work better for our needs we add Flask-RESTful, which introduces a lot of helpful methods to handle creating a REST API. Flask-mongoengine is the same as the mongoengine we've used previously; it just adds a little more code to integrate mongoengine with our Flask app.

## Disclaimer

A lot of the terminology in Flask, or the terminology that I use to describe certain features, is not the same terminology that Karim uses to describe SOAs. For example, Resources are not entities, but more like HTTP controllers in Flask-RESTful. Services are not necessarily Services in a SOA, either.

We're building a monolithic web-server, meaning that this server can only be deployed as one whole instance. A SOA back-end will have different parts deployed separately to support better scaling. However, if you're monolith server is well-designed, you could re-use the code to break down the project into multiple deployed services.

What we're concerned here is with the basics. And the basics are the same no matter whether your project is deployed as one instance or many instances that communicate to one another.

## New Folder Structure

You'll notice that we have some new folders: database, models, resources, services, and utils. 

The database folder has the code we used previously to set up the connection with the MongoDB database.

The models folder stores all the schemas for our MongoDB documents.

The resources folder contains all our Flask-RESTful resources (think of these as HTTP controllers)

The services folder contains code for our "services." Here, we have our business logic that can be called up by our Flask-RESTful resources.

The utils folder contains any miscellaneous code we use in our app.

## New app.py
We initialize our Flask web-server in app.py by creating a Flask app and passing on our MongoDB info.

```
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'workshop4',
    'host': 'mongodb://localhost:27017/workshop4'
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
class Questions(Resource):

    def get(self, q_id=None):
        min_reply = request.args.get('min_replies')

        if q_id:
            return jsonify(get_question(q_id))

        if min_reply:
            return jsonify(get_questions_min_replies(min_reply))

        return jsonify(get_all_questions())

    def patch(self, q_id=None):
        if q_id:
            args = patch_parser.parse_args()
            return jsonify(add_reply_to_question(q_id, args.reply))
        return 400

    def post(self):
        args = post_parser.parse_args()
        the_created_q_doc = create_question_in_db(args.question_text)
        return jsonify(the_created_q_doc)
```

You'll see that each method corresponds to a certain HTTP request. Here, we have defined behavior for GET, PATCH, and POST.

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
api.add_resource(Questions,
                 '/questions',
                 '/questions/<string:q_id>')
```

Here, we are passing our Flask app into a Flask-RESTful constructor to convert it into a Flask-RESTful API.

Flask-RESTful allows us to create routes in this way. We pass in our Flask-RESTful resource along with any API paths it should support. In our case, our app supports two paths. One ends with /questions and the other allows the requester to append a question_id (e.g. /questions/1) to target a question with that specific ID.

It will then use our specified Resource to handle the different HTTP calls at those endpoints.

Technically, you can mix these two kinds of routing, but I highly recommend you stick to the Flask-RESTful routing format.

## Services

Our services encapsulate our business logic. In this project, our services mainly deal with handling changes to the database.

## Adding more endpoints
I highly recommend you follow the pattern I established as you add more features to your server. For example, if I were to create a User entity that can be modified through HTTP calls, I would create a User MongoEngine document in the models folder, a Users Flask-RESTful resource in the resources folder, and a UsersService service in the services folder. Then you need to add the appropriate routing in app.py

It would look something like this
```
api.add_resource(Users, '/users')
```