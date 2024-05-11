# (b)Key Release:
# ---------------
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
driver=webdriver.Edge()
driver.get("https://open.spotify.com/")
print(driver.title)
time.sleep(3)
z=driver.find_element(By.XPATH,"/html/body/div[3]/div/div[2]/div[2]/nav/div[1]/ul/li[2]")
action=ActionChains(driver)
action.click(z)
time.sleep(5)

action.key_down(Keys.SHIFT)
action.send_keys("tamil")
action.key_up(Keys.SHIFT)
action.send_keys("Songs")
action.perform()
time.sleep(10)
print("Test is Ok")