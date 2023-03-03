import telebot
import config
import brains
import random 
import requests
from gtts import gTTS

bot = telebot.TeleBot(config.token)
admin = config.administrator
API_KEY = config.unsplash

def start(message):
     keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
     keyboard.row('Комплимент', 'Выход', 'Обо мне', 'Котик')
     bot.send_message(message.chat.id, brains.startAnswer, reply_markup=keyboard)
    
def usr(message):
    if message.from_user.id in admin:
        bot.send_message(message.chat.id, "Вы администратор")
    else:
        bot.send_message(message.chat.id, "Вы не являетесь администратором")

def roll(message):
  chat_id = message.chat.id
  text = message.text[50:]  # Skip the "/roll" part of the message
  dice, sides = (1, 50)
  if text:
    dice, sides = map(int, text.split('d'))
  result = [random.randint(1, sides) for _ in range(dice)]
  bot.send_message(chat_id, "Допустим это: " + "  ".join(map(str, result)))
  
def random_image(message):
  unsplash_url = "https://api.unsplash.com/photos/random"
  headers = {
    "Authorization": f"Client-ID {API_KEY}"
  }
  response = requests.get(unsplash_url, headers=headers)
  if response.status_code == 200:
    image_url = response.json()['urls']['full']
    bot.send_photo(message.chat.id, image_url)
  else:
    bot.send_message(message.chat.id, "Sorry, there was an error getting a random image.")

def voice(message):
    text = message.text[6:]
    tts = gTTS(text, lang="ru")
    tts.save('voice.ogg')
    bot.send_voice(message.chat.id, open('voice.ogg', 'rb'))
    
def send_text(message):
    if message.text.lower() == 'комплимент':
        bot.send_message(message.chat.id, brains.random_message())
    elif message.text.lower() == 'выход':
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Пока', reply_markup=a)
    elif message.text.lower() == 'обо мне':
        bot.send_message(message.chat.id, brains.aboutme)
    elif message.text.lower() == 'котик':
        cat_photos = requests.get("https://api.thecatapi.com/v1/images/search?limit=10").json()
        cat_photo = random.choice(cat_photos)
        bot.send_photo(message.chat.id, cat_photo["url"])