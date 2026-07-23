from pydantic import BaseModel

from api.src.dtos.User import User


class UserPayload(BaseModel):
    user: User