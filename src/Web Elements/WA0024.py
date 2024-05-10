# (b) TEXT:
# ---------
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Henry_Ossawa_Tanner")
time.sleep(4)
t = (driver.find_element(By.PARTIAL_LINK_TEXT, "Henry ").text)
t1 = (driver.find_element(By.CLASS_NAME, "infobox").text)
print(t)
print(t1)
