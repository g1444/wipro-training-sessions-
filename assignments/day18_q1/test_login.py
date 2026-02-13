from selenium import webdriver
from login_page import LoginPage

def test_login():
    driver=webdriver.Chrome()
    driver.get("file:///G:/codes/wipro training/assignments/day18_q1/login.html")


    lp=LoginPage(driver)
    lp.login("admin",'1234')

    assert 'Login Successful' in lp.get_text(lp.result)
    print("test passed")

    driver.quit