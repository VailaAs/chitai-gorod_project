import pytest
from pages.MainPage import MainPage
from pages.CartPage import CartPage


@pytest.mark.parametrize('input', [
    'Test',
    'Дюна',
    '123',
    ',,'
])
def test_positive_search(browser, config, input: str):
    search = MainPage(browser, config)
    search.go_to_page()
    search.search(input)
    current_url = search.get_current_url()
    assert '/search?phrase=' in current_url

@pytest.mark.xfail()
@pytest.mark.parametrize('input', [
    '$%^',
    '',
    ' ',
    None
])
def test_negative_search(browser, config, input: str):
    search = MainPage(browser, config)
    search.go_to_page()
    search.search(input)
    current_url = search.get_current_url()
    assert '/search?phrase=' in current_url

def test_add_to_cart(browser, config):
    main = MainPage(browser, config)
    cart = CartPage(browser, config)
    c_b = cart.go_to_cart()
    main.go_to_page()
    main.add_to_cart()
    c_a = cart.go_to_cart()
    assert c_a-c_b == 1
    cart.clear_cart()

def test_default_user_order(browser, config):
    main = MainPage(browser, config)
    cart = CartPage(browser, config)
    main.go_to_page()
    main.add_to_cart()
    cart.go_to_cart()
    cart.go_to_order_page()
    cart.choose_city_in_rus()
    cart.choose_pickup_point()
    success = cart.checkout_order()
    if success == True:
        main.cancel_orders()
    else:
        cart.clear_cart()
    assert success == True

@pytest.mark.parametrize('payment_method', [
    'sbp',
    'webcard',
    'face-to-face'
])
def test_payment_methods(browser, config, payment_method: str):
    main = MainPage(browser, config)
    cart = CartPage(browser, config)
    main.go_to_page()
    main.add_to_cart()
    cart.go_to_cart()
    cart.go_to_order_page()
    cart.choose_city_in_rus()
    cart.choose_pickup_point()
    cart.choose_payment_method(payment_method)
    success = cart.checkout_order()
    if success == True:
        main.cancel_orders()
    else:
        cart.clear_cart()
    assert success == True
