from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SelectField, TextAreaField, DateTimeField, SubmitField, \
    FileField
from wtforms.validators import DataRequired


class ProblemForm(FlaskForm):
    message = StringField('Message', validators=[DataRequired()])
    image = FileField('Image')
    submit = SubmitField('Submit')
    user_id = SelectField()



class UserRoomForm(FlaskForm):
    user_id = SelectField()
    message = StringField('Message', validators=[DataRequired()])
    description = TextAreaField('Description')
    notification_time = DateTimeField('Notification Time')
    submit = SubmitField('Create User Room')


class MessageForm(FlaskForm):
    user_id = SelectField()
    message = StringField('Message', validators=[DataRequired()])
    finish = DateTimeField('Finish')
    notification_time = DateTimeField('Notification Time')
    submit = SubmitField('Create Message')