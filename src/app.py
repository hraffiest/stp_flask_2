from flask import Flask
from models.models import db, User
from configz import Config
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms import StringField
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
admin = Admin(app)


if __name__ == '__main__':
    app.run(port=4999, debug=True)