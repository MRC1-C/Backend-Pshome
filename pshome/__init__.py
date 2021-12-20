from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pshome.db'
db = SQLAlchemy(app)
from pshome import routes
