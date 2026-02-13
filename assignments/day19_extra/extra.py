from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class DemoQAAutomation:

    def setup(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 10)

    def open_site(self):
        try:
            self.driver.get("https://demoqa.com/")
            header = self.wait.until(
                EC.visibility_of_element_located((By.TAG_NAME, "body"))
            )
            print("DemoQA Loaded")
        except TimeoutException as e:
            print("Page load failed:", e)

    def handle_frame(self):
        try:
            self.driver.get("https://demoqa.com/frames")

            self.wait.until(
                EC.frame_to_be_available_and_switch_to_it((By.ID, "frame1"))
            )

            text = self.wait.until(
                EC.visibility_of_element_located((By.TAG_NAME, "h1"))
            )

            print("Frame Text:", text.text)

            self.driver.switch_to.default_content()

        except (TimeoutException, NoSuchElementException) as e:
            print("Frame handling failed:", e)

    def handle_windows(self):
        try:
            self.driver.get("https://demoqa.com/browser-windows")

            parent = self.driver.current_window_handle

            self.wait.until(
                EC.element_to_be_clickable((By.ID, "tabButton"))
            ).click()

            self.wait.until(EC.number_of_windows_to_be(2))

            for handle in self.driver.window_handles:
                if handle != parent:
                    self.driver.switch_to.window(handle)
                    break

            text = self.wait.until(
                EC.visibility_of_element_located((By.ID, "sampleHeading"))
            )

            print("New Tab Text:", text.text)

            self.driver.close()
            self.driver.switch_to.window(parent)

        except (TimeoutException, NoSuchElementException) as e:
            print("Window handling failed:", e)

    def handle_alert(self):
        try:
            self.driver.get("https://demoqa.com/alerts")

            self.wait.until(
                EC.element_to_be_clickable((By.ID, "alertButton"))
            ).click()

            alert = self.wait.until(EC.alert_is_present())
            alert.accept()

            print("Alert Accepted")

        except TimeoutException as e:
            print("Alert handling failed:", e)

    def handle_elements(self):
        try:
            self.driver.get("https://demoqa.com/text-box")

            self.wait.until(
                EC.visibility_of_element_located((By.ID, "userName"))
            ).send_keys("Big Brother")

            self.driver.find_element(By.ID, "userEmail").send_keys("big@brother.com")
            self.driver.find_element(By.ID, "currentAddress").send_keys("Chennai")
            self.driver.find_element(By.ID, "permanentAddress").send_keys("Tamil Nadu")

            self.driver.find_element(By.ID, "submit").click()

            print("Text Box Submitted")

            self.driver.get("https://demoqa.com/checkbox")

            checkbox = self.wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "rct-checkbox"))
            )
            checkbox.click()

            print("Checkbox Selected")

        except (TimeoutException, NoSuchElementException) as e:
            print("Elements interaction failed:", e)

    def teardown(self):
        if hasattr(self, "driver") and self.driver is not None:
            self.driver.quit()


if __name__ == "__main__":
    test = DemoQAAutomation()
    test.setup()
    test.open_site()
    test.handle_frame()
    test.handle_windows()
    test.handle_alert()
    test.handle_elements()
    test.teardown()
