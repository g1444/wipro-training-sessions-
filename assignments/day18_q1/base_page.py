class BasePage:

    def __init__(self,driver):
        self.driver=driver
    
    def click(self,locator):
        self.driver.find_element(*locator).click()
    
    def enter_input(self,locator,text):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys()
    
    def get_text(self,locator):
        return self.driver.find_element(*locator).text