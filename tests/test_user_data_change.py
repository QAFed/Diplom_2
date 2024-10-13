import pytest

from endpoints.user_data_change import UserDataChange
from copy import copy

@pytest.mark.parametrize('mod_param', [
    ["name"],
    ["email"],
    ["name","email"],
    [],
    ["noChange"]
])
class TestUserDataChange:
    def test_user_data_change_if_user_authorized(self, add_and_delete_gen_user, mod_param):
        gen_user_data = add_and_delete_gen_user
        gen_user_data.mod_data(mod_param)
        print ("Почта: ", gen_user_data.email)
        print("Пароль: ", gen_user_data.password)
        print ("Запрос ", gen_user_data.mod_data_request)
        user_data_change = UserDataChange(gen_user_data.mod_data_request, gen_user_data.access_token)
        user_data_change.request()
        print("Ожидаемый ответ ", gen_user_data.exp_mod_data_response)
        print("Фактический ответ ", user_data_change.response.json())
        user_data_change.check_status_code(200)
        user_data_change.check_user_data_is_change(gen_user_data.exp_mod_data_response)



