import time

import pytest

from page_objects.dashboard_page import DashboardPage
from page_objects.login_page import loginPage
from page_objects.task_page import taskPage


@pytest.mark.login
@pytest.mark.positive3
@pytest.mark.parametrize("username,password",
                         [("admin", "admin123")])

# login page open and perform login
def test_task_menu_p(driver,username,password):
    login_page = loginPage(driver)
    login_page.open()
    login_page.perform_login(username, password)

# create a dashboard page object and verify dashboard url
    dashboard_page = DashboardPage(driver)
    assert dashboard_page.current_url == 'https://login-app-iota.vercel.app/dashboard', 'Default URL should be Dashboard URL'

# create a Task page object and locate Task menu and click on Tasks menu
    task_page = taskPage(driver)
    task_page.perform_task_menu_click()

# verify url of task menu
    assert task_page.get_current_url() =='https://login-app-iota.vercel.app/task',"Task menu URL is not matching"

# verify title of Task menu is displayed and is matching
    assert task_page.get_task_menu_title() =='TASK TRACKER',"Task menu title is not matching 'TASK TRACKER'"
    task_page.is_task_menu_title_displayed()

# verify instruction of task menu is displayed
    assert task_page.get_intsruction_text().__contains__("Instructions")
    assert task_page.is_instruction_list_displayed(), "Intructions title is not displayed"

# verify  add , edit, done , delete instruction inside task menu are displayed
    assert task_page.get_add_text_is_displayed()    =="- Add -> Add New Tasks","Add instruction is not listed inside Instruction of Task menu"
    assert task_page.get_edit_text_is_displayed()   =="- Edit -> Edit existing task" ,"Edit instruction is not listed inside Instruction of Task menu"
    assert task_page.get_done_text_is_displayed()   =="- Done -> If task is completed","Done instruction is not listed inside Instruction of Task menu"
    assert task_page.get_delete_text_is_displayed() =="- Delete -> If you want to delete task","Delete instruction is not listed inside Instruction of Task menu"

# locate the textbox--fill today's timesheet, clear the text, add and submit entry in timesheet
    task_page.perform_entering_data1_on_timesheet()
    task_page.add_button_field_click()

    task_page.perform_entering_data2_on_timesheet()
    task_page.perform_wait_before_add_timesheet2()
    task_page.add_button_field2_click()


    task_page.perform_entering_data3_on_timesheet()
    task_page.perform_wait_before_add_timesheet3()
    task_page.add_button_field3_click()

    task_page.perform_entering_data4_on_timesheet()
    task_page.perform_wait_before_add_timesheet4()
    task_page.add_button_field4_click()

    task_page.perform_entering_data5_on_timesheet()
    task_page.perform_wait_before_add_timesheet5()
    task_page.add_button_field5_click()


# verify the task added is displayed in the Task menu
    assert task_page.get_task_tracker_list() =="session1 of automation","Task added is not displayed on Task Tracker"
    assert task_page.get_task2_tracker_list() =="session2 of automation","Task2 added is not displayed on Task Tracker"
    assert task_page.get_task3_tracker_list() =="session3 of automation","Task3 added is not displayed on Task Tracker"
    assert task_page.get_task4_tracker_list() == "session4 of automation", "Task4 added is not displayed on Task Tracker"
    assert task_page.get_task5_tracker_list() == "session5 of automation", "Task5 added is not displayed on Task Tracker"

# locate edit icon, save button, task textbox and perform edit and save of task
    task_page.perform_edit_click()

# add some text to the textbox --append of python session make it session1 using sendkeys
    task_page.perform_wait_before_add_timesheet2()
    task_page.perform_edit_of_task()
    task_page.perform_save_click()

#  verify the task is updated with text   in below section
    assert task_page.get__edited_task_tracker_list() =="session1 edited automation task- selenium and python", "Edited task does not match"

# locate the delete icon ,click on delete icon,verify the task is removed from the list
    task_page.perform_wait_before_add_timesheet3()
    task_page.perform_delete_of_task()
    assert task_page.get__edited_task_tracker_list() =="session1 edited automation task- selenium and python", "Edited task does not match"
    assert task_page.get_task3_tracker_list() == "session3 of automation", "Task3 added is not displayed on Task Tracker"

# locate the done icon,click on done icon,wait for visibility of text added,
    task_page.perform_wait_before_add_timesheet4()
    task_page.perform_done_of_task()

# verify strike out is displayed for the task4 and all other task on timesheet are intact
    assert task_page.get__edited_task_tracker_list() == "session1 edited automation task- selenium and python", "Edited task does not match"
    assert task_page.get_task3_tracker_list() == "session3 of automation", "Task3 added is not displayed on Task Tracker"
    assert task_page.get_done_task_tracker_list() == "s̶e̶s̶s̶i̶o̶n̶4̶ ̶o̶f̶ ̶a̶u̶t̶o̶m̶a̶t̶i̶o̶n̶", "Striked Done task does not match"
    assert task_page.all_session4_icon_displayed() == True, "All icons are not displayed for session4"
    assert task_page.get_task5_tracker_list() == "session5 of automation", "Task5 added is not displayed on Task Tracker"
    time.sleep(5)

# locate logout button,click on logout
    task_page.perform_task_logout()

# verify the user is on Login page after logout
    assert task_page.current_url  =='https://login-app-iota.vercel.app/login','Login page is not displayed'
    driver.quit()

