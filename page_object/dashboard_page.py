from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class DashboardPage():
    __logout_button = (By.LINK_TEXT, "Logout")
    __contact_list_header = (By.XPATH,"/html//div[@id='root']//h1[.='Contact List']")

    __dashboard_list_name=(By.XPATH,"/html//div[@id='root']/div[@class='App']//table[@class='table']/tbody/tr[1]/td[.='Ivo Costa']")
    __dashboard_list_email=(By.XPATH,"/html//div[@id='root']/div[@class='App']//table[@class='table']//td[.='ivo.costa@creativecapsule.com']")
    __dashboard_list_phone=(By.XPATH,"/html//div[@id='root']/div[@class='App']//table[@class='table']//td[.='9523100223']")
    __dashboard_list_address =(By.CSS_SELECTOR,"tr:nth-of-type(1) > td:nth-of-type(4)")
    #__dashboard_list_address=(By.XPATH,"/html//div[@id='root']/div[@class='App'] //table[@class='table']//td[.='Goa, DDD (If you know, you know!!!']")
                                        #/html//div[@id='root']/div[@class='App'] //table[@class='table']//td[.='Goa, DDD (If you know, you know!!!'

    def __init__(self,driver:WebDriver):
        self._driver= driver

    @property
    def current_url(self):
        return (self._driver.current_url)


    def get_contact_title(self):
       wait = WebDriverWait(self._driver,10)
       wait.until(ec.presence_of_element_located(self.__contact_list_header))
       return(self._driver.find_element(*self.__contact_list_header)).text

    def get_home_page_contact_list_name(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__dashboard_list_name))
        dashboard_contact_list_name_field = self._driver.find_element(*self.__dashboard_list_name)
        actual_dashboard_contact_list_name = dashboard_contact_list_name_field.text
        return (actual_dashboard_contact_list_name)

    def get_home_page_contact_list_email(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__dashboard_list_email))
        dashboard_contact_list_email_field = self._driver.find_element(*self.__dashboard_list_email)
        actual_dashboard_contact_list_email = dashboard_contact_list_email_field.text
        return (actual_dashboard_contact_list_email)

    def get_home_page_contact_list_phone(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__dashboard_list_phone))
        dashboard_contact_list_phone_field = self._driver.find_element(*self.__dashboard_list_phone)
        actual_dashboard_contact_list_phone = dashboard_contact_list_phone_field.text
        return (actual_dashboard_contact_list_phone)

    def get_home_page_contact_list_address(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__dashboard_list_address))
        dashboard_contact_list_address_field = self._driver.find_element(*self.__dashboard_list_address)
        actual_dashboard_contact_list_address = dashboard_contact_list_address_field.text
        return actual_dashboard_contact_list_address

    def perform_logout(self):
        logout_button_field = self._driver.find_element(*self.__logout_button).click()