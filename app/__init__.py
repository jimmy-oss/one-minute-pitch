from flask import Flask
from flask_sqlalchemy import SQLAlchemy
 
 
# create an instance of my app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'f9bf78b9a18ce6d46a0cd2b0b86df9da'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db = SQLAlchemy(app)

from app import app