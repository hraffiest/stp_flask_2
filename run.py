import __init__
from src.config import Config

__init__.app.run(port=1861, debug=Config.DEBUG)