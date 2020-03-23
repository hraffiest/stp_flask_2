from __init__ import app, db
from models import *
import json
from pymorphy2 import MorphAnalyzer
from flask import abort, flash, render_template, request, redirect, session, url_for


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


# ------------------------------------------------------
# для корзины
@app.route("/cart/", methods=['GET', 'POST'])
def show_the_cart():
    cart_info = get_right_cart_end()
    return render_template('cart.html', cart_info=cart_info)
#
#
# # ------------------------------------------------------
# # Страница аутентификации
# @app.route("/login", methods=["GET", "POST"])
# def do_the_login():
#     pass
#     # (код страницы аутентификации)
#
#
# # ------------------------------------------------------
# # Страница выхода из админки
# @app.route('/logout', methods=["POST"])
# def do_the_logout():
#     pass
#     # (код выхода из админки)
#
#
# # ------------------------------------------------------
# # Страница добавления пользователя
# @app.route("/register", methods=["GET", "POST"])
# def do_the_reg():
#     pass
#     # (код страницы регистрации)
#
#
# # ------------------------------------------------------
# # для подтверждения отправки
# @app.route("/ordered/", methods=["GET", "POST"])
# def show_the_order():
#     pass
#     # (код страницы для подтверждения отправки)
#
#
# # ------------------------------------------------------
# # для личного кабинета
# @app.route("/account/", methods=["GET", "POST"])
# def show_the_lk():
#     pass
#     # (код страницы для лк)
