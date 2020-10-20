from flask_restful import fields, marshal_with, reqparse, Resource
from flask import jsonify, make_response
from services.QuestonService import create_question_in_db
from utils.JSONEncoder import JSONEncoder

post_parser = reqparse.RequestParser()
post_parser.add_argument('question_text', type=str)

# post_return = {
#     'question_text': fields.String,
#     'replies': fields.List,
#     'num_replies': fields.Integer,
#     'date_created': fields.DateTime,
# }


class Questions(Resource):

    # @marshal_with(post_return, envelope='data')
    def post(self):
        args = post_parser.parse_args()
        the_created_q_doc = create_question_in_db(args.question_text)
        return jsonify(the_created_q_doc)


