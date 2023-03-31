from flask import Blueprint, jsonify
from flask_apispec import use_kwargs, marshal_with
from flask_jwt_extended import jwt_required, get_jwt_identity
from service import db
from service.model.problem import Problem
from service.shema.problem import ProblemSchema
from flask_apispec.extension import FlaskApiSpec

docs = FlaskApiSpec()
problem = Blueprint('problems', __name__, url_prefix='/api/problems')


@problem.route('/list', methods=['GET'])
@marshal_with(ProblemSchema(many=True))
def list_problem():
    problems = Problem.query.all()
    return problems


@problem.route('/list/<int:id>', methods=['GET'])
@use_kwargs(ProblemSchema)
@marshal_with(ProblemSchema)
def detail_problem(id, **kwargs):
    try:
        user_id = get_jwt_identity()
        problems = Problem.get(id, user_id)

    except Exception as e:
        return jsonify({
            'message': 'error'
        })


@problem.route('/create', methods=['POST'])
@marshal_with(ProblemSchema)
@use_kwargs(ProblemSchema)
def create_problem(**kwargs):
    db.session.add()
    db.session.commit()


docs.register(list_problem, blueprint='problems')
docs.register(create_problem, blueprint='problems')