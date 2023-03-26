from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SelectField, TextAreaField, DateTimeField, SubmitField, \
    FileField, IntegerField
from wtforms.validators import DataRequired, NumberRange
from service.model.model import User, Role


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


class ProblemForm(FlaskForm):
    title = StringField('Message', validators=[DataRequired()])
    description = TextAreaField('Text')
    image = FileField('Image')
    submit = SubmitField('Submit')
    user_id = None

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_id = SelectField('User', choices=[(e.id, e.first_name) for e in user if
                                                    'admin' in [role.name for role in e.roles]])


class VoteForm(FlaskForm):
    problem_id = IntegerField('Problem ID', validators=[DataRequired()])
    rating = SelectField('Rating', choices=[(str(i), str(i)) for i in range(1, 6)],
                         validators=[DataRequired(), NumberRange(1, 5)])
    submit = SubmitField('Vote')


