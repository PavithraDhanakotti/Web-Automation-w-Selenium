# (h) XPATH:
# ----------
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get("https://www.meesho.com/")
time.sleep(5)
s=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/div[2]/div[1]/input").send_keys("Jewel set"+Keys.RETURN)
time.sleep(10)
print("Test is OK!")