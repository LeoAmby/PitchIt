from flask import Flask
# from flask_bootstrap import Bootstrap
# from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
db = SQLAlchemy(app)


def create_app():
    app.config['SECRET_KEY'] = '0da924e0a1'
    app.config[SQLALCHEMY_DATABASE_URI] = 'sqlite:///db.sqlite3'

    db.init_app(app)

    from auth import auth as auth_blueprint
    app.register_blurprint(auth_blueprint)


    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app