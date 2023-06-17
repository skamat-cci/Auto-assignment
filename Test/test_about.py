
import pytest

from page_object.about_page import AboutPage
from page_object.dashboard_page import DashboardPage
from page_object.login_page import loginPage


@pytest.mark.login
@pytest.mark.positive_about
@pytest.mark.parametrize("username,password",
                         [("admin", "admin123")])

# login page open and perform login
def test_about_menu_p(driver,username,password):
    login_page = loginPage(driver)
    login_page.open()
    login_page.perform_login(username, password)

# verifying url of dashboard page to ensure user is on dashboard page
    dashboard_page = DashboardPage(driver)
    assert dashboard_page.current_url == 'https://login-app-iota.vercel.app/dashboard', 'Default URL should be Dashboard URL'

# about menu click
    about_page =AboutPage(driver)
    about_page.perform_about_menu_click()

# about url verified to ensure user is on about page
    assert about_page.current_url =='https://login-app-iota.vercel.app/about', 'About URL is not matching'

# About page title verified
    assert about_page.get_about_page_title() == 'Welcome to Selenium Learning Group', "About page title does not match 'Welcome to Selenium Learning Group'"

# About page click the logout
    about_page.perform_about_logout()

# verify the user is on Login page after logout
    assert about_page.current_url  =='https://login-app-iota.vercel.app/login','Login page is not displayed'
    driver.quit()


