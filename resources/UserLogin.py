from flask import jsonify, make_response
from flask_restful import reqparse, Resource
from utils.Hash import get_hash

from services.UserService import *
from flask_jwt_extended import create_access_token

login_parser = reqparse.RequestParser()
login_parser.add_argument('email', type=str, default="")
login_parser.add_argument('password', type=str, default="")


class UserLogin(Resource):
    def get(self):
        return "Use POST method to login", 200

    def post(self):
        args = login_parser.parse_args()
        if len(args.email) == 0 or len(args.password) == 0:
            return "ERROR! email and password are required fields.", 400
        found_user = find_user_by_email(args.email)
        if found_user:
            password_hash = get_hash(args.password.encode('utf-8'))
            if password_hash == found_user.password_hash:
                access_token = create_access_token(identity=args.email)
                return make_response(jsonify(access_token=access_token), 200)

        return "No account with these credentials", 401
