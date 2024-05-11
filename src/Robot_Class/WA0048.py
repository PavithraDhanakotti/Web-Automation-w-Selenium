# (a) Key Press:
# --------------
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
driver=webdriver.Edge()
driver.get("https://www.wikipedia.org/")
time.sleep(3)
print(driver.title)
z=driver.find_element(By.ID,"searchInput")
z.send_keys("Longest English Words")
z.send_keys(Keys.ENTER)
time.sleep(5)
print("Test Ok")