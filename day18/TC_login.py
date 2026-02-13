from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t
from loginpage import login_page
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions
driver=webdriver.Chrome()
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
driver.implicitly_wait(10)
loginobj=login_page(driver)

loginobj.enter_username("Admin")

loginobj.enter_password("admin123")
t.sleep(5)
loginobj.clicklogin()
t.sleep(5)