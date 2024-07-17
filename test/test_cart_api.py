from time import sleep
from pages.MainPageApi import MainPage
# from pages.CartPageApi import CartPage

def test_add_to_cart(config):
    main = MainPage(config)
    main.add_to_cart()