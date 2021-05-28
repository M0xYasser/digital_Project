
import telebot
from telebot import types
import math
API_TOKEN="1844883186:AAHS-wqGST-ryVd-FkVmWMzb6P0q9Xwa67w"
bot = telebot.TeleBot(API_TOKEN, parse_mode=None) 


@bot.message_handler(commands=['start','upgrade'],content_types=["text","audio","voice","image","sticker"])
def start(message):
    enstart="The bot is in maintenance to add a new solution method (J-K FLIP FLOP), and it will work again at 8 pm"
    bot.send_message(message.chat.id,enstart,parse_mode="MarkdownV2",reply_markup=keyboard)
    bot.send_message(1109158839,"TRY : "+str(message.from_user.first_name)+" "+str(message.from_user.last_name))
bot.polling(none_stop=True)
