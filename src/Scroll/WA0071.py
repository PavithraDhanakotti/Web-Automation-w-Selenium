# a) To Bottom:
# -------------
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Edge()
driver.get("https://www.globalsqa.com/demo-site/")
driver.maximize_window()
time.sleep(8)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(10)
print("Test is Ok")