from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t
driver=webdriver.Chrome()
driver.get("https://letcode.in/window")
driver.find_element(By.ID,"multi").click()

windows=driver.window_handles
for child in windows:
    driver.switch_to.window(child)
    t.sleep(4)
    print("the title of the page:",driver.current_url)
driver.quit()