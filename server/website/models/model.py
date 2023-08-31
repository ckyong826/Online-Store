from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
  id=db.Column(db.Integer, primary_key=True)
  email=db.Column(db.String(150), unique=True)
  password=db.Column(db.String(150))
  userName=db.Column(db.String(150))
  cart=db.relationship('Cart')

class Items(db.Model):
  id=db.Column(db.Integer, primary_key=True)
  name=db.Column(db.String(150))
  price=db.Column(db.Integer)
  quantity=db.Column(db.Integer)
  description=db.Column(db.String(150))
  image=db.Column(db.String(150))

class Cart(db.Model):
  id=db.Column(db.Integer, primary_key=True)
  name=db.Column(db.String(150))
  price=db.Column(db.Integer)
  quantity=db.Column(db.Integer)
  description=db.Column(db.String(150))
  image=db.Column(db.String(150))
  user_id=db.Column(db.Integer, db.ForeignKey('user.id'))
  user=db.relationship('User')
