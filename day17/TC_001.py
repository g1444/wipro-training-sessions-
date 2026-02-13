from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t

driver=webdriver.Chrome()
driver.get("https://www.amazon.in")
t.sleep(5)
links=driver.find_elements(By.TAG_NAME,'a')
t.sleep(2)
for link in links:
    url=link.get_attribute("href")
    text=link.text.strip()
    print(text)
driver.quit()