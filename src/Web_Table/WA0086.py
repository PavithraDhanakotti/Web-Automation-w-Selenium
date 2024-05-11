# b) printing the length:
# -----------------------

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Edge()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(3)
table = driver.find_element(By.NAME,"BookTable")
print(table.text)
time.sleep(3)
r = driver.find_elements(By.XPATH,'//*[@id="HTML1"]/div[1]/table/tbody/tr')
print(len(r))
time.sleep(3)
c = driver.find_elements(By.XPATH,'//*[@id="HTML1"]/div[1]/table/tbody/tr[5]/td')
print(len(c))
time.sleep(10)
print("test ok")