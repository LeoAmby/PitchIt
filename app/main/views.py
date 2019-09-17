from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import main
from app.models import User
from werkzeug.security import generate_password_hash
from .. import db
from flask_login import login_user #creates cookie in the app
from flask_login import login_required, current_user


main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/')
@login_required
def profile():
    return render_template ('profile.html', name=current_user.name)

@main.route('/login')
def login():
    return render_template('login.html')
    

@main.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    
    user = User.query.filter_by(email=email).first()

    if not user and not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('main.login'))

    login_user(user)
    return redirect(url_for('main.profile'))

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
