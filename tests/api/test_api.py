import pytest
from api.api_client import APIClient
from api.base_api import PostAPI, CommentsAPI
from helpers.helpers import count_json_objects


@pytest.fixture
def api_client():
    base_url = "https://jsonplaceholder.typicode.com"
    return APIClient(base_url)


class TestAPI:

    @pytest.mark.parametrize('post_id', range(1, 101))
    def test_get_post_comments(self, api_client, post_id):
        """ Тест проверяет, что количество комментариев под каждым постом больше трёх"""
        comments_api = CommentsAPI(api_client)
        comments = comments_api.get_post_comments(post_id)
        assert count_json_objects(comments) > 3

    def test_delete_post(self, api_client):
        """Тест проверяет успешное удаление поста"""
        post_api = PostAPI(api_client, 1)
        status_code = post_api.delete_post()
        assert status_code == 200

    def test_update_post_title(self, api_client):
        """"Тест проверяет успешное изменение заголовка поста"""
        post_api = PostAPI(api_client, 1)
        updated_post = post_api.update_post_title("Updated Title")
        assert updated_post['title'] == "Updated Title"

    def test_create_new_post(self, api_client):
        """Тест проверяет успешное создание нового поста"""
        posts_api = PostAPI(api_client, 1)
        post = posts_api.create_post("Test Title", "Test Body", 1)
        assert post['title'] == "Test Title", post['body'] == "Test Body"
