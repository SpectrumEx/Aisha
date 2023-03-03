#!venv/bin/python
#Aisha v.0.1

import telebot
import config
import logging
import command.admin_cmd
import command.user_cmd
import requests
import speech_recognition as sr 

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

bot = telebot.TeleBot(config.token)
admin = config.administrator
logging.info('Start bot')

######### Admin CMD #########
@bot.message_handler(commands=['restart'])
def handle_restart(message):
    if message.from_user.id in admin:
        bot.send_message(message.chat.id, "Рестарт...")
        bot.stop_polling()
        bot.polling()
    else: 
        bot.send_message(message.chat.id, "Вы не являетесь администратором")  
     
@bot.message_handler(commands=['stop'])
def handle_stop(message):
    if message.from_user.id in admin:
        bot.send_message(message.chat.id, "Остановка...")
        bot.stop_polling()
    else: 
        bot.send_message(message.chat.id, "Вы не являетесь администратором")

@bot.message_handler(commands=['say'])
def handle_say(message):
    command.admin_cmd.say(message)
############################
    
######### User CMD #########
@bot.message_handler(commands=['start'])
def handle_start(message):
     command.user_cmd.start(message)
    
@bot.message_handler(commands=['usr'])
def handle_usr(message):
    command.user_cmd.usr(message)

@bot.message_handler(commands=['roll'])
def handle_roll(message):
    command.user_cmd.roll(message)
  
@bot.message_handler(commands=['rimage'])
def handle_random_image(message):
    command.user_cmd.random_image(message)

@bot.message_handler(commands=['voice']) #Google voice
def handle_voice(message):
    command.user_cmd.voice(message)
    

######### User Markup #########
@bot.message_handler(content_types=['text'])
def handle_send_text(message):
    command.user_cmd.send_text(message)
############################

if __name__ == '__main__':
     bot.polling(none_stop=True)