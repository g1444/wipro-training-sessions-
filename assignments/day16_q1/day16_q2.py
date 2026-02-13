from selenium import webdriver
import time as t

driver=webdriver.Chrome()
driver.get("https://example.com")
print("page 1 title: ",driver.title)

t.sleep(2)
driver.get("https://example.com/#more")
print("page 2 title: ",driver.title)

t.sleep(2)
driver.back()
print("after back title: ",driver.title)

t.sleep(2)
driver.forward()
print("after forward title: ",driver.title)

t.sleep(2)
driver.refresh()
print("after refresh title: ",driver.title)

t.sleep(2)

driver.quit()
print("browser is closed")