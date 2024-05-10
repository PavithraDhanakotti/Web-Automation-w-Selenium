# (a) CLEAR:
# ----------

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
time.sleep(3)
c=driver.find_element(By.NAME, "email").send_keys("Pavithra Dhanakotti")
time.sleep(3)
c11=driver.find_element(By.ID, "pass").send_keys("Pavithra")
time.sleep(3)
c1=driver.find_element(By.CLASS_NAME,"inputtext").clear()
time.sleep(3)
c2=driver.find_element(By.ID, "pass").send_keys("Pavithra123")
time.sleep(3)
c3=driver.find_element(By.CSS_SELECTOR, ".inputtext").clear()
time.sleep(3)
c4=driver.find_element(By.XPATH,"//*[@id='pass']").send_keys("Pavithra_!23"+Keys.RETURN)
time.sleep(10)
print("Test is OK")