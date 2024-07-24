import allure
import requests


class ApiPage:
    def __init__(self, config) -> None:
        self.url = config.get('data', 'api_url')
        self.url2 = config.get('data', 'api_url2')
        self.access_token = config.get('data', 'access_token')
        self.productID = int(config.get('data', 'productID'))
        self.headers = {'Authorization': 'Bearer ' + self.access_token}
        self.session = requests.Session()

    @allure.step("API - Отправить GET запрос")
    def get_request(self, url: str, params: dict = {}) -> requests.Response:
        try:
            response = self.session.get(url, headers=self.headers, params=params)
            return response
        except requests.RequestException as e:
            print("An error occurred:", e.response)
            return None

    @allure.step("API - Отправить POST запрос")
    def post_request(self, url: str, params: dict = {}, body: dict = {}) -> requests.Response:
        try:
            response = self.session.post(url, headers=self.headers, params=params, json=body)
            return response
        except requests.RequestException as e:
            print("An error occurred:", e.response)
            return None

    @allure.step("API - Добавить товар в корзину")
    def add_to_cart(self) -> int:
        _body = {"id": self.productID, "adData": {
            "item_list_name": "articles-slug",
            "product_shelf": "Блок товара в статьях"}}
        response = self.post_request(self.url + '/cart/product', body=_body)
        return response.status_code

    @allure.step("API - Просмотреть корзину")
    def view_cart(self) -> int:
        response = self.get_request(self.url + '/cart')
        return response.json()['products'][0]['goodsId']

    @allure.step("API - Получить информацию о магазине")
    def shops_info(self, city_id: int) -> dict:
        my_params = {
            'isCheckout': True,
            'userType': 'individual',
            'cityId': city_id
        }
        response = self.get_request(self.url + '/order-info/shop', params=my_params)
        return response.json()
   
    @allure.step("API - Отправить запрос на поиск адреса по ключевому слову")
    def suggest_address_street(self, country_code: str = 'RU') -> str:
        my_params = {
            'countryCode': country_code,
            'count': 1,
            'query': 'ленин'
        }
        response = self.get_request(self.url + '/location/suggest/address', params=my_params)
        return response.json()[0]['address']

    @allure.step("API - Получить информацию об адресе получения")
    def suggest_address_house(self, country_code: str = 'RU') -> dict:
        my_params = {
            'countryCode': country_code,
            'count': 2,
            'query': self.suggest_address_street()
        }
        response = self.get_request(self.url + '/location/suggest/address', params=my_params)
        return response.json()

    @allure.step("API - Получить тело запроса")
    def order_body(self,
                   city_id: int,
                   shipment_type: str,
                   username: str,
                   userphone: str,
                   useremail: str) -> dict:

        shops_data = self.shops_info(city_id)['data']['items'][0]
        address_data = self.suggest_address_house()
        _body = {
            "cityId": city_id,
            "paymentType": 'sbp',
            "useAmountBonusPay": 0,
            "user": {
                "type": "individual",
                "name": username,
                "phone": userphone,
                "email": useremail,
                "emailNotifications": True,
                "smsNotifications": True
            },
            "legalEntity": None,
            "shelf": "",
            "listName": "",
            "deliveryDate": shops_data['deliveryDate'],
            "orderType": "order",
            "bonusPayment": 0
        }

        if shipment_type == 'shop':
            _body["shipment"] = {
                "type": 'shop',
                "id": 19,
                "pointId": shops_data['id']
            }
            _body["address"] = {
                "index": None,
                "street": None,
                "house": None,
                "building": None,
                "block": None,
                "apartment": None,
                "fullAddress": None,
                "comment": None
            }

        elif shipment_type == 'courier':
            _body["shipment"] = {
                "type": 'courier',
                "id": 53,
                "address": {
                    "address": shops_data['address'],
                    "apartment": None,
                    "building": None,
                    "cityId": city_id,
                    "house": None,
                    "housing": None,
                    "street": None,
                    "zip": '123060',
                    "fullAddress": shops_data['address'],
                    "index": None,
                    "block": None,
                    "comment": None
                },
                "isLoadedData": False,
                "deliveryId": 19,
                "providerPickpointId": shops_data['providerPickpointId'],
            }
            _body["address"] = {
                "index": address_data[0]['postcode'],
                "street": address_data[1]['street']['fullName'],
                "house": address_data[1]['houseDetails']['house'],
                "building": None,
                "block": None,
                "apartment": None,
                "fullAddress": address_data[1]['addressFull'],
                "comment": None,
                "coordinates": {
                    "latitude": address_data[1]['coordinates']['latitude'],
                    "longitude": address_data[1]['coordinates']['longitude']
                }
            }

        elif shipment_type == 'post':
            _body["shipment"] = {
                "type": 'post',
                "id": 0
            }
            _body["address"] = {
                "index": address_data[0]['postcode'],
                "street": address_data[1]['street']['fullName'],
                "house": address_data[1]['houseDetails']['house'],
                "building": None,
                "block": None,
                "apartment": None,
                "fullAddress": address_data[1]['addressFull'],
                "comment": None,
                "coordinates": {
                    "latitude": address_data[1]['coordinates']['latitude'],
                    "longitude": address_data[1]['coordinates']['longitude']
                }
            }
        return _body

    @allure.step("API - Создать данные для заказа")
    def orders_calculate(self,
                         city_id: int,
                         shipment_type: str,
                         username: str,
                         userphone: str,
                         useremail: str) -> int:

        _body = self.order_body(city_id, shipment_type, username, userphone, useremail)
        response = self.post_request(self.url + '/orders-calculate', body=_body)
        return response.status_code

    @allure.step("API - Оформить заказ")
    def order_create(self,
                     city_id: int,
                     shipment_type: str,
                     username: str,
                     userphone: str,
                     useremail: str) -> str:

        _body = self.order_body(city_id, shipment_type, username, userphone, useremail)
        calculation_status = self.orders_calculate(city_id, shipment_type, username, userphone, useremail)
        if calculation_status != 200:
            raise Exception("Order calculation failed with status code: {}".format(calculation_status))

        response = self.post_request(self.url + '/orders', body=_body)

        if 'id' in response.json():
            return response.json()['id']
        else:
            print("Warning: 'id' not found in response. Response content:", response.json())
            return ''

    @allure.step("API - Просмотреть заказ")
    def view_order(self, order_id: int) -> int:
        response = self.get_request(self.url2 + '/orders/' + order_id)
        return response.status_code

    @allure.step("API - Удалить заказ")
    def delete_order(self, order_id: int) -> int:
        try:
           response = self.session.delete(self.url + '/orders/' + order_id, headers = self.headers)
           return response.status_code

        except requests.RequestException as e:
            print("An error occurred:", e.response)
            return None
