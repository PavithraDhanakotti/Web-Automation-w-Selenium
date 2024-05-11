# (f) File Upload:
# ----------------
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
driver = webdriver.Edge()
driver.get("https://demo.automationtesting.in/FileUpload.html")
driver.maximize_window()
time.sleep(6)
r = driver.find_element(By.ID, "input-4").send_keys("C:\\Users\\pavit\\Documents\\2022-01-29 (1).png")
time.sleep(5)
print("Test is ok")