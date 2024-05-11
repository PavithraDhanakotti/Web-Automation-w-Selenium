# b) By Pixel:
# ------------
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as e
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
driver = webdriver.Edge()
driver.get("https://www.globalsqa.com/demo-site/")
driver.maximize_window()
time.sleep(5)
driver.execute_script("scrollTo(0,1523)")
time.sleep(8)
print("Test is Ok")