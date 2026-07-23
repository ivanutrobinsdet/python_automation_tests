import allure

from api.src.dtos.User import User
from api.src.dtos.UserPayload import UserPayload
from api.src.dtos.builders.UserBuilder import UserBuilder
from api.src.utils.Generator import Generator
from api.src.utils.RestClient import RestClient


class Steps:
    def register_user(self):
        user = (
            UserBuilder()
            .email(f"{Generator().generate_random_alphabetical_string(10)}@gmail.com")
            .username(Generator().generate_random_alphabetical_string(10))
            .password(Generator().generate_random_digital_string(10))
            .build()
        )
        with allure.step(f"Generate user payload for user: {user}"):
            user_payload = UserPayload(user=user)
        client = RestClient()
        with allure.step("Register a new user"):
            client.post_request(end_point="/users", body=user_payload)
        return user

    def login(self, user: User):
        client = RestClient()
        # user_data = (
        #     UserBuilder()
        #     .email(user.email)
        #     .password(user.password)
        #     .build()
        # )
        user_payload = UserPayload(user=user)
        with allure.step(f"Login with the user {user}"):
            response = client.post_request(end_point="/users/login", body=user_payload)

        return UserPayload.model_validate(response.json()).user.token
