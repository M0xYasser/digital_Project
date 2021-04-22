import telebot
from telebot import types

bot = telebot.TeleBot("1755271135:AAHb9TywoZ0v9YXIYpDaFAQ3kbRm8LZIPz0", parse_mode=None) 



keyboardmain = types.InlineKeyboardMarkup(row_width=1)
first_button = types.InlineKeyboardButton(text="Video 📹", url="https://telegra.ph/test-04-22-166")
second_button = types.InlineKeyboardButton(text="PDF 📄", url="https://telegra.ph/test-04-22-166")
t_button = types.InlineKeyboardButton(text="Task 🎯", url="https://telegra.ph/test-04-22-166")
s_button = types.InlineKeyboardButton(text="Task Form ✔️", url="https://telegra.ph/test-04-22-166")
keyboardmain.add(first_button, second_button,t_button,s_button)


@bot.inline_handler(lambda query : query.query=='course3')
def test (inline_query):
    r=types.InlineQueryResultArticle(
        id='1',
        title='Session 1️⃣', 
        input_message_content=types.InputTextMessageContent('Session 1️⃣'),
        reply_markup=keyboardmain,
        thumb_url="https://miro.medium.com/max/2000/1*ilC2Aqp5sZd1wi0CopD1Hw.png"
    )
    bot.answer_inline_query(inline_query.id,[r])
    

bot.polling(none_stop=True)
