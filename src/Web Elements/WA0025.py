# (c) Submit:
# -----------

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Edge()
driver.get("https://www.titan.co.in/")
time.sleep(4)
t = driver.find_element(By.PARTIAL_LINK_TEXT, "LOG")
t.click()
time.sleep(4)
t1=driver.find_element(By.ID, "mobilePhone1").send_keys("6380659846")
time.sleep(4)
t2=driver.find_element(By.CLASS_NAME, "btns").submit()
time.sleep(10)
print("OK")