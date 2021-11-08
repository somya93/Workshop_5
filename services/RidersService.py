from models.Rider import Rider
import uuid

default_riders = {'Karim': 'karim@cmu.org',
                  'Manuja': 'manuja@cmu.org',
                  'Phil': 'phil@cmu.org'}


def get_rider_by_id(rider_id: str):  # Service for the GET() method
    rider_doc = None
    if rider_id is not None:
        rider_doc = Rider.objects(rider_id=rider_id).first()  # Returning the only object that matches the specific id
    return rider_doc


def get_rider_by_email(email: str):  # Service for the GET() method
    rider_doc = None
    if email is not None:
        rider_doc = Rider.objects(email=email).first()  # Returning the only object that matches the specific email
    return rider_doc


def create_rider(rider_name: str, email: str, is_rider_premium: bool = False):  # Service for the POST() method
    while True:
        gen_rider_id = str(uuid.uuid4())[0:7]
        if len(Rider.objects(rider_id=gen_rider_id)) == 0:
            break
    rider_doc = Rider(rider_id=gen_rider_id,
                      name=rider_name,
                      email=email,
                      premium=is_rider_premium
                      )  # Create a new rider object
    rider_doc.save()  # Save the newly created rider object to the db
    return rider_doc  # Return the list of one rider object that was created


def update_rider(rider_id: str, is_rider_premium: bool):  # Service for the PATCH() method
    rider_doc = Rider.objects(rider_id=rider_id).first()  # extracting the first object from a list of one object
    rider_doc.update(premium=is_rider_premium)
    rider_doc.reload()  # Get the latest copy from the db
    return rider_doc  # Return the list of one rider object that was updated


def init_riders():  # Initialize the db with default riders if there are no existing riders
    existing_riders = Rider.objects()  # List of all rider objects in the db
    if len(existing_riders) == 0:
        for rider_name in default_riders:
            create_rider(rider_name, default_riders[rider_name])
