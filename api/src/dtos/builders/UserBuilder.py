from typing import Self

from api.src.dtos.User import User


class UserBuilder:
    def __init__(self) -> None:
        self._data: dict[str, str | None] = {}

    def email(self, value: str | None) -> Self:
        self._data["email"] = value
        return self

    def password(self, value: str | None) -> Self:
        self._data["password"] = value
        return self

    def username(self, value: str | None) -> Self:
        self._data["username"] = value
        return self

    def bio(self, value: str | None) -> Self:
        self._data["bio"] = value
        return self

    def image(self, value: str | None) -> Self:
        self._data["image"] = value
        return self

    def token(self, value: str | None) -> Self:
        self._data["token"] = value
        return self

    def build(self) -> User:
        return User.model_validate(self._data)