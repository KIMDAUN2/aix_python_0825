import requests
from bs4 import BeautifulSoup

url="https://www.google.com/"
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}
res = requests.get(url,headers=headers)
res.raise_for_status() #에러시 종료


soup = BeautifulSoup(res.text,'lxml')
print("-"*50)
#태그,태그속성1개,태그속성전체,태그id,태그class
print(soup.title)
print(soup.title.get_text())
print(soup.find("a",{"class":"w5hRs"}))     #속성값을 사용할 때는 find를 사용한다.
print(soup.find("a",{"class":"gb_6"}).get_text())
