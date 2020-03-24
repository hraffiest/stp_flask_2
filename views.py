from __init__ import app, db
from models import *
import json
from pymorphy2 import MorphAnalyzer
import datetime
from flask import abort, flash, render_template, request, redirect, session, url_for
from forms import OrderForm, LoginForm, RegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash


def get_cart_info(ids):
    cart = []
    for id in ids:
        cart.append(db.session.query(Dish).get(id).price)
    return [len(ids), sum(cart)]


def get_right_cart_end():
    morph = MorphAnalyzer()
    word = morph.parse('блюдо')[0]
    cart = session.get("cart")
    cart_info = [0, 0]
    if cart:
        cart_info = get_cart_info(session['cart'])
        cart_info1 = '{} {}'.format(cart_info[0], word.make_agree_with_number(cart_info[0]).word)
        cart_info[0] = cart_info1
    return cart_info


#
# # ------------------------------------------------------
# # Декораторы авторизации
# def login_required(f):
#     pass
#     # (код декоратора)
#
#
# def admin_only(f):
#     pass
#     # (код декоратора)
#


# ------------------------------------------------------
# Главная
@app.route('/')
def home():
    # cook the dict 'dishes_d' for main page
    cart_info = get_right_cart_end()
    dishes_d = dict()
    cats = db.session.query(Category).order_by(Category.c_id).all()
    dishes = db.session.query(Dish).order_by(Dish.cat_id).all()
    for cat in cats:
        dishes_d[cat.title] = []
        for dish in dishes:
            if cat.c_id == dish.cat_id:
                dishes_d[cat.title].append(dish)
    return render_template('main.html', dishes_d=dishes_d, cart_info=cart_info)


@app.route("/addtocart/<int:d_id>/")
def add_to_cart(d_id):
    cart = session.get("cart", [])
    cart.append(d_id)
    session['cart'] = cart
    return redirect('/cart/')


@app.route("/delfromcart/<int:d_id>/")
def del_from_cart(d_id):
    cart = session.get("cart")
    cart.remove(d_id)
    session['cart'] = cart
    return redirect('/cart/')


# ------------------------------------------------------
# для корзины
@app.route("/cart/", methods=['GET'])
def show_the_cart():
    cart_info = get_right_cart_end()
    form = OrderForm(price=cart_info[1])
    cart = session.get("cart", [])
    dishes_for_buy = []
    for d in cart:
        dishes_for_buy.append(db.session.query(Dish).get(d))
    return render_template('cart.html', cart_info=cart_info, form=form, dishes=dishes_for_buy)


# ------------------------------------------------------
# Страница аутентификации
@app.route("/login/", methods=["GET", "POST"])
def do_the_login():
    if session.get('user'):
        return redirect('/account/')
    cart_info = get_right_cart_end()
    form = LoginForm()
    if request.method == "POST":
        if form.validate_on_submit():
            user = db.session.query(User).filter(User.mail == form.username.data).first()
            if user and user.password_valid(form.password.data):
                session['user'] = {'user_id': user.u_id, 'mail': user.mail}
                return redirect('/account/')
            elif not user:
                form.errors['auth'] = ['Пользователь с таким email не найден']
                return render_template("login.html", form=form, cart_info=cart_info)
            elif not user.password_valid(form.password.data):
                form.errors['pass'] = ['Неверный пароль']
                return render_template("login.html", form=form, cart_info=cart_info)
            else:
                return render_template("login.html", form=form, cart_info=cart_info)
        else:
            return render_template("login.html", form=form, cart_info=cart_info)
    return render_template('login.html', cart_info=cart_info, form=form)


# ------------------------------------------------------
# Страница выхода из админки
@app.route('/logout/')
def do_the_logout():
    session.pop("user")
    # (код выхода из админки)
    return redirect('/')


# ------------------------------------------------------
# Страница добавления пользователя
@app.route("/registration/", methods=["GET", "POST"])
def do_the_reg():
    if session.get('user_id'):
        return redirect("/")
    cart_info = get_right_cart_end()
    # Создаем форму
    form = RegistrationForm()
    if request.method == "POST":
        if form.validate_on_submit():
            user = db.session.query(User).filter(User.mail == form.username.data).first()
            if not user:
                user = User()
                user.mail = form.username.data
                user.password_hash = form.password.data
                db.session.add(user)
                db.session.commit()
                session['user'] = {'user_id': user.u_id, 'mail': user.mail}
                return redirect('/account/')
            else:
                form.errors['auth'] = ['Пользователь с таким email уже существует']
                return render_template("register.html", form=form, cart_info=cart_info)
        else:
            return render_template("register.html", form=form, cart_info=cart_info)
    else:
        return render_template("register.html", form=form, cart_info=cart_info)


# ------------------------------------------------------
# для подтверждения отправки
@app.route("/ordered/", methods=["GET", "POST"])
def show_the_order():
    if request.method == "POST":
        form = OrderForm()
        if form.validate_on_submit():
            dishes_ids = session['cart']
            date = datetime.datetime
            user = db.session.query(User).get(session['user']['user_id'])
            print(user)
            user.address = form.address.data
            user.name = form.username.data
            order = Order(price=form.price.data, date=date, dishes=dishes_ids, buyer_id=user)
            db.session.add(order, user)
            db.session.commit()
        return render_template('ordered.html')
    return redirect('/cart/')


# ------------------------------------------------------
# для личного кабинета
@app.route("/account/", methods=["GET", "POST"])
def show_the_lk():
    cart_info = get_right_cart_end()
    return render_template('account.html', cart_info=cart_info)
