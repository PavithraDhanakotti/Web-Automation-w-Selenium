# (g) File Download:
# ------------------
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
driver = webdriver.Edge()
driver.get("https://demo.imacros.net/Automate/Downloads")
driver.maximize_window()
time.sleep(8)
download1 = driver.find_element(By.XPATH, "/html/body/div[1]/section/div/div/div/table/tbody/tr[1]/td[2]/a")
download2 = driver.find_element(By.XPATH, '//*[@id="downloaddemo"]/table/tbody/tr[2]/td[2]/a')
action = ActionChains(driver)
a1 = action.click(download1).perform()
time.sleep(4)
a2 = action.click(download2).perform()
time.sleep(4)
print("Test is Ok")