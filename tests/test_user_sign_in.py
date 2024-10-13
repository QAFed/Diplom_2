import pytest

from endpoints.user_sign_in import UserSignIn

class TestUserSignIn:
    def test_user_sign_in_if_all_data_correct(self, add_and_delete_gen_user):
        gen_user_data = add_and_delete_gen_user
        user_sign_in = UserSignIn(gen_user_data.for_sing_in())
        user_sign_in.request()
        user_sign_in.check_status_code(200)
        user_sign_in.check_token_is_present()

    @pytest.mark.parametrize()

    def test_user_not_sign_in_if_wrong_name_or_pass(self, add_and_delete_gen_user):



