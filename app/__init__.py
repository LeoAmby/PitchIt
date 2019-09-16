from flask import Flask
# from flask_bootstrap import Bootstrap
# from config import config
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
db = SQLAlchemy(app)
manager = Manager(app)

def create_app():
    app.config.from_object(Config)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app