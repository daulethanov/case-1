from flasgger import Swagger
from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_security import Security
from flask_swagger_ui import get_swaggerui_blueprint
from flask_uploads import configure_uploads
from service.config.Base import Config
from service.model import db
from service.model.model import user_datastore, images, ProblemRating, User
from service.admin.admin import admin
from service.sh.serizlizer import UserSchema, api, UserResource, docs, ma, ProblemResource
from service.view.auth import auth
from service.view.problem import problem


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    admin.init_app(app)
    ma.init_app(app)
    swagger = Swagger(app)
    configure_uploads(app, images)

    with app.app_context():

        db.create_all()
    migrate = Migrate(app, db)
    docs.init_app(app)
    security = Security(app, user_datastore)
    app.register_blueprint(auth)
    app.register_blueprint(problem)

    api.add_resource(ProblemResource, '/problem', '/problem/<int:problem_id>')



    return app
