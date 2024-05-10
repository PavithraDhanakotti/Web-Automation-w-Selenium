# (d) Mouse Over Action:
# ----------------------

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
driver=webdriver.Chrome()
driver.get("https://www.nerolac.com/")
driver.maximize_window()
time.sleep(3)
moa=driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div/div/header/div/div/div[1]/div[2]/ul[2]/li[3]/a")
time.sleep(3)
action=ActionChains(driver)
action.click(on_element=moa).perform()
time.sleep(5)
print("Test Ok")