# (a) Key Press:
# --------------
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Edge()
driver.get("https://timesofindia.indiatimes.com/india")
time.sleep(3)
print(driver.title)
'''s=driver.find_element(By.XPATH, "/html/body/div[9]/div/div/div/div[1]")
s.click()
time.sleep(5)'''
time.sleep(3)
search=driver.find_element(By.CLASS_NAME, "OG1TB")
search.click()
time.sleep(3)
text=driver.find_element(By.NAME, "query")
text.send_keys("todays' share market value")
text.send_keys(Keys.ENTER)
print(driver.title)
time.sleep(10)
print("Test is Ok")