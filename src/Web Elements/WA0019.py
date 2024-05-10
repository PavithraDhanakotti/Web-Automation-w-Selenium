# (a) CLEAR:
# ----------

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://www.ajio.com/")
driver.maximize_window()
c=driver.find_element(By.CSS_SELECTOR, ".react-autosuggest__input").send_keys("kids dress")
time.sleep(3)
c1=driver.find_element(By.NAME,"searchVal").clear()
time.sleep(3)
c2=driver.find_element(By.TAG_NAME, "input").send_keys("Girls accessories")
time.sleep(3)
c3=driver.find_element(By.CLASS_NAME, "react-autosuggest__input").clear()
time.sleep(3)
c4=driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/div/header/div[3]/div[2]/form/div/div/input").send_keys("Trendy girl dress"+Keys.RETURN)
time.sleep(10)
print("Test is OK")