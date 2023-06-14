from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class AboutPage:

    #__about_menu =(By.LINK_TEXT,"//a[@href='/about']")
    __about_menu =(By.XPATH,"//div[@id='navbarSupportedContent']//a[@href='/about']")
    # By.XPATH,"/html//div[@id='root']//h1[@class='text-center text-primary']"
    #__about_title =(By.TAG_NAME,"h1")
    __about_title =(By.XPATH,"/html//div[@id='root']//h1[@class='text-center text-primary']")
    #__about_logout_button = (By.LINK_TEXT, "//a[@href='/login']")
    __about_logout_button =(By.XPATH,"//div[@id='navbarSupportedContent']//a[@href='/login']")
    #__wait = WebDriverWait(self._driver, 10)

    def __init__(self,driver:WebDriver):
        self._driver= driver

    @property
    def current_url(self):
        return (self._driver.current_url)

    def perform_about_menu_click(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__about_menu))
        about_menu_field = self._driver.find_element(*self.__about_menu)
        about_menu_field.click()


    def get_about_page_title(self)->str:
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__about_title))
        about_title_field = self._driver.find_element(*self.__about_title)
        actual_about_title_text= about_title_field.text
        return actual_about_title_text

    def perform_about_logout(self):
        about_logout_button_field=self._driver.find_element(*self.__about_logout_button)
        about_logout_button_field.click()
