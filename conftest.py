import pytest
from helpers.generators import GenUserData
from endpoints.user_delete import UserDelete

@pytest.fixture
def add_gen_data_and_delete_user():
    gen_user_data = GenUserData()
    yield gen_user_data
    user_delete = UserDelete(gen_user_data.access_token)
    user_delete.request()





