from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t
from selenium.webdriver.support.ui import Select
driver=webdriver.Chrome()
driver.get("http://127.0.0.1:5500/selenium_form.html")
t.sleep(5)
user_name=driver.find_element(By.ID,"username")
user_name.send_keys("gowtham")
pass_word=driver.find_element(By.ID,'password')
pass_word.send_keys("12345678")
radio=driver.find_element(By.ID,"male").click()
skills=driver.find_element(By.ID,"python").click()
select=Select(driver.find_element(By.ID,"country"))
select.select_by_visible_text("India")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
t.sleep(2)
message=driver.find_element(By.ID,"message")
print(message.text)
t.sleep(6)
driver.quit()