from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mongoalchemy import MongoAlchemy

app = Flask(__name__, template_folder="frontend/templates", static_folder="frontend/static")

#Secret key
app.config['SECRET_KEY'] = '83a06f37055cbb6f8eb86a4a2608748c'

#SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///SQLdb.db' #temporal db
SQLdb = SQLAlchemy(app)

#Mongodb
app.config['MONGOALCHEMY_DATABASE'] = 'mongodb:///Mongodb.db' #temporal db
Mongodb = SQLAlchemy(app)

from App.backend import routes