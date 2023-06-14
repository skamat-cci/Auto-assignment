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
def test_contact_menu_p(driver,username,password):
    login_page = loginPage(driver)
    login_page.open()
    login_page.perform_login(username, password)

# create a dashboard page object and verify dashboard url
    dashboard_page = DashboardPage(driver)
    assert dashboard_page.current_url == 'https://login-app-iota.vercel.app/dashboard', 'Default URL should be Dashboard URL'

# create a Contact page object and locate Contact menu and click on Contact menu
    contact_page = contactPage(driver)
    contact_page.perform_contact_menu_click()

# verify the contact url
    assert contact_page.current_url=="https://login-app-iota.vercel.app/contact","Contact url should be displayed for contact menu click"

# verify title of contact page
    assert contact_page.get_contact_page_title() =="ADD CONTACTS","Contact page title is not matching"

# verify the existing contact list below Add contact title and Add contact icon
    assert contact_page.get_existing_contact_list_name() == "Ivo Costa", "Contact name added does not match as mentioned in Contact List"
    assert contact_page.get_existing_contact_list_email() == "ivo.costa@creativecapsule.com", "Email address added does not match as mentioned in Contact List"
    assert contact_page.get_existing_contact_list_phone() == "9523100223", "phone number added does not match as mentioned in Contact List"
    assert contact_page.get_existing_contact_list_address() == "Goa, DDD (If you know, you know!!!)", "address added does not match as mentioned in Contact List"

# add contact icon click
    contact_page.perfrom_add_contact_icon_click()

# adding a contact
    contact_page.perform_add_first_name()
    contact_page.perform_add_last_name()
    contact_page.perform_add_email_address()
    contact_page.perform_add_phone_number()
    contact_page.perform_add_address()
    contact_page.perform_submit_contact_button_click()

# verify the added contact is displayed in the Contact List
    assert contact_page.get_added_contact_list_name()=="Ashley Fernandes","Contact name added does not match as mentioned in Contact List"
    assert contact_page.get_added_contact_list_email() =="ashley.fernandes@aol.com", "Email address added does not match as mentioned in Contact List"
    assert contact_page.get_added_contact_list_phone() =="9989980001","phone number added does not match as mentioned in Contact List"
    assert contact_page.get_added_contact_list_address() == "FLAT-001, OLIVE GARDEN, OVERLAND PARK, KANSAS-66102","address added does not match as mentioned in Contact List"

# add contact icon click from Contact page to verify the negative condition
    contact_page.perfrom_add_contact_icon_click()

# verify empty first name field
    assert contact_page.perform_empty_first_name_check() =="Please fill out this field.","Empty First name validation is not matching "
    assert contact_page.perform_empty_last_name_check()  =="Please fill out this field.","Empty Last name validation is not matching "
    assert contact_page.perform_invalid_email_id_check() =="Please include an '@' in the email address. 'shanti' is missing an '@'.", "Validation for invalid email id is not matching"
    assert contact_page.perform_incomplete_email_id_check() =="Please enter a part following '@'. 'nikita@' is incomplete.","Incomplete email id validation is not matching"

# verify logout click
    contact_page.perform_contact_logout()

# verify the user is on Login page after logout
    assert contact_page.current_url  =='https://login-app-iota.vercel.app/login','Login page is not displayed'
    driver.quit()