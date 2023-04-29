import telebot
from telebot import types 
import config
import menu.start
import requests

bot = telebot.TeleBot(config.token)
main_button = types.InlineKeyboardButton("На главную", callback_data='main')
allowed_users = config.administrator

def inline_news(call):
    user_id = call.message.chat.id
    user_name = call.message.chat.first_name
    user_ip = requests.get('https://api.ipify.org').text
    response = requests.get(f'http://api.ipstack.com/{user_ip}?access_key=cf16db6e0049421b9019f6366802afdf')
    data = response.json()
    region_name = data['region_name']
    if user_id in allowed_users:
        user_group = 'Администратор'
    else: 
        user_group = 'Пользователь'
    markup = types.InlineKeyboardMarkup()
    markup.add(main_button)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(call.message.chat.id, f'Вот информация о вас:\nВаш ID - {user_id}\nВаше имя - {user_name}\nВаша группа - {user_group}\nВаш IP - {user_ip}\nВаш регион - {region_name}', reply_markup=markup)
def inline_about(call):
    markup = types.InlineKeyboardMarkup()
    markup.add(main_button)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(call.message.chat.id, "Здесь будет информация обо мне", reply_markup=markup)
def inline_support(call):
    markup = types.InlineKeyboardMarkup()
    markup.add(main_button)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(call.message.chat.id, "Здесь будет информация о том, как поддержать разработчика", reply_markup=markup)