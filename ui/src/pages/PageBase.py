from abc import ABC

from ui.src.webdriver.Browser import Browser


class PageBase(ABC):
    BROWSER: Browser
    _URL: str

    def __init__(self, driver: Browser):
        self.BROWSER = driver

    def open(self):
        self.BROWSER.navigate(self._URL)

    def set_url(self, url: str):
        self._URL = url

    def get_url(self):
        return self._URL

    def refresh(self):
        self.BROWSER.refresh()
