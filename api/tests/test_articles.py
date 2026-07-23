import allure
from pytest_check import check

from api.src.Steps import Steps
from api.src.dtos.ArticlePayload import ArticlePayload
from api.src.dtos.builders.ArticleBuilder import ArticleBuilder
from api.src.utils.Generator import Generator
from api.src.utils.RestClient import RestClient


@allure.suite("Tests for api")
@allure.description("Articles creations, manipulations")
class TestArticle:
    @allure.description("New article creation")
    def test_create_article(self):
        steps = Steps()
        user = steps.register_user()
        token = steps.login(user)

        with allure.step(f"Generate a new article payload"):
            article = (
                ArticleBuilder()
                .title(Generator().generate_random_alphabetical_string(10))
                .description(Generator().generate_random_alphabetical_string(10))
                .body(Generator().generate_random_alphabetical_string(40))
                .tag_list(["python", "testing"])
                .build()
            )
            article_payload = ArticlePayload(article=article)

        client = RestClient()
        client.set_token(token=token)
        with allure.step("Create a new article"):
            response = client.post_request(end_point="/articles", body=article_payload)

        with allure.step("Check status code"):
            check.equal(response.status_code, 201, "response code is not equal to CREATED 201")

        article_response = ArticlePayload.model_validate(response.json())
        with allure.step("Check the new article"):
            response = client.get_request(end_point=f"/articles/{article_response.article.slug}", params=None)
            article_response = ArticlePayload.model_validate(response)
            check.equal(article.title,
                        article_response.article.title,
                        "Titles are not equal")
            check.equal(article.description,
                        article_response.article.description,
                        "Descriptions are not equal")
            check.equal(article.body,
                        article_response.article.body,
                        "Bodies are not equal")
            check.equal(sorted(article.tag_list),
                        sorted(article_response.article.tag_list),
                        "Article tag lists do not match")
