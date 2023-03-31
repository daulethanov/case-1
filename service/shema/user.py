from marshmallow import Schema, fields as f


class UserSchema(Schema):
    id = f.Integer(dump_only=True)
    first_name = f.String()
    last_name = f.String()
    email = f.String(required=True)
    password = f.String()
    token = f.Integer()
    dom = f.Integer()
    number = f.Integer()
    roles = f.String()
    street = f.String()

class AuthSchema(Schema):
    access_token = f.String(dump_only=True)
    message = f.String(dump_only=True)


