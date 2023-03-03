import telebot
import config

bot = telebot.TeleBot(config.token)
admin = config.administrator
        
def say(message):
    if message.from_user.id in admin:
        chat_id = message.chat.id
        text = message.text[5:]
        bot.send_message(chat_id, text)
    else: 
        bot.send_message(message.chat.id, "Вы не являетесь администратором")