class PostAPI:
    """Базовые функции взаимодействия с постом"""
    def __init__(self, client, post_id):
        self.client = client
        self.post_id = post_id

    def delete_post(self):
        response = self.client.delete(f'/posts/{self.post_id}')
        return response.status_code

    def update_post_title(self, title):
        data = {'title': title}
        response = self.client.put(f'/posts/{self.post_id}', json=data)
        return response.json()

    def create_post(self, title, body, user_id):
        data = {
            'title': title,
            'body': body,
            'userId': user_id
        }
        response = self.client.post('/posts', json=data)
        return response.json()


class CommentsAPI:
    """Базовые функции взаимодействия с комментариями"""
    def __init__(self, api_client):
        self.api_client = api_client

    def get_post_comments(self, post_id):
        response = self.api_client.get(f'/comments?postId={post_id}')
        return response.json()