# (d) Mouse Over Action:
# ----------------------
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
driver=webdriver.Edge()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(3)
moa=driver.find_element(By.CLASS_NAME,"wikipedia-icon")
time.sleep(3)
action=ActionChains(driver)
action.click(on_element=moa)
action.perform()
time.sleep(5)
print("Test Ok")