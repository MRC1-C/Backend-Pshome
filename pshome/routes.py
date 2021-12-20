
from pshome import app
from pshome import db
from pshome.models import User, Food, Notification, Statistical
from flask import jsonify
from flask import request
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from flask_cors import CORS
JWTManager(app)
CORS(app)

monney = 0

def food(f):
    return {
        "id": f.id,
        "name": f.name,
        "url": f.url,
        "price": f.price
    }

def user(f):
    return {
        "id": f.id,
        "username": f.username,
        "password": f.password,
        "monney": int(f.money)
    }
def notification(f):
    return {
        "id": f.id,
        "username": f.username,
        "name": f.name,
        "quantity": f.quantity,
        "price": f.price,
        "notification": f.notification
    }

@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user = User.query.filter_by(username=username).first()
    if user:
        global monney
        monney = user.money
        if user.password!=password:
            return jsonify({"msg": "Bad username or password"}), 401
        access_token = create_access_token(identity=username)
        return jsonify({"access_token":access_token, "monney": monney})
    else:
        return jsonify({"msg": "Bad username or password"}), 401
@app.route("/getuser", methods=["GET"])
@jwt_required()
def getuser():
    current_user = get_jwt_identity()
    return jsonify({"username": current_user, "monney": monney}), 200

@app.route("/changepassword", methods=["POST"])
@jwt_required()
def changepassword():
    current_user = get_jwt_identity()
    user = User.query.filter_by(username=current_user).first()
    user.password = request.json.get("newpassword", None)
    db.session.commit()
    return ""

@app.route("/getfood", methods=["GET"])
def getfood():
    foods = Food.query.all() 
    return jsonify([*map(food,foods)])

@app.route("/getalluser", methods=["GET"])
def getalluser():
    users = User.query.all() 
    return jsonify([*map(user,users)])

@app.route("/getnotification", methods=["GET"])
def getnotification():
    notifications = Notification.query.all() 
    return jsonify([*map(notification,notifications)])

@app.route("/getcount", methods=["GET"])
def getcount():
    notifications = Notification.query.all() 
    return jsonify({"count": len(notifications)})

@app.route("/moremonney", methods=["POST"])
@jwt_required()
def moremonney():
    current_user = get_jwt_identity()
    user = User.query.filter_by(username=current_user).first()
    user.money = request.json.get("moremonney", None)
    db.session.commit()
    return "1"

@app.route("/moremonneyuser", methods=["POST"])
def moremonneyuser():
    username = request.json.get("username", None)
    user = User.query.filter_by(username=username).first()
    user.money = request.json.get("moremonney", None)
    db.session.commit()
    return "1"

@app.route("/createuser", methods=["POST"])
def createuser():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    money = request.json.get("monney", None)
    newUser = User(username = username,password=password,money=money)
    db.session.add(newUser)
    db.session.commit()
    return "1"

@app.route("/createfood", methods=["POST"])
def createfood():
    name = request.json.get("name", None)
    url = request.json.get("url", None)
    price = request.json.get("price", None)
    newFoods = Food(name = name,url=url,price=price)
    db.session.add(newFoods)
    db.session.commit()
    return "1"

@app.route("/createnotification", methods=["POST"])
def createnotification():
    username = request.json.get("username", None)
    name = request.json.get("name", None)
    quantity = request.json.get("quantity", None)
    price = request.json.get("price", None)
    notification = request.json.get("notification", None)
    newNotification = Notification(username = username,name=name,notification=notification,quantity=quantity,price=price)
    db.session.add(newNotification)
    db.session.commit()
    return "1"

@app.route("/deleteuser", methods=["POST"])
def deleteuser():
    username = request.json.get("username", None)
    user = User.query.filter_by(username=username).first()
    db.session.delete(user)
    db.session.commit()
    return "1"
@app.route("/deletenotification", methods=["POST"])
def deletenotification():
    id = request.json.get("id", None)
    notification = Notification.query.filter_by(id=id).first()
    db.session.delete(notification)
    db.session.commit()
    return "1"
@app.route("/createstatistical", methods=["POST"])
def createstatistical():
    priceFood = request.json.get("priceFood", None)
    priceMonney = request.json.get("priceMonney", None)
    newStatistical = Statistical(priceMonney = priceMonney,priceFood=priceFood)
    db.session.add(newStatistical)
    db.session.commit()
    return "1"

@app.route("/deletefood", methods=["POST"])
def deletefood():
    name = request.json.get("name", None)
    food = Food.query.filter_by(name=name).first()
    db.session.delete(food)
    db.session.commit()
    return "1"

@app.route("/editfood", methods=["POST"])
def editfood():
    nameold = request.json.get("nameold", None)
    name = request.json.get("name", None)
    url = request.json.get("url", None)
    price = request.json.get("price", None)
    food = Food.query.filter_by(name=nameold).first()
    food.name = name
    food.url = url
    food.price = price
    db.session.commit()
    return "1"
@app.route("/getStatiscical", methods=["GET"])
def getStatiscical():
    statistical = Statistical.query.all() 
    priceFood = 0
    priceMonney = 0
    for i in statistical:
        priceFood = priceFood + i.priceFood
        priceMonney = priceMonney + i.priceMonney
    return jsonify({"priceMonney": priceMonney, "priceFood": priceFood})

