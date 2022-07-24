from telebot import *
import os
import datetime
path = os.getcwd()
bot = telebot.TeleBot('5541132089:AAHqkS-dCUz32vul1mMsJrznob31XccMiX0')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Добрый день, вы попали на мое портфолио, вы можете обратится по следующим кнопкам или же цифрам для ознакомления : \n \n 1. Мой GitHub \n 2. Мое образование \n 3. Способы свзяи со мной'
    photo = open(path + '/tmp/Ava.jpg', 'rb')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    GitHub = types.KeyboardButton('GitHub')
    Education = types.KeyboardButton('Образование')
    Feedback = types.KeyboardButton('Связь со мной')
    markup.add(GitHub,Education, Feedback)
    bot.send_photo(message.chat.id, photo, mess, reply_markup=markup)

@bot.message_handler(commands=['help'])
def help(message):
    mess = f'Вот список моих команд : \n1.Привет \n2.Какао'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler()
def main(message):
    TestOTVcomm = False
    timenow = datetime.datetime.now()
    if (message.text.upper().lower() == "привет"): #Приветствие
        Hi(message)
        TestOTVcomm = True
    if (message.text.upper().lower() == "1" or message.text.upper().lower() == "github"): #GitGub
        GitHub(message)
        TestOTVcomm = True
    if (message.text.upper().lower() == "2" or message.text.upper().lower() == "образование"): #Образование
        Education(message)
        TestOTVcomm = True
    if (message.text.upper().lower() == "3" or message.text.upper().lower() == "связь со мной"): #Образование
        Feedback(message)
        TestOTVcomm = True
    if (message.text.upper().lower() == "какао"): #Секретная команда, при использовании выдает соо. с какао
        Cocoa(message)
        TestOTVcomm = True
    if(TestOTVcomm == False): #Если команда не нашлась, то выдает что извините , но я вас не понимаю
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


def GitHub(name):
    mess = f'Вот мои работы в GitHub: \n Мое портфолио(Вы сейчас тут) : https://github.com/BreackUp/TelegramBotTest'
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


def Education(name):
    mess = f'Окончил 11 классов, \n Бла-бла-бла'
    bot.send_message(name.chat.id, mess, parse_mode='html')


def Feedback(name):
    mess = f'Вот все способы связи со мной : \n 1. VK: https://vk.com/breackup \n 2. Telegram: @BreackUp \n 3. Mail: BreackUp@mail.ru'
    bot.send_message(name.chat.id, mess, parse_mode='html')


bot.polling(none_stop=True)