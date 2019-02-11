from flask import render_template,redirect,url_for, flash,request
from  . import auth
from flask_login import login_user,logout_user,login_required, current_user
from ..models import User
from ..email import send_email, send_reset_email
from .forms import LoginForm,RegistrationForm
import os

from .. import db

@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get("next") or url_for('main.index'))
        flash('Invalid username or Password')
    title = "login"
    return render_template('auth/login.html', login_form = login_form, title = title)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    # flash("You have been successfully logged out")
    return redirect(url_for('main.index'))

@auth.route('/register',methods = ['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()

        # mail_message('Welcome to one minute pitch', 'email/welcome_user', user.email, user=user)
        # send_email(subject="Registration", sender=os.environ.get('MAIL_USERNAME'),recepients=[user.email],text_body='Test Email',html_body=render_template('fourOwfour.html'))

        return redirect(url_for('auth.login'))

    title = "New Account"

    return render_template('auth/register.html',registration_form = form, title = title)
