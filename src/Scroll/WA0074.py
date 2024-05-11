# b) By Pixel:
# ------------
import time
from selenium import webdriver
driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://www.yatra.com/")
time.sleep(7)
driver.execute_script("scrollTo(0,1963)")
print("Test is Ok")