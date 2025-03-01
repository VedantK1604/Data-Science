from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np
import time

#path to chrome Driver
s = Service("F:\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=s)

headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}

#link to each page 
driver.get("https://www.bookchor.com/category/1/fiction")
time.sleep(3)

link1 = driver.find_element(by=By.XPATH,value='/html/body/div[3]/div/div[2]/div[2]/div[1]/div[2]/h3/a')
link1.click()

#link fetched for beautifulsoup webpage

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "sellingPMob1"))  # Adjust this if necessary
)

time.sleep(3)
current_url = driver.current_url

webpage=requests.get(current_url,headers=headers).text
soup=BeautifulSoup(webpage,'lxml')
print('url Fetched')

print(soup.find_all('h1')[0].text.strip())
print(soup.find_all('h3')[8].text.strip())
print(soup.find('p', id='sellingPMob1').text.strip())
print(soup.find('p', id='desc_full').text.strip())
print(soup.find_all('p', class_='rating'))
print(soup.find_all('p', class_='Highlights'))

driver.back()

while True:
    pass