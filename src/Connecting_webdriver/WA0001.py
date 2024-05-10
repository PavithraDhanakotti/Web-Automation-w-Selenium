import time
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("https://in.pinterest.com/")
time.sleep(5)
driver.quit()
print("Test is OK!")