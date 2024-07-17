from time import sleep
from pages.MainPageUi import MainPage
from pages.CartPageUi import CartPage

def test_add_to_cart(browser, config):
    main = MainPage(browser, config)
    cart = CartPage(browser, config)
    main.go_to_page()
    main.add_cookies()
    main.add_to_cart()
    cart.go_to_cart()
    cart.go_to_order_page()
    cart.choose_city_in_rus()
    cart.choose_pickup_point()
    cart.choose_payment_method('webcard')
    cart.checkout_order()
    sleep(5)

def test_order_sbp_user_latin_name_email_ru_phone(browser, config):
    main = MainPage(browser, config)
    cart = CartPage(browser, config)