import logging

import pytest
from selenium import webdriver

from core.selenium_core import SeleniumCore


class WIKI:
    _input_search = "search", "name"
    _button_search = "//button[text()='Search']", "xpath"
    _text_pushpa = "//h1[@id='firstHeading']", "xpath"
    _text_country = "//th[text()='Country']/..//td", "xpath"
    _text_date_of_release = "//div[text()='Release date']/../..//li", "xpath"

    _wiki_url = "https://en.wikipedia.org/wiki/Main_Page"

    def __init__(self, driver):
        self.driver: webdriver = driver
        self.selenium_core = SeleniumCore()

    def enter_movie_name(self, movie_name):
        logging.info("launching the url")
        pytest.driver.get(self._wiki_url)
        self.selenium_core.send_keys(*self._input_search, movie_name)
        logging.info("entered movie name")
        self.selenium_core.click_element(*self._button_search)
        actual_movie_name = self.selenium_core.get_text(*self._text_pushpa)
        assert movie_name == actual_movie_name
        logging.info("both the names are matched successfully")

    def get_country_of_origin(self):
        logging.info("getting the country name from wikipedia")
        self.selenium_core.scroll_to_element( *self._text_country)
        country = self.selenium_core.get_text(*self._text_country)
        return country

    def get_release_date(self):
        logging.info("getting the movie release data from wikipedia")
        release_date = self.selenium_core.get_text(*self._text_date_of_release)
        return release_date.split()

