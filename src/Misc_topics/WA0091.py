# b)Passing input to the alerts & Get the text present in the alert:
# ------------------------------------------------------------------
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
driver=webdriver.Edge()
driver.get("C:\\Users\\pavit\\PycharmProjects\\firstproject\\Exercise\\Alerts\\Passinginput_alerts1.html")
z=driver.find_element(By.NAME,"employeeLogin").click()
alt=driver.switch_to.alert
time.sleep(3)
alt.send_keys("Pavithra")
time.sleep(3)
alt.accept()
time.sleep(3)
alt.accept()
z1=driver.find_element(By.ID,'msg')
print(z1.text)
time.sleep(10)
print("Test is OK")