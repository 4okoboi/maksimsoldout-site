from flask import Flask, render_template, redirect, request, url_for, flash, make_response, session
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from datetime import date

app = Flask(__name__)

app.config['SECRET_KEY'] = 'maximsoldout_secret_key'
app.config[
    'SQLALCHEMY_DATABASE_URI'] = "postgresql://eefhinrg:TV-ibXGUzVrEv4TPiGSob_ZQJCFo7B3f@babar.db.elephantsql.com/eefhinrg"
api = Api(app)
db = SQLAlchemy(app)


# модели для базы данных
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    psw = db.Column(db.String)
    date_of_birth = db.Column(db.String)
    vip_lvl = db.Column(db.Integer)
    date_registred = db.Column(db.Date, default=date.today())
    status = db.Column(db.String)
    orders = db.Column(db.Text)


class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Integer)
    brand = db.Column(db.Integer)
    name = db.Column(db.String)
    vendor_code = db.Column(db.String)
    description = db.Column(db.Text)
    # дописать фотки


class Brands(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.Text)
    # дописать лого


class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    items = db.Column(db.String)
    money_sum = db.Column(db.Integer)
    status = db.Column(db.String)
    comment = db.Column(db.String)
    # дописать способы доставки (самовывоз, доставка курьерской службой), способы оплаты (наличными при получении,
    # картой онлайн, криптовалютой)


# ресурсы для апишки
# для пользователей
class UsersApi(Resource):
    def get(self):
        pass

    def post(self):
        pass


# для товаров
class ItemsApi(Resource):
    def get(self):
        pass

    def post(self):
        pass


# для заказов
class OrdersApi(Resource):
    def get(self):
        pass

    def post(self):
        pass


api.add_resource(UsersApi, "/users/<int:id>")
# api.add_resource(ItemsApi, "/items/<int:id>"
api.add_resource(OrdersApi, "/orders/<int:id>")
