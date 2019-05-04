from App import Mongodb

class Book(Mongodb.Document):
	title = db.StringField()
	author = db.StringField()
	year = db.IntField()
	genre = db.StringField()
	