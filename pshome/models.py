from pshome import db   

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    password = db.Column(db.String(length=60), nullable=False)
    money = db.Column(db.Integer(), nullable = False, default=0)

class Food(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False)
    url = db.Column(db.String(length=60), nullable=False)
    price = db.Column(db.Integer(), nullable=False)

class Notification(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False)
    name = db.Column(db.String(length=30), nullable=False)
    notification = db.Column(db.String(length=30), nullable=False)
    quantity = db.Column(db.Integer(), nullable=False)
    price = db.Column(db.Integer(), nullable=False)

class Statistical(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    priceFood = db.Column(db.Integer(), nullable=False)
    priceMonney = db.Column(db.Integer(), nullable=False)