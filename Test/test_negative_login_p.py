
import pytest
from selenium.webdriver.common.by import By
from page_object.login_page import loginPage

@pytest.mark.login
@pytest.mark.negative
@pytest.mark.parametrize("username,password,expected_error",
                        [("adminxyz","admin123","Invalid Credentials"),
                         ("admin","admin234","Invalid Credentials")])
                   #      ("abc","abc123","Invalid Credentials")])
def test_invalid_username_login_p(driver,username,password,expected_error):
    login_page = loginPage(driver)
    login_page.open()
    login_page.perform_login(username,password)
    assert login_page.current_url == 'https://login-app-iota.vercel.app/login', 'URL should not change '
    assert login_page.is_error_message_displayed, "Invalid credential is not displayed"
    assert login_page.error_message_text == expected_error, ' Validation for invalid username is not matching'
