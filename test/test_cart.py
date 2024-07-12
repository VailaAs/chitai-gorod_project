from time import sleep
import pytest
from pages.MainPage import MainPage
from pages.CartPage import CartPage

def test_order(browser, config):
    main = MainPage(browser, config)
    cart = CartPage(browser, config)
    main.go_to_page()
    main.popup_close()
    main.cookie_close()
    main.add_to_cart()
    cart.go_to_cart() #fix add to cart, too fast