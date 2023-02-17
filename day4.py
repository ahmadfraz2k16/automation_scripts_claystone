import time
import pyautogui as PAG
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select


browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get("https://changeofaddresspros.com/Apply/#/start/1")
browser.maximize_window()
time.sleep(5)
fname = browser.find_element(By.ID, "fname")
lname = browser.find_element(By.ID, "lname")


fname.send_keys("ahmad")
lname.send_keys('fraz')
buttons = browser.find_elements(By.XPATH,"//*[contains(text(), 'Get Started')]")

for btn in buttons:
    btn.click()
time.sleep(2)
bussiness= browser.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div/div/div/div/div/div[1]/div/div/div[5]/button')
bussiness.click()
time.sleep(1)

bname= browser.find_element(By.ID, "bName")
bname.send_keys("Claystone Tech")
time.sleep(2)
btn1 = browser.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/div[4]/button[1]')
for btn in btn1:
    btn.click()
time.sleep(5)

address=browser.find_element(By.NAME, "address")
address.send_keys("usa")
time.sleep(2)

PAG.press('down')
PAG.press('down')
time.sleep(3)
PAG.press('down')
PAG.press('enter')
time.sleep(2)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
nxt = browser.find_element("xpath", "/html/body/div[1]/div[2]/div/div/div/div/div/div/div[3]/button")
nxt.click()
time.sleep(3)
temp_btn = browser.find_element("xpath", "/html/body/div[1]/div[2]/div/div/div/div/div/div/div/button[1]")
temp_btn.click()
time.sleep(2)

date_month = browser.find_element("id", "End-Datemonth")
date_month.send_keys("2")
Dateday = browser.find_element("id", "End-Dateday")
Dateday.send_keys("3")
Dateyear = browser.find_element("id", "End-Dateyear")
Dateyear.send_keys("2030")

nxt6 = browser.find_element("xpath", "/html/body/div[1]/div[2]/div/div/div/div/div/div/div[3]/button")
nxt6.click()
time.sleep(2)
browser.find_element("name","address").send_keys('ssdkjfhsadkfhsadfsldfk')
PAG.press('down')
PAG.press('enter')
time.sleep(2)
browser.find_element("name","streetAddress").send_keys('railway scheme 3')
browser.find_element("name","unitNumber2").send_keys('23')
browser.find_element("name","city").send_keys('rawalpindi')
browser.find_element("name","state").send_keys('pubjab')
browser.find_element("name","zipCode").send_keys('123456')
nxt8 = browser.find_element("xpath", "/html/body/div[1]/div[2]/div/div/div/div/div/div/div[4]/button")
nxt8.click()
time.sleep(3)
browser.find_element("xpath","/html/body/div[1]/div[2]/div/div/div/div/div/div/div[1]/div/div/input").send_keys('12345678909')
nxt9 = browser.find_element("xpath", "/html/body/div[1]/div[2]/div/div/div/div/div/div/div[2]/button")
time.sleep(2)
nxt9.click()
time.sleep(3)
browser.find_element("name","email").send_keys('hinafraz025@gmail.com')
time.sleep(2)
nxt10 = browser.find_element("xpath", "/html/body/div[1]/div[2]/div/div/div/div/div/div/div[2]/button")
nxt10.click()

time.sleep(6000)