from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import cv2
import numpy as np
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
# options = Options()
# driver = webdriver.Firefox(options=options)

# Navigate site zameen
driver.get("https://www.zameen.com/")
time.sleep(9)

# # refreshing page to bypass ad
# pyautogui.keyDown('ctrl')  # hold down the shift key
# pyautogui.press('r')       # press r
# pyautogui.keyUp('ctrl')    # release the shift key


# firing javascript function to close the ad, no need to bypass via refreshing
driver.execute_script("show_sitewide_ad('hide');")

# selecting city rawalpindi
time.sleep(3)
city_selector = driver.find_element("xpath", "/html/body/div[1]/header/div[6]/div/div[2]/div[2]/div[1]/div[1]/div/div")
city_selector.click()
time.sleep(2)
rawalpindi_city = driver.find_element("xpath", "/html/body/div[1]/header/div[6]/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div[1]/div/span[4]/button")
rawalpindi_city.click()
time.sleep(3)

# searching location Bahria Town
location_search = driver.find_element("xpath", "/html/body/div[1]/header/div[6]/div/div[2]/div[2]/div[1]/div[2]/div/div/div/ul/input")
location_search.click()
time.sleep(3)
location_search.send_keys("Bahria Town phase 4")
time.sleep(2)
pyautogui.press('enter')
time.sleep(1)

# selecting price range
price_range = driver.find_element("xpath", "/html/body/div[1]/header/div[6]/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/span/span[3]")
price_range.click()
time.sleep(2)
set_max_price = driver.find_element("xpath", "/html/body/div[1]/header/div[6]/div/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/input")
set_max_price.send_keys("15000000")
time.sleep(2)
price_range.click()

# selecting bedtype = 3
bedtype = driver.find_element("xpath", "/html/body/div[1]/header/div[6]/div/div[2]/div[2]/div[2]/div[4]/div/div")
bedtype.click()
time.sleep(2)
three_bedtype = driver.find_element("xpath", "/html/body/div[1]/header/div[6]/div/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[1]/div/span[5]/button")
three_bedtype.click()
time.sleep(1)
bedtype.click()

# clicking Find button
time.sleep(1)
find_button = driver.find_element("xpath", "/html/body/div[1]/header/div[6]/div/div[2]/div[2]/div[1]/a")
time.sleep(2)
find_button.click()


# slowly scrolling down
for scroll_down in range(1, 130):
    pyautogui.press('down')
    time.sleep(0.5)

# Close browser  after 6000 seconds
time.sleep(6000)
driver.close()


