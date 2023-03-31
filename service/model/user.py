from datetime import datetime, timedelta
from flask_jwt_extended import create_access_token
from flask_security import SQLAlchemySessionUserDatastore, RoleMixin, UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from service import db
from service.model.enum import Dom, Street


class Role(db.Model, RoleMixin):
    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(200))

    def __repr__(self):
        return self.name


class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    token = db.Column(db.BigInteger(), unique=True)
    active = db.Column(db.Boolean(), default=1)
    created_at = db.Column(db.DateTime, default=datetime.now())
    street = db.Column(db.Enum(Street))
    dom = db.Column(db.Enum(Dom))
    number = db.Column(db.Integer(), default=8)
    # messages = db.relationship('Message', secondary='users_messages', backref=db.backref('users', lazy='dynamic'))
    user_room = db.relationship('UserRoom', secondary='users_rooms', backref=db.backref('users', lazy='dynamic'))
    roles = db.relationship('Role', secondary='roles_users', backref=db.backref('users', lazy='dynamic'))
    problem = db.relationship('Problem', backref=db.backref('users'))
    idea = db.relationship('Idea', backref=db.backref('users'))
    price = db.Column(db.Integer)
    star = db.Column(db.Integer)

    def __repr__(self):
        return self.first_name

    def password_hash(self, password):
        self.password = generate_password_hash(password)

    def create_users(self, user):
        db.session.add(user)
        db.session.commit()

    def create_token(self, expire_time=24):
        expire_delta = timedelta(expire_time)
        token = create_access_token(
            identity=self.id, expires_delta=expire_delta
        )
        return token

    @classmethod
    def authenticate(cls, email, password):
        user = cls.query.filter(cls.email == email).one()
        if not check_password_hash(password, user.password):
            return user
        else:
            raise Exception('Invalid email or password')


user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)
