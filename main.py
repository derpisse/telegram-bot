import telebot

bot = telebot.TeleBot(8826087429:AAHRGd-gKEXOtlQIiQgJYOO1i7j537htZXs')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой первый бот, и я успешно работаю на Railway! 🚀")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Ты написал: {message.text}")

if __name__ == "__main__":
    bot.infinity_polling()
