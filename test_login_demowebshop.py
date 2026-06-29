from selenium.webdriver.common.by import By
from dummy.dummy_data.dummy import base_data, obj_loct


def test_L1_login_with_valid_email(browser):
    browser.get(base_data.URL + '/login')
    browser.find_element(*obj_loct.inpt_vld_email).send_keys(base_data.vld_email)
    browser.find_element(*obj_loct.inpt_vld_pass).send_keys(base_data.vld_pass)
    browser.find_element(*obj_loct.btn_login).click()
    get_url = browser.current_url
    assert get_url[:len(get_url) - 1] == base_data.URL


def test_L2_login_with_invalid_email_format(browser):
    browser.get(base_data.URL + '/login')
    invalid = base_data.vld_email
    invld_email = invalid[:len(invalid) - 4]
    browser.find_element(*obj_loct.inpt_vld_email).send_keys(invld_email)
    browser.find_element(*obj_loct.inpt_vld_pass).send_keys(base_data.vld_pass)
    browser.find_element(*obj_loct.btn_login).click()
    err_msg = browser.find_element(By.CLASS_NAME, "field-validation-error").text
    assert err_msg == "Please enter a valid email address."


def test_L3_login_with_empty_email(browser):
    browser.get(base_data.URL + '/login')
    browser.find_element(*obj_loct.inpt_vld_pass).send_keys(base_data.vld_pass)
    browser.find_element(*obj_loct.btn_login).click()
    err_msg = browser.find_element(By.CLASS_NAME, "validation-summary-errors").text
    assert "No customer account found" in err_msg


def test_L4_login_with_empty_password(browser):
    browser.get(base_data.URL + '/login')
    browser.find_element(*obj_loct.inpt_vld_email).send_keys(base_data.vld_email)
    browser.find_element(*obj_loct.btn_login).click()
    err_msg = browser.find_element(By.CLASS_NAME, "validation-summary-errors").text
    assert "The credentials provided are incorrect" in err_msg


def test_L5_login_with_invalid_password(browser):
    browser.get(base_data.URL + '/login')
    invalid = base_data.vld_pass
    invld_pass = invalid[:len(invalid) - 1]
    browser.find_element(*obj_loct.inpt_vld_email).send_keys(base_data.vld_email)
    browser.find_element(*obj_loct.inpt_vld_pass).send_keys(invld_pass)
    browser.find_element(*obj_loct.btn_login).click()
    err_msg = browser.find_element(By.CLASS_NAME, "validation-summary-errors").text
    assert "The credentials provided are incorrect" in err_msg