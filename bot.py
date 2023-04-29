#!venv/bin/python
#Aisha v.0.2

import telebot
import requests
import logging
from telebot import types 
import random
import menu
import config

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

bot = telebot.TeleBot(config.token)
allowed_users = config.administrator
logging.info('Start bot')

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Создаем inline клавиатуру с тремя кнопками (или двумя, если пользователь не в списке allowed_users)
    markup = types.InlineKeyboardMarkup()
    info_button = types.InlineKeyboardButton("Информация", callback_data='info')
    games_button = types.InlineKeyboardButton("Развлечения", callback_data='games')
    if message.from_user.id in allowed_users:
        adm_button = types.InlineKeyboardButton("ADM", callback_data='adm')
        markup.add(info_button, games_button, adm_button)
    else:
        markup.add(info_button, games_button)
    with open('img/start.jpg', 'rb') as f:
        photo = f.read()
        res = bot.send_photo(chat_id=message.chat.id, photo=photo, caption=config.startAnswer, reply_markup=markup)
        message_id = res.message_id      
        
@bot.message_handler(commands=['say'])
def handle_say(message):
    if message.from_user.id in allowed_users:
        chat_id = message.chat.id
        text = message.text[5:]
        bot.send_message(chat_id, text)
    else: 
        bot.send_message(message.chat.id, "Вы не являетесь администратором")
    
# Обработчик inline кнопок в стартовом меню
@bot.callback_query_handler(func=lambda call: True)
def callback_main(call):
    if call.data == 'info': ###Кнопка "Информация"
        menu.start.inline_info(call)
    elif call.data == 'games':
        menu.start.inline_games(call)
    elif call.data == 'adm' and call.message.chat.id in allowed_users:
        menu.start.inline_adm(call)
### Обработчик inline кнопок в меню информации 
    elif call.data == 'news':
        menu.info.inline_news(call)
    elif call.data == 'about':
        menu.info.inline_about(call)
    elif call.data == 'support':
        menu.info.inline_support(call)
### Обработчик inline кнопок в меню развлечений
    elif call.data == 'compl':
        menu.games.inline_compl(call)
    elif call.data == 'roll':
        menu.games.inline_roll(call)
    elif call.data == 'cat':
        menu.games.inline_cat(call)
### Обработчик inline кнопок в меню администрации
    elif call.data == 'stop':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, "Остановка...")
        bot.stop_polling()
    elif call.data == 'restart':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, "Рестарт...")
        bot.stop_polling()
        bot.polling()
    elif call.data == 'main':
        menu.start.inline_main(call)
#Запускаем бота
if __name__ == '__main__':
     bot.polling(none_stop=True)