import time

import pytest

from page_objects.contact_page import contactPage
from page_objects.dashboard_page import DashboardPage
from page_objects.login_page import loginPage


@pytest.mark.login
@pytest.mark.positive3
@pytest.mark.parametrize("username,password",
                         [("admin", "admin123")])

# login page open and perform login
def test_dashboard_menu_p(driver,username,password):
    login_page = loginPage(driver)
    login_page.open()
    login_page.perform_login(username, password)

# create a dashboard page object and verify dashboard url
    dashboard_page = DashboardPage(driver)
    assert dashboard_page.current_url == 'https://login-app-iota.vercel.app/dashboard', 'Default URL should be Dashboard URL'

# verify title of contact page
    assert dashboard_page.get_contact_title()=="Contact List","DASHBOARD HOME page title is not matching"


# verify the added contact is displayed in the Contact List
    assert dashboard_page.get_home_page_contact_list_name()=="Ivo Costa","Contact name does not match as mentioned in Home page Contact List"
    assert dashboard_page.get_home_page_contact_list_email()=="ivo.costa@creativecapsule.com", "Email address does not match as mentioned in Home page Contact List"
    assert dashboard_page.get_home_page_contact_list_phone()=="9523100223","phone number does not match as mentioned in Home page Contact List"
    assert dashboard_page.get_home_page_contact_list_address()=="Goa, DDD (If you know, you know!!!)","address does not match as mentioned in Home page Contact List"

# verify logout click
    dashboard_page.perform_logout()

# verify the user is on Login page after logout
    assert dashboard_page.current_url =='https://login-app-iota.vercel.app/login','Login page is not displayed'
    driver.quit()