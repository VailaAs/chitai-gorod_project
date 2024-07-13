from time import sleep
from pages.MainPage import MainPage
from pages.CartPage import CartPage

def test_order(browser, config):
    main = MainPage(browser, config)
    cart = CartPage(browser, config)
    token = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIwODkwOTMxLCJpYXQiOjE3MjA4MjcxNzgsImV4cCI6MTcyMDgzMDc3OCwidHlwZSI6MjB9.o8tgbyOxOU-S8Pmahn6pfy4pLP4PKCahRNpj8KBGYAE'
    main.auth(token, browser)
    main.go_to_page()
    main.add_to_cart()
    cart.go_to_cart()
    cart.go_to_order_page()
