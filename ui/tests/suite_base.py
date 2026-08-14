import pytest

from ui.src.pages.MainPage import MainPage
from ui.src.webdriver.Browser import Browser


class SuiteBase:
    _BROWSER: Browser
    _MAIN_PAGE: MainPage

    @pytest.fixture(autouse=True)
    def initialize_and_clean(self):
        self._BROWSER = Browser()
        self._MAIN_PAGE = MainPage(self._BROWSER)
        yield
        self._BROWSER.stop_driver()