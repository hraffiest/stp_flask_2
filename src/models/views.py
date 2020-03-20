from __init__ import app, db
from flask import abort, flash, render_template, request, redirect


# ------------------------------------------------------
# Декораторы авторизации
def login_required(f):
    pass
    # (код декоратора)


def admin_only(f):
    pass
    # (код декоратора)


# ------------------------------------------------------
# Страница админки
@app.route('/')
@login_required
def home():
    pass
    # (код страницы админки)


# ------------------------------------------------------
# Страница аутентификации
@app.route("/login", methods=["GET", "POST"])
def login():
    pass
    # (код страницы аутентификации)


# ------------------------------------------------------
# Страница выхода из админки
@app.route('/logout', methods=["POST"])
@login_required
def logout():
    pass
    # (код выхода из админки)


# ------------------------------------------------------
# Страница добавления пользователя
@app.route("/registration", methods=["GET", "POST"])
@admin_only
@login_required
def registration():
    pass
    # (код страницы регистрации)


# ------------------------------------------------------
# Страница смены пароля
@app.route("/change-password", methods=["GET", "POST"])
@login_required
def change_password():
    pass
    # (код страницы смены пароля)