# (b) TEXT:
# ---------

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.indiaonlinepages.com/articles/national-leaders-of-india/")
time.sleep(4)
t=(driver.find_element(By.CLASS_NAME, "wp-block-heading").text)
t1=(driver.find_element(By.XPATH, "/html/body/div[1]/div/div/main/article/div/p[2]").text)
print(t)
print(t1)