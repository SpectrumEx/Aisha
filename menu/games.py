import telebot
from telebot import types 
import config
import random
import requests
from menu.start import cat_button
from menu.start import compl_button

bot = telebot.TeleBot(config.token)
main_button = types.InlineKeyboardButton("На главную", callback_data='main')

def inline_compl(call):
    markup = types.InlineKeyboardMarkup()
    markup.add(compl_button, main_button)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(call.message.chat.id, config.random_message(), reply_markup=markup)
def inline_roll(call):
    markup = types.InlineKeyboardMarkup()
    markup.add(main_button)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(call.message.chat.id, "доделать.", reply_markup=markup)
    #chat_id = call.message.chat.id
    #text = call.text[50:]  # Skip the "/roll" part of the message
    #dice, sides = (1, 50)
   # if text:
    #  dice, sides = map(int, text.split('d'))
    #result = [random.randint(1, sides) for _ in range(dice)]
   # bot.send_message(chat_id, "Допустим это: " + "  ".join(map(str, result)))
def inline_cat(call):
    markup = types.InlineKeyboardMarkup()
    markup.add(cat_button, main_button)
    cat_photos = requests.get("https://api.thecatapi.com/v1/images/search?limit=10").json()
    cat_photo = random.choice(cat_photos)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_photo(call.message.chat.id, cat_photo["url"], reply_markup=markup)