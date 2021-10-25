from mongoengine import Document, StringField, BooleanField


class Rider(Document):
    name = StringField(max_length=100, required=True)
    premium = BooleanField(required=True, default=False)
