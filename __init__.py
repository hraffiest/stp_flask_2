from flask import Flask
from config import Config
from models import *
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
admin = Admin(app)


class NewModel(ModelView):
    can_create = False
    can_edit = False
    can_delete = False


admin.add_view(NewModel(User, db.session))
admin.add_view(NewModel(Order, db.session))
admin.add_view(NewModel(Dish, db.session))
admin.add_view(NewModel(Category, db.session))

from views import *

with app.app_context():
    db.create_all()

