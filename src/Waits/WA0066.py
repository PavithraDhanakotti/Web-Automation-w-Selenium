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
driver.get("https://www.purplle.com/")
try:
    z=WebDriverWait(driver,10).until(ec.presence_of_element_located((By.XPATH,"/html/body/app-root/main/app-home-common/app-home/header-content-hybrid/desktop-header-content/div[3]/desktop-search-content/div[1]/div/div[1]/p/input")))
except TimeoutError:
    print("Check Error")
print("test ok")