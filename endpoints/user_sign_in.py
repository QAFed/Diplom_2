import requests
from main_data import Links

class UserSignIn:
    def __init__(self, payload):
        self.endpoint = "/auth/login"
        self.payload = payload
        self.response = None

    def request(self):
        self.response = requests.post(Links.MAIN_URL + self.endpoint, json=self.payload)

    def check_status_code(self, status_code):
        assert self.response.status_code == status_code

    def check_token_is_present(self):
        assert  self.response.json().get("accessToken", None) is not None

    def check_text_message(self, expect_message):
        assert self.response.json().get("message", None) == expect_message