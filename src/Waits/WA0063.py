# a) Implicit waits:
# -------------------
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
driver=webdriver.Edge()
driver.get("https://tamilpaatu.com/")
driver.implicitly_wait(10)
driver.find_element(By.NAME,"keyword").send_keys("Kamal Hassan Songs")
driver.implicitly_wait(5)
print("Test is ok")