# d) Horizontal:
# --------------
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as e
from selenium.webdriver.support.ui import WebDriverWait
drive = webdriver.Edge()
drive.maximize_window()
drive.get("https://www.vogue.es/")
a = drive.title
print(a)
print(len(a))
time.sleep(8)
drive.execute_script("window.scrollBy(129,0)")
time.sleep(8)
print("Test is Ok")