from appium import webdriver
from selenium.common.exceptions import *

desired_caps = {}
desired_caps['automationName'] = 'Appium'
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9.0'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['app'] = 'https://s3-ap-northeast-1.amazonaws.com/dl-mobile/android/release/276_1.9.0_2R/debug.apk'
desired_caps['noReset'] = False
desired_caps['autoGrantPermissions'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


def test_guest_login():
    driver.implicitly_wait(15)
    try:
        driver.find_element_by_id('net.fun.ns:id/btnAccept').click()
    except NoSuchElementException:
        pass
    driver.implicitly_wait(5)
    try:
        driver.find_element_by_id('android:id/ok').click()
    except NoSuchElementException:
        pass
    driver.implicitly_wait(5)
    assert driver.find_element_by_accessibility_id('首页') and driver.find_element_by_accessibility_id('热门')


def test_user_login():
    driver.implicitly_wait(15)
    driver.find_element_by_accessibility_id('个人').click()
    driver.implicitly_wait(5)
    driver.find_element_by_id('net.fun.ns:id/tvUserName').click()
    driver.implicitly_wait(5)
    driver.find_element_by_id('net.fun.ns:id/etPhoneNumber').send_keys('1371')
    driver.find_element_by_id('net.fun.ns:id/etVerificationCode').send_keys('735')
    driver.find_element_by_id('net.fun.ns:id/btnNext').click()

    assert driver.find_element_by_id('net.fun.ns:id/vgEditProfile')
