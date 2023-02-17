from selenium import webdriver
import requests
from bs4 import BeautifulSoup as bs
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
images_list = []
browser.get('https://www.google.com/imghp')
browser.maximize_window()
time.sleep(5)
search_image = browser.find_element("xpath", "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
search_image.send_keys("dha Pakistan")
time.sleep(3)
search_image.send_keys(Keys.ENTER);
time.sleep(6)
image1 = browser.find_element("xpath", "/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[1]/a[1]/div[1]/img").get_attribute("src")
images_list.append(image1)
print(image1)

time.sleep(6)
image2 = browser.find_element("xpath", "/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[2]/a[1]/div[1]/img").get_attribute("src")
images_list.append(image2)
print(image2)

time.sleep(6)
image3 = browser.find_element("xpath", "/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[3]/a[1]/div[1]/img").get_attribute("src")
images_list.append(image3)
print(image3)

import urllib.request
imgURL = images_list[0]
urllib.request.urlretrieve(imgURL, './image1.jpg')
for image in images_list:
    a = browser.execute_script("window.open('');")
    chwd = browser.window_handles
    browser.switch_to.window(chwd[-1])
    browser.get(str(image))
    time.sleep(3)
time.sleep(6000)
# There is an interesting picture in front of me.
# • By having a closer look at the picture, I can see a number of things in the
# image.
# • As I have to describe it for 40 secs, I will start the title of the Picture. The
# title is … or I don't see any given title.
# • Apart from that, there are many interesting words in the image like...
# • The Image also has some significant numbers / years / shapes / percentages
# such as...
# • There are also some beautiful colors like ... and … is my favorite color.
# • I cannot go into further details as my time is over so I will click next. Thank
# you.
# Extra sentence for all the graphical images:
# • The graph not only gives us information about the highest value like…, but
# also about the lowest value which is ...



