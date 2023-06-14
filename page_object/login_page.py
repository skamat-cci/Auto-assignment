from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class loginPage:
    __url="https://login-app-iota.vercel.app/"
    #__dashboard_url=__url+"\dashboard"

    __username_field =(By.XPATH, "//input[@id='username_textbox']")
    __password_field =(By.ID, "password_textbox")
    __login_button =(By.XPATH, "//div[@id='root']/div[@class='App']/section/div//form//button[@type='submit']")
    __error_message_field =(By.XPATH, "//div[.='Invalid Credentials']")

    def __init__(self,driver:WebDriver):
        self._driver=driver

    def open(self):
        self._driver.get(self.__url)

    @property
    def current_url(self):
        return(self._driver.current_url)

    def perform_login(self,username,password):
       username_data= self._driver.find_element(*self.__username_field)
       password_data = self._driver.find_element(*self.__password_field)
       submit_button_field = self._driver.find_element(*self.__login_button)

       username_data.send_keys(username)
       password_data.send_keys(password)
       submit_button_field.click()

    @property
    def error_message_text(self)->str:
       error_message_data = self._driver.find_element(*self.__error_message_field)
       actual_text = error_message_data .text
       return actual_text

    def is_error_message_displayed(self)->bool:
       error_message_data = self._driver.find_element(*self.__error_message_field)
       return error_message_data.is_displayed()

