from selenium.webdriver.common.by import By
from dummy.dummy_data.dummy import base_data, obj_loct


def test_R1_Register_with_valid_data(browser):
    browser.get(base_data.URL + '/register')
    browser.find_element(*obj_loct.rbg_male).click()
    browser.find_element(*obj_loct.inpt_frstname).send_keys(base_data.firstname)
    browser.find_element(*obj_loct.inpt_lstname).send_keys(base_data.lastname)
    browser.find_element(*obj_loct.inpt_email).send_keys(base_data.new_email)
    browser.find_element(*obj_loct.inpt_pw).send_keys(base_data.password)
    browser.find_element(*obj_loct.inpt_cnfrmpw).send_keys(base_data.confirm_password)
    browser.find_element(*obj_loct.btn_regist).click()
    get_url = browser.current_url
    assert '/registerresult/1' in get_url


def test_R2_Register_with_empty_username(browser):
    browser.get(base_data.URL + '/register')
    browser.find_element(*obj_loct.rbg_male).click()
    browser.find_element(*obj_loct.inpt_lstname).send_keys(base_data.lastname)
    browser.find_element(*obj_loct.inpt_email).send_keys(base_data.email)
    browser.find_element(*obj_loct.inpt_pw).send_keys(base_data.password)
    browser.find_element(*obj_loct.inpt_cnfrmpw).send_keys(base_data.confirm_password)
    browser.find_element(*obj_loct.btn_regist).click()
    err_msg = browser.find_element(By.CSS_SELECTOR, "span.field-validation-error[data-valmsg-for='FirstName'] > span").text
    assert "First name is required" in err_msg


def test_R3_Register_with_empty_lastname(browser):
    browser.get(base_data.URL + '/register')
    browser.find_element(*obj_loct.rbg_male).click()
    browser.find_element(*obj_loct.inpt_frstname).send_keys(base_data.firstname)
    browser.find_element(*obj_loct.inpt_email).send_keys(base_data.email)
    browser.find_element(*obj_loct.inpt_pw).send_keys(base_data.password)
    browser.find_element(*obj_loct.inpt_cnfrmpw).send_keys(base_data.confirm_password)
    browser.find_element(*obj_loct.btn_regist).click()
    err_msg = browser.find_element(By.CSS_SELECTOR, "span.field-validation-error[data-valmsg-for='LastName'] > span").text
    assert "Last name is required" in err_msg


def test_R4_Register_with_invalid_email_format(browser):
    browser.get(base_data.URL + '/register')
    invalid = base_data.email
    invl_email = invalid[:len(invalid) - 8]
    browser.find_element(*obj_loct.rbg_male).click()
    browser.find_element(*obj_loct.inpt_frstname).send_keys(base_data.firstname)
    browser.find_element(*obj_loct.inpt_lstname).send_keys(base_data.lastname)
    browser.find_element(*obj_loct.inpt_email).send_keys(invl_email)
    browser.find_element(*obj_loct.inpt_pw).send_keys(base_data.password)
    browser.find_element(*obj_loct.inpt_cnfrmpw).send_keys(base_data.confirm_password)
    browser.find_element(*obj_loct.btn_regist).click()
    err_msg = browser.find_element(By.CSS_SELECTOR, "span.field-validation-error[data-valmsg-for='Email'] > span").text
    assert "Wrong email" in err_msg


def test_R5_Register_with_empty_email(browser):
    browser.get(base_data.URL + '/register')
    browser.find_element(*obj_loct.rbg_male).click()
    browser.find_element(*obj_loct.inpt_frstname).send_keys(base_data.firstname)
    browser.find_element(*obj_loct.inpt_lstname).send_keys(base_data.lastname)
    browser.find_element(*obj_loct.inpt_pw).send_keys(base_data.password)
    browser.find_element(*obj_loct.inpt_cnfrmpw).send_keys(base_data.confirm_password)
    browser.find_element(*obj_loct.btn_regist).click()
    err_msg = browser.find_element(By.CSS_SELECTOR, "span.field-validation-error[data-valmsg-for='Email'] > span").text
    assert "Email is required" in err_msg


def test_R6_Register_with_empty_password(browser):
    browser.get(base_data.URL + '/register')
    browser.find_element(*obj_loct.rbg_male).click()
    browser.find_element(*obj_loct.inpt_frstname).send_keys(base_data.firstname)
    browser.find_element(*obj_loct.inpt_lstname).send_keys(base_data.lastname)
    browser.find_element(*obj_loct.inpt_email).send_keys(base_data.email)
    browser.find_element(*obj_loct.inpt_cnfrmpw).send_keys(base_data.confirm_password)
    browser.find_element(*obj_loct.btn_regist).click()
    err_msg1 = browser.find_element(By.CSS_SELECTOR, "span.field-validation-error[data-valmsg-for='Password'] > span").text
    err_msg2 = browser.find_element(By.CSS_SELECTOR, "span.field-validation-error[data-valmsg-for='ConfirmPassword'] > span").text
    assert "Password is required" in err_msg1
    assert "The password and confirmation password do not match" in err_msg2


def test_R7_Register_with_empty_confirmpassword(browser):
    browser.get(base_data.URL + '/register')
    browser.find_element(*obj_loct.rbg_male).click()
    browser.find_element(*obj_loct.inpt_frstname).send_keys(base_data.firstname)
    browser.find_element(*obj_loct.inpt_lstname).send_keys(base_data.lastname)
    browser.find_element(*obj_loct.inpt_email).send_keys(base_data.email)
    browser.find_element(*obj_loct.inpt_pw).send_keys(base_data.password)
    browser.find_element(*obj_loct.btn_regist).click()
    err_msg = browser.find_element(By.CSS_SELECTOR, "span.field-validation-error[data-valmsg-for='ConfirmPassword'] > span").text
    assert "Password is required" in err_msg


def test_R8_Register_with_empty_unmatch_password_n_confirmpassword(browser):
    browser.get(base_data.URL + '/register')
    invalid = base_data.confirm_password
    invld_pw = invalid[:len(invalid) - 1]
    browser.find_element(*obj_loct.rbg_male).click()
    browser.find_element(*obj_loct.inpt_frstname).send_keys(base_data.firstname)
    browser.find_element(*obj_loct.inpt_lstname).send_keys(base_data.lastname)
    browser.find_element(*obj_loct.inpt_email).send_keys(base_data.email)
    browser.find_element(*obj_loct.inpt_pw).send_keys(base_data.password)
    browser.find_element(*obj_loct.inpt_cnfrmpw).send_keys(invld_pw)
    browser.find_element(*obj_loct.btn_regist).click()
    err_msg = browser.find_element(By.CSS_SELECTOR, "span.field-validation-error[data-valmsg-for='ConfirmPassword'] > span").text
    assert "The password and confirmation password do not match" in err_msg


def test_R9_with_none_input_form(browser):
    browser.get(base_data.URL + '/register')
    browser.find_element(*obj_loct.btn_regist).click()
    err_msg1 = browser.find_element(By.CSS_SELECTOR, "span.field-validation-error[data-valmsg-for='FirstName'] > span").text
    err_msg2 = browser.find_element(By.CSS_SELECTOR, "span.field-validation-error[data-valmsg-for='LastName'] > span").text
    err_msg3 = browser.find_element(By.CSS_SELECTOR, "span.field-validation-error[data-valmsg-for='Email'] > span").text
    err_msg4 = browser.find_element(By.CSS_SELECTOR, "span.field-validation-error[data-valmsg-for='Password'] > span").text
    err_msg5 = browser.find_element(By.CSS_SELECTOR, "span.field-validation-error[data-valmsg-for='ConfirmPassword'] > span").text
    assert "First name is required" in err_msg1
    assert "Last name is required" in err_msg2
    assert "Email is required" in err_msg3
    assert "Password is required" in err_msg4
    assert "Password is required" in err_msg5