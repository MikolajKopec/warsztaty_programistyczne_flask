from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Auction(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(150))
    price = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone = True), default = func.now())
    owner_id = db.Column(db.Integer,db.ForeignKey('user.id'))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(150),unique = True)
    password = db.Column(db.String(150))
    login = db.Column(db.String(150),unique = True)
    auctions = db.relationship('Auction')