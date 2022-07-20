import telebot
import os
import datetime
path = os.getcwd()
bot = telebot.TeleBot('5541132089:AAHqkS-dCUz32vul1mMsJrznob31XccMiX0')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет <b>{message.from_user.username}</b>! \n Спасибо что пользуешься моим ботом :з \n '
    bot.send_message(message.chat.id,mess, parse_mode='html')


@bot.message_handler()
def TEXTOTV(message):
    timenow = datetime.datetime.now()
    if (message.text == "Да"):
        mess = f'Вау, невероятно <b>{message.from_user.first_name}</b>, да ты крут!:з'
        bot.send_message(message.chat.id, mess, parse_mode='html')
    else:
        bot.send_message(message.chat.id, "Прости, но я тебя не понимаю", parse_mode='html')
    if(os.path.exists(path + '/' + str(message.chat.id) ) == False):
        os.mkdir(f"{message.chat.id}")
    my_file = open(f"{message.chat.id}\Text.txt", "a")
    my_file.write(f"[{str(timenow)}]  " + message.from_user.username +": "+ message.text+"\n")
    my_file.close( )


bot.polling(none_stop=True)