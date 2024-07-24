import allure
import pytest
from pages.ApiPage import ApiPage


@allure.epic("Читай-город")
@allure.suite('API')
@allure.severity(severity_level='critical')
@allure.title('Самовывоз из магазина')
@allure.description('Оформление заказа самовывозом из магазина и его отмена')
@allure.feature('Test 1')
def test_pickup_from_shop(config):
    api = ApiPage(config)
    api.add_to_cart()
    """Проверяем добавление товара в корзину"""
    assert api.view_cart() == int(config.get('data', 'productID'))
    order_id = api.order_create(213, 'shop', 'Ивано Ива ИВ', '79123456789', 'email@gmail.com')
    """Проверяем успешное оформление заказа"""
    assert api.view_order(order_id) == 200
    """Проверяем успешное удаление заказа"""
    assert api.delete_order(order_id) == 204


@allure.epic("Читай-город")
@allure.suite('API')
@allure.severity(severity_level='high')
@allure.title('Курьер в России')
@allure.description('Оформление заказа курьером в России и его отмена')
@allure.feature('Test 2')
def test_courier_in_rus(config):
    api = ApiPage(config)
    api.add_to_cart()
    """Проверяем добавление товара в корзину"""
    assert api.view_cart() == int(config.get('data', 'productID'))
    order_id = api.order_create(213, 'courier', 'Ивано Ива ИВ', '79123456789', 'email@gmail.com')
    """Проверяем успешное оформление заказа"""
    assert api.view_order(order_id) == 200
    """Проверяем успешное удаление заказа"""
    assert api.delete_order(order_id) == 204


@allure.epic("Читай-город")
@allure.suite('API')
@allure.severity(severity_level='high')
@allure.title('Почта РФ')
@allure.description('Оформление заказа почтой РФ и его отмена')
@allure.feature('Test 3')
def test_rus_post(config):
    api = ApiPage(config)
    api.add_to_cart()
    """Проверяем добавление товара в корзину"""
    assert api.view_cart() == int(config.get('data', 'productID'))
    order_id = api.order_create(213, 'post', 'Ивано Ива ИВ', '79123456789', 'email@gmail.com')
    """Проверяем успешное оформление заказа"""
    assert api.view_order(order_id) == 200
    """Проверяем успешное удаление заказа"""
    assert api.delete_order(order_id) == 204


@allure.epic("Читай-город")
@allure.suite('API')
@allure.severity(severity_level='low')
@allure.title('Пользователь с английским именем')
@allure.description('Заказ курьером в России от пользователя с английским именем и его отмена')
@allure.feature('Test 4')
def test_courier_latin_username(config):
    api = ApiPage(config)
    api.add_to_cart()
    """Проверяем добавление товара в корзину"""
    assert api.view_cart() == int(config.get('data', 'productID'))
    order_id = api.order_create(213, 'courier', 'Lohn John', '79123456789', 'email@gmail.com')
    """Проверяем неуспешное оформление заказа"""
    assert api.view_order(order_id) == 400


@allure.epic("Читай-город")
@allure.suite('API')
@allure.severity(severity_level='low')
@allure.title('Почта с недействительным доменом')
@allure.description('Оформление заказа самовывозом из магазина от пользователя с почтой с недействительным доменом и его отмена')
@allure.feature('Test 5')
@pytest.mark.xfail()
def test_useremail_with_wrong_domain(config):
    api = ApiPage(config)
    api.add_to_cart()
    """Проверяем добавление товара в корзину"""
    assert api.view_cart() == int(config.get('data', 'productID'))
    order_id = api.order_create(213, 'shop', 'Ивано Ива ИВ', '79123456789', 'sanich@aaa.aaaaa')
    res = api.view_order(order_id)
    api.delete_order(order_id)
    """Проверяем успешное оформление заказа"""
    assert res == 200


@allure.epic("Читай-город")
@allure.suite('API')
@allure.severity(severity_level='low')
@allure.title('Телефон с недействительным кодом страны')
@allure.description('Оформление заказа самовывозом из магазина от пользователя с телефоном с недействительным кодом страны и его отмена')
@allure.feature('Test 6')
@pytest.mark.xfail()
def test_userephone_with_wrong_code(config):
    api = ApiPage(config)
    api.add_to_cart()
    """Проверяем добавление товара в корзину"""
    assert api.view_cart() == int(config.get('data', 'productID'))
    order_id = api.order_create(213, 'shop', 'Ивано Ива ИВ', '19999999999', 'email@gmail.com')
    res = api.view_order(order_id)
    api.delete_order(order_id)
    """Проверяем успешное оформление заказа"""
    assert res == 200
