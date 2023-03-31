from flask import Blueprint, jsonify, request, flash
from flask_apispec import use_kwargs, marshal_with
from flask_jwt_extended import jwt_required, get_jwt_identity
from service import User, docs
from service.shema.user import UserSchema, AuthSchema
from service.mail import send_password_reset_email
auth = Blueprint('auth', __name__, url_prefix='/api/auth')


@auth.route('/register', methods=['POST'])
@use_kwargs(UserSchema(only=['first_name', 'last_name', 'email', 'password']))
@marshal_with(AuthSchema)
def register(**kwargs):
    user = User(**kwargs)
    user.password_hash(kwargs['password'])
    user.create_users(user)
    return user, 201


@auth.route('/login', methods=['POST'])
@use_kwargs(UserSchema(only=['email', 'password']))
@marshal_with(UserSchema)
def login(**kwargs):
    user = User.authenticate(**kwargs)
    token = user.get_auth_token()
    return {'access_token': token}


@auth.route('/account', methods=['GET'])
@use_kwargs(UserSchema(only=('token', 'street', 'dom', 'first_name', 'last_name', 'email', 'number', 'roles')))
@jwt_required()
def me_account():
    user_id = get_jwt_identity()
    user = User.query.filter_by(id=user_id).first()
    return user


@auth.route('/reset_password', methods=["POST"])
@use_kwargs(UserSchema(only=('email', )))
def reset_password(email):
    user = User.query.filter_by(email=email).first()
    if user:
        send_password_reset_email(user)
    else:
        return jsonify({
            'message': 'Не найдено почты'
        })
    return jsonify({
        'message': 'Проверь почту'
    })


docs.register(register, blueprint='auth')
docs.register(login, blueprint='auth')
docs.register(me_account, blueprint='auth')
