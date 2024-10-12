import requests
from main_data import Links

class UserSignUp:
    def __init__(self, payload):
        self.endpoint = "/auth/register"
        self.payload = payload
        self.response = None

    def request(self):
        self.response = requests.post(Links.MAIN_URL + self.endpoint, json=self.payload)

    def check_status_code(self, status_code):
        assert self.response.status_code == status_code

    def check_token_is_present(self):
        assert  self.response.json().get("accessToken", None) is not None