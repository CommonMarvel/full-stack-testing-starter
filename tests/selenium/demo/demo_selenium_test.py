import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.parametrize("env", ["dev"])
def test_selenium_login(setup_function, env):
    config = setup_function
    timeout = config["demo"][env]["timeout"]

    options = webdriver.FirefoxOptions()

    executable_path = "./drivers/geckodriver_mac_greater_60"

    options.headless = True
    options.add_argument("--disable-gpu")

    browser = webdriver.Firefox(executable_path=executable_path, options=options)
    browser.implicitly_wait(300)
    browser.get("http://www.google.com.tw")

    WebDriverWait(browser, timeout, 2).until(EC.visibility_of(browser.find_element_by_css_selector("input[name='q']")))
    search_txt = browser.find_element_by_css_selector("input[name='q']")
    search_txt.send_keys("selenium")
    search_txt.submit()

    WebDriverWait(browser, timeout, 2).until(EC.visibility_of(browser.find_element_by_css_selector("input[name='q']")))
    search_txt = browser.find_element_by_css_selector("input[name='q']")
    assert search_txt.get_attribute("value") == "selenium"

    browser.quit()
