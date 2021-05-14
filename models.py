from flask_mongoengine import MongoEngine

db = MongoEngine()

COURSE_GOAL = ['all_body', 'butt', 'drying', 'stretching']
COURSE_TYPE = ['at_home', 'at_gym']
FAQ_TYPE = ['other', 'food', 'giveaway', 'training']


class Course(db.Document):
    name = db.StringField(required=True, max_lenght=70)
    price = db.fields.IntField(required=True, min_value=0)
    goal = db.StringValue(required=True, choices=COURSE_GOAL)
    type = db.StringField(required=True, choices=COURSE_TYPE)
    description = db.StringField()


class Client(db.Document):
    first_name = db.StringField(required=True, max_lenght=70)
    last_name = db.StringField(required=True, max_lenght=70)
    birth_date = db.DateTimeField(required=True)
    email = db.EmailField(reqired=True)
    phone = db.StringField(required=True, max_lenght=13)
    country = db.StringField(required=True, max_lenght=70)
    location = db.StringField(required=True, max_lenght=70)


class FAQ(db.Document):
    type = db.StringField(required=True, choices=FAQ_TYPE)
    content = db.StringField(required=True, max_lenght=1000)


class Question(db.Document):
    type = db.StringField(required=True, choices=FAQ_TYPE)
    first_name = db.StringField(required=True, max_lenght=70)
    email = db.EmailField(reqired=True)
    phone = db.StringField(required=True, max_lenght=13)
    content = db.StringField(required=True, max_lenght=1000)
