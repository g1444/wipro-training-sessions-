from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t
driver=webdriver.Chrome()
driver.get("http://127.0.0.1:5500/alert.html")
t.sleep(5)

driver.find_element(By.ID,'alertBtn').click()
pop=driver.switch_to.alert
print(pop.text)
pop.accept()
result=driver.find_element(By.ID,"result").text
print(result)
t.sleep(5)
driver.find_element(By.ID,'confirmBtn').click()
alert=driver.switch_to.alert
print(pop.text)
alert.accept()
t.sleep(5)
result=driver.find_element(By.ID,"result").text
print(result)

driver.find_element(By.ID,'promptBtn').click()
alert=driver.switch_to.alert
alert.send_keys("gowtham")
alert.accept()
result=driver.find_element(By.ID,"result").text
print(result)

driver.quit()
