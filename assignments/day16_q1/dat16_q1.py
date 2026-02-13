from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time as t

options=Options()
options.add_argument("--disable-blink-features=AutomationControlled")
driver=webdriver.Chrome(options=options)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
t.sleep(5)
user_name=driver.find_element(By.NAME,"username")
user_name.send_keys("Admin")
pass_word=driver.find_element(By.CSS_SELECTOR,"input[name='password']")
pass_word.send_keys("admin12")
login_btn=driver.find_element(By.XPATH,"//button[@type='submit']")
t.sleep(2)
login_btn.click()

t.sleep(5)
error_message=driver.find_element(By.CLASS_NAME,"oxd-alert-content-text")

assert "Invalid credentials" in error_message.text
print("error message is validated")