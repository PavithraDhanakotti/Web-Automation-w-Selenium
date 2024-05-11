# a)Performing Multiple actions like Key-up and Key-down:
# -------------------------------------------------------

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
driver=webdriver.Edge()
driver.get("file:///C:/Users/pavit/PycharmProjects/firstproject/Exercise/Action/multi_action1.html")
time.sleep(5)
z=driver.find_element(By.NAME,"one")
z1=driver.find_element(By.NAME,"ten")
z2=driver.find_element(By.NAME,"five")
y=ActionChains(driver)
y.key_down(Keys.CONTROL)
y.click(z)
time.sleep(5)
y.click(z1)
time.sleep(3)
y.click(z2)
y.perform()
print("test ok")


