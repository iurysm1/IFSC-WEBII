from config import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    email = db.Column(db.String(200))
    login = db.Column(db.String(20))
    password = db.Column(db.String(150))
    tasks = db.relationship('Task')

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    complete = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Fornecedor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    razao_social = db.Column(db.String(200))
    email = db.Column(db.String(200))
    telefone = db.Column(db.String(13))
    site = db.Column(db.String(200))
    produtos = db.relationship('Produto')

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200))
    estoque = db.Column(db.Integer)
    preco = db.Column(db.Float)
    fornecedor_id = db.Column(db.Integer, db.ForeignKey('fornecedor.id'))