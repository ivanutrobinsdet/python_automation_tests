from typing import Self

from api.src.dtos.Article import Article


class ArticleBuilder:
    def __init__(self):
        self._data: dict[str, object] = {}

    def title(self, value: str) -> Self:
        self._data["title"] = value
        return self

    def description(self, value: str) -> Self:
        self._data["description"] = value
        return self

    def body(self, value: str) -> Self:
        self._data["body"] = value
        return self

    def tag_list(self, value: list[str]) -> Self:
        self._data["tag_list"] = value
        return self

    def build(self) -> Article:
        return Article.model_validate(self._data)
