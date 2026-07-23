from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class Article(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    slug: str | None = None
    title: str
    description: str
    body: str
    tag_list: list[str] = Field(alias="tagList")
    created_at: str | None = Field(default=None, alias="createdAt")
    updated_at: str | None = Field(default=None, alias="updatedAt")
    favorited: bool | None = None
    favorites_count: int | None = Field(default=None, alias="favoritesCount")
    author: dict[str, Any] | None = None
