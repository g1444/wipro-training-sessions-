
from selenium.webdriver.common.by import By
class login_page:
    def __init__(self,driver):
        self.driver=driver
    username=(By.NAME,"username")
    password=(By.NAME,"password")
    login_btn=(By.XPATH,"//button[@type='submit']")
    
    def enter_username(self,user):
        self.driver.find_element(*self.username).send_keys(user)

    def enter_password(self,password):
        self.driver.find_element(*self.password).send_keys(password)

    def clicklogin(self):
        self.driver.find_element(*self.login_btn).click()