# (g)TAG NAME:
# ------------
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Edge()
driver.get("https://www.google.com/?gws_rd=ssl")
time.sleep(5)
c=driver.find_element(By.TAG_NAME,"textarea").send_keys("Tamil Movies from 2000-2005"+Keys.RETURN)
time.sleep(5)
print("Test is ok!")