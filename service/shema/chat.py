from marshmallow import Schema, fields as f
from service.shema.user import UserSchema


class MessageSchema(Schema):
    id = f.Integer(dump_only=True)
    body = f.String(required=True)
    timestamp = f.DateTime(dump_only=True)
    user = f.Nested(UserSchema, only=['id', 'first_name', 'last_name', 'email', 'number'])
