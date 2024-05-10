# (b) TEXT:
# ---------

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://voterportal.eci.gov.in/")
time.sleep(4)
t=(driver.find_element(By.CLASS_NAME, "list-content").text)
t1=(driver.find_element(By.CSS_SELECTOR, ".mb-5").text)
print(t)
print(t1)