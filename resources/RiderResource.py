from flask_restful import reqparse, Resource
from flask import make_response   # returns an HTML response
from services.RiderService import *
from flask_jwt_extended import jwt_required, get_jwt_identity

post_parser = reqparse.RequestParser()
post_parser.add_argument('name', type=str, default="")
post_parser.add_argument('email', type=str, default="")
post_parser.add_argument('premium', type=bool, default=False)

patch_parser = reqparse.RequestParser()
patch_parser.add_argument('premium', type=bool, default=False)

headers = {'Content-Type': 'application/json'}


class RiderResource(Resource):
    @jwt_required()
    def get(self, rider_id=None):
        email_identity = get_jwt_identity()
        if rider_id is None:
            rider = get_rider_by_email(email_identity)
        else:
            rider = get_rider_by_id(rider_id)
        if rider and email_identity == rider.email:
            return make_response(rider.to_json(), 200, headers)
        else:
            return 403

    @jwt_required()
    def post(self):
        email_identity = get_jwt_identity()
        args = post_parser.parse_args()
        if len(args.name) == 0 or len(args.email) == 0:
            return "ERROR! name and email are required fields.", 400
        elif email_identity == args.email:
            found_rider = get_rider_by_email(args.email)
            if found_rider is None:
                response = create_rider(args.name, args.email, args.premium)
                return make_response(response.to_json(), 200, headers)
            else:
                return "ERROR! Rider with this email already exists."
        else:
            return 403

    @jwt_required()
    def patch(self, rider_id):
        email_identity = get_jwt_identity()
        rider = get_rider_by_id(rider_id)
        if rider and email_identity == rider.email:
            args = patch_parser.parse_args()
            rider = update_rider(rider_id, args.premium)
            return make_response(rider.to_json(), 200, headers)
        else:
            return 403
