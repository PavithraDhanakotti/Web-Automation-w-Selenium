import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()
# CLASS NAME LOCATOR
CNL = driver.find_element(By.CLASS_NAME, "gLFyf")
CNL.send_keys("Youtube"+Keys.RETURN)
driver.implicitly_wait(5)
# CSS LOCATOR
CL = driver.find_element(By.CSS_SELECTOR, ".LC20lb")
CL.click()
driver.implicitly_wait(5)
# PARTIAL LINK TEXT LOCATOR
PT = driver.find_element(By.PARTIAL_LINK_TEXT, "Tren")
PT.click()
driver.implicitly_wait(5)
# TAG NAME, XPATH AND NAME LOCATOR
TANA = driver.find_element(By.TAG_NAME, "input")
TANA.click()
driver.implicitly_wait(5)
TAG = driver.find_element(By.NAME, "search_query")
TAG.send_keys("Harris Jayaraj Love Hits Tamil | Favourite | Harris Jayaraj Tamil Songs Collection | Jukebox Vol-01")
TAG.click()
driver.implicitly_wait(5)
BTN = driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/button/yt-icon")
BTN.click()
driver.implicitly_wait(5)
# LINK TEXT
CNL = driver.find_element(By.LINK_TEXT, "Harris Jayaraj Love Hits Tamil | Favourite | Harris Jayaraj Tamil Songs Collection | Jukebox Vol-01")
CNL.click()
driver.implicitly_wait(5)
# ID LOCATOR
Idl = driver.find_element(By.ID, "expand")
Idl.click()
time.sleep(20)