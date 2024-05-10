# (d) CSS SELECTOR:
# -----------------
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get("https://www.nykaa.com/")
time.sleep(3)
a=driver.find_element(By.CSS_SELECTOR,".css-1upamjb").send_keys("Tinted lip balm"+Keys.RETURN)
time.sleep(10)
print("Test is Ok")