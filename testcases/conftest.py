import pytest
from selenium import webdriver

# for multiple browser

def pytest_addoption(parser):
   parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Launching chrome browser")
    elif browser == "edge":
        driver = webdriver.Edge()
        print("Launching edge browser")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching firefox browser")
    else :
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        driver = webdriver.Chrome(options = chrome_options)
        print("Running headless mode")
        # driver = webdriver.Chrome()
        # print("Launching chrome browser")
    driver.maximize_window()
    driver.implicitly_wait(5)
    return driver

@pytest.fixture(params=[
    ("Admin", "admin123", "Pass"),
    ("Admin1", "admin123", "Fail"),
    ("Admin", "admin1231", "Fail"),
    ("Admin1", "admin1231", "Fail")
])

def getdataforlogin(request):
    return request.param