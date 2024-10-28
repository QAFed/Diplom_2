import allure
import pytest
from copy import copy
from endpoints.user_sign_in import UserSignIn


@allure.suite('Test User Sign In')
class TestUserSignIn:
    @allure.title('test user sign in if all data correct')
    def test_user_sign_in_if_all_data_correct(self, add_and_delete_gen_user):
        gen_user_data = add_and_delete_gen_user
        user_sign_in = UserSignIn(gen_user_data.for_sing_in())
        user_sign_in.request()
        user_sign_in.check_status_code(200)
        user_sign_in.check_token_is_present()

    @allure.title('test user not sign in if wrong email or pass')
    @pytest.mark.parametrize('mod_param', ["email", "password"])
    def test_user_not_sign_in_if_wrong_email_or_pass(self, add_and_delete_gen_user, mod_param):
        gen_user_data = add_and_delete_gen_user
        mod_gen_user_data = copy(gen_user_data.for_sing_in())
        mod_gen_user_data[mod_param] = f"wrng{mod_gen_user_data[mod_param]}"
        user_sign_in = UserSignIn(mod_gen_user_data)
        user_sign_in.request()
        user_sign_in.check_status_code(401)
        user_sign_in.check_text_message("email or password are incorrect")
