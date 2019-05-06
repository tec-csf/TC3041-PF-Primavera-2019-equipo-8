from App import SQLdb, login_manager
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(SQLdb.Model, UserMixin):
    id = SQLdb.Column(SQLdb.Integer, primary_key=True)
    username = SQLdb.Column(SQLdb.String(20), unique=True, nullable=False)
    email = SQLdb.Column(SQLdb.String(120), unique=True, nullable=False)
    image_file = SQLdb.Column(SQLdb.String(20), nullable=False, default='default.jpg')
    password = SQLdb.Column(SQLdb.String(60), nullable=False)
    reviews = SQLdb.relationship('Review', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}', '{self.username}')"

class Review(SQLdb.Model):
    id = SQLdb.Column(SQLdb.Integer, primary_key=True)
    date_posted = SQLdb.Column(SQLdb.DateTime, nullable=False, default=datetime.utcnow)
    content = SQLdb.Column(SQLdb.Text, nullable = False)
    user_id = SQLdb.Column(SQLdb.Integer, SQLdb.ForeignKey('user.id'), nullable=False)
    book_id = SQLdb.Column(SQLdb.Integer, SQLdb.ForeignKey('book.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.date_posted}','{self.content}')"

class Book(SQLdb.Model):
    id = SQLdb.Column(SQLdb.Integer, primary_key=True)
    title = SQLdb.Column(SQLdb.String(20), nullable=False)
    author = SQLdb.Column(SQLdb.String(20), nullable=False)
    year = SQLdb.Column(SQLdb.Integer, nullable=False)
    genre = SQLdb.Column(SQLdb.String(20), nullable=False)
    image_file = SQLdb.Column(SQLdb.String(20), nullable=False)
    reviews = SQLdb.relationship('Review', backref='book_reviewed', lazy=True)

    def __repr__(self):
        return f"Book('{self.title}','{self.author}','{self.genre}')"

SQLdb.create_all()
SQLdb.session.commit()