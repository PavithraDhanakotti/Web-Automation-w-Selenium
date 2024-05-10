# (a) ID:
# -------

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://www.amazon.in/?&ext_vrnc=hi&tag=googhydrabk1-21&ref=pd_sl_7hz2t19t5c_e&adgrpid=58355126069&hvpone=&hvptwo=&hvadid=486458755421&hvpos=&hvnetw=g&hvrand=12499410799333791113&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9303072&hvtargid=kwd-10573980&hydadcr=14453_2154373")
time.sleep(5)
a=driver.find_element(By.ID,"twotabsearchtextbox").send_keys("Mobiles"+Keys.RETURN)
time.sleep(5)
print("Test  is Ok!")