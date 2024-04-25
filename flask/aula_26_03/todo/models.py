from config import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    email = db.Column(db.String(200))
    login = db.Column(db.String(20))
    password = db.Column(db.String(150))
    tasks=db.relationship('Task')


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(200))
    complete = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))