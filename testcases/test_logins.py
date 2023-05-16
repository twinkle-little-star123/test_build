import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from openpyxl.worksheet.worksheet import Worksheet
from openpyxl import load_workbook


def get_logins():
    wb = load_workbook("d://study/pythonProject/testcases/data.xlsx")
    ws: Worksheet = wb['logins']
    logins = []
    print(ws.values)
    for row in ws.values:
        # print(row)
        if row[0] != "url":
            logins.append(row)
    return logins


@pytest.mark.parametrize('url,user,passwd,msg', get_logins())
def test_logins(brower, url, user, passwd, msg):
    driver = brower
    print(get_logins())

    print(url, user, passwd, msg)

    driver.get(url)
    time.sleep(5)
    userEle = driver.find_element(By.ID, "form_item_username")
    if user is not None:
        userEle.send_keys(user)
    passwdEle = driver.find_element(By.ID, "form_item_password")
    if passwd is not None:
        passwdEle.send_keys(passwd)



    time.sleep(5)

    driver.find_element(By.XPATH, "//span[text()='登 录']").click()
    time.sleep(5)
    # m = driver.find_element(By.XPATH,"//html/body/div[3]/div/div/div/div/div/span[2]")
    # ActionChains(driver).move_to_element(m).perform()#鼠标悬停
    # msg1 = m.text
    # assert msg == msg1

    #m = driver.find_element(By.XPATH,"//*[text()='"+msg+"']")

    assert driver.page_source.__contains__(msg) is not None


