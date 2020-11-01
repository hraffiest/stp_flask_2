from . import app
from config import Config

if __name__ == 'main':
    app.run(port=1861, debug=Config.DEBUG)