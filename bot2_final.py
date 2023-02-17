from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import selenium.webdriver as webdriver
import requests
from bs4 import BeautifulSoup as bs
import re


############
import time
import pyautogui as PAG
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from bot2_function import proper_links


browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# def search_fetched_urls_on_google(url):
#     time.sleep(2)
#     search_local = browser.find_element("xpath", "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
#     search_local.send_keys(url)
#     time.sleep(3)
#     search_local.send_keys(Keys.ENTER);


browser.get('https://www.google.com')
browser.maximize_window()
time.sleep(5)
search = browser.find_element("xpath", "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
search.send_keys("dha Pakistan")
time.sleep(3)
search.send_keys(Keys.ENTER);
time.sleep(15)
url_holder = proper_links()
for link in url_holder:
    a = browser.execute_script("window.open('');")
    chwd = browser.window_handles
    browser.switch_to.window(chwd[-1])
    browser.get(str(link))
    time.sleep(3)
