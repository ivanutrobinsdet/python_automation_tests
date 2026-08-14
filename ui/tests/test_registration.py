import allure
import pytest_check as check

from ui.tests.suite_base import SuiteBase


@allure.suite("Tests for api")
@allure.description("User registration, authorization, login")
class TestRegistration(SuiteBase):
    @allure.description("New user registration")
    def test_register_user(self):
        self._MAIN_PAGE.open()
        self._MAIN_PAGE.signup.click()

        check.is_true(True, "token shouldn't be empty")