from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")

wait = WebDriverWait(driver, 20)

# ✅ Wait for username field
wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")

# ✅ Wait for password field
wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("admin123")

# ✅ Click login
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

# ✅ Wait until URL contains dashboard
wait.until(EC.url_contains("dashboard"))

print("Login Successful ✅")
print("Current URL:", driver.current_url)

driver.quit()
