import telebot
import config

API_TOKEN = config.token

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Привет, я Эхобот.
Я здесь, чтобы ответить вам добрыми словами. Просто скажите что-нибудь приятное, и я отвечу вам тем же!\
""")

@bot.message_handler(commands=['info'])
def send_info(message):
    bot.reply_to(message, """\
Обо мне пока что нет информации, но вскоре они будут :)\
""")
    

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    if message.text == "Привет":
        bot.send_message(message.chat.id, 'Приветик!:D')
    else:
        bot.reply_to(message, message.text)


bot.infinity_polling()