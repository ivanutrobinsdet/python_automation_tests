from pydantic import BaseModel


class User(BaseModel):
    email: str | None = None
    password: str | None = None
    username: str | None = None
    bio: str | None = None
    image: str | None = None
    token: str | None = None
