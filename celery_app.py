from celery import Celery

from bot import bot

celery = Celery(__name__, broker='redis://redis:6379/0', backend='redis://redis:6379/0', )
celery.conf['CELERY_TIMEZONE'] = 'Asia/Almaty'


@celery.task()
@bot.message_handler(content_types=['text'])
def send_message(messages, user_id):
    from telebot import types

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Начать')
    markup.add(btn1)
    bot.send_message(user_id, messages, reply_markup=markup)