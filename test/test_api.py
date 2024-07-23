import pytest
from pages.ApiPage import ApiPage


def test_pickup_from_shop(config):
    api = ApiPage(config)
    assert api.add_to_cart() == 200
    assert api.view_cart() == 200
    order_id = api.order_create(213, 'shop', 'Ивано Ива ИВ', '79123456789', 'email@gmail.com')
    assert api.view_order(order_id) == 200
    assert api.delete_order(order_id) == 204

def test_courier_in_rus(config):
    api = ApiPage(config)
    api.add_to_cart()
    api.view_cart()
    order_id = api.order_create(213, 'courier', 'Ивано Ива ИВ', '79123456789', 'email@gmail.com')
    assert api.view_order(order_id) == 200
    assert api.delete_order(order_id) == 204
   
def test_rus_post(config):
    api = ApiPage(config)
    api.add_to_cart()
    api.view_cart()
    order_id = api.order_create(213, 'post', 'Ивано Ива ИВ', '79123456789', 'email@gmail.com')
    assert api.view_order(order_id) == 200
    assert api.delete_order(order_id) == 204

def test_courier_latin_username(config):
    api = ApiPage(config)
    api.add_to_cart()
    api.view_cart()
    order_id = api.order_create(213, 'courier', 'Lohn John', '79123456789', 'email@gmail.com')
    assert api.view_order(order_id) == 400

@pytest.mark.xfail()
def test_useremail_with_wrong_domain(config):
    api = ApiPage(config)
    api.add_to_cart()
    api.view_cart()
    order_id = api.order_create(213, 'shop', 'Ивано Ива ИВ', '79123456789', 'sanich@aaa.aaaaa')
    res = api.view_order(order_id)
    api.delete_order(order_id)
    assert res == 400

@pytest.mark.xfail()
def test_userephone_with_wrong_code(config):
    api = ApiPage(config)
    api.add_to_cart()
    api.view_cart()
    order_id = api.order_create(213, 'shop', 'Ивано Ива ИВ', '19999999999', 'email@gmail.com')
    res = api.view_order(order_id)
    api.delete_order(order_id)
    assert res == 400