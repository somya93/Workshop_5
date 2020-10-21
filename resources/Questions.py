from flask_restful import reqparse, Resource
from flask import jsonify
from services.QuestonService import create_question_in_db, get_all_questions, get_question
from utils.JSONEncoder import JSONEncoder

post_parser = reqparse.RequestParser()
post_parser.add_argument('question_text', type=str)

class Questions(Resource):

    def get(self, q_id=None):
        if q_id:
            return jsonify(get_question(q_id))

        return jsonify(get_all_questions())


    def post(self):
        args = post_parser.parse_args()
        the_created_q_doc = create_question_in_db(args.question_text)
        return jsonify(the_created_q_doc)


