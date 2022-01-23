
import telebot
from dopoln import TOKEN, exchanger
from extensions import Convertor, APIException
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start','help'])
def help(message: telebot.types.Message):
    text = 'для начала работы введите команду:\n<имя валюты> \
<в какую валюту> \
<количество валюты>(Чтобы узнать валюты используйте команду: values)'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def help(message: telebot.types.Message):
    text = 'Валюты:\n'
    text +="\n".join(exchanger.keys())
    bot.reply_to(message, text)
@bot.message_handler(content_types=['text'])
def upd(message: telebot.types.Message):
    values = message.text.split()
    values = list(map(str.lower,values))
    try:
        len(values)!= 3
    except APIException as e:
        bot.reply_to(message, 'Неверное количество параметров')
    try:
        result = Convertor.get_price(values)
    except APIException as e:
        bot.reply_to(message,f'Ошибка пользователя \n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду \n{e}')
    else:
        text= f'цена {values[0]} в {values[1]} {values[2]} --> {result} {exchanger[values[1]]}'
        bot.reply_to(message, text)




bot.polling(none_stop=True,interval=0)

