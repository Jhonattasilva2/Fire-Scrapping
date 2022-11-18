import requests
from bs4 import BeautifulSoup

url = 'https://firealarm.com/shop/?swoof=1&orderby=popularity'
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}

html = requests.get(url, headers=headers).content
soup = BeautifulSoup(html, 'html.parser')
item_cards = soup.find_all('a', class_='woocommerce-LoopProduct-link woocommerce-loop-product__link')
last_page = soup.find_all('a', class_='page-numbers')[-2].get_text()

for i in range(1, int(last_page)):
    url_page = f'https://firealarm.com/shop/page/{i}/?swoof=1&orderby=popularity'
    html = requests.get(url_page, headers=headers).content
    soup = BeautifulSoup(html, 'html.parser')
    item_cards = soup.find_all('a', class_='woocommerce-LoopProduct-link woocommerce-loop-product__link')

    with open('FireScrapping/firealarm.com_Scrapping.csv', 'a', encoding='UTF-8') as file:
        for card in item_cards:
            item_title = card.find('h2', class_='woocommerce-loop-product__title').text
            item_description = card.find('span', class_='mws-short-description').text
            item_link = card['href']

            try:
                item_price = card.find('bdi').text
            except:
                item_price = '0'
   
            line = item_title + ';' + item_description + ';' + item_link + ';' + item_price + ';' + '\n'
            print(line)
            file.write(line)
    print(url_page)
