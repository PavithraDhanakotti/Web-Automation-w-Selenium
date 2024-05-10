# (f) PARTIAL LINK TEXT:
# ----------------------
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
driver = webdriver.Edge()
driver.get("https://www.ajio.com/")
time.sleep(5)
driver.maximize_window()
time.sleep(10)
d=driver.find_element(By.PARTIAL_LINK_TEXT,"WOM").click()
time.sleep(10)
print("Test is Ok")