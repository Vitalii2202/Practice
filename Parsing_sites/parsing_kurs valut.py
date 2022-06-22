import requests
from bs4 import BeautifulSoup


DOLLAR_GRN = 'https://www.google.com/search?q=ljkkfh+r+uhbdyt&oq=ljkkfh+r+uhbdyt&aqs=chrome..69i57j0i10l9.2729j1j9&sourceid=chrome&ie=UTF-8'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Mobile Safari/537.36'
}

full_page = requests.get(DOLLAR_GRN, headers=HEADERS)


soup = BeautifulSoup(full_page.content, 'html.parser')
convert = soup.find_all('div', class_='dDoNo ikb4Bb gsrt')
print(convert)


