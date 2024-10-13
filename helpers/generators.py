from datetime import datetime
import random
class GenUserData:
    def __init__(self):
        self.gen_id = datetime.now().strftime("%Y%m%d%H%M%S" + str(random.randint(1, 99)))
        self.login = f"lgfedqa{self.gen_id}"
        self.password = f"pssfedqa{self.gen_id}"
        self.email = f"emlfedqa{self.gen_id}@yandex.ru"
        self.access_token = None

    def for_sing_up(self):
        return {
            "email": self.email,
            "password": self.password,
            "name": self.login
        }

    def for_sing_in(self):
        return {
            "email": self.email,
            "password": self.password
        }