import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class SeleniumCore:
    def __init__(self):
        self.driver = pytest.driver

    def get_element(self, locator: str, by_type=By.XPATH) -> WebElement:
        """ get web element

        parameters:
        by_type (str): type of element
        locator (str): locator

        return WebElement
        """
        return self.driver.find_element(by_type, locator)

    def click_element(self, locator: str, by_type=By.XPATH):
        """ click on web element

        parameters:
        by_type (str): type of element
        locator (str): locator

        return None"""
        self.get_element(locator, by_type).click()

    def get_elements(self, locator: str, by_type=By.XPATH) -> list:
        """ get web elements

        parameters:
        by_type (str): type of element
        locator (str): locator

        return list of WebElement
        """
        return self.driver.find_elements(by_type, locator)

    def send_keys(self, locator: str, by_type=By.XPATH, value=""):
        """ sends value to the web element

        parameters:
        by_type (str): type of element
        locator (str): locator
        value (str): value

        return None
        """
        self.get_element(locator, by_type).send_keys(value)

    def scroll_to_element(self, locator: str, by_type=By.XPATH):
        """ scroll to element

        parameters:
        by_type (str): type of element
        locator (str): locator

        return None
        """
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});",
                                   self.get_element(locator, by_type))

    def get_text(self, locator: str, by_type=By.XPATH) -> str:
        """ get text from element

        parameters:
        by_type (str): type of element
        locator (str): locator

        return str
        """
        return self.get_element(locator, by_type).text




