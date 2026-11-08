import telebot

# ضع توكن البوت الخاص بك هنا بين العلامتين
TOKEN = 'YOUR_BOT_TOKEN'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك! البوت يعمل الآن بنجاح على منصة Render.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# أمر تشغيل البوت باستمرار
bot.infinity_polling()
