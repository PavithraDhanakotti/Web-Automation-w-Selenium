# (b)NoSuchElement:
# -----------------

import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Edge()
driver.maximize_window()
time.sleep(5)
driver.get("https://www.target.com/")
try:
    d = driver.find_element(By.NAME, "searchTerming").send_keys("kids dress"+Keys.RETURN)
except NoSuchElementException:
    print("Please Check The Web Element")
    time.sleep(3)
print("Test OK")