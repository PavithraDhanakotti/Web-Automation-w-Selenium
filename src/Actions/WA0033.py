# (a) Drag &Drop:
# ---------------
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
dri=webdriver.Edge()
dri.get("https://codepen.io/miclgael/pen/JqWJma")
dri.maximize_window()
time.sleep(5)
drag = dri.find_element(By.ID, "p1")
drop = dri.find_element(By.ID, "target")
action = ActionChains(dri)
action.drag_and_drop(drag,drop).perform()
time.sleep(5)
print("Test ok")
