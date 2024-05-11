# (g) File Download:
# ------------------
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
driver = webdriver.Edge()
driver.get("https://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()
time.sleep(8)
download = driver.find_element(By.XPATH, "/html/body/section/div[1]/div/div/div[1]/a")
action = ActionChains(driver)
a1 = action.click(download).perform()
time.sleep(4)
print("Test is Ok")