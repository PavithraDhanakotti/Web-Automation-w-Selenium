# (c) Double Click:
# -----------------
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
driver=webdriver.Edge()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(3)
dc=driver.find_element(By.ID,"field1").clear()
time.sleep(3)
dc1=driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[4]/div[1]/input[1]")
dc1.send_keys("PAvithra")
btn=driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[4]/div[1]/button")
action=ActionChains(driver)
action.double_click(btn).perform()
time.sleep(5)
print("Test Ok")
