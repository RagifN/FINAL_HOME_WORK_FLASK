from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mynewsdatabase.db'
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'{self.firstname} {self.lastname}'


class TheGoods(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    goods_name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    price = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'{self.goods_name} {self.description} {self.price}'


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(80), db.ForeignKey('user.id'))
    goods_id = db.Column(db.String(80), db.ForeignKey('goods.id'))
    date = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    students = db.relationship('TheGoods', backref='user', lazy=True)

    def __repr__(self):
        return f'{self.date} {self.status}'
