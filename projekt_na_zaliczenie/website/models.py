from sqlalchemy.orm import backref
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Auction(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    item_name = db.Column(db.String(150))
    informations = db.Column(db.String(300))
    cw = db.Column(db.Integer)
    kt = db.Column(db.Integer)
    img = db.Column(db.String(150))
    date = db.Column(db.DateTime(timezone = True), default = func.now())
    winner = db.Column(db.String(30))
    owner_id = db.Column(db.Integer,db.ForeignKey('user.id'))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(150),unique = True)
    password = db.Column(db.String(150))
    login = db.Column(db.String(150),unique = True)
    auctions = db.relationship('Auction',backref='user',lazy='dynamic')