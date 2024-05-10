import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://www.google.com/")
time.sleep(4)
driver.maximize_window()
print(driver.title)
driver.back()
time.sleep(3)
driver.get("https://www.jiomart.com/customer/account/login")
print(driver.title)
time.sleep(3)
r=driver.find_element(By.NAME, "undefined").send_keys("6380659846")
time.sleep(3)
r1=driver.find_element(By.ID, "basic-button").submit()
time.sleep(5)
driver.back()
driver.refresh()
time.sleep(10)
print("Test ok")