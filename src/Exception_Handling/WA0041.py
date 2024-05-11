# (a) Webdriver Exception:
# ------------------------
import time
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
driver=webdriver.Edge()
driver.maximize_window()
time.sleep(5)
try:
    driver.get("https://opening.spotify.com/")
    d=driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div[2]/nav/div[1]/ul/li[2]/a")
    d.click()
except WebDriverException:
    print("Please Check The Web Address")
    time.sleep(3)
print("Test OK")