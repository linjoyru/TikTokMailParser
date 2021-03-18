import requests
import re
from bs4 import BeautifulSoup
import random as r
import string
from threading import Thread


HEADERS = {
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5",
    "Content-Type": "application/json",
    "Accept": "*/*",
}

PATTERN = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"


class ParseTT():


    def __init__(self):
        """Тут создаю файл, куда буду записывать.
        """
        with open('result.txt', 'w'):
            pass

    def parse(self, nick):
        """Функция парса.
        """
        response = requests.get(f"https://www.tiktok.com/@{nick}", headers = HEADERS)
        print(response.status_code)
        if response.status_code == 200:# Если такой аккаунт существует :
            
            soup = BeautifulSoup(response.text, 'lxml')
            text = soup.find_all('h2', class_='share-desc mt10')[0].text #Достаю текст из описания канала.
                
            text = text.split("\n")
            for line in text:
                line = line.split(" ")
                for word in line:
                    if re.search(PATTERN, word):#Если слово подходит по паттерну, то записываю и прерываю цикл.
                        with open('result.txt','a') as f:
                            f.write(word)
                            break




def generate_random_string(len_sep, no_of_blocks):
    """Функция для генерации случайной строки.
    """
    random_string = ''
    random_str_seq = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(0,len_sep*no_of_blocks):
        random_string += str(random_str_seq[r.randint(0, len(random_str_seq) - 1)])
    return random_string

def gen_random_str(amount):
    """Функция, которая генерирует нужное кол-во строк.
    """
    answer = []

    for x in range(0, amount):
        answer.append(generate_random_string(1,r.randint(4,15)))
    return answer

def thread_work():
    """Функция для потока.
    """
    global a, nick_list
    while len(nick_list) != 1:
        a.parse(nick_list[0])
        nick_list.pop(0)

a = ParseTT() #Инициализирую класс для парса.
nick_list = gen_random_str(100) #Создаю и заполняю список рандомными никами.


for x in range(0,1):#Запускаю потоки
    Thread(target=thread_work).start()



    
