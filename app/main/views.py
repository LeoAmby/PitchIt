from flask import Blueprint, render_template, redirect, url_for
from . import main

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

# @uth.route('/signup', methods=['POST'])
# def signup_post():

@main.route('/logout')
def logout():
    return redirect(url_for('main.index'))


