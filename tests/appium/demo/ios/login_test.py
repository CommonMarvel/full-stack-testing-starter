from time import sleep

from appium import webdriver


def test_login():
    app = ("/Users/yfr/Library/Developer/Xcode/DerivedData/poc-grsjwodlglibhwdlyihjfcpffevz/Build/Products/Stage-iphonesimulator/poc.app")
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723/wd/hub',
        desired_capabilities={
            'app': app,
            'platformName': 'iOS',
            'platformVersion': '13.3',
            'deviceName': 'iPhone 11 Pro Max',
            'autoAcceptAlerts': True,
        }
    )

    sleep(3)
    profile_tab = driver.find_element_by_name("个人")
    profile_tab.click()
    login_text = driver.find_element_by_name("点击登录")
    login_text.click()
    phone_text = driver.find_element_by_accessibility_id("phone_txt")
    phone_text.send_keys("13712345678")
    verify_text = driver.find_element_by_accessibility_id("verify_txt")
    verify_text.send_keys("068735")
    submit_text = driver.find_element_by_name("登录")
    submit_text.click()
    landing_tab = driver.find_element_by_name("首页")
    landing_tab.click()
    profile_tab.click()
    assert driver.find_element_by_name("个人资料").is_displayed() == True
