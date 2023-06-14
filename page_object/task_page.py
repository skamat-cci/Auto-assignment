# import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class taskPage:
    __task_menu = (By.XPATH, "//div[@id='navbarSupportedContent']//a[@href='/task']")
    __task_page_title = (
    By.XPATH, "/html//div[@id='root']/div[@class='App']//div[@class='container mt-2 w-50']//h4[.='Task Tracker']")

    __instruction_list = (By.CSS_SELECTOR, "h5")
    __add_instruction = (By.XPATH,
                         "/html//div[@id='root']/div[@class='App']//div[@class='container mt-2 w-50']//span[.='- Add -> Add New Tasks']")
    __edit_instruction = (By.XPATH,
                          "/html//div[@id='root']/div[@class='App']//div[@class='container mt-2 w-50']//span[.='- Edit -> Edit existing task']")
    __done_instruction = (By.XPATH,
                          " /html//div[@id='root']/div[@class='App']//div[@class='container mt-2 w-50']//span[.='- Done -> If task is completed']")
    __delete_instruction = (By.XPATH,
                            "/html//div[@id='root']/div[@class='App']//div[@class='container mt-2 w-50']//span[.='- Delete -> If you want to delete task']")

    # __fill_timesheet_textbox=(By.XPATH,"/html//input[@id='task-input']")
    __fill_timesheet_textbox = (By.XPATH, "/html//input[@id='task-input']")
    __fill_timesheet_textbox2 = (By.XPATH, "/html//input[@id='task-input']")
    __fill_timesheet_textbox3 = (By.XPATH, "/html//input[@id='task-input']")
    __fill_timesheet_textbox4 = (By.XPATH, "/html//input[@id='task-input']")
    __fill_timesheet_textbox5 = (By.XPATH, "/html//input[@id='task-input']")

    __add_task_button = (
    By.XPATH, "/html//div[@id='root']/div[@class='App']//div[@class='container mt-2 w-50']//button[@type='button']")
    __add_task_button2 = (
    By.XPATH, "/html//div[@id='root']/div[@class='App']//div[@class='container mt-2 w-50']//button[@type='button']")
    __add_task_button3 = (
    By.XPATH, "/html//div[@id='root']/div[@class='App']//div[@class='container mt-2 w-50']//button[@type='button']")
    __add_task_button4 = (
    By.XPATH, "/html//div[@id='root']/div[@class='App']//div[@class='container mt-2 w-50']//button[@type='button']")
    __add_task_button5 = (
    By.XPATH, "/html//div[@id='root']/div[@class='App']//div[@class='container mt-2 w-50']//button[@type='button']")

    # __view_task_Css  =(By.CSS_SELECTOR, "div:nth-of-type(1) > .col-10.text-break.wrap")
    # __view_task2_css =(By.CSS_SELECTOR, "div:nth-of-type(2) > .col-10.text-break.wrap")
    # __view_task3_css =(By.CSS_SELECTOR, "div:nth-of-type(3) > .col-10.text-break.wrap")
    # __view_task4_css = (By.CSS_SELECTOR, "div:nth-of-type(4) > .col-10.text-break.wrap")
    # __view_task5_css = (By.CSS_SELECTOR, "div:nth-of-type(5) > .col-10.text-break.wrap")

    __view_task = (By.XPATH,
                   "/html//div[@id='root']/div[@class='App']//div[@class='container mt-2 w-50']/div/div[@class='col']/div[3]/div/div[.='session1 of automation']")
    __view_task2 = (By.XPATH,
                    "/html//div[@id='root']/div[@class='App']//div[@class='container mt-2 w-50']/div/div[@class='col']/div[3]/div/div[.='session2 of automation']")
    __view_task3 = (By.XPATH,
                    "/html//div[@id='root']/div[@class='App']//div[@class='container mt-2 w-50']/div/div[@class='col']/div[3]/div/div[.='session3 of automation']")
    __view_task4 = (By.XPATH,
                    "/html//div[@id='root']/div[@class='App']//div[@class='container mt-2 w-50']/div/div[@class='col']/div[3]/div/div[.='session4 of automation']")
    __view_task5 = (By.XPATH,
                    "/html//div[@id='root']/div[@class='App']//div[@class='container mt-2 w-50']/div/div[@class='col']/div[3]/div/div[.='session5 of automation']")

    __edit_icon = (By.CSS_SELECTOR, ".col > svg:nth-of-type(1)")
    __save_button = (
    By.XPATH, "/html//div[@id='root']/div[@class='App']//div[@class='container mt-2 w-50']//button[@type='button']")
    __view_edited_task = (By.XPATH,
                          "/html//div[@id='root']/div[@class='App']//div[@class='container mt-2 w-50']/div/div[@class='col']/div[3]/div/div[.='session1 edited automation task- selenium and python']")

    __done_icon4 = (By.CSS_SELECTOR, "div:nth-of-type(3) > .col > svg:nth-of-type(2) > path")
    __view_done_text4 = (By.CSS_SELECTOR,
                         "/html//div[@id='root']/div[@class ='App'] // div[@ class ='container mt-2 w-50'] / div / div[@ class ='col'] / div[3] / div[3] / div[.='session4 of automation']")

    __delete_icon1 = (By.CSS_SELECTOR, "div:nth-of-type(1) > .col > svg:nth-of-type(3) > path")
    __delete_icon2 = (By.CSS_SELECTOR, "div:nth-of-type(2) > .col > svg:nth-of-type(3) > path")
    __delete_icon3 = (By.CSS_SELECTOR, "div:nth-of-type(3) > .col > svg:nth-of-type(3) > path")

    __edit_icon4 = (By.CSS_SELECTOR, "div:nth-of-type(4) > .col > svg:nth-of-type(1) > path")
    __delete_icon4 = (By.CSS_SELECTOR, "div:nth-of-type(4) >.col > svg:nth-of-type(3) > path")

    __task_logout_button = (By.XPATH, "//div[@id='navbarSupportedContent']//a[@href='/login']")

    def __init__(self, driver: WebDriver):
        self._driver = driver

    @property
    def current_url(self):
        return (self._driver.current_url)

    def perform_task_menu_click(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__task_menu))
        task_menu_field = self._driver.find_element(*self.__task_menu)
        task_menu_field.click()

    def get_current_url(self):
        return (self._driver.current_url)

    def get_task_menu_title(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__task_page_title))
        task_menu_header_field = self._driver.find_element(*self.__task_page_title)
        actual_task_menu_header = task_menu_header_field.text
        return actual_task_menu_header

    def is_task_menu_title_displayed(self) -> bool:
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__task_page_title))
        # wait.until(ec.title_is(self.__task_page_title))
        # wait.until(ec.title_contains(":TASK TRACKER"))
        print("title is expected condition for wait")
        task_menu_header_field = self._driver.find_element(*self.__task_page_title)
        return task_menu_header_field.is_displayed()

    def is_instruction_list_displayed(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__instruction_list))
        # wait.until(ec.title_contains("Instructions"))
        instruction_list_field = self._driver.find_element(*self.__instruction_list)
        # print("inside instruction list is displayed method")
        return instruction_list_field.is_displayed()

    def get_intsruction_text(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__instruction_list))
        instruction_list_field = self._driver.find_element(*self.__instruction_list)
        actual_instruction_field_text = instruction_list_field.text
        # print("actual instruction field in text",actual_instruction_field_text)
        return actual_instruction_field_text

    def get_add_text_is_displayed(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__add_instruction))
        add_instruction_field = self._driver.find_element(*self.__add_instruction)
        add_instruction_text = add_instruction_field.text
        # print(add_instruction_text)
        return add_instruction_text

    def get_edit_text_is_displayed(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__edit_instruction))
        edit_instruction_field = self._driver.find_element(*self.__edit_instruction)
        edit_instruction_text = edit_instruction_field.text
        # print(edit_instruction_text)
        return edit_instruction_text

    def get_done_text_is_displayed(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__done_instruction))
        done_instruction_field = self._driver.find_element(*self.__done_instruction)
        done_instruction_text = done_instruction_field.text
        # print(done_instruction_text)
        return done_instruction_text

    def get_delete_text_is_displayed(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__delete_instruction))
        delete_instruction_field = self._driver.find_element(*self.__delete_instruction)
        delete_instruction_text = delete_instruction_field.text
        # print(delete_instruction_text)
        return delete_instruction_text

    def perform_entering_data1_on_timesheet(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__fill_timesheet_textbox))
        # print("before sendkeys on fill timessheet field")
        fill_timesheet_field = self._driver.find_element(*self.__fill_timesheet_textbox)
        fill_timesheet_field.clear()
        # print ("before",fill_timesheet_field.text)
        fill_timesheet_field.send_keys("session1 of automation")
        # print ("after",fill_timesheet_field.text)
        return fill_timesheet_field

    def perform_entering_data2_on_timesheet(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__fill_timesheet_textbox2))
        # print("before sendkeys on fill timessheet field")
        fill_timesheet_field2 = self._driver.find_element(*self.__fill_timesheet_textbox2)
        fill_timesheet_field2.clear()
        # print ("before fill timesheet textbook2",fill_timesheet_field.text,"xyz")
        fill_timesheet_field2.send_keys("session2 of automation")
        # print ("after fill timesheet textbook2",fill_timesheet_field.text,"abc")
        return fill_timesheet_field2.text

    def perform_entering_data3_on_timesheet(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__fill_timesheet_textbox3))
        # print("before sendkeys on fill timesheet3 field")
        fill_timesheet_field3 = self._driver.find_element(*self.__fill_timesheet_textbox3)
        fill_timesheet_field3.clear()
        # print ("before session3 sent",fill_timesheet_field.text)
        fill_timesheet_field3.send_keys("session3 of automation")
        # print ("after session3 sent",fill_timesheet_field.text)
        return fill_timesheet_field3

    def perform_entering_data4_on_timesheet(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__fill_timesheet_textbox4))
        # print("before sendkeys on fill timessheet field")
        fill_timesheet_field4 = self._driver.find_element(*self.__fill_timesheet_textbox4)
        fill_timesheet_field4.clear()
        # print ("before",fill_timesheet_field.text)
        fill_timesheet_field4.send_keys("session4 of automation")
        # print ("after",fill_timesheet_field.text)
        return fill_timesheet_field4

    def perform_entering_data5_on_timesheet(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__fill_timesheet_textbox5))
        # print("before sendkeys on fill timessheet field")
        fill_timesheet_field5 = self._driver.find_element(*self.__fill_timesheet_textbox5)
        fill_timesheet_field5.clear()
        # print ("before",fill_timesheet_field.text)
        fill_timesheet_field5.send_keys("session5 of automation")
        # print ("after",fill_timesheet_field.text)
        return fill_timesheet_field5

    def add_button_field_click(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.visibility_of_element_located(self.__add_task_button))
        add_task_entry_button = self._driver.find_element(*self.__add_task_button).click()
        # add_task_entry_button.click()

    def add_button_field2_click(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.visibility_of_element_located(self.__add_task_button2))
        add_task_entry_button2 = self._driver.find_element(*self.__add_task_button2).click()
        # add_task_entry_button2.click()

    def add_button_field3_click(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.visibility_of_element_located(self.__add_task_button3))
        add_task_entry_button3 = self._driver.find_element(*self.__add_task_button3).click()
        # add_task_entry_button3.click()

    def add_button_field4_click(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.visibility_of_element_located(self.__add_task_button4))
        add_task_entry_button4 = self._driver.find_element(*self.__add_task_button4).click()
        # add_task_entry_button4.click()

    def add_button_field5_click(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.visibility_of_element_located(self.__add_task_button5))
        add_task_entry_button5 = self._driver.find_element(*self.__add_task_button5).click()
        # add_task_entry_button5.click()

    def perform_wait_before_add_timesheet2(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until((ec.visibility_of_element_located(self.__task_page_title)))
        wait.until(ec.presence_of_element_located(self.__fill_timesheet_textbox))
        wait.until((ec.presence_of_element_located(self.__view_task)))

    def perform_wait_before_add_timesheet3(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until((ec.visibility_of_element_located(self.__task_page_title)))
        wait.until(ec.presence_of_element_located(self.__fill_timesheet_textbox2))
        wait.until((ec.presence_of_element_located(self.__view_task2)))

    def perform_wait_before_add_timesheet4(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until((ec.visibility_of_element_located(self.__task_page_title)))
        wait.until(ec.presence_of_element_located(self.__fill_timesheet_textbox3))
        wait.until((ec.presence_of_element_located(self.__view_task3)))

    def perform_wait_before_add_timesheet5(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until((ec.visibility_of_element_located(self.__task_page_title)))
        wait.until(ec.presence_of_element_located(self.__fill_timesheet_textbox4))
        wait.until((ec.presence_of_element_located(self.__view_task4)))

    def get_task_tracker_list(self):
        wait = WebDriverWait(self._driver, 20)
        # wait.until((ec.visibility_of_element_located(self.__task_page_title)))
        wait.until((ec.presence_of_element_located(self.__fill_timesheet_textbox)))
        wait.until((ec.presence_of_element_located(self.__add_task_button)))
        task_menu_header_field = self._driver.find_element(*self.__task_page_title)
        actual_task_menu_header = task_menu_header_field.text
        # print(actual_task_menu_header)
        wait.until((ec.visibility_of_element_located(self.__view_task)))
        view_task_field = self._driver.find_element(*self.__view_task)
        actual_view_task = view_task_field.text
        # print(actual_view_task)
        return actual_view_task

    def get_task2_tracker_list(self):
        wait = WebDriverWait(self._driver, 20)
        wait.until((ec.visibility_of_element_located(self.__task_page_title)))
        wait.until((ec.presence_of_element_located(self.__fill_timesheet_textbox2)))
        wait.until((ec.presence_of_element_located(self.__add_task_button2)))
        task_menu_header_field2 = self._driver.find_element(*self.__task_page_title)
        actual_task_menu_header2 = task_menu_header_field2.text
        # print("actual_task_menu_header",actual_task_menu_header2)
        wait.until((ec.presence_of_element_located(self.__view_task2)))
        view_task_field2 = self._driver.find_element(*self.__view_task2)
        actual_view_task2 = view_task_field2.text
        # print("actual_view_task2",actual_view_task2)
        return actual_view_task2

    def get_task3_tracker_list(self):
        wait = WebDriverWait(self._driver, 10)
        # wait.until((ec.visibility_of_element_located(self.__task_page_title)))
        wait.until((ec.presence_of_element_located(self.__fill_timesheet_textbox3)))
        wait.until((ec.presence_of_element_located(self.__add_task_button)))
        task_menu_header_field = self._driver.find_element(*self.__task_page_title)
        actual_task_menu_header = task_menu_header_field.text
        # print("get task3 tracker header",actual_task_menu_header)
        wait.until((ec.visibility_of_element_located(self.__view_task3)))
        view_task_field3 = self._driver.find_element(*self.__view_task3)
        actual_view_task3 = view_task_field3.text
        # print("actual viewing task3",actual_view_task3)
        return actual_view_task3

    def get_task4_tracker_list(self):
        wait = WebDriverWait(self._driver, 20)
        # wait.until((ec.visibility_of_element_located(self.__task_page_title)))
        wait.until((ec.presence_of_element_located(self.__fill_timesheet_textbox4)))
        wait.until((ec.presence_of_element_located(self.__add_task_button)))
        task_menu_header_field = self._driver.find_element(*self.__task_page_title)
        actual_task_menu_header = task_menu_header_field.text
        # print(actual_task_menu_header)
        wait.until((ec.visibility_of_element_located(self.__view_task4)))
        view_task_field4 = self._driver.find_element(*self.__view_task4)
        actual_view_task4 = view_task_field4.text
        # print(actual_view_task)
        return actual_view_task4

    def get_task5_tracker_list(self):
        wait = WebDriverWait(self._driver, 20)
        # wait.until((ec.visibility_of_element_located(self.__task_page_title)))
        wait.until((ec.presence_of_element_located(self.__fill_timesheet_textbox5)))
        wait.until((ec.presence_of_element_located(self.__add_task_button)))
        task_menu_header_field = self._driver.find_element(*self.__task_page_title)
        actual_task_menu_header = task_menu_header_field.text
        # print(actual_task_menu_header)
        wait.until((ec.visibility_of_element_located(self.__view_task5)))
        view_task_field5 = self._driver.find_element(*self.__view_task5)
        actual_view_task5 = view_task_field5.text
        # print(actual_view_task)
        return actual_view_task5

    def perform_edit_click(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until((ec.presence_of_element_located(self.__edit_icon)))
        edit_icon_field = self._driver.find_element(*self.__edit_icon)
        edit_icon_field.click()

    def perform_edit_of_task(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until((ec.presence_of_element_located(self.__fill_timesheet_textbox)))
        edit_textbox_text = self._driver.find_element(*self.__fill_timesheet_textbox)
        edit_textbox_text.clear()
        edit_textbox_text.send_keys("session1 edited automation task- selenium and python")
        # print ("after edit")
        return edit_textbox_text

    def perform_save_click(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__save_button))
        # wait.until((ec.presence_of_element_located(self.__save_button)))
        save_button_field = self._driver.find_element(*self.__save_button)
        save_button_field.click()

    def get__edited_task_tracker_list(self):
        wait = WebDriverWait(self._driver, 20)
        # wait.until((ec.visibility_of_element_located(self.__task_page_title)))
        wait.until((ec.presence_of_element_located(self.__fill_timesheet_textbox)))
        wait.until((ec.presence_of_element_located(self.__add_task_button)))
        task_menu_header_field = self._driver.find_element(*self.__task_page_title)
        actual_task_menu_header = task_menu_header_field.text
        # print(actual_task_menu_header)
        wait.until((ec.visibility_of_element_located(self.__view_edited_task)))
        view_edited_task_field = self._driver.find_element(*self.__view_edited_task)
        actual_view_edited_task_field = view_edited_task_field.text
        # print(actual_view_task)
        return actual_view_edited_task_field

    def perform_delete_of_task(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until((ec.presence_of_element_located(self.__view_task2)))
        delete_textbox_text = self._driver.find_element(*self.__fill_timesheet_textbox2)
        wait.until((ec.presence_of_element_located(self.__delete_icon2)))
        delete_icon_clicked = self._driver.find_element(*self.__delete_icon2).click()

    def perform_done_of_task(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until((ec.presence_of_element_located(self.__view_task4)))
        done_textbox_text = self._driver.find_element(*self.__fill_timesheet_textbox4)
        wait.until(ec.presence_of_element_located(self.__done_icon4))
        # print("inside done task")
        done_icon_clicked = self._driver.find_element(*self.__done_icon4).click()
        # print("clicked done task")

    def get_done_task_tracker_list(self):
        wait = WebDriverWait(self._driver, 20)
        # wait.until((ec.visibility_of_element_located(self.__task_page_title)))
        wait.until((ec.presence_of_element_located(self.__fill_timesheet_textbox)))
        wait.until((ec.presence_of_element_located(self.__add_task_button)))
        task_menu_header_field = self._driver.find_element(*self.__task_page_title)
        actual_task_menu_header = task_menu_header_field.text
        # print(actual_task_menu_header)
        wait.until((ec.visibility_of_element_located(self.__view_task4)))
        view_done_task_field = self._driver.find_element(*self.__view_task4)
        actual_view_done_task_field = view_done_task_field.text
        # print("actual_view_done_task_field =",actual_view_done_task_field)
        i = 0
        new_striked_done = ''
        while i < len(actual_view_done_task_field):
            new_striked_done = new_striked_done + (actual_view_done_task_field[i] + u'\u0336')
            i = i + 1
        # print("striked text =",new_striked_done)
        # print(actual_view_task)
        return new_striked_done

    def all_session4_icon_displayed(self):
        wait = WebDriverWait(self._driver, 20)
        # wait.until((ec.visibility_of_element_located(self.__task_page_title)))
        wait.until((ec.presence_of_element_located(self.__edit_icon4)))
        wait.until((ec.presence_of_element_located(self.__done_icon4)))
        wait.until(ec.presence_of_element_located(self.__delete_icon4))
        edit4_icon = self._driver.find_element(*self.__edit_icon4)
        done4_icon = self._driver.find_element(*self.__done_icon4)
        delete4_icon = self._driver.find_element(*self.__delete_icon4)
        if ((edit4_icon.is_displayed()) and (done4_icon.is_displayed()) and (delete4_icon.is_displayed())):
            flag = True
        return flag

    def perform_task_logout(self):
        task_logout_button_field = self._driver.find_element(*self.__task_logout_button)
        task_logout_button_field.click()