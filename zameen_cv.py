import cv2
import numpy as np
from selenium import webdriver

# Load the target image using OpenCV
template = cv2.imread("close_cross_big.png", cv2.IMREAD_GRAYSCALE)

# Initialize the webdriver
options = webdriver.ChromeOptions()
options.add_argument("--disable-extensions")
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=options)

# Navigate to the website
driver.get("https://www.example.com/")

# Take a screenshot of the page
screenshot = driver.get_screenshot_as_png()

# Convert the screenshot to a numpy array
image = np.array(bytearray(screenshot), dtype=np.uint8)

# Load the screenshot into OpenCV
screenshot = cv2.imdecode(image, cv2.IMREAD_GRAYSCALE)

# Use OpenCV to match the target image with the screenshot
result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)

# Get the coordinates of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# Calculate the position of the target image on the page
x, y = max_loc
w, h = template.shape[::-1]

# Click at the position of the target image
driver.execute_script("window.scrollTo(0, {0})".format(y))
driver.execute_script("document.elementFromPoint({0}, {1}).click()".format(x + w // 2, y + h // 2))

# Close the browser
driver.close()
