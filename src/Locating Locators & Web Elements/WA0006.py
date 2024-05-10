# (c) CLASS NAME:
# ---------------
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Edge()
driver.get("https://www.google.com/?gws_rd=ssl")
time.sleep(3)
Q=driver.find_element(By.CLASS_NAME,"gLFyf").send_keys("Indian Foods"+Keys.RETURN)
time.sleep(10)
print("Test is Ok!")