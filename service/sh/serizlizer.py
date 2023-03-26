from flask import request
from flask_apispec import use_kwargs
from flask_apispec.annotations import doc
from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields, ValidationError
from flask_restful import Resource, Api, marshal_with
from service import db
from service.model.model import User, Problem
from flask_apispec import FlaskApiSpec

api = Api()
ma = Marshmallow()
docs = FlaskApiSpec()


class UserSchema(ma.Schema):
    id = fields.Integer()
    first_name = fields.String()
    last_name = fields.String()
    email = fields.String()


class UserResource(Resource):
    @doc(description='Get list of users')
    @marshal_with(UserSchema(many=True))
    def get(self):
        """Get all users"""
        pass

    @doc(description='Create new user')
    @use_kwargs(UserSchema(), location='json')
    @marshal_with(UserSchema())
    def post(self, **kwargs):
        """Create new user"""
        pass


class ProblemSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    create_at = fields.DateTime(dump_only=True)
    finish = fields.DateTime()
    completed = fields.Bool(dump_only=True)
    image = fields.Str()
    act_job = fields.Str(required=True)
    star = fields.Int(required=True)


problem_schema = ProblemSchema()

class ProblemResource(Resource):
    def get(self, problem_id):
        problem = Problem.query.filter_by(id=problem_id).first_or_404()
        return problem_schema.dump(problem), 200

    def post(self):
        problem_data = request.get_json()
        try:
            problem = problem_schema.load(problem_data)
        except ValidationError as err:
            return err.messages, 422
        db.session.add(problem)
        db.session.commit()
        return problem_schema.dump(problem), 201

    def put(self, problem_id):
        problem = Problem.query.filter_by(id=problem_id).first_or_404()
        problem_data = request.get_json()
        try:
            problem = problem_schema.load(problem_data, instance=problem, partial=True)
        except ValidationError as err:
            return err.messages, 422
        db.session.commit()
        return problem_schema.dump(problem), 200

    def delete(self, problem_id):
        problem = Problem.query.filter_by(id=problem_id).first_or_404()
        db.session.delete(problem)
        db.session.commit()
        return '', 204
