# (a) CLEAR:
# ----------

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")
driver.maximize_window()
time.sleep(3)
c=driver.find_element(By.TAG_NAME, "input").send_keys("Tamil Songs")
driver.implicitly_wait(3)
c1=driver.find_element(By.NAME, "search_query").clear()
driver.implicitly_wait(3)
c2=driver.find_element(By.NAME, "search_query").send_keys("Tamil Evergreen songs")
driver.implicitly_wait(3)
c3=driver.find_element(By.TAG_NAME, "input").clear()
driver.implicitly_wait(3)
c4=driver.find_element(By.XPATH,"/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input").send_keys("Tamil Love hits song"+Keys.RETURN)
time.sleep(10)
print("Test is OK")