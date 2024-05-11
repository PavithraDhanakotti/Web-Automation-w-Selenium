# (c) Mouse move:
# ---------------
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
driver=webdriver.Edge()
driver.get("https://www.irctc.co.in/nget/train-search")
driver.maximize_window()
time.sleep(5)
action=ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH,"/html/body/app-root/app-home/div[1]/app-header/div[2]/div[2]/div[2]/nav/ul/li[7]/a"))
action.perform()
time.sleep(5)
action.move_to_element(driver.find_element(By.XPATH,"/html/body/app-root/app-home/div[1]/app-header/div[2]/div[2]/div[2]/nav/ul/li[7]/ul/li[2]/a")).click()
time.sleep(5)
print("Test is Ok")