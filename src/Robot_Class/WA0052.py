# (c) Mouse move:
# ---------------
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
driver=webdriver.Edge()
driver.get("https://portal2.passportindia.gov.in/AppOnlineProject/")
driver.maximize_window()
time.sleep(5)
action=ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH,"/html/body/table/tbody/tr/td/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/div/div[3]/ul/li[2]/a"))
action.perform()
time.sleep(5)
action.move_to_element(driver.find_element(By.XPATH,"/html/body/table/tbody/tr/td/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/div/div[3]/ul/li[2]/ul/li[2]/a")).click()
time.sleep(5)
print("Test is Ok")