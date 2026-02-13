from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchWindowException, TimeoutException
import pytest
from driverfactory import get_driver

@pytest.mark.parametrize("browser", ["chrome", "edge"])
def test_google_search(browser):
    driver = get_driver(browser)

    try:
        driver.get("https://www.google.com")

        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("selenium grid")
        search_box.submit()

        WebDriverWait(driver, 10).until(
            EC.title_contains("selenium")
        )

        assert "selenium" in driver.title.lower()

    except (NoSuchWindowException, TimeoutException):
        pytest.skip(f"{browser} triggered Google verification page")


