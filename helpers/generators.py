from datetime import datetime
import random
from copy import copy
class GenUserData:
    def __init__(self):
        self.gen_id = datetime.now().strftime("%Y%m%d%H%M%S" + str(random.randint(1, 99)))
        self.name = f"lgfedqa{self.gen_id}"
        self.password = f"pssfedqa{self.gen_id}"
        self.email = f"emlfedqa{self.gen_id}@yandex.ru"
        self.access_token = None
        self.mod_data_request = {}
        self.exp_mod_data_response = None

    def for_sing_up(self):
        return {
            "email": self.email,
            "password": self.password,
            "name": self.name
        }

    def for_sing_in(self):
        return {
            "email": self.email,
            "password": self.password
        }

    def mod_data(self, mod_params):
        if mod_params == ["noChange"]:
            self.mod_data_request = {
            "email": self.email,
            "name": self.name
        }
        elif mod_params != []:
            for m_param in mod_params:
                setattr(self, m_param, f'md{getattr(self, m_param, None)}')
                self.mod_data_request[m_param] = getattr(self, m_param, None)

        self.exp_mod_data_response = {
            "email": self.email,
            "name": self.name
        }



