from flask import Flask
# from flask_bootstrap import Bootstrap
# from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'



db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '0da924e0a1'
    app.config[SQLALCHEMY_DATABASE_URI] = 'sqlite:///db.sqlite3'

    db.init_app(app)
    


    from auth import auth as auth_blueprint
    app.register_blurprint(auth_blueprint)


    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app