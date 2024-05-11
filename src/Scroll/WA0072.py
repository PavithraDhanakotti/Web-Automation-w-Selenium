# b) By Pixel:
# ------------
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
driver=webdriver.Edge()
driver.get("https://youtube.com/")
time.sleep(10)
driver.execute_script("scrollTo(0,1000)")
time.sleep(15)
print("test ok")