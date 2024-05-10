# (a) CLEAR:
# ----------

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://www.amazon.in/?&ext_vrnc=hi&tag=googhydrabk1-21&ref=pd_sl_7hz2t19t5c_e&adgrpid=58355126069&hvpone=&hvptwo=&hvadid=486458755421&hvpos=&hvnetw=g&hvrand=12499410799333791113&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9303072&hvtargid=kwd-10573980&hydadcr=14453_2154373")
driver.maximize_window()
time.sleep(3)
c=driver.find_element(By.CSS_SELECTOR, ".nav-input").send_keys("Organizer item")
time.sleep(3)
c1=driver.find_element(By.ID,"twotabsearchtextbox").clear()
time.sleep(3)
c2=driver.find_element(By.CLASS_NAME, "nav-input").send_keys("Kitchen Organizer")
time.sleep(3)
c3=driver.find_element(By.CLASS_NAME, "nav-input").clear()
time.sleep(3)
c4=driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input").send_keys("Makeup for oily skin"+Keys.RETURN)
time.sleep(10)
print("Test is OK")