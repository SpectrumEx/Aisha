import telebot
from telebot import types 
import config

bot = telebot.TeleBot(config.token)

main_button = types.InlineKeyboardButton("На главную", callback_data='main')
cat_button = types.InlineKeyboardButton("Котик", callback_data='cat')
info_button = types.InlineKeyboardButton("Информация", callback_data='info')
games_button = types.InlineKeyboardButton("Развлечения", callback_data='games')
adm_button = types.InlineKeyboardButton("ADM", callback_data='adm')
news_button = types.InlineKeyboardButton("Профиль", callback_data='news')                                                 
about_button = types.InlineKeyboardButton("Обо мне", callback_data='about')
support_button = types.InlineKeyboardButton("Поддержать", callback_data='support')
roll_button = types.InlineKeyboardButton("Случайнон число", callback_data='roll')
compl_button = types.InlineKeyboardButton("Комплимент", callback_data='compl')
stop_button = types.InlineKeyboardButton("Стоп", callback_data='stop')
restart_button = types.InlineKeyboardButton("Рестарт", callback_data='restart')

allowed_users = config.administrator

def inline_main(call):
    # Создаем inline клавиатуру с тремя кнопками (или двумя, если пользователь не в списке allowed_users)
    markup = types.InlineKeyboardMarkup()
    if call.from_user.id in allowed_users:
        markup.add(info_button, games_button, adm_button)
    else:
        markup.add(info_button, games_button)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    with open('img/start.jpg', 'rb') as f:
            photo = f.read()
            res = bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption=config.startAnswer)
            message_id = res.message_id
    bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=message_id, reply_markup=markup)

def inline_info(call):
    markup = types.InlineKeyboardMarkup() ###Создаем inline кнопки:                                                                                             
    markup.add(news_button, about_button, support_button, main_button) ###Добавляем кнопки
    bot.delete_message(call.message.chat.id, call.message.message_id)
    with open('img/info.jpg', 'rb') as f:
            photo = f.read()
            res = bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption="Вы можете получить любую интересующую вас информацию. Для связи с разработчиком напишите на почту koroleevskiy@gmail.com")
            message_id = res.message_id
    bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=message_id, reply_markup=markup)
def inline_games(call):
    markup = types.InlineKeyboardMarkup()
    markup.add(cat_button, roll_button, compl_button, main_button)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    with open('img/games.jpg', 'rb') as f:
            photo = f.read()
            res = bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption="Развлечения специально для вас! Выбери, что по вкусу")
            message_id = res.message_id
    bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=message_id, reply_markup=markup)
def inline_adm(call):
    markup = types.InlineKeyboardMarkup()
    markup.add(stop_button, restart_button, main_button)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    with open('img/adm.jpg', 'rb') as f:
            photo = f.read()
            res = bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption="Твоя админпанель")
            message_id = res.message_id
    bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=message_id, reply_markup=markup)