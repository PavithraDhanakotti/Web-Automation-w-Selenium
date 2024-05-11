# (f) File Upload:
# ----------------
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
driver = webdriver.Edge()
driver.get("https://easyupload.io/")
driver.maximize_window()
time.sleep(6)
'''clck = driver.find_element(By.CSS_SELECTOR, ".dz-button")
action = ActionChains(driver)
a1 =action.click(clck).perform()'''
r = driver.find_element(By.CLASS_NAME, "dz-button").send_keys("C:\\Users\\pavit\\Documents\\2022-01-29 (1).png")
time.sleep(8)
print("Test is ok")