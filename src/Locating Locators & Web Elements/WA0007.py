# (c) CLASS NAME:
# ---------------
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get("https://www.myntra.com/")
time.sleep(3)
g=driver.find_element(By.CLASS_NAME,"desktop-searchBar").send_keys("Colour Changing Lip Gloss"+Keys.RETURN)
time.sleep(10)
print("Test is OK!")