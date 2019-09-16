from flask import Flask
# from flask_bootstrap import Bootstrap
# from config import config
# from flask_sqlalchemy import flask_sqlalchemy



app = Flask(__name__)


def create_app():
    app.config.from_object(Config)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app