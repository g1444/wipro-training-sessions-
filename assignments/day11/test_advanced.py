def test_browser_option(browser):
    print("Browser Selected:", browser)
    assert browser in ["chrome", "firefox"]
