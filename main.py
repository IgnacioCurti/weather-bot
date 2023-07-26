import os
import telebot
from dotenv import load_dotenv
from get_data import get_current_weather


load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands = ['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hi! I'm the ⛅weather bot🌧. \nType /clima to get current weather")


@bot.message_handler(commands = ['clima'])
def current_weather(message):
    text = "What's your city?"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode = "Markdown")
    bot.register_next_step_handler(sent_msg, city_handler)


def city_handler(message):
    city = message.text
    text =  get_current_weather(city) + "\n\nClick /clima for another city."
    bot.send_message(message.chat.id, text, parse_mode = "Markdown")


if __name__ == "__main__":
    print("Bot is running")
    bot.infinity_polling()
    print("Turning the bot off")
