from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
driver=webdriver.Chrome()
driver.get("https://tutorialsninja.com/demo/")

driver.find_element(By.LINK_TEXT,"Desktops").click()
driver.find_element(By.LINK_TEXT,"Mac (1)").click()
drop_down=Select(driver.find_element(By.ID,"input-sort"))
options=drop_down.options
for option in options:
    print(option.text)
drop_down.select_by_index(4)