from marshmallow import Schema, fields as f


class ProblemSchema(Schema):

    id = f.Int(dump_only=True)
    user_id = f.Int(required=True)
    title = f.Str(required=True)
    description = f.Str(required=True)
    create_at = f.DateTime(dump_only=True)
    finish = f.DateTime()
    completed = f.Bool(dump_only=True)
    image = f.Str()
    act_job = f.Str(required=True)
    star = f.Int(required=True)




