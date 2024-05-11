# c) By Visibility:
# -----------------
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
driver=webdriver.Edge()
driver.get("https://en.wikipedia.org/wiki/Indian_Forest_Act,_1927")
time.sleep(3)
z=driver.find_element(By.ID,'Reserved_forest')
driver.execute_script("arguments[0].scrollIntoView()",z)
time.sleep(10)
print("test ok")