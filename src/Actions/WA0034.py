# (b) Right Click:
# ----------------
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
driver=webdriver.Edge()
driver.get("https://www.softwaretestingmaterial.com/sample-webpage-to-automate/")
time.sleep(3)
r=driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/main/div/article/div/div[1]/form/p[10]/a[1]")
time.sleep(3)
action=ActionChains(driver)
action.context_click(r).perform()
print("Test Ok")