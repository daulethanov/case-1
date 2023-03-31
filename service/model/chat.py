from datetime import datetime

from service.model import db

messages_users = db.Table(
    'messages_users',
    db.Column('id', db.Integer, primary_key=True, autoincrement=True),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('message_id', db.Integer, db.ForeignKey('message.id'))
)


class Message(db.Model):
    __tablename__ = 'message'

    id = db.Column(db.Integer(), primary_key=True)
    message = db.Column(db.Text())
    create_at = db.Column(db.DateTime(), default=datetime.now())
    finish = db.Column(db.DateTime())
    status = db.Column(db.Boolean(), default=0)
    notification_time = db.Column(db.DateTime())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    users = db.relationship('User', secondary=messages_users,
                            backref=db.backref('messages', lazy='dynamic'))

    def __repr__(self):
        return self.user_id

    def create_messages(self, message):
        db.session.add(message)
        db.session.commit()
