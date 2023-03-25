from flask import Blueprint, redirect, url_for, render_template

from service.form.auth import RegisterForm, LoginForm
from service.model.model import User
auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, password=form.password.data, street=form.street.data)
        user.password_hash(form.password.data)
        user.create_users(user)
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, password=form.password.data)
        if user:
            user.check_password(password=form.password.data)
            return redirect('register')

    return render_template('login.html', form=form)
