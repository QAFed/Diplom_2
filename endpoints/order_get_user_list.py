import allure
import requests
from main_data import Links


class OrderGetUserList:
    def __init__(self, access_token):
        self.endpoint = "/orders"
        self.headers = {'authorization': access_token}
        self.response = None

    @allure.step('request')
    def request(self):
        self.response = requests.get(Links.MAIN_URL + self.endpoint, headers=self.headers)

    @allure.step('check status code')
    def check_status_code(self, status_code):
        assert self.response.status_code == status_code

    @allure.step('check order list exist')
    def check_order_list_exist(self):
        assert isinstance(self.response.json()['orders'], list)

    @allure.step('check text message')
    def check_text_message(self, expect_message):
        assert self.response.json().get("message", None) == expect_message
