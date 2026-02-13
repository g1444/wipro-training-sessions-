from selenium import webdriver
import time as t

driver=webdriver.Chrome()

driver.get("https://amazon.in")
# alert=driver.execute_script("alert('hello amazon')")
t.sleep(5)
# alert=driver.switch_to.alert
# alert.accept()
driver.execute_script("window,scrollBy(0,900)")
t.sleep(5)
# driver.execute_script("window,scrollTo(0,document.body.scrollHeight)")