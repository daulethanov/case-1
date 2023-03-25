from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SelectField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    street = SelectField('улица')
    email = EmailField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])


class LoginForm(FlaskForm):
    email = EmailField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])



