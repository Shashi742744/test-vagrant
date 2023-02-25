import logging
from time import sleep

import pytest
from selenium import webdriver

from core.selenium_core import SeleniumCore


class IMDB:
    _input_search = "//input[@name='q']", "xpath"
    _button_search = "suggestion-search-button", "id"
    _text_pushpa = "//a[contains(text(),'Pushpa') and contains(text(),'The Rise') and  contains(text()," \
                   "'Part 1')] ", "xpath"
    _text_country = "//button[text()='Country of origin']/..//a", "xpath"
    _text_movie_title = "//h1", "xpath"
    _img_release_arrow = "//a[text()='Release date']//following-sibling::div", "xpath"
    _text_more_releases = "//span[contains(text(),'more')]", "xpath"
    _text_date_of_release = "//a[contains(text(),'India')]/..//following-sibling::div", "xpath"

    _imdb_url = "https://www.imdb.com/"

    def __init__(self, driver):
        self.driver: webdriver = driver
        self.selenium_core = SeleniumCore()

    def enter_movie_name(self, movie_name):
        logging.info("launching the url")
        pytest.driver.get(self._imdb_url)
        self.selenium_core.send_keys(*self._input_search, movie_name)
        logging.info("entered movie name")
        self.selenium_core.click_element(*self._button_search)
        self.selenium_core.click_element(*self._text_pushpa)
        movie_title = self.selenium_core.get_text(*self._text_movie_title)
        assert movie_name in movie_title
        logging.info("both the names are matched successfully")

    def get_country_of_origin(self):
        logging.info("getting the country name from imdb")
        self.selenium_core.scroll_to_element(*self._text_country)
        country = self.selenium_core.get_text(*self._text_country)
        return country

    def get_release_date(self):
        sleep(3)
        logging.info("getting the movie release data from imdb")
        self.selenium_core.click_element(*self._img_release_arrow)
        self.selenium_core.scroll_to_element(*self._text_more_releases)
        sleep(1)
        self.selenium_core.click_element(*self._text_more_releases)
        release_date = self.selenium_core.get_text(*self._text_date_of_release)
        return release_date.split()
