# a)Performing Multiple actions like Key-up and Key-down:
# -------------------------------------------------------


import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver import ActionChains
driver = webdriver.Edge()
driver.get("file:///C:/Users/pavit/PycharmProjects/firstproject/HW/Action/multi_action3.html")
time.sleep(5)
a1 = driver.find_element(By.NAME, "B")
b1 = driver.find_element(By.NAME, "L")
c1 = driver.find_element(By.NAME, "H")
d1 = driver.find_element(By.NAME, "J")
e1 = driver.find_element(By.NAME, "E")
f = ActionChains(driver)
f.key_down(Keys.CONTROL)
f.click(a1)
time.sleep(3)
f.click(b1)
time.sleep(3)
f.click(c1)
time.sleep(3)
f.click(d1)
time.sleep(3)
f.click(e1)
time.sleep(3)
f.perform()
print("Test is OK")
