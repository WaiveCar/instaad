from flask import Blueprint, render_template, url_for, flash, redirect, request
from flask_login import current_user, login_required, login_user, logout_user
from website import db, bcrypt
from website.users.forms import RegistrationForm, LoginForm
from website.models import User


users = Blueprint('users', __name__)

@users.route("/login", methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Log In Unsuccessful, please check email and password', 'danger')
    return (render_template('login.html',title='Login',form=form))

@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@users.route("/register", methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account successfully created for '+user.email+'!','success')
        login_user(user)
        return redirect(url_for('users.user'))
    return (render_template('register.html', title='Register',form=form))

@users.route("/user")
@login_required
def user():
    if current_user.is_authenticated:
        return (render_template('user.html',title='User'))
    else:
        flash('You are not logged in', 'danger')
