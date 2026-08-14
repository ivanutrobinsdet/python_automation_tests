from ui.src.page_object.WebElementExt import WebElementExt
from ui.src.pages.PageBase import PageBase
from ui.src.webdriver.Browser import Browser
from functools import cached_property


class MainPage(PageBase):
    def __init__(self, driver: Browser):
        super().__init__(driver)
        self.set_url("https://automationexercise.com/")

    @cached_property
    def signup(self) -> WebElementExt:
        return WebElementExt(driver=self.BROWSER, is_hidden=False, xpath="//*[@href='/login']")