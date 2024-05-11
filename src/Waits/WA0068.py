# b) Explicit Waits:
# ------------------

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
driver=webdriver.Edge()
driver.get("https://www.swiggy.com/")
try:
    z=WebDriverWait(driver,10).until(ec.presence_of_element_located((By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div[1]/div[1]/div/div[2]/div/div/input")))
except TimeoutError:
    print("Check Error")
print("test ok")
