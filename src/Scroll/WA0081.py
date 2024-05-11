# e) Multiple Scroll:
# -------------------
import time
from selenium import webdriver
driver=webdriver.Edge()
driver.get("https://www.themultiversesummit.xyz/?ref=onepagelove")
time.sleep(3)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(5)
driver.execute_script("scrollTo(0,890)")
time.sleep(5)
driver.execute_script("scrollTo(890,0)")
print("Test is Ok")