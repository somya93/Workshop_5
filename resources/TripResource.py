from flask_restful import reqparse, Resource
from flask import make_response   # returns an HTML response
from services.RiderService import *
from services.TripService import *
from flask_jwt_extended import jwt_required, get_jwt_identity

post_parser = reqparse.RequestParser()
post_parser.add_argument('fare', type=str, default="")

headers = {'Content-Type': 'application/json'}


class TripResource(Resource):
    @jwt_required()
    def get(self, rider_id):
        email_identity = get_jwt_identity()
        rider = get_rider_by_id(rider_id)
        if rider and email_identity == rider.email:
            trips = get_trips_by_rider(rider_id)
            return make_response(trips.to_json(), 200, headers)
        else:
            return 403

    @jwt_required()
    def post(self, rider_id):
        email_identity = get_jwt_identity()
        rider = get_rider_by_id(rider_id)
        args = post_parser.parse_args()
        if len(args.fare) == 0:
            return "ERROR! fare is a required field.", 400
        elif email_identity == rider.email:
            trip_doc = create_trip_by_rider(rider_id, args.fare)
            return make_response(trip_doc.to_json(), 200, headers)
        else:
            return 403
