# (d) CSS SELECTOR:
# -----------------
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Edge()
driver.get("https://www.nykaa.com/")
time.sleep(3)
a=driver.find_element(By.CSS_SELECTOR,".css-1upamjb").send_keys("Gel Primer"+Keys.RETURN)
time.sleep(5)
print("Test is Ok")