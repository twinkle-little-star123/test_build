import pytest
from selenium.webdriver.common.by import By
import time


def test_login(brower, logindata):
    driver = brower
    par = logindata
    url = par[0]
    user = par[1]
    passwd = par[2]

    driver.get(url)
    time.sleep(5)
    #userEle = driver.find_element(By.ID, "form_item_username")
    userEle = driver.find_element(By.CSS_SELECTOR, f'[id="form_item_username"]')
    userEle.send_keys(user)
    print(userEle.get_attribute('value'))
    passwdEle = driver.find_element(By.ID, "form_item_password")
    passwdEle.send_keys(passwd)

    time.sleep(5)

    driver.find_element(By.XPATH, "//span[text()='登 录']").click()
    #driver.find_element(By.CSS_SELECTOR, "#rc-tabs-1-panel-login > div > button").click()
    time.sleep(5)
    a = driver.find_element(By.XPATH, "//span[text()='点击选择入口类型']")


    assert a.is_displayed() is True

    a.clear()
