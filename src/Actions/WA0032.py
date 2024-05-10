# (a) Drag &Drop:
# ---------------
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
dri=webdriver.Edge()
dri.get("https://demoqa.com/droppable/")
dri.maximize_window()
time.sleep(5)
d=dri.find_element(By.ID, "draggable")
d1=dri.find_element(By.ID, "droppable")
action = ActionChains(dri)
action.drag_and_drop(d, d1).perform()
time.sleep(5)
print("Test ok")