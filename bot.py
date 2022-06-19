import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start']) # приветсвтенное сообщение
def welcome(message):
	
	# кнопка
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Чё сожрать?")

	markup.add(item1)

	жри = ['Сожри пицц', 'Сожри роллс', 'Сожри курицу из KFC', 'Сожри чикан', 'Закажи арбыс или дыню', 'Сожри бургерс', 'Сожри шашлык', 'Сожри шаурму', 'Сожри хинкали с хачапури']

	bot.send_message(message.chat.id, "Жеееесть, {0.first_name} опять жрать хочет".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)



@bot.message_handler(content_types=['text']) # сообщение
def lalala(message):
  if message.text == 'Чё сожрать?':
    bot.send_message(message.chat.id, random.choice(жри))
  else:
    bot.send_message(message.chat.id, 'Блять, ты тупой? Тут одна кнопка, на неё и жми жесть')



bot.polling(none_stop=True)	