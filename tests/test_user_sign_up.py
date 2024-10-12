import pytest
from copy import copy

from endpoints.user_sign_up import UserSignUp


class TestUserSignUp:
    def test_user_sign_up_if_all_data_correct(self, add_gen_data_and_delete_user):
        gen_user_data = add_gen_data_and_delete_user
        user_sign_up = UserSignUp(gen_user_data.for_sing_up())
        user_sign_up.request()
        user_sign_up.check_status_code(200)
        user_sign_up.check_token_is_present()
        gen_user_data.access_token = user_sign_up.response.json().get("accessToken", None)

    def test_user_not_sign_in_if_user_exist(self, add_and_delete_gen_user):
        gen_user_data = add_and_delete_gen_user
        user_sign_up = UserSignUp(gen_user_data.for_sing_up())
        user_sign_up.request()
        user_sign_up.check_status_code(403)
        user_sign_up.check_text_message("User already exists")

    @pytest.mark.parametrize('kill_param', ["email","password","name"])
    def test_user_not_sign_in_if_not_all_required_fields_send(self, add_gen_data_and_delete_user, kill_param):
        gen_user_data = add_gen_data_and_delete_user
        mod_gen_user_data = copy(gen_user_data.for_sing_up())
        mod_gen_user_data.pop(kill_param)
        print(mod_gen_user_data)
        user_sign_up = UserSignUp(mod_gen_user_data)
        user_sign_up.request()
        user_sign_up.check_status_code(403)
        print(user_sign_up.response.json())
        user_sign_up.check_text_message("Email, password and name are required fields")