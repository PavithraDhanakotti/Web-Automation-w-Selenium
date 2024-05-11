# c) By Visibility:
# -----------------
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Edge()
driver.get("https://magento.softwaretestingboard.com/?ref=hackernoon.com")
driver.maximize_window()
time.sleep(7)
print(driver.title)
word = driver.find_element(By.CLASS_NAME, "title")
driver.execute_script("arguments[0].scrollIntoView()", word)
print("Test is Ok")