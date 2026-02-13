from selenium import webdriver
from selenium.webdriver.common.by import By

import time as t

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_input_text")
iframe=driver.find_element(By.TAG_NAME,"iframe")
t.sleep(2)
driver.switch_to.frame(iframe)
t.sleep(2)
editor=driver.find_element(By.NAME,"fname")
editor.clear()
editor.send_keys("hello everyone")
t.sleep(2)

driver.switch_to.default_content()

driver.execute_script("window.open('https://www.w3schools.com/js/js_popup.asp','_blank');")
windows=driver.window_handles
parent_window=windows[0]
child_window=windows[1]
driver.switch_to.window(parent_window)
print("Parent window title:",driver.title)
driver.switch_to.window(child_window)
print("child window title :",driver.title)
t.sleep(2)

driver.close()
driver.switch_to.window(parent_window)
print("returned to parent window")
driver.quit()