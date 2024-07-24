import allure
import pytest
from pages.MainPage import MainPage
from pages.CartPage import CartPage


@allure.epic("Читай-город")
@allure.suite('UI')
@allure.severity(severity_level='high')
@allure.title('Поиск товара по ключевым словам')
@allure.description('Проверка корректности работы функции поиска товаров на сайте с различными входными данными.')
@allure.feature('Test 1')
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
    """Проверяем, что поисковая строка принимает вводные данные"""
    assert '/search?phrase=' in current_url


@allure.epic("Читай-город")
@allure.suite('UI')
@allure.severity(severity_level='low')
@allure.title('Поиск товара по ключевым словам')
@allure.description('Проверка корректности работы функции поиска товаров на сайте с различными входными данными.')
@allure.feature('Test 2')
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
    """Проверяем, что поисковая строка не принимает вводные данные"""
    assert '/search?phrase=' in current_url


@allure.epic("Читай-город")
@allure.suite('UI')
@allure.severity(severity_level='high')
@allure.title('Добавление товара в корзину')
@allure.description('Проверка возможности добавления товара в корзину.')
@allure.feature('Test 3')
def test_add_to_cart(browser, config):
    main = MainPage(browser, config)
    cart = CartPage(browser, config)
    items_in_cart_before = cart.go_to_cart()
    main.go_to_page()
    main.add_to_cart()
    items_in_cart_after = cart.go_to_cart()
    cart.clear_cart()
    """Проверяем, что в корзине стало на один товар больше"""
    assert items_in_cart_after - items_in_cart_before == 1


@allure.epic("Читай-город")
@allure.suite('UI')
@allure.severity(severity_level='high')
@allure.title('Оформление заказа')
@allure.description('Проверка возможности оформления заказа со стандартными данными пользователя.')
@allure.feature('Test 4')
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
    if success:
        main.cancel_orders()
    else:
        cart.clear_cart()
    """Проверяем успешное оформление заказа"""
    assert success is True


@allure.epic("Читай-город")
@allure.suite('UI')
@allure.severity(allure.severity_level.NORMAL)
@allure.title('Проверка различных методов оплаты')
@allure.description('Проверка оформления заказа разными методами оплаты.')
@allure.feature('Test 5')
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
    if success:
        main.cancel_orders()
    else:
        cart.clear_cart()
    """Проверяем успешное оформление заказа"""
    assert success is True
