# a) To Bottom:
# -------------
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
driver=webdriver.Edge()
driver.get("https://www.lenskart.com/")
time.sleep(3)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(10)
print("test ok")