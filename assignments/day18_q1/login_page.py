from selenium.webdriver.common.by import By
from base_page import BasePage


class LoginPage(BasePage):
    username=(By.ID,"username")
    password=(By.ID,"password")
    loginbtn=(By.ID,"loginBtn")
    result=(By.ID,"result")

    def login(self,user,pwd):
        self.enter_input(self.username,user)
        self.enter_input(self.password,pwd)
        self.click(self.loginbtn)