import requests


class APIClient:
    """Базовый API клиент"""
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint):
        url = self.base_url + endpoint
        response = requests.get(url)
        response.raise_for_status()
        return response

    def post(self, endpoint, json):
        url = self.base_url + endpoint
        response = requests.post(url, json=json)
        response.raise_for_status()
        return response

    def put(self, endpoint, json):
        url = self.base_url + endpoint
        response = requests.put(url, json=json)
        response.raise_for_status()
        return response

    def delete(self, endpoint):
        url = self.base_url + endpoint
        response = requests.delete(url)
        response.raise_for_status()
        return response

