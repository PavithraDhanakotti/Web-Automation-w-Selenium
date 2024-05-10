# (a) CLEAR:
# ----------
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()
time.sleep(3)
c=driver.find_element(By.CSS_SELECTOR, ".gLFyf").send_keys("Pictures")
time.sleep(3)
c1=driver.find_element(By.ID,"APjFqb").clear()
time.sleep(3)
c2=driver.find_element(By.NAME, "q").send_keys("NAture Picture")
time.sleep(3)
c3=driver.find_element(By.CLASS_NAME, "gLFyf").clear()
time.sleep(3)
c4=driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea").send_keys("Mountain River view pictures"+Keys.RETURN)
time.sleep(10)
print("Test is OK")