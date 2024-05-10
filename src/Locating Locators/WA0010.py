# (e)LINK TEXT:
# -------------
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Edge()
driver.get("https://demo.automationtesting.in/FileDownload.html")
time.sleep(5)
z=driver.find_element(By.LINK_TEXT,"More").click()
time.sleep(10)
z1=driver.find_element(By.PARTIAL_LINK_TEXT,"File Download").click()
time.sleep(10)
z2=driver.find_element(By.LINK_TEXT,"Download").click()
time.sleep(10)
print("Test Ok")