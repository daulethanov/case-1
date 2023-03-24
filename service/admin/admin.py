from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from service import db
from service.model.model import User, Role
admin = Admin()


class MyModelView(ModelView):
    def is_accessible(self):
        if not current_user.is_authenticated:
            return False

        for role in current_user.roles:
            if role.name == 'admin':
                return True
        return False


admin.add_view(
    ModelView(User, db.session)
)

admin.add_view(
    ModelView(Role, db.session)
)