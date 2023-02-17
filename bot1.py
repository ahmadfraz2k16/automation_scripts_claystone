from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# import KEYS
from selenium.webdriver.common.keys import Keys
import time
# Step 1) Open Firefox 
browser = webdriver.Firefox()
# Step 2) Navigate to Facebook
browser.get("http://www.facebook.com")
# Step 3) Search & Enter the Email or Phone field & Enter Password
username = browser.find_element('id', 'email')
password = browser.find_element('id', "pass")
submit   = browser.find_element('name',"login")
# username.send_keys("03084290325")
# password.send_keys("pass")
username.send_keys("pass")
password.send_keys("pass")
# Step 4) Click Login
submit.click()
time.sleep(4)
search = browser.find_element('xpath', '/html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div/label/input')
time.sleep(3)
search.send_keys("john wick")
time.sleep(3)
search.send_keys(Keys.ENTER);
time.sleep(2)
# openProfile = browser.find_element('xpath', '/html/body/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div/div/div/span/div/a')
openProfile = browser.get('https://web.facebook.com/johnwickmovie')
time.sleep(2)
# openProfile.click()
# profilePicture = browser.find_element('xpath', '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[1]/div[2]/div/div/div/div[1]/div/div/a/div/svg/g/image')
profilePicture = browser.get('https://web.facebook.com/johnwickmovie/photos/a.356632744501626/2265536703611211/')
# profilePicture.click()
