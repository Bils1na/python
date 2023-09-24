import telebot
from config import token, API_URL
import json
import requests
import random


movies = []
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    movies.append("Matrix")
    movies.append("Solaris")
    movies.append("The lord of the Rings")
    movies.append("The Texas Chain Saw Massacre")
    movies.append("Santa Barbara")
    bot.send_message(message.chat.id, "Library has downloaded")

@bot.message_handler(commands=['all'])
def show_all(message):
    try:
        bot.send_message(message.chat.id, "Here is your list of movies")
        bot.send_message(message.chat.id, ", ".join(movies))
    except:
        bot.send_message(message.chat.id, "The list of movies is empty")

@bot.message_handler(commands=['save'])
def save_all(message):
    with open("movies_list.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(movies, ensure_ascii=False))
    bot.send_message(message.chat.id, "The movies were successfully saved")

@bot.message_handler(commands=['wiki'])
def wiki(message):
    quest = message.text.split()[1:]
    qq = " ".join(quest)
    data = {"question_raw": [qq]}
    try:
        res = requests.post(API_URL, json=data, verify=False).json()
        bot.send_message(message.chat.id, res)
    except:
        bot.send_message(message.chat.id, "The bot didn't find anything")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if "дела" in message.text.lower():
        bot.send_message(message.chat.id, "Дела у меня хорошо, сам как?")



bot.polling()