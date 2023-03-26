from flask import Blueprint, redirect, url_for, render_template
import random
from service.form.auth import RegisterForm, LoginForm, CreateBaseUserForm
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


@auth.route('/create_account', methods=["GET", "POST"])
def create_base_user():
    form = CreateBaseUserForm()
    if form.validate_on_submit():
        password_hash = random.randint(1, 9)
        pwd = User.password_hash(password_hash)
        user = User(first_name=form.first_name.data, last_name=form.last_name.data, token=form.token.data, password=pwd)
        user.create_users(user)
        return redirect(url_for('home'))
    return render_template('index.html', form=form)


