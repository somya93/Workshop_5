from mongoengine import Document, StringField, BooleanField


class Rider(Document):
    rider_id = StringField(max_length=10, required=True)
    name = StringField(max_length=100, required=True)
    email = StringField(max_length=100, required=True)
    premium = BooleanField(required=True, default=False)
