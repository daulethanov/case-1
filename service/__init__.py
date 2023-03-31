from flask import Flask
from flask_migrate import Migrate
from flask_security import Security
from flask_uploads import configure_uploads

from service.chat import redis
from service.chat.socket import socketio
from service.config.Base import Config
from service.model import db
from service.model.problem import images, ProblemRating
from service.model.user import User, user_datastore
from service.admin.admin import admin
from service.view.problem import docs
from service.view.auth import auth
from service.view.problem import problem, list_problem
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    admin.init_app(app)
    configure_uploads(app, images)
    redis.init_app(app)
    CORS(app, resources={r"/*": {"origins": "*"}})
    with app.app_context():
        db.create_all()
    migrate = Migrate(app, db)
    security = Security(app, user_datastore)
    socketio.init_app(app, cors_allowed_origins="*")
    app.register_blueprint(auth)
    app.register_blueprint(problem)
    docs.init_app(app)

    return app
