from mongoengine import Document, StringField, BooleanField


class RiderDocument(Document):
    name = StringField(max_length=100, required=True)
    premium = BooleanField(required=True, default=False)
