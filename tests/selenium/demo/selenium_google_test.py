from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Test 3A (arrange, act, assert)
@pytest.mark.parametrize("env", ["dev"])
def test_selenium_google(setup_function, env):
    # get config from setup function (arrange)
    config = setup_function
    timeout = config["demo"][env]["selenium"]["timeout"]

    # setting browser (arrange)
    executable_path = "./drivers/geckodriver_mac_greater_60"

    options = webdriver.FirefoxOptions()
    options.headless = True
    options.add_argument("--disable-gpu")

    browser = webdriver.Firefox(executable_path=executable_path, options=options)
    browser.implicitly_wait(timeout)

    # operate browser (act)
    browser.get(config["demo"][env]["selenium"]["host"])

    WebDriverWait(browser, timeout, 2).until(EC.visibility_of(browser.find_element_by_css_selector("input[name='q']")))
    search_txt = browser.find_element_by_css_selector("input[name='q']")
    sleep(1)
    search_txt.send_keys("selenium")
    sleep(1)
    search_txt.submit()

    # get result (act)
    WebDriverWait(browser, timeout, 2).until(EC.visibility_of(browser.find_element_by_css_selector("input[name='q']")))
    search_txt = browser.find_element_by_css_selector("input[name='q']")

    # assert
    assert search_txt.get_attribute("value") == "selenium"

    browser.quit()
