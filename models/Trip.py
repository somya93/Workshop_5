from mongoengine import Document, StringField


class Trip(Document):
    trip_id = StringField(max_length=10, required=True)
    fare = StringField(max_length=100, required=True)
    rider_id = StringField(max_length=10, required=True)
