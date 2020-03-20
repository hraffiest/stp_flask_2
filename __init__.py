from flask import Flask
from src.models.models import db
from src.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

from src.models.views import *
