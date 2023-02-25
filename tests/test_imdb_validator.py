import pytest

from pom.imdb import IMDB
from pom.wikipedia import WIKI


@pytest.mark.usefixtures("finalize_driver")
class TestImdbWiki:

    @pytest.fixture(autouse=True)
    def SetUp(self, finalize_driver):
        self.driver = finalize_driver
        self.page_imdb = IMDB(self.driver)
        self.page_wiki = WIKI(self.driver)

    def test_validate_imdb(self, movie_name="Pushpa: The Rise"):
        self.page_imdb.enter_movie_name(movie_name)
        imdb_country = self.page_imdb.get_country_of_origin()
        month_imdb, date_imdb, year_imdb = [elements.lower() for elements in self.page_imdb.get_release_date()]

        self.page_wiki.enter_movie_name(movie_name)
        wiki_country = self.page_wiki.get_country_of_origin()
        wiki_date, wiki_month, wiki_yyyy = [elements.lower() for elements in self.page_wiki.get_release_date()]
        
        assert imdb_country == wiki_country
        assert date_imdb.strip(",") == wiki_date
        assert month_imdb == wiki_month
        assert year_imdb == wiki_yyyy

