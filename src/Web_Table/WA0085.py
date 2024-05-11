# b) printing the length:
# -----------------------
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Edge()
driver.get("https://www.amazon.in/")
driver.maximize_window()
time.sleep(3)
table = driver.find_element(By.CLASS_NAME,"navFooterMoreOnAmazon")
print(table.text)
time.sleep(3)
r = driver.find_elements(By.XPATH,'//*[@id="navFooter"]/div[5]/table/tbody/tr')
print(len(r))
time.sleep(3)
c = driver.find_elements(By.XPATH,'//*[@id="navFooter"]/div[5]/table/tbody/tr[1]/td')
print(len(c))
time.sleep(10)
print("test ok")