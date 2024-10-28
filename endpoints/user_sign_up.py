import allure
import requests
from main_data import Links


class UserSignUp:
    def __init__(self, payload):
        self.endpoint = "/auth/register"
        self.payload = payload
        self.response = None

    allure.step('request')
    def request(self):
        self.response = requests.post(Links.MAIN_URL + self.endpoint, json=self.payload)

    allure.step('check status code')
    def check_status_code(self, status_code):
        assert self.response.status_code == status_code

    allure.step('check token is present')
    def check_token_is_present(self):
        assert self.response.json().get("accessToken", None) is not None

    allure.step('check text message')
    def check_text_message(self, expect_message):
        assert self.response.json().get("message", None) == expect_message
