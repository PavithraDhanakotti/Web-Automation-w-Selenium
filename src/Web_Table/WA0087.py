# b) printing the length:
# -----------------------
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Edge()
driver.get("https://www.softwaretestingmaterial.com/sample-webpage-to-automate/#google_vignette")
driver.maximize_window()
time.sleep(3)
table = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/main/div/article/div/div[1]/form/table")
print(table.text)
time.sleep(3)
r = driver.find_elements(By.XPATH,'//*[@id="post-1688"]/div/div[1]/form/table/tbody/tr')
print(len(r))
time.sleep(3)
c = driver.find_elements(By.XPATH,'//*[@id="post-1688"]/div/div[1]/form/table/tbody/tr[2]/td')
print(len(c))
time.sleep(10)
print("test ok")