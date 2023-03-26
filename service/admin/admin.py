from datetime import datetime, timedelta
import pytz
from flask import flash
from flask_admin import Admin
from flask_admin.actions import action
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from service import db
from service.model.model import User, Role, Message, UserRoom, Problem, ProblemRating, Idea

admin = Admin()


class MyModelView(ModelView):
    def is_accessible(self):
        if not current_user.is_authenticated:
            return False

        for role in current_user.roles:
            if role.name == 'admin':
                return True
        return False


class UserAdminView(ModelView):
    # column_display_pk = True
    column_hide_backrefs = False
    column_list = ('id', 'first_name', 'last_name', 'email', 'password', 'token', 'active',
                   'created_at', 'street', 'dom', 'number', 'message', 'roles')
    # form_columns = ('first_name', 'last_name', 'email', 'password', 'token', 'active',
    #                 'street', 'dom', 'number', 'messages', 'roles')


class RatingAdmin(ModelView):
    column_hide_backrefs = False
    column_list = ('problem_id', 'user_id', 'rating')


class IdeaAdmin(ModelView):
    column_hide_backrefs = False

    column_list = ('user_id', 'title', 'description', 'create_at')


class ProblemAdmin(ModelView):
    column_hide_backrefs = False

    column_list = ('user_id', 'title', 'create_at', 'image', 'rating', 'finish')


admin.add_view(
    UserAdminView(User, db.session)
)


admin.add_view(
    ModelView(Role, db.session)
)

admin.add_view(
    ModelView(Message, db.session)
)


admin.add_view(
    ModelView(UserRoom, db.session)
)


admin.add_view(
    RatingAdmin(ProblemRating, db.session)
)

admin.add_view(
    ProblemAdmin(Problem, db.session)
)


admin.add_view(
    ModelView(Idea, db.session)
)
