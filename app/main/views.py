from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import main
from app.models import User
from werkzeug.security import generate_password_hash
from .. import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/')
def profile():
    render_template ('profile.html')

@main.route('/login')
def login():
    return render_template('login.html')

# @auth.route('/login', methods=['POST'])
# def login_post():

@main.route('/signup')
def signup():
    return render_template('signup.html')

@main.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if user:
        flash('Email address already exists!')
        return redirect(url_for('main.signup'))

    new_user = User(email=email, name=name, password=generate_password_hash(password, method='leo357'))
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('main.login'))

@main.route('/logout')
def logout():
    return redirect(url_for('main.index'))


if __name__ == '__main__':
    main.run(debug=True)
