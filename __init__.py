from flask import Flask
from config import Config
from models import *
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
admin = Admin(app)

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Order, db.session))
admin.add_view(ModelView(Dish, db.session))
admin.add_view(ModelView(Category, db.session))

from views import *

with app.app_context():
    db.create_all()

