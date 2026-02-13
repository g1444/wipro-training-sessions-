from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/dynamic-properties")

driver.implicitly_wait(10)

try:
    explicit_wait = WebDriverWait(driver, 15)
    enable_btn = explicit_wait.until(
        EC.element_to_be_clickable((By.ID, "enableAfter"))
    )
    print("Explicit wait: element is clickable")
except TimeoutException:
    print("Explicit wait failed")

try:
    fluent_wait = WebDriverWait(driver,timeout=20,poll_frequency=1,ignored_exceptions=[NoSuchElementException])
    visible_btn = fluent_wait.until(
        EC.visibility_of_element_located((By.ID, "visibleAfter"))
    )
    print("Fluent wait: element is visible")
except TimeoutException:
    print("Fluent wait failed")

print("Element is available for interaction")

time.sleep(3)
driver.quit()
