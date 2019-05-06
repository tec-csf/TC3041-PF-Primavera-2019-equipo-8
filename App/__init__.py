from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#import pymongo
#import urllib
from flask_mongoalchemy import MongoAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager



app = Flask(__name__, template_folder="frontend/templates", static_folder="frontend/static")

#Secret key
app.config['SECRET_KEY'] = '83a06f37055cbb6f8eb86a4a2608748c'

#SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///SQLdb.db' #temporal db
SQLdb = SQLAlchemy(app)

#Mongodb
#mongodb_url = urllib.parse.quote('mongodb+srv://Bookmark:FL8qe83XmlAn9cy4@bookmark-t5ss4.mongodb.net/test?retryWrites=true')
#app.config['MONGOALCHEMY_SERVER'] = mongodb_url 
#app.config['MONGOALCHEMY_DATABASE'] = 'Bookmark'
#app.config['MONGOALCHEMY_USER'] = 'Papyrus'
#app.config['MONGOALCHEMY_PASSWORD'] = 'uW0Kt3DuWDyAP76h'
#Mongodb = MongoAlchemy(app) 
#client = pymongo.MongoClient("mongodb+srv://Papyrus:bIY9JeyQIrg8aatP@bookmark-t5ss4.mongodb.net/test?retryWrites=true")
#db = client.test

#Password encryptation
bcrypt = Bcrypt(app)

#Login manager
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from App.backend import routes