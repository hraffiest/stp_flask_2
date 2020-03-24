from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Настройки соединения сделаем позже в модуле приложения
db = SQLAlchemy()

orders_dishes_association = db.Table(
    "orders_dishes",
    db.Column("dish_id", db.Integer, db.ForeignKey("dishes.d_id")),
    db.Column("order_id", db.Integer, db.ForeignKey("orders.o_id")),
)


class User(db.Model):
    __tablename__ = 'users'
    u_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    mail = db.Column(db.String(50), nullable=False)
    _password_hash = db.Column(db.String(180), nullable=False)
    address = db.Column(db.String(190))
    orders = db.relationship("Order", back_populates="user")

    @property
    def password_hash(self):
        # Запретим прямое обращение к паролю
        raise AttributeError("Вам не нужно знать пароль!")

    @password_hash.setter
    def password_hash(self, password):
        # Устанавливаем пароль через этот метод
        self._password_hash = generate_password_hash(password)

    def password_valid(self, password):
        # Проверяем пароль через этот метод
        # Функция check_password_hash превращает password в хеш и сравнивает с хранимым
        return check_password_hash(self._password_hash, password)


class Order(db.Model):
    __tablename__ = 'orders'
    o_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    final_price = db.Column(db.Float, nullable=False)
    user = db.relationship("User", back_populates="orders")
    buyer_id = db.Column(db.Integer, db.ForeignKey("users.u_id"))
    dishes = db.relationship(
        "Dish", secondary=orders_dishes_association, back_populates="orders"
    )


class Dish(db.Model):
    __tablename__ = 'dishes'
    d_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(180), nullable=False)
    picture = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    category = db.relationship("Category", back_populates="dishes")
    cat_id = db.Column(db.Integer, db.ForeignKey("categories.c_id"))
    orders = db.relationship(
        "Order", secondary=orders_dishes_association, back_populates="dishes"
    )


class Category(db.Model):
    __tablename__ = 'categories'
    c_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    dishes = db.relationship("Dish", back_populates="category")
