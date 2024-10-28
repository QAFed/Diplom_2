import allure
import requests
from main_data import Links


class UserDataChange:
    def __init__(self, payload, access_token):
        self.endpoint = "/auth/user"
        self.headers = {'authorization': access_token}
        self.response = None
        self.payload = payload

    @allure.step('request')
    def request(self):
        self.response = requests.patch(Links.MAIN_URL + self.endpoint, headers=self.headers, json=self.payload)

    @allure.step('check status code')
    def check_status_code(self, status_code):
        assert self.response.status_code == status_code

    @allure.step('check user data is change')
    def check_user_data_is_change(self, exp_user_data):
        assert self.response.json().get("user", None) == exp_user_data

    @allure.step('check text message')
    def check_text_message(self, expect_message):
        assert self.response.json().get("message", None) == expect_message
