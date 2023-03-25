from datetime import datetime, timedelta
import pytz
from flask import flash
from flask_admin import Admin
from flask_admin.actions import action
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from service import db
from celery_app import send_message
from service.model.model import User, Role, Message, UserRoom, Problem

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


class TelegramMessage(ModelView):
    # column_display_pk = True
    column_hide_backrefs = False
    column_list = ('id', 'user_id', 'message', 'create_at', 'completed_ticket', 'status', 'notification_time')
    # form_columns = ('user_id', 'message', 'create_at', 'completed_ticket', 'status', 'notification_time')

    # @action('Запустить рассылку', 'Запустить рассылку', 'Вы уверены, что хотите отправить выбранные сообщения?')
    # def action_send_message(self, ids):
    #     from service.model.model import Message
    #     try:
    #         local_tz = pytz.timezone('Asia/Almaty')
    #         messages = Message.query.filter(Message.id.in_(ids)).all()
    #         for message in messages:
    #             send_at = message.notification_time.astimezone(local_tz)
    #             now = datetime.now(tz=local_tz) + timedelta(hours=6)
    #             if send_at >= now:
    #                 delay = (send_at - now).total_seconds()
    #                 send_message.apply_async(args=[message.messages, message.user_id], countdown=delay)
    #             else:
    #                 send_message.apply_async(args=[message.messages, message.user_id])
    #
    #         flash('Messages scheduled for sending.', 'success')
    #     except Exception as ex:
    #         flash(str(ex), 'error')




admin.add_view(
    ModelView(User, db.session)
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
    ModelView(Problem, db.session)
)