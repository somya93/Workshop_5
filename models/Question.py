from mongoengine import Document, StringField, ListField, IntField, DateField, ObjectIdField


class QuestionDocument(Document):
    question_text = StringField(max_length=200, required=True)
    replies = ListField(field=StringField())
    num_replies = IntField()
    date_created = DateField(required=True)

