# (i) Other Web Elements:
# -----------------------
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Edge()
driver.get("https://www.softwaretestingmaterial.com/sample-webpage-to-automate/")
driver.maximize_window()
t = driver.find_element(By.CLASS_NAME, "spTextField")
t.send_keys("Pavithra")
y = driver.find_element(By.NAME, "password").send_keys("pavi123")
u = driver.find_element(By.TAG_NAME, "textarea").send_keys("Welcome to automation testing")
driver.implicitly_wait(5)
i = driver.find_element(By.NAME, "checkboxes[]")
driver.execute_script("arguments[0].scrollIntoView();", i)
driver.execute_script("arguments[0].click();", i)
driver.implicitly_wait(3)
o = driver.find_element(By.NAME, "checkboxes[]")
driver.execute_script("arguments[0].scrollIntoView();", o)
driver.execute_script("arguments[0].click();", o)
driver.implicitly_wait(3)
p=driver.find_element(By.XPATH,'//*[@id="post-1688"]/div/div[1]/form/p[5]/input[1]')
driver.execute_script("arguments[0].scrollIntoView();", o)
driver.execute_script("arguments[0].click();", p)
driver.implicitly_wait(3)
a = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/div/article/div/div[1]/form/p[5]/input[3]")
driver.execute_script("arguments[0].scrollIntoView();", o)
driver.execute_script("arguments[0].click();", a)
driver.implicitly_wait(3)
time.sleep(20)