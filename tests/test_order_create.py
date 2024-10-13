from endpoints.order_create import OrderCreate


class TestOrderCreate:
    def test_order_create_if_user_authorized(self, add_and_delete_gen_user):
        gen_user_data = add_and_delete_gen_user
        ingred_id_payload = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
        }
        order_create = OrderCreate(ingred_id_payload, gen_user_data.access_token)
        order_create.request()
        print("ответ", order_create.response.json())
        order_create.check_status_code(200)
        order_create.check_id_in_order_list(ingred_id_payload["ingredients"])
        order_create.check_order_number_exist()


