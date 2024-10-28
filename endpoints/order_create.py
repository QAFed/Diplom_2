import allure
import requests
from main_data import Links


class OrderCreate:
    def __init__(self, payload, access_token):
        self.endpoint = "/orders"
        self.headers = {'authorization': access_token}
        self.response = None
        self.payload = payload

    @allure.step('request')
    def request(self):
        self.response = requests.post(Links.MAIN_URL + self.endpoint, headers=self.headers, json=self.payload)

    @allure.step('check status code')
    def check_status_code(self, status_code):
        assert self.response.status_code == status_code

    @allure.step('check id in order list')
    def check_id_in_order_list(self, order_list):
        responce_list_ids = [ingredient['_id'] for ingredient in self.response.json()['order']['ingredients']]
        assert sorted(order_list) == sorted(responce_list_ids)

    @allure.step('check text message')
    def check_text_message(self, expect_message):
        assert self.response.json().get("message", None) == expect_message

    @allure.step('check order number exist')
    def check_order_number_exist(self):
        assert isinstance(self.response.json()['order']["number"], int)
