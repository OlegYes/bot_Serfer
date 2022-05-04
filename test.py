import telebot
from telebot import types
import requests
import bs4
from bs4 import BeautifulSoup as BS
import re
def start_ref(q):
    URL = "https://www.google.com/search?q="
    headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0"
    }
    URLI = URL + q
    req = requests.get(URLI, headers=headers)
    print(req.status_code)
    if req.status_code ==200:
        print("good")
    src = req.text
    with open('index.html', 'w') as f:
        f.write(src)
    soup = BS(src, "lxml")
    
    menu = soup.find("div", id="search").find_all("a")
    
    for i in menu:
        

        lincs = i.get("href")
        
    return 0


if __name__ == '__main__':
     start_ref("peyper")