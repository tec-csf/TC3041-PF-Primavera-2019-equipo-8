from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="frontend/templates")

#Secret key
app.config['SECRET_KEY'] = '83a06f37055cbb6f8eb86a4a2608748c'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///SQLdb.db'
SQLdb = SQLAlchemy(app)

from App.backend import routes