from endpoints.order_get_user_list import OrderGetUserList

class TestOrderGetUserList:
    def test_get_order_list_success_if_user_authorized(self, add_user_and_order):
        access_token = add_user_and_order
        get_list_order = OrderGetUserList(access_token)
        get_list_order.request()
        get_list_order.check_status_code(200)
        get_list_order.check_order_list_exist()

