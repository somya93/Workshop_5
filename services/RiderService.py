from models.Rider import RiderDocument

default_riders = ['Karim', 'Manuja', 'Phil']


def get_rider(rider_id: str):
    if rider_id is None:
        rider_doc = RiderDocument.objects()
    else:
        rider_doc = RiderDocument.objects(id=rider_id)
    return rider_doc


def create_rider(rider_name: str, is_rider_premium: bool = False):
    rider_doc = RiderDocument(name=rider_name,
                              premium=is_rider_premium
                              )
    rider_doc.save()
    return [rider_doc]


def update_rider(rider_id: str, is_rider_premium: bool):
    rider_doc = RiderDocument.objects(id=rider_id).first()
    rider_doc.update(premium=is_rider_premium)
    rider_doc.reload()
    return [rider_doc]


def init_riders():
    existing_riders = RiderDocument.objects()
    if len(existing_riders) == 0:
        for rider_name in default_riders:
            create_rider(rider_name)
