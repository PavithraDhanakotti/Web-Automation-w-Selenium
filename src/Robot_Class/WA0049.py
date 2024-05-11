# (b)Key Release:
# ---------------
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
driver=webdriver.Edge()
driver.get("https://www.google.com/")
print(driver.title)
time.sleep(3)
z=driver.find_element(By.NAME,"q")
action=ActionChains(driver)
action.click(z)
time.sleep(5)
action.key_down(Keys.SHIFT)
action.send_keys("Indian Actors")
print(driver.title)
action.perform()
time.sleep(5)
print("Test is Ok")