# (c) Submit:
# -----------

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Edge()
driver.get("https://www.jiomart.com/customer/account/login")
time.sleep(3)
r=driver.find_element(By.NAME, "undefined").send_keys("6380659846")
time.sleep(3)
r1=driver.find_element(By.ID, "basic-button").submit()
time.sleep(10)
print("OK")