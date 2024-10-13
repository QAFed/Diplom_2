import requests
from main_data import Links


class UserDelete:
    def __init__(self, access_token):
        self.endpoint = "/auth/user"
        self.headers = {'authorization':access_token}
        self.response = None

    def request(self):
        self.response = requests.delete(Links.MAIN_URL + self.endpoint, headers=self.headers)

