import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService


browsers = {"chrome": (webdriver.Chrome, ChromeService, ChromeDriverManager, ChromeOptions, "chrome"),
            "firefox": (webdriver.Firefox, FirefoxService, GeckoDriverManager, FirefoxOptions, "firefox"),
            "edge": (webdriver.Edge, EdgeService, EdgeChromiumDriverManager, EdgeOptions, "edge")}

test_case_name = ""


@pytest.fixture()
def finalize_driver(browser, headless):
    instance = browsers.get(browser.lower(), browsers.get("chrome"))
    browser_address, browser_service, browser_manager, *rem = instance
    pytest.driver = browser_address(service=browser_service(browser_manager().install()))
    pytest.driver.maximize_window()
    pytest.driver.implicitly_wait(30)
    pytest.driver.delete_all_cookies()
    yield pytest.driver
    allure.attach(pytest.driver.get_screenshot_as_png(),
                  name="/screenshots/" + test_case_name + "_web",
                  attachment_type=AttachmentType.PNG)
    pytest.driver.quit()


def initialize_headless(instance):
    options = instance[3]()
    browser = instance[4]
    if browser == "chrome":
        options.add_argument("--headless")
        print("jjjj")
    elif browser == "edge":
        options.use_chromium = True
        options.add_argument("headless")
    elif browser == "firefox":
        options.headless = True
    return options


def finalize_headless(headless, instance):
    if headless or headless.lower() == "yes":
        return initialize_headless(instance)
    else:
        return instance[3]()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="options are chrome, firefox or edge")
    parser.addoption("--headless", action="store", default="no", help="here we have to use yes or no")


@pytest.fixture(scope="session")
def headless(request) -> str:
    return request.config.getoption("--headless").lower()


@pytest.fixture(scope="session")
def browser(request) -> str:
    return request.config.getoption("--browser").lower()
