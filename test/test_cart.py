from time import sleep
from pages.MainPage import MainPage
from pages.CartPage import CartPage

def test_order(browser, config):
    main = MainPage(browser, config)
    cart = CartPage(browser, config)
    main.go_to_page()
    main.add_to_cart()
    cart.go_to_cart()
    cart.go_to_order_page()
