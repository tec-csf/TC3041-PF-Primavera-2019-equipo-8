from App import Mongodb

class User(Mongodb.Model):
    username = Mongodb.StringField()
    email = Mongodb.StringField()
    image_file = Mongodb.StringField(default='default.jpg')
    password = Mongodb.StringField()
    reviews = Mongodb.DocumentField(Review)

class Review(Mongodb.Model):
    date_posted = Mongodb.DateTimeField(default=datetime.utcnow)
    content = Mongodb.StringField()
    user_id = Mongodb.StringField()

class Book(Mongodb.Document):
	title = Mongodb.StringField()
	author = Mongodb.StringField()
	year = Mongodb.IntField()
	genre = Mongodb.StringField()
	image_file = Mongodb.StringField()