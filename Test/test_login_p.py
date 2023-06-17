
#import pytest
#from page_objects.dashboard_page import DashboardPage
#from page_objects.login_page import loginPage

import pytest
from page_object.dashboard_page import DashboardPage
from page_object.login_page import loginPage

@pytest.mark.login
@pytest.mark.positive1
@pytest.mark.parametrize("username,password",
                         [("admin", "admin123")])

def test_valid_user_login_p(driver,username,password):
    login_page = loginPage(driver)
    login_page.open()
    login_page.perform_login(username, password)
    assert login_page.current_url == 'https://login-app-iota.vercel.app/dashboard', 'Default URL should be Dashboard URL'

    driver.quit()

@pytest.mark.login
@pytest.mark.positive
@pytest.mark.parametrize("username,password",
                         [("admin", "admin123")])
def test_valid_user_login_logout_p(driver, username, password):

    login_page = loginPage(driver)
    login_page.open()
    login_page.perform_login(username, password)

    dashboard_page = DashboardPage(driver)
    assert dashboard_page.current_url == 'https://login-app-iota.vercel.app/dashboard', 'Default URL should be Dashboard URL'
    assert dashboard_page.get_contact_title() == "Contact List","Title does not match'Contact List'"

    dashboard_page.perform_logout()
    assert login_page.current_url == 'https://login-app-iota.vercel.app/login', 'Login page is not displayed after logout'

    driver.quit()