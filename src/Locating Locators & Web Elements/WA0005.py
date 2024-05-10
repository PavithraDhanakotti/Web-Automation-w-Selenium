# (b) NAME:
# ---------
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Edge()
driver.get("https://www.google.com/")
time.sleep(5)
d=driver.find_element(By.NAME,"q").send_keys("Cricket"+Keys.RETURN)
time.sleep(10)
print("Test is OK!.")