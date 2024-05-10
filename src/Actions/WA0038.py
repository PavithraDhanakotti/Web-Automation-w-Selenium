# (c) Double Click:
# -----------------

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
driver=webdriver.Edge()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(3)
dc=driver.find_element(By.ID,"field1").clear()
time.sleep(3)
dc1=driver.find_element(By.CLASS_NAME, "title")
action=ActionChains(driver)
action.double_click(dc1).perform()
time.sleep(5)
print("Test Ok")