import telebot
import os
import datetime
path = os.getcwd()
bot = telebot.TeleBot('5541132089:AAHqkS-dCUz32vul1mMsJrznob31XccMiX0')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет <b>{message.from_user.username}</b>! \n Спасибо что пользуешься моим ботом :з \n '
    bot.send_message(message.chat.id,mess, parse_mode='html')

@bot.message_handler(commands=['help'])
def help(message):
    mess = f'Вот список моих команд : \n1.Привет \n2.Какао'


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
    if (message.text.upper().lower() == "какао"):
        Cocoa(message)
        TestOTVcomm = True
    if(TestOTVcomm == False):
        Sry(message)
    if (os.path.exists(path + '/message/' + str(message.chat.id)) == False):
        os.mkdir(f"message/{message.chat.id}")
    print(message.text.upper().lower())
    my_file = open(f"message/{message.chat.id}\Text.txt", "a")
    my_file.write(f"[{str(timenow)}]  " + message.from_user.username + ": " + message.text + "\n")
    my_file.close()


def Sry(name):
    mess = f'Прости пожалуйста, но в моей базе данных нет такой команды :( \nпопробуй прописать команду : <b> /help </b>'
    bot.send_message(name.chat.id, mess, parse_mode='html')


def Yes(name):
    mess = f'Вау, невероятно <b>{name.from_user.first_name}</b>, да ты крут!:з'
    bot.send_message(name.chat.id, mess, parse_mode='html')


def Hi(name):
    mess = f'И тебе привет <b>{name.from_user.username}</b>'
    bot.send_message(name.chat.id, mess, parse_mode='html')


def Cocoa(name):
    mess = f'Вот ваше какао, приятного какаопития :^'
    photo = open(path + '/tmp/cocoa.png', 'rb')
    bot.send_photo(name.chat.id, photo, '')

bot.polling(none_stop=True)