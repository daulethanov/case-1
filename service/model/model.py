from datetime import datetime
from flask_security import RoleMixin, UserMixin, SQLAlchemySessionUserDatastore
from flask_uploads import UploadSet, IMAGES
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .enum import Street, Dom, ActJob


images = UploadSet('images', IMAGES)

roles_users = db.Table(
    'roles_users',
    db.Column('id', db.Integer, primary_key=True, autoincrement=True),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
)


users_rooms = db.Table(
    'users_rooms',
    db.Column('id', db.Integer, primary_key=True, autoincrement=True),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('room_id', db.Integer, db.ForeignKey('user_room.id'))
)

users_messages = db.Table(
    'users_messages',
    db.Column('id', db.Integer, primary_key=True, autoincrement=True),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('message_id', db.Integer, db.ForeignKey('message.id'))
)


users_company = db.Table(
    'users_company',
    db.Column('id', db.Integer, primary_key=True, autoincrement=True),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('company_id', db.Integer, db.ForeignKey('company.id'))
)


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
    messages = db.relationship('Message', secondary='users_messages', backref=db.backref('users', lazy='dynamic'))
    user_room = db.relationship('UserRoom', secondary='users_rooms', backref=db.backref('users', lazy='dynamic'))
    roles = db.relationship('Role', secondary='roles_users', backref=db.backref('users', lazy='dynamic'))
    problem = db.relationship('Problem', backref=db.backref('users'))
    price = db.Column(db.Integer)
    star = db.Column(db.Integer)

    def __repr__(self):
        return self.first_name

    def password_hash(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def create_users(self, user):
        db.session.add(user)
        db.session.commit()


user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)


class Message(db.Model):
    __tablename__ = 'message'

    id = db.Column(db.Integer(), primary_key=True)
    message = db.Column(db.Text())
    create_at = db.Column(db.DateTime(), default=datetime.now())
    finish = db.Column(db.DateTime())
    status = db.Column(db.Boolean(), default=0)
    notification_time = db.Column(db.DateTime())

    def __repr__(self):
        return self.user_id


class UserRoom(db.Model):
    __tablename__ = 'user_room'

    id = db.Column(db.Integer(), primary_key=True)
    message = db.Column(db.Text())
    description = db.Column(db.Text())
    notification_time = db.Column(db.DateTime())

    def __repr__(self):
        return self.message


class Problem(db.Model):
    __tablename__ = 'problem'

    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    message = db.Column(db.Text())
    create_at = db.Column(db.DateTime(), default=datetime.now())
    finish = db.Column(db.DateTime())
    completed = db.Column(db.Boolean(), default=0)
    image = db.Column(db.String(255))
    act_job = db.Column(db.Enum(ActJob))
    star = db.Column(db.Integer, nullable=False, default=1)

    def save_image(self, image):
        """
        Save the uploaded image and update the database record.
        """
        filename = images.save(image, folder='uploads/images')
        self.image = filename
        db.session.add(self)
        db.session.commit()

    def delete_image(self):
        """
        Delete the image file and update the database record.
        """
        if self.image:
            images.delete(self.image, folder='uploads/images')
            self.image = None
            db.session.add(self)
            db.session.commit()


class Company(db.Model):
    __tablename__ = 'company'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    users = db.relationship('User', secondary='users_company', backref=db.backref('users', lazy='dynamic'))
    star = db.Column(db.Integer)

    def __repr__(self):
        return self.name
