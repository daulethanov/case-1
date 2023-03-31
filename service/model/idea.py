from datetime import datetime
from service import db


class Idea(db.Model):
    __tablename__ = 'idea'

    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    title = db.Column(db.String())
    description = db.Column(db.Text())
    create_at = db.Column(db.DateTime(), default=datetime.now())
