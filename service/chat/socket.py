from flask_socketio import SocketIO, emit
from flask import Blueprint, request, json

from service.chat import redis
from service.model.chat import Message
from service.shema.chat import MessageSchema

socketio = SocketIO()
chat = Blueprint('chats', __name__, url_prefix='/chat')


@socketio.on('start_chat')
def handle_start_chat(data):
    user_id = data.get('user_id')
    emit('chat_started', {'user_id': user_id})


@chat.route('/start_chat', methods=['POST'])
def start_chat():
    user_id = request.json.get('user_id')
    return '', 204


@chat.route('/new_messages', methods=['GET', 'POST'])
@socketio.on('new_message')
def handle_new_message(data):
    user_id = data.get('user_id')
    message_text = data.get('body')
    message = Message(user_id=user_id, text=message_text)
    redis.rpush(f'messages:{user_id}', json.dumps(MessageSchema.dump(message)))
    emit('new_message', MessageSchema.dump(message), broadcast=True)


@chat.route('/get_user_messages', methods=['GET', 'POST'])
@socketio.on('get_user_messages')
def handle_get_user_messages():
    user_id = request.json.get('user_id')
    messages = Message.query.filter_by(user_id=user_id).all()
    emit('user_messages', Message.dump(messages))
