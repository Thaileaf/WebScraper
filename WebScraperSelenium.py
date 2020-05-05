from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options)

url = "https://www.whenisthenextsteamsale.com/"

driver.get(url)
html = driver.execute_script("return document.documentElement.outerHTML")
soup = BeautifulSoup(html, 'html.parser')

print(soup.find('p',{'id':'mainTimer'}).text)