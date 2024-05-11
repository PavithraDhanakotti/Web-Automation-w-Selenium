# a) Printing the table:
# ----------------------
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Edge()
driver.get("https://www.amazon.in/")
driver.maximize_window()
time.sleep(3)
table = driver.find_element(By.CLASS_NAME, "navFooterMoreOnAmazon")
print(table.text)
time.sleep(10)
print("test ok")