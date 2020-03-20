from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms import StringField
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = 'asdwefwedf'
db = SQLAlchemy(app)
admin = Admin(app)


if __name__ == '__main__':
    app.run(port=4999, debug=True)