import allure
import pytest
from helpers.generators import GenUserData
from endpoints.user_delete import UserDelete
from endpoints.user_sign_up import UserSignUp
from endpoints.order_create import OrderCreate
from helpers.test_data import TestData


@pytest.fixture
def add_gen_data_and_delete_user():
    gen_user_data = GenUserData()
    yield gen_user_data
    if gen_user_data.access_token is not None:
        user_delete = UserDelete(gen_user_data.access_token)
        user_delete.request()


@pytest.fixture
def add_and_delete_gen_user():
    gen_user_data = GenUserData()
    user_sign_up = UserSignUp(gen_user_data.for_sing_up())
    user_sign_up.request()
    gen_user_data.access_token = user_sign_up.response.json().get("accessToken", None)
    yield gen_user_data
    if gen_user_data.access_token is not None:
        user_delete = UserDelete(gen_user_data.access_token)
        user_delete.request()


@pytest.fixture
def add_user_and_order(add_and_delete_gen_user):
    access_token = add_and_delete_gen_user.access_token
    create_order = OrderCreate(TestData.ingred_id_payload, access_token)
    create_order.request()
    yield access_token
