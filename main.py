import telebot
from telebot import types

import div
import minus
import mult
import sum
import exception
import logging

logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s",
                    level = logging.INFO, filename="bot.log", encoding="utf-8")
bot = telebot.TeleBot("5713334456:AAHrZykC9kpmWY1l1IngK7XVDrE9OSawxbw")

@bot.message_handler(commands=["start"])
def start (message):
    logging.info("start bot")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(f"/ рациональные числа")
    button2 = types.KeyboardButton(f"/ комплексные числа")
    markup.add (button1, button2)
    send_msg = f" привет, {message.from_user.first_name}. это бот калькулятор"
    bot.send_message (message.chat.id, send_msg, reply_markup=markup)

@bot.message_handler(commands=["рациональные числа"])
def ration (message):
    logging.info(f"{message.from_user.first_name}/ {message.from_user.id}/ рациональные числа")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = types.KeyboardButton(f"/ сумма")
    button2 = types.KeyboardButton(f"/ вычитание")
    button3 = types.KeyboardButton(f"/ умножение")
    button4 = types.KeyboardButton(f"/ деление")
    button5 = types.KeyboardButton(f"/ возведение в степень")
    markup.add (button1, button2, button3, button4, button5)
    send_msg = f" ну что, {message.from_user.first_name}. выбирай"
    bot.send_message (message.chat.id, send_msg, reply_markup=markup)

@bot.message_handler(commands=["комплексные числа"])
def ration (message):
    logging.info(f"{message.from_user.first_name}/ {message.from_user.id}/ комплексные числа")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = types.KeyboardButton(f"/ сумма")
    button2 = types.KeyboardButton(f"/ вычитание")
    button3 = types.KeyboardButton(f"/ умножение")
    button4 = types.KeyboardButton(f"/ деление")
    button5 = types.KeyboardButton(f"/ pow")
    button6 = types.KeyboardButton(f"/ возведение в степень")
    markup.add (button1, button2, button3, button4, button5, button6)
    send_msg = f" ну что, {message.from_user.first_name}. выбирай"
    bot.send_message (message.chat.id, send_msg, reply_markup=markup)

@bot.message_handler(commands=["сумма"])
def summa (message):
    logging.info(f"{message.from_user.first_name}/ {message.from_user.id}/ сумма")
    global operation
    operation = message.text.split()
    markup = types.ForceReply(selective=True)
    send_msg = f"{message.from_user.first_name}. введи два числа через пробел"
    bot.send_message (message.chat.id, send_msg, reply_markup=markup)

@bot.message_handler(commands=["вычитание"])
def minu_s (message):
    logging.info(f"{message.from_user.first_name}/ {message.from_user.id}/ вычитание")
    global operation
    operation = message.text.split()
    markup = types.ForceReply(selective=True)
    send_msg = f"{message.from_user.first_name}. введи два числа через пробел"
    bot.send_message (message.chat.id, send_msg, reply_markup=markup)



bot.polling(non_stop=True)