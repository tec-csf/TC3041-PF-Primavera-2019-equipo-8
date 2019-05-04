from App import SQLdb
from datetime import datetime

class User(SQLdb.Model):
    id = SQLdb.Column(SQLdb.Integer, primary_key=True)
    username = SQLdb.Column(SQLdb.String(20), unique=True, nullable=False)
    email = SQLdb.Column(SQLdb.String(120), unique=True, nullable=False)
    image_file = SQLdb.Column(SQLdb.String(20), nullable=False, default='default.jpg')
    password = SQLdb.Column(SQLdb.String(60), nullable=False)
    posts = SQLdb.relationship('Review', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}', '{self.username}')"

class Review(SQLdb.Model):
    id = SQLdb.Column(SQLdb.Integer, primary_key=True)
    date_posted = SQLdb.Column(SQLdb.DateTime, nullable=False, default=datetime.utcnow)
    content = SQLdb.Column(SQLdb.Text, nullable = False)
    user_id = SQLdb.Column(SQLdb.Integer, SQLdb.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.date_posted}','{self.content}')"
