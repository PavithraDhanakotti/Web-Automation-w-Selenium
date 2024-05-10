import time
from selenium import webdriver
driver=webdriver.Edge()
driver.get("https://youtube.com/")
time.sleep(5)
driver.quit()
print("Test is OK!")
