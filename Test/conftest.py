#import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
#from webdriver_manager.core import driver
#from selenium.webdriver.common.by import By

@pytest.fixture()
#@pytest.fixture(params=["chrome","firefox","edge"])
def driver(request):
    browser = request.config.getoption("--browser")
    #  Open browser
    #browser= request.param
    #browser=request.config.getoption("--browser")  --commented to take the browser from params instead of argument
    print(f"Opening driver for {browser} browser")
    if browser=="chrome":
        browser_driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == "firefox":
        browser_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser == "edge":
        browser_driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    else:
        raise TypeError(f"Expected browser to be chrome,firefox,edge and got {browser}")
# using explicit wait for commented implicit wait
   # browser_driver.implicitly_wait(10)
    yield browser_driver
    print(f"closing driver for {browser} browser")
    browser_driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", help="provide browser as chrome,edge,firefox")

