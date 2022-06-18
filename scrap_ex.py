from ast import Div
import requests
import urllib
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
URL = "https://127.0.0.1:5000/show"
page = requests.get(URL).text
#req = Request(URL,headers={'User-Agent': 'Mozilla/5.0'})
#webpage = urlopen(req).read()
# with urllib.request.urlopen(URL) as url:
#     s = url.read()
#page = requests.get(URL)
soup = BeautifulSoup(page, "lxml")

#soup = BeautifulSoup(page.content, "html.parser")
#soup = BeautifulSoup(page.text, "html.parser")
print(soup.prettify())

print(len(soup.find_all("img")))
#tags = soup.findAll('img', class_="rg_i Q4LuWd")
tags = soup.find_all('img', class_="yWs4tf")
print("mm",len(soup.find_all(class_="rg_i Q4LuWd)")))
print("nr imagens",len(tags))
# links = []
# for image_tag in tags:
#     print(links.append(tags['src']))

#results = soup.find(id="PruXVj6cRhXQZM")

a = soup.find("div", class_ ="bRMDJfislir")
#b= soup.find(class_="rg_iQ4LuWd")

#b = a.find_all("img", class_="bRMDJf islir")
#print(len(a))
print(a)
#print(b)
