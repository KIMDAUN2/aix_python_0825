from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time
import os
from dotenv import load_dotenv

#2.selenium :자동화 구현
browser = webdriver.Chrome()
browser.maximize_window() #화면최대창 확대
url = "https://www.naver.com/"

#검색부분- 날씨입력>enter : 온도 , 날씨를 출력하시오.

browser.get(url)
elem=browser.find_element(By.CLASS_NAME,"weather_graphic")
elem.send_keys("날씨")




#브라우저열기
browser.get(url)
browser.find_element(By.CLASS_NAME,'MyView-module__link_login___VlF7z').click()
time.sleep(3)
elem= browser.find_element(By.ID,'id')
elem.send_keys('aaa')
elem2= browser.find_element(By.ID,'pw')
elem2.send_keys('1111')
input()

# .env파일 읽기
# load_dotenv()
# print(os.getenv('naver_id'))











# a='1,123만원'
# print(a[:-1])  #1,123만
# print(a[:-2])  #1,123
# print(a[-2:])  #만원
# print(a[-1])   #원
# a_int = int(a[:-2].replace(",",""))

