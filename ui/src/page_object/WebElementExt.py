from selenium.webdriver.remote.webelement import WebElement

from ui.src.webdriver.Browser import  Browser
from typing import Final


class WebElementExt:
    _DRIVER: Final[Browser]
    _IS_HIDDEN: Final[bool]
    _XPATH: Final[str]
    _ELEMENT: WebElement
    _RELOAD_OBJECT: bool = True
    _TIMEOUT_IN_SEC: Final[int] = 10

    def __init__(self, driver: Browser, is_hidden: bool, xpath: str):
        self._DRIVER = driver
        self._IS_HIDDEN = is_hidden
        self._XPATH = xpath

    def set_element(self, element: WebElement):
        self._ELEMENT = element
        self._RELOAD_OBJECT = False

    def exists(self, timeout_in_sec: int):
        self._check_condition(timeout_in_sec)
        return self._ELEMENT != None

    def click(self):
        self._check_condition(self._TIMEOUT_IN_SEC)
        self._check_null()
        self._ELEMENT.click()

    def get_text(self) -> str:
        self._check_condition(self._TIMEOUT_IN_SEC)
        self._check_null()
        return self._ELEMENT.text

    def send_keys(self, text: str):
        self._check_condition(self._TIMEOUT_IN_SEC)
        self._check_null()
        self._ELEMENT.send_keys(text)

    def _check_condition(self, timeout_in_sec: int):
        if not self._RELOAD_OBJECT:
            return
        if not self._IS_HIDDEN:
            self._ELEMENT = self._DRIVER.find_element(self._XPATH, timeout_in_sec)
        else:
            raise Exception("Not implemented")

    def _check_null(self):
        if self._ELEMENT == None:
            raise Exception(f"Element with xpath = ({self._XPATH}) is not found")

