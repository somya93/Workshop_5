from models.Rider import RiderDocument

default_riders = ['Karim', 'Manuja', 'Phil']


def get_rider(rider_id: str):  # Service for the GET() method
    if rider_id is None:
        rider_doc = RiderDocument.objects()  # Returning a list of all objects
    else:
        rider_doc = RiderDocument.objects(id=rider_id)  # Returning a list of all objects that match the specific id
    return rider_doc


def create_rider(rider_name: str, is_rider_premium: bool = False):  # Service for the POST() method
    rider_doc = RiderDocument(name=rider_name,
                              premium=is_rider_premium
                              )  # Create a new rider object
    rider_doc.save()  # Save the newly created rider object to the db
    return [rider_doc]  # Return the list of one rider object that was created


def update_rider(rider_id: str, is_rider_premium: bool):  # Service for the PATCH() method
    rider_doc = RiderDocument.objects(id=rider_id).first()  # extracting the first object from a list of one object
    rider_doc.update(premium=is_rider_premium)
    rider_doc.reload()  # Get the latest copy from the db
    return [rider_doc]  # Return the list of one rider object that was updated


def init_riders():  # Initialize the db with default riders if there are no existing riders
    existing_riders = RiderDocument.objects()  # List of all rider objects in the db
    if len(existing_riders) == 0:
        for rider_name in default_riders:
            create_rider(rider_name)
