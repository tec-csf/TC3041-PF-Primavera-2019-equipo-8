from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymongo
from flask_bcrypt import Bcrypt
from flask_session import Session


app = Flask(__name__, template_folder="frontend/templates",
            static_folder="frontend/static")

# Secret key
app.config['SECRET_KEY'] = '83a06f37055cbb6f8eb86a4a2608748c'

# SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbs/SQLdb.db'  # temporal db
SQLdb = SQLAlchemy(app)

# Password encryptation
bcrypt = Bcrypt(app)

# Session manager
SESSION_TYPE = 'redis'
app.config.from_object(__name__)
Session(app)

from App.backend import routes
