from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import json

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38'

client = urlopen(my_url)
byte_page = client.read()
client.close()

# html parsing
page_soup = soup(byte_page, 'html.parser')

containers = page_soup.findAll('div', {'class':'item-container'})

with open('page.html', 'w') as f:
    f.write(str(containers[0]))

graphics_cards = []
# dictionary = attribute in html
for container in containers:
    brand = container.find('div', {'class':'item-info'}).div.a.img['title']
    title = container.findAll('a', {'class':'item-title'})[0].text
    shipping_container = container.findAll('li', {'class':'price-ship'})[0].text.strip()

    graphics_cards.append([brand, title, shipping_container])

with open('graphics_cards.csv', 'w') as f:
    headers = 'brand, product_name, shipping\n'
    f.write(headers)

    for graphics_card in graphics_cards:
        f.write(','.join([i.replace(',', '|') for i in graphics_card]) + '\n')

print(graphics_cards)

