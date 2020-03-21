from __init__ import app, db
from flask import abort, flash, render_template, request, redirect


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
    return render_template('main.html')


# ------------------------------------------------------
# для корзины
@app.route("/cart/", methods=["GET", "POST"])
def show_the_cart():
    pass
    # (код страницы для корзины)


# ------------------------------------------------------
# Страница аутентификации
@app.route("/login", methods=["GET", "POST"])
def do_the_login():
    pass
    # (код страницы аутентификации)


# ------------------------------------------------------
# Страница выхода из админки
@app.route('/logout', methods=["POST"])
def do_the_logout():
    pass
    # (код выхода из админки)


# ------------------------------------------------------
# Страница добавления пользователя
@app.route("/register", methods=["GET", "POST"])
def do_the_reg():
    pass
    # (код страницы регистрации)


# ------------------------------------------------------
# для подтверждения отправки
@app.route("/ordered/", methods=["GET", "POST"])
def show_the_order():
    pass
    # (код страницы для подтверждения отправки)


# ------------------------------------------------------
# для личного кабинета
@app.route("/account/", methods=["GET", "POST"])
def show_the_lk():
    pass
    # (код страницы для лк)
