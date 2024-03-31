import requests
from ...core import config

class Api:
    def __init__(self) -> None:
        self.base_url = config.BASE_URL
        self.login = config.API_LOING

    def get(self, endpoint, params={}, headers={}):
        url = f"{self.base_url}{endpoint}"
        headers["X-Auth-Token"] = self.login

        response = requests.get(url=url, params=params, headers=headers)

        return response

    def post(self, endpoint, params={}, headers={}, data={}):
        url = f"{self.base_url}{endpoint}"
        headers["X-Auth-Token"] = self.login

        response = requests.get(url=url, params=params, headers=headers, data=data)

        return response
