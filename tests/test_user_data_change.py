import pytest

from endpoints.user_data_change import UserDataChange


class TestUserDataChange:
    @pytest.mark.parametrize('mod_param', [
        ["name"],
        ["email"],
        ["name", "email"],
        [],
        ["noChange"]
    ])
    def test_user_data_change_if_user_authorized(self, add_and_delete_gen_user, mod_param):
        gen_user_data = add_and_delete_gen_user
        gen_user_data.mod_data(mod_param)
        user_data_change = UserDataChange(gen_user_data.mod_data_request, gen_user_data.access_token)
        user_data_change.request()
        user_data_change.check_status_code(200)
        user_data_change.check_user_data_is_change(gen_user_data.exp_mod_data_response)

    def test_user_data_not_change_if_user_not_authorize(self):
        data_request = {
            "email": "fkuser@ya.ya",
            "name": "fkName378a"
        }
        user_data_change = UserDataChange(data_request, "")
        user_data_change.request()
        user_data_change.check_status_code(401)
        user_data_change.check_text_message("You should be authorised")
