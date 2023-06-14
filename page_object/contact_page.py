import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains

class contactPage:
    __contact_menu=(By.LINK_TEXT,"Contact")
    __contact_page_title =(By.XPATH,"/html//div[@id='root']//div[@role='button']/div[@class='text-uppercase']")
    __add_contact_icon =(By.CSS_SELECTOR,"div[role='button']>.fs-2.pointer-event")

    __first_name=(By.XPATH,"/html//input[@id='name_textbox']")
    __last_name=(By.XPATH,"/html//div[@id='root']/div[@class='App']//form/div[1]/div[2]/input[@id='name_textbox']")
    __email_address=(By.XPATH,"/html//input[@id='email_textbox']")
    __phone_number=(By.XPATH,"/html//input[@id='phone_textbox']")
    __address=(By.XPATH,"/html//textarea[@id='message_textbox']")
    __submit_contact_button=(By.XPATH,"/html//div[@id='root']/div[@class='App']//form//button[@type='submit']")

    __contact_list_name =(By.XPATH,"/html//div[@id='root']/div[@class='App']//table[@class='table']/tbody/tr[2]/td[.='Ashley Fernandes']")
    __contact_list_email =(By.XPATH,"/html//div[@id='root']/div[@class='App']//table[@class='table']//td[.='ashley.fernandes@aol.com']")
    __contact_list_phone =(By.XPATH,"/html//div[@id='root']/div[@class='App']//table[@class='table']//td[.='9989980001']")
    __contact_list_address =(By.XPATH,"/html//div[@id='root']/div[@class='App']//table[@class='table']//td[.='FLAT-001, OLIVE GARDEN, OVERLAND PARK, KANSAS-66102']")


    __first_name_negative=(By.ID,"name_textbox")
    __last_name_negative = (By.CSS_SELECTOR, "div:nth-of-type(2) > input#name_textbox")
    __email_address_negative = (By.ID, "email_textbox")

    __existing_name =(By.XPATH,"/html//div[@id='root']/div[@class='App']//table[@class='table']/tbody/tr[1]/td[.='Ivo Costa']")
    __existing_email =(By.XPATH,"/html//div[@id='root']/div[@class='App']//table[@class='table']//td[.='ivo.costa@creativecapsule.com']")
    __existing_phone_number =(By.XPATH,"/html//div[@id='root']/div[@class='App']//table[@class='table']//td[.='9523100223']")
    __existing_address =(By.CSS_SELECTOR,"tr:nth-of-type(1) > td:nth-of-type(4)")
    #__existing_address = (By.XPATH,"/html//div[@id='root']/div[@class='App']//table[@class='table']//td[.='Goa, DDD (If you know, you know!!!']")

    __contact_logout_button = (By.XPATH, "//div[@id='navbarSupportedContent']//a[@href='/login']")

    def __init__(self,driver:WebDriver):
        self._driver = driver
    @property
    def current_url(self):
        return (self._driver.current_url)
    def perform_contact_menu_click(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__contact_menu))
        contact_menu_field = self._driver.find_element(*self.__contact_menu)
        contact_menu_field.click()

    def get_contact_page_title(self):
        wait =WebDriverWait(self._driver,10)
        wait.until(ec.presence_of_element_located(self.__contact_page_title))
        contact_page_title_field=self._driver.find_element(*self.__contact_page_title)
        #print(contact_page_title_field.text)
        actual_contact_page_title_field = contact_page_title_field.text
        return actual_contact_page_title_field

    def get_existing_contact_list_name(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__existing_name))
        existing_contact_list_name_field = self._driver.find_element(*self.__existing_name)
        actual_existing_contact_list_name=existing_contact_list_name_field.text
        return (actual_existing_contact_list_name)

    def get_existing_contact_list_email(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__existing_email))
        existing_contact_list_email_field =self._driver.find_element(*self.__existing_email)
        actual_existing_contact_list_email = existing_contact_list_email_field.text
        return(actual_existing_contact_list_email)

    def get_existing_contact_list_phone(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__existing_phone_number))
        existing_contact_list_phone_field = self._driver.find_element(*self.__existing_phone_number)
        actual_existing_contact_list_phone = existing_contact_list_phone_field.text
        return (actual_existing_contact_list_phone)

    def get_existing_contact_list_address(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__existing_address))
        existing_contact_list_address_field =self._driver.find_element(*self.__existing_address)
        actual_existing_contact_list_address = existing_contact_list_address_field.text
        return actual_existing_contact_list_address

    def perfrom_add_contact_icon_click(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__add_contact_icon))
        add_contact_button_field = self._driver.find_element(*self.__add_contact_icon)
        add_contact_button_field.click()

    def perform_add_first_name(self):
        wait=WebDriverWait(self._driver,10)
        wait.until(ec.presence_of_element_located(self.__first_name))
        add_first_name_field=self._driver.find_element(*self.__first_name)
        add_first_name_field.send_keys("Ashley")

    def perform_add_last_name(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__last_name))
        add_last_name_field = self._driver.find_element(*self.__last_name)
        add_last_name_field.send_keys("Fernandes")

    def perform_add_email_address(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__email_address))
        add_email_address_field = self._driver.find_element(*self.__email_address)
        add_email_address_field.send_keys("ashley.fernandes@aol.com")

    def perform_add_phone_number(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__phone_number))
        add_phone_number_field = self._driver.find_element(*self.__phone_number)
        add_phone_number_field.send_keys("9989980001")

    def perform_add_address(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__address))
        add_address_field = self._driver.find_element(*self.__address)
        add_address_field.send_keys("FLAT-001, OLIVE GARDEN, OVERLAND PARK, KANSAS-66102")

    def perform_submit_contact_button_click(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__submit_contact_button))
        submit_contact_button_field = self._driver.find_element(*self.__submit_contact_button)
        submit_contact_button_field.click()

    def get_added_contact_list_name(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__contact_list_name))
        contact_list_name_field = self._driver.find_element(*self.__contact_list_name)
        actual_contact_list_name=contact_list_name_field.text
        return (actual_contact_list_name)

    def get_added_contact_list_email(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__contact_list_email))
        contact_list_email_field =self._driver.find_element(*self.__contact_list_email)
        actual_contact_list_email = contact_list_email_field.text
        return(actual_contact_list_email)

    def get_added_contact_list_phone(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__contact_list_phone))
        contact_list_phone_field = self._driver.find_element(*self.__contact_list_phone)
        actual_contact_list_phone = contact_list_phone_field.text
        return (actual_contact_list_phone)

    def get_added_contact_list_address(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__contact_list_address))
        contact_list_address_field =self._driver.find_element(*self.__contact_list_address)
        actual_contact_list_address = contact_list_address_field.text
        return actual_contact_list_address

    def perform_empty_first_name_check(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__first_name_negative))
        first_name_blank = self._driver.find_element(*self.__first_name_negative)
        first_name_blank.send_keys("")

        wait.until(ec.presence_of_element_located(self.__submit_contact_button))
        submit_btn_field = self._driver.find_element(*self.__submit_contact_button).click()

        actualtooltip_firstname_empty = first_name_blank.get_attribute("validationMessage")
        return actualtooltip_firstname_empty

    def perform_empty_last_name_check(self):
        wait = WebDriverWait(self._driver, 10)
        first_name_for_invalid_email = self._driver.find_element(*self.__first_name_negative)
        first_name_for_invalid_email.clear()
        first_name_for_invalid_email.send_keys("shanti")

        wait.until(ec.presence_of_element_located(self.__last_name_negative))
        blank_last_name = self._driver.find_element(*self.__last_name_negative)
        blank_last_name.send_keys("")

        wait.until(ec.presence_of_element_located(self.__submit_contact_button))
        submit_btn_field = self._driver.find_element(*self.__submit_contact_button).click()

        actualtooltip_blank_lastname = blank_last_name.get_attribute("validationMessage")
        #print("last name tooltip is ",actualtooltip_blank_lastname)
        return actualtooltip_blank_lastname


    def perform_invalid_email_id_check(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__first_name_negative))
        first_name_for_invalid_email =self._driver.find_element(*self.__first_name_negative)
        first_name_for_invalid_email.clear()
        first_name_for_invalid_email.send_keys("shanti")

        wait.until(ec.presence_of_element_located(self.__last_name))
        last_name_for_invalid_email = self._driver.find_element(*self.__last_name)
        last_name_for_invalid_email.clear()
        last_name_for_invalid_email.send_keys("kamat")

        wait.until(ec.presence_of_element_located(self.__email_address_negative))
        invalid_email_id_text=self._driver.find_element(*self.__email_address_negative)
        invalid_email_id_text.clear()
        invalid_email_id_text.send_keys("shanti")

        wait.until(ec.presence_of_element_located(self.__submit_contact_button))
        submit_btn_field = self._driver.find_element(*self.__submit_contact_button).click()

        actualtooltip_email = invalid_email_id_text.get_attribute("validationMessage")
        return actualtooltip_email

    def perform_incomplete_email_id_check(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__first_name_negative))
        first_name_for_incomplete_email = self._driver.find_element(*self.__first_name_negative)
        first_name_for_incomplete_email.clear()
        first_name_for_incomplete_email.send_keys("nikita")

        wait.until(ec.presence_of_element_located(self.__last_name))
        last_name_for_incomplete_email = self._driver.find_element(*self.__last_name)
        last_name_for_incomplete_email.clear()
        last_name_for_incomplete_email.send_keys("kamat")

        wait.until(ec.presence_of_element_located(self.__email_address_negative))
        incomplete_email_id_text = self._driver.find_element(*self.__email_address_negative)
        incomplete_email_id_text.clear()
        incomplete_email_id_text.send_keys("nikita@")

        wait.until(ec.presence_of_element_located(self.__submit_contact_button))
        submit_btn_field = self._driver.find_element(*self.__submit_contact_button).click()

        actualtooltip__incomplete_email = incomplete_email_id_text.get_attribute("validationMessage")
        return actualtooltip__incomplete_email

    def perform_contact_logout(self):
        contact_logout_button_field = self._driver.find_element(*self.__contact_logout_button)
        contact_logout_button_field.click()
