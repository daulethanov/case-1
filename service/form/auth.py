from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SelectField, IntegerField
from wtforms.validators import DataRequired

from service.model.model import User


class RegisterForm(FlaskForm):
    # street = SelectField('улица', choices=[(user.name, user.value) for user in User.street])
    email = EmailField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])


class LoginForm(FlaskForm):
    email = EmailField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])


class CreateBaseUserForm(FlaskForm):
    token = IntegerField('Номер', validators=[DataRequired()])
    first_name = StringField('Name', validators=[DataRequired()])
    last_name = StringField('last_namr', validators=[DataRequired()])
    # street = SelectField('улица', choices=[(user.dom, user.value) for user in User.street])
    # dom = SelectField('дом', choices=[(user.dom, user.value) for user in User.dom])
