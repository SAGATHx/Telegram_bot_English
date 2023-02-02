import requests
from bs4 import BeautifulSoup
from time import sleep

URL = 'https://www.dotabuff.com/heroes'

headers = {
    "Accept": "*/*",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

def extract_heroes():

    req = requests.get(URL, headers=headers)
    soup = BeautifulSoup(req.text, 'lxml')
    data = soup.find('div', class_='hero-grid').find_all('a')
    for link in data:
        link_heroes = 'https://www.dotabuff.com' + link.get('href')
        yield link_heroes

def extract_info(link):

    for link_h in link:
        req = requests.get(link_h, headers=headers)
        soup = BeautifulSoup(req.text, 'lxml')
        data = soup.find_all('div', class_='header-content')
        for info in data:
            name = info.find('h1').text
            if info.find('span', class_='lost') is None:
                rate = info.find('span', class_='won').text
            else:
                rate = info.find('span', class_='lost').text
        print(name,'\n', rate)


extract_info(extract_heroes())

print()





