from mongoengine import Document, StringField, DictField

class Form(Document):
    name = StringField(required=True, unique=True)
    fields = DictField()
    