import requests
from bs4 import BeautifulSoup as bs
import re


all_fetched_links=[]
r = requests.get("https://www.google.com/search?q=dha")
# convert to a beautiful soup object
webpage = bs(r.content)
# print(webpage.prettify())
h = webpage.find_all(href=re.compile(r'(.*)/url\?q=\d*'))
# method 3
# links = webpage.select("a")
actual_links = [link['href'] for link in h]
for eachlink in actual_links:
    # print(eachlink.replace("/url?q=", ""))
    all_fetched_links.append(eachlink.replace("/url?q=", ""))
count = 0
for link in all_fetched_links:
    print(link)
    count = count + 1
    if count == 5:
        break
#
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.keys import Keys
# import time
# import requests
# from bs4 import BeautifulSoup as bs
# import re
#
#
# def fetch_anchor_tags():
#     r = requests.get("https://www.google.com/search?q=dha")
#     # convert to a beautiful soup object
#     webpage = bs(r.content)
#     # print(webpage.prettify())
#     h = webpage.find_all(href=re.compile(r'(.*)/url\?q=\d*'))
#     # method 3
#     actual_links = [link['href'] for link in h]
#     for eachlink in actual_links:
#         print(eachlink.replace("/url?q=", ""))
#
#
# browser = webdriver.Firefox()
# browser.get('https://www.google.com')
# browser.maximize_window()
# time.sleep(5)
# search = browser.find_element("xpath", "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
# search.send_keys("dha")
# time.sleep(3)
# search.send_keys(Keys.ENTER);
#



