from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Настройки соединения сделаем позже в модуле приложения
db = SQLAlchemy()

orders_dishes_association = db.Table(
    "orders_dishes",
    db.Column("dish_id", db.Integer, db.ForeignKey("dishes.id")),
    db.Column("order_id", db.Integer, db.ForeignKey("orders.id")),
)

class User(db.Model):
    __tablename__ = 'users'
    u_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    mail = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(150), nullable=False)
    orders = db.relationship("Order", back_populates="user")


class Order(db.Model):
    __tablename__ = 'orders'
    o_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    final_price = db.Column(db.Float, nullable=False)
    user = db.relationship("User", back_populates="orders")
    buyer_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    dishes = db.relationship(
        "Dish", secondary=orders_dishes_association, back_populates="orders"
    )


class Dish(db.Model):
    __tablename__ = 'dishes'
    d_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    picture = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(150), nullable=False)
    category = db.relationship("Category", back_populates="dishes")
    cat_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    orders = db.relationship(
        "Order", secondary=orders_dishes_association, back_populates="dishes"
    )


class Category(db.Model):
    __tablename__ = 'categories'
    c_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    dishes = db.relationship("Dish", back_populates="category")

