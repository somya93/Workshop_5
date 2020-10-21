from flask_restful import reqparse, Resource
from flask import jsonify
from services.QuestonService import *

post_parser = reqparse.RequestParser()
post_parser.add_argument('question_text', type=str)

patch_parser = reqparse.RequestParser()
patch_parser.add_argument('reply', type=str)
# to add more arguments... patch_parser.add_argument('example_arg', type=str)

class Questions(Resource):

    def get(self, q_id=None):
        if q_id:
            return jsonify(get_question(q_id))

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


