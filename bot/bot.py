import telebot

API_TOKEN = 'YOUR_TELEGRAM_BOT_API_TOKEN'
WEB_APP_URL = 'http://your-web-app-url.com'  # Replace with your actual web app URL

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.InlineKeyboardMarkup()
    showapp_button = telebot.types.InlineKeyboardButton('Show App', url=WEB_APP_URL)
    markup.add(showapp_button)
    bot.send_message(message.chat.id, "Welcome! Click the button below to open the web application.", reply_markup=markup)

if __name__ == '__main__':
    bot.polling()

