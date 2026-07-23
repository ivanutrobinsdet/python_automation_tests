import allure

from api.src.utils.RestClient import RestClient
from api.src.dtos.UserPayload import UserPayload
from api.src.dtos.builders.UserBuilder import UserBuilder
import pytest_check as check

@allure.suite("Tests for api")
@allure.description("User registration, authorization, login")
class TestUser:
    @allure.description("New user registration")
    def test_register_user(self):
        user = (
            UserBuilder()
            .email("someTestEmail@gmail.com")
            .username("test_user")
            .password("password")
            .build()
        )
        with allure.step(f"Generate user payload for user: {user}"):
            user_payload = UserPayload(user=user)

        client = RestClient()
        with allure.step("Register a new user"):
            response = client.post_request(end_point="/users", body=user_payload)

        with allure.step("Check status code"):
            check.equal(response.status_code, 201, "response code is not equal to CREATED 201")

        with allure.step("Check returned user"):
            created_user = UserPayload.model_validate(response.json())
            check.equal(created_user.user.email,user.email,"returned email is not equal to the original one")
            check.equal(created_user.user.username,user.username, "returned username is not equal to the original one")
            check.is_not_none(created_user.user.token,"token shouldn't be empty")
