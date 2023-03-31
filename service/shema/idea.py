from marshmallow import Schema, fields as f
from service.model.idea import Idea


class ProblemSchema(Schema):
    id = f.Integer(dump_only=True)
    user_id = f.Integer(dump_only=True)
    title = f.String()
    description = f.String()
    create_at = f.DateTime()
