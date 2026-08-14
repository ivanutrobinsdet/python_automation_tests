from typing import List

from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import element_to_be_clickable, visibility_of_all_elements_located, \
    presence_of_all_elements_located
from selenium.webdriver.support.wait import WebDriverWait
from typing import Final


class Browser:
    _MAIN_WINDOW_HANDLER: str
    _DRIVER: Final[WebDriver]

    def __init__(self):
        prefs = {
            "download.default_directory": "downloads\\",
            "safebrowsing.enabled": "false",
            "acceptInsecureCerts": "true"
        }

        options = Options()
        options.add_argument("disable-extensions")
        options.add_argument("ignore-certificate-errors")
        options.add_argument("ignore-urlfetcher-cert-requests")
        options.add_argument("allow-insecure-localhost")
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument("--incognito")

        self._DRIVER = webdriver.Chrome(options=options)
        self._start()
        self._DRIVER.start_client()

    def _start(self):
        self._DRIVER.maximize_window()
        self._DRIVER.delete_all_cookies()
        self._DRIVER.set_page_load_timeout(60)   #seconds
        self._DRIVER.set_script_timeout(60) #seconds
        self._MAIN_WINDOW_HANDLER = self._DRIVER.current_window_handle

    def switch_to_new_tab(self):
        handles = self._DRIVER.window_handles
        for handle in handles:
            if handle != self._MAIN_WINDOW_HANDLER:
                self._DRIVER.switch_to.window(handle)
                break

    def find_element(self, xpath: str, timeout_in_sec: int):
        fluent_wait = WebDriverWait(
            self._DRIVER,
            timeout=timeout_in_sec,
            poll_frequency=0.2,
            ignored_exceptions=(NoSuchElementException,)
        )
        element: WebElement
        try:
            element = fluent_wait.until(element_to_be_clickable((By.XPATH, xpath)))
        except Exception:
            return None
        return element

    def find_elements(self, xpath: str, timeout_in_sec: int):
        fluent_wait = WebDriverWait(
            self._DRIVER,
            timeout=timeout_in_sec,
            poll_frequency=0.2,
            ignored_exceptions=(NoSuchElementException,)
        )
        elements: List[WebElement] = fluent_wait.until(visibility_of_all_elements_located((By.XPATH, xpath)))
        return elements

    def find_hidden_elements(self, xpath: str, timeout_in_sec: int):
        fluent_wait = WebDriverWait(
            self._DRIVER,
            timeout=timeout_in_sec,
            poll_frequency=0.2,
            ignored_exceptions=(NoSuchElementException,)
        )
        elements: List[WebElement] = fluent_wait.until(presence_of_all_elements_located((By.XPATH, xpath)))
        return elements

    def go_back(self):
        self._DRIVER.back()

    def get_url(self):
        return self._DRIVER.current_url

    def refresh(self):
        self._DRIVER.refresh()

    def navigate(self, url):
        self._DRIVER.get(url)

    def stop_driver(self):
        self._DRIVER.quit()
