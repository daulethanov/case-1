from flask import Flask
from flask_migrate import Migrate
from flask_security import Security

from service.config.Base import Config
from service.model import db
from service.model.model import user_datastore
from service.admin.admin import admin


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    migrate = Migrate(app, db)
    security = Security(app, user_datastore)
    admin.init_app(app)


    return app