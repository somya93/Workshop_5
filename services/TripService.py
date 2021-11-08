from models.Trip import Trip
import uuid


def get_trips_by_rider(rider_id: str):  # Service for the GET() method
    trips = None
    if rider_id is not None:
        trips = Trip.objects(rider_id=rider_id)  # Returning all objects that matches the specific id
    return trips


def create_trip_by_rider(rider_id: str, fare: str):  # Service for the POST() method
    while True:
        gen_trip_id = str(uuid.uuid4())[0:7]
        if len(Trip.objects(trip_id=gen_trip_id)) == 0:
            break
    trip_doc = Trip(rider_id=rider_id,
                    trip_id=gen_trip_id,
                    fare=fare
                    )  # Create a new trip object
    trip_doc.save()  # Save the newly created trip object to the db
    return trip_doc  # Return the list of one trip object that was created
