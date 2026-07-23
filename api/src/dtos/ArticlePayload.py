from pydantic import BaseModel

from api.src.dtos.Article import Article


class ArticlePayload(BaseModel):
    article: Article
