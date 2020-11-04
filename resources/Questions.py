from flask_restful import reqparse, Resource, request
from flask import jsonify, make_response
from services.QuestonService import *

post_parser = reqparse.RequestParser()
post_parser.add_argument('question_text', type=str)

patch_parser = reqparse.RequestParser()
patch_parser.add_argument('reply', type=str)
# to add more arguments... patch_parser.add_argument('example_arg', type=str)


def convertToHTMLString(questions) -> str:
    to_return = ""
    for question in questions:
        to_return += f"<h1>{question.question_text}</h1>"
        for index, reply in enumerate(question.replies):
            to_return += f"<p>{index+1}) {reply}</p>"
    return to_return


class Questions(Resource):

    def get(self, q_id=None):
        headers = {'Content-Type': 'text/html'}
        min_reply = request.args.get('min_replies')

        questions = []

        if q_id:
            questions.append(get_question(q_id))
        if min_reply:
            questions = get_questions_min_replies(min_reply)

        if not q_id and not min_reply:
            questions = get_all_questions()

        return make_response(convertToHTMLString(questions), 200, headers)

    def patch(self, q_id=None):
        headers = {'Content-Type': 'text/html'}
        if q_id:
            args = patch_parser.parse_args()
            return make_response(convertToHTMLString([add_reply_to_question(q_id, args.reply)]), 200, headers)
        return 400

    def post(self):
        headers = {'Content-Type': 'text/html'}
        args = post_parser.parse_args()
        the_created_q_doc = create_question_in_db(args.question_text)
        return make_response(convertToHTMLString([the_created_q_doc]), 200, headers)

    # old code that returns json
    # def get(self, q_id=None):
    #     headers = {'Content-Type': 'text/html'}
    #     min_reply = request.args.get('min_replies')
    #
    #     if q_id:
    #         return jsonify(get_question(q_id))
    #
    #     if min_reply:
    #         return jsonify(get_questions_min_replies(min_reply))
    #
    #     return make_response("hello world",200,headers)
    #
    # def patch(self, q_id=None):
    #     if q_id:
    #         args = patch_parser.parse_args()
    #         return jsonify(add_reply_to_question(q_id, args.reply))
    #     return 400
    #
    # def post(self):
    #     args = post_parser.parse_args()
    #     the_created_q_doc = create_question_in_db(args.question_text)
    #     return jsonify(the_created_q_doc)


