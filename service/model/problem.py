from datetime import datetime
from flask_uploads import UploadSet, IMAGES
from . import db
from .enum import ActJob

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

users_company = db.Table(
    'users_company',
    db.Column('id', db.Integer, primary_key=True, autoincrement=True),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('company_id', db.Integer, db.ForeignKey('company.id'))
)


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
    title = db.Column(db.Text())
    description = db.Column(db.Text())
    create_at = db.Column(db.DateTime(), default=datetime.now())
    finish = db.Column(db.DateTime())
    completed = db.Column(db.Boolean(), default=0)
    image = db.Column(db.String(255))
    act_job = db.Column(db.Enum(ActJob))
    star = db.Column(db.Integer, nullable=False, default=1)
    rating = db.relationship('ProblemRating', backref=db.backref('users'))


    def get_average_rating(self):
        ratings = [r.rating for r in self.ratings]
        if not ratings:
            return 0
        return sum(ratings) / len(ratings)

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


class ProblemRating(db.Model):
    __tablename__ = 'problem_rating'

    id = db.Column(db.Integer(), primary_key=True)
    problem_id = db.Column(db.Integer(), db.ForeignKey('problem.id'))
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    rating = db.Column(db.Integer(), nullable=False)

    __table_args__ = (
        db.UniqueConstraint('problem_id', 'user_id', name='_problem_user_uc'),
    )


class Company(db.Model):
    __tablename__ = 'company'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    users = db.relationship('User', secondary='users_company', backref=db.backref('users', lazy='dynamic'))
    star = db.Column(db.Integer)

    def __repr__(self):
        return self.name

