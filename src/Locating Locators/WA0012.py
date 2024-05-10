# (g)TAG NAME:
# ------------
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
drivers=webdriver.Chrome()
drivers.get("https://www.youtube.com/")
time.sleep(5)
s=drivers.find_element(By.TAG_NAME,"input").send_keys("Tamil Nadu"+Keys.RETURN)
time.sleep(10)
print("Test is ok")