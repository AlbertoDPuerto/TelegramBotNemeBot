import telebot

bot = telebot.TeleBot("782708669:AAHSfimc2kTGaSiZN8IW8IvNqrx3dLT0l04")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Conio Ihor")

bot.polling()