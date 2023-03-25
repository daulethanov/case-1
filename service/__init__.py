from flask import Flask
from flask_migrate import Migrate
from flask_security import Security
from flask_uploads import configure_uploads
from service.config.Base import Config
from service.model import db
from service.model.model import user_datastore, images
from service.admin.admin import admin
from flask_jwt_extended import JWTManager

from service.view.auth import auth
from service.view.problem import problem


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    admin.init_app(app)
    configure_uploads(app, images)
    with app.app_context():

        db.create_all()
    migrate = Migrate(app, db)
    security = Security(app, user_datastore)
    app.register_blueprint(auth)
    app.register_blueprint(problem)

    return app
