from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

GRIDURL = "http://10.95.249.121:4444"



def get_driver(browser):
    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")

    elif browser == "edge":
        options = EdgeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")

    elif browser == "firefox":
        options = FirefoxOptions()
        options.set_preference("dom.webdriver.enabled", False)
        options.set_preference("useAutomationExtension", False)

    else:
        raise ValueError("Browser not supported")

    driver = webdriver.Remote(
        command_executor=GRIDURL,
        options=options
    )

    driver.maximize_window()
    return driver
