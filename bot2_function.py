from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')  # Last I checked this was necessary.
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# Query to obtain links
query = 'dha Pakistan'
links = [] # Initiate empty list to capture final results
# Specify number of pages on google search, each page contains 10 #links
n_pages = 2
def proper_links():
    for page in range(1, n_pages):
        url = "http://www.google.com/search?q=" + query + "&start=" + str((page - 1) * 10)
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        # soup = BeautifulSoup(r.text, 'html.parser')

        search = soup.find_all('div', class_="yuRUbf")
        for h in search:
            links.append(h.a.get('href'))
    return links

# for link in links:
#     print(link)

