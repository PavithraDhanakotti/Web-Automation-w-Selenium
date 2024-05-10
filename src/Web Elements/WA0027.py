# (c) Submit:
# -----------

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get("https://in.bookmyshow.com/explore/home/vellore")
time.sleep(4)
b1=driver.find_element(By.CSS_SELECTOR, ".bwc__sc-1nbn7v6-14").click()
time.sleep(4)
b2=driver.find_element(By.ID, "mobileNo").send_keys("6380659846")
time.sleep(4)
b3=driver.find_element(By.CLASS_NAME,"bwc__sc-dh558f-37").submit()
time.sleep(10)