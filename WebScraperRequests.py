from bs4 import BeautifulSoup
import requests

source = requests.get('http://coreyms.com').text
print(source)

soup = BeautifulSoup(source, 'lxml')


