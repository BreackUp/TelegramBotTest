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
def main(message):
    TestOTVcomm = False
    timenow = datetime.datetime.now()
    if (message.text.upper().lower() == "да"):
        Yes(message)
        TestOTVcomm = True
    if (message.text.upper().lower() == "привет"):
        Hi(message)
        TestOTVcomm = True
    if(TestOTVcomm == False):
        bot.send_message(message.chat.id, "Прости, но я тебя не понимаю", parse_mode='html')
    if (os.path.exists(path + '/' + str(message.chat.id)) == False):
        os.mkdir(f"{message.chat.id}")
    print(message.text.upper().lower())
    my_file = open(f"{message.chat.id}\Text.txt", "a")
    my_file.write(f"[{str(timenow)}]  " + message.from_user.username + ": " + message.text + "\n")
    my_file.close()


def Yes(name):
    mess = f'Вау, невероятно <b>{name.from_user.first_name}</b>, да ты крут!:з'
    bot.send_message(name.chat.id, mess, parse_mode='html')


def Hi(name):
    mess = f'И тебе привет <b>{name.from_user.username}</b>'
    bot.send_message(name.chat.id, mess, parse_mode='html')

bot.polling(none_stop=True)