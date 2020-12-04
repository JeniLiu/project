from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)

class Breakfast(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(300))
    date = db.Column(db.String(50))
    burger = db.Column(db.Integer)
    cheese = db.Column(db.Integer)
    bacon = db.Column(db.Integer)
    hashbrown = db.Column(db.Integer)

class Tea(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    date = db.Column(db.String(50))
    passionfruit = db.Column(db.Integer)
    milktea = db.Column(db.Integer)

class Lunch(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    date = db.Column(db.String(50))
    fries = db.Column(db.Integer)

