# Задача: Парсить данные с сайта
import requests
from bs4 import BeautifulSoup
import csv

CSV = 'cards.csv'
HOST = 'https://minfin.com.ua'
URL = 'https://minfin.com.ua/cards/'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Mobile Safari/537.36'
}

def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='be80pr-0 jWpvDc')
    cards = []

    for item in items:
        cards.append(
            {
                'title': item.find('div', class_='be80pr-15 kwXsZB').find('a', class_='cpshbz-0 eRamNS').get('alt'),
                'link_product': HOST + item.find('div', class_='be80pr-15 kwXsZB').find('a', class_='cpshbz-0 eRamNS').get('href'),
                'brand': item.find('div', class_='be80pr-16 be80pr-17 kpDSWu cxzlon').find('a', class_='be80pr-35 UOQtz').get('alt'),
                'card_image': item.find('div', class_='be80pr-9 fJFiLL').find('a', class_='cpshbz-0 knHhYO').find('img', class_='be80pr-10 jIGseK').get('src')
            }
        )
    return cards

def save_doc(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['title', 'link', 'brand', 'image_link'])
        for item in items:
            writer.writerow( [item['title'], item['link_product'], item['brand'], item['card_image']] )

def parser():
    PAGENATION = input('Укажите кол-во страниц страниц для парсинга: ')
    PAGENATION = int(PAGENATION.strip())
    html = get_html(URL)
    if html.status_code == 200:
        cards = []
        for page in range(1, PAGENATION):
            print(f'Парсим страницу: {page}')
            html = get_html(URL, params={'page': page})
            cards.extend(get_content(html.text))
            save_doc(cards, CSV)
        pass
    else:
        print('Error')

parser()








