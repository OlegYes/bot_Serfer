import telebot
from telebot import types 
import requests
import bs4
from bs4 import BeautifulSoup as BS
from urllib.parse import urlparse

def uri_validator(x):
    try:
        result = urlparse(x)
        return all([result.scheme, result.netloc, result.path])
    except:
        return False

def split(s):
    return [char for char in s]
bot = telebot.TeleBot('5390758994:AAGVi9FOFsv2fXoXD23jvJ_tNbeIUy94gqg')
stats = 3

def start_ref(q):
    URL = "https://www.google.com/search?q="
    headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0"
    }
    URLI = URL + q.text
    req = requests.get(URLI, headers=headers)
    src = req.text
    with open('index.html', 'w') as f:
        f.write(src)
    soup = BS(src, "lxml")
    menu = soup.find("div", id="search").find_all("a")
    for i in menu:
        print(i)

        lincs = i.get("href")
        if lincs == None:
            print(505)
        else:
            bot.send_message(q.chat.id, lincs)
            lincs200 = uri_validator(lincs)
            if lincs200 == True:
                bot.send_message(q.chat.id, lincs)
            else:
                print(404)
        print(lincs)
    return 0


def start_img(q):
    URL = "https://www.google.com/images?q="
    headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0"
    }
    URLI = URL + q.text
    req = requests.get(URLI, headers=headers)
    src = req.text
    with open('index.html', 'w') as f:
        f.write(src)
    soup = BS(src, "lxml")
    menu = soup.find_all("img")
    for i in menu:
        print(i)

        lincs = i.get("data-src")
        if lincs == None:
            lincs1 = i.get("src")
            if lincs == None:

                print(505)
            else:
                bot.send_message(q.chat.id, lincs1)
        else:

            bot.send_message(q.chat.id, lincs)
            print(lincs)

    return 0

# keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
# keyboard1.row('Искать картинки', 'Обычный поиск')

@bot.message_handler(commands=["stop"])
def start (message):
    global stats
    stats = 3

@bot.message_handler(commands=["start"])
def start (message):
    markup = types.InlineKeyboardMarkup()
    buttonA = types.InlineKeyboardButton(' картинки', callback_data='image')
    buttonB = types.InlineKeyboardButton(' поиск', callback_data='search')

    markup.row(buttonA, buttonB)

    bot.send_message(message.from_user.id, "Hi, I'm a bot that surf the internet via telegram =).", reply_markup=markup)
    
@bot.callback_query_handler(func=lambda call:True)
def inline(call):
  if call.data == 'image':
    bot.send_message(call.message.chat.id, 'What are we looking for?')
    global stats
    stats = 1
            
  if call.data == 'search':
    bot.send_message(call.message.chat.id, 'What to find an article about?')
    stats = 0

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    if stats == 1:

        start_img(message)
        print(100)
        bot.send_message(message.chat.id, message.text)
    if stats == 0:

        start_ref(message)
        print(100)
        bot.send_message(message.chat.id, message.text)
    if stats == 3:
        bot.send_message(message.chat.id, "Напишите /start и выберите что будете искать.")

bot.polling(none_stop = True)
# if __name__ == '__main__':
#     start()