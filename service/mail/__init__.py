from flask_jwt_extended import create_access_token
from flask_mail import Mail
from flask import url_for
from service.model.chat import Message

mail = Mail()


def send_password_reset_email(user):
    token = user.create_token()
    msg = Message('Reset Your Password',
                  sender='aliz1233773@gmail.com',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('auth.reset_password', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)