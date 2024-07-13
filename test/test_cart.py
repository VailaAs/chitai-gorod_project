from time import sleep
from pages.MainPage import MainPage
from pages.CartPage import CartPage
from pages.AuthPage import AuthPage

def test_order(browser, config):
    main = MainPage(browser, config)
    cart = CartPage(browser, config)
    auth = AuthPage(browser, config)
    main.go_to_page()
    auth.add_token()
    sleep(5)
    name = auth.auth_name()
    assert name != 'Войти'
    main.add_to_cart()
    cart.go_to_cart()
    cart.go_to_order_page()
