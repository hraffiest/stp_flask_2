import re

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError, Email, InputRequired


def password_check(form, field):
    pass


class LoginForm(FlaskForm):
    pass


class RegistrationForm(FlaskForm):
    username = StringField('Ваше имя(email)',
                           [Length(min=4, max=25, message='Ваше имя должно быть в пределах от 4-х до 25-ти символов'),
                            InputRequired(message='Поле Ваше имя обязательно для заполнения'),
                            Email(message='Email введен неверно')])
    password = PasswordField('Пароль',
                             [Length(min=8, max=25, message='Ваш пароль должно быть в пределах от 8 до 25-ти символов'),
                              InputRequired(message='Поле Пароль обязательно для заполнения')])


class OrderForm(FlaskForm):
    username = StringField('Ваше имя',
                           [Length(min=4, max=25, message='Ваше имя должно быть в пределах от 4-х до 25-ти символов'),
                            InputRequired(message='Поле Ваше имя обязательно для заполнения')])

    address = StringField('Адрес', [Length(min=4, message='Поле Адрес слишком короткое'),
                                    InputRequired(message='Поле Адрес обязательно для заполнения')])

    email = StringField('Email', [Email(message='Email введен неверно'),
                                  InputRequired(message='Поле Email обязательно для заполнения')])

    telephone = StringField('Телефон для связи', [Length(min=4),
                                                  InputRequired(message='Поле Телефон обязательно для заполнения')])
