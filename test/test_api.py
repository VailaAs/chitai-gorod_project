from pages.ApiPage import ApiPage
# from pages.CartPageApi import CartPage

def test_add_to_cart(config):
    main = ApiPage(config)
    main.add_to_cart()
    main.view_cart()
    point_id = main.shops_info(213)['data']['items'][0]['id']
    delivery_date = main.shops_info(213)['data']['items'][0]['deliveryDate']
    cal = main.orders_calculate(213, point_id, 'sbp', 'Ивано Ива ИВ', '+79123456789', 'email@email.com', delivery_date)
    assert cal == 200
    order_id = main.create_shop_order(213, point_id, 'sbp', 'Ивано Ива ИВ', '+79123456789', 'email@email.com', delivery_date)
    assert order_id == 201