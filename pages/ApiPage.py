import allure
import requests

class ApiPage:
    def __init__(self, config) -> None:
        self.url = config.get('data', 'api_url')
        self.access_token = config.get('data', 'access_token')
        self.productID = int(config.get('data', 'productID'))
        self.cookies = {}
        self.headers = {
            'Cookie': f'__ddg1__=qPo057pMnfImFBsSjlYl; access-token=Bearer%20{self.access_token}; refresh-token=',
            'Authorization': 'Bearer ' + self.access_token
        }
        self.session = requests.Session()

    def get_request(self, url, params=''):
        try:
            response = self.session.get(url, headers=self.headers, params=params)
            self.cookies.update(response.cookies.get_dict())
            return response
        except requests.RequestException as e:
            print("An error occurred:", e)
            return None

    def post_request(self, url, params='', body='', headers=None):
        try:
            _headers = self.headers.copy()
            if headers:
                _headers.update(headers)
            response = self.session.post(url, headers=_headers, params=params, json=body)
            self.cookies.update(response.cookies.get_dict())
            return response
        except requests.RequestException as e:
            print("An error occurred:", e)
            return None

    def add_to_cart(self):
        _body = {"id": self.productID,"adData":{"item_list_name":"articles-slug","product_shelf":"Блок товара в статьях"}}
        response = self.post_request(self.url + '/cart/product', body=_body)
        return response.status_code
    
    def view_cart(self):
        response = self.get_request(self.url + '/cart')
        return response.status_code
    
    def shops_info(self, city_id:int):
        my_params = {
            'isCheckout': True,
            'userType': 'individual',
            'cityId': city_id
        }
        response = self.get_request(self.url + '/order-info/shop', params=my_params)
        return response.json()

    def orders_calculate(self, city_id:int, point_id:int, payment_type: str, username: str, userphone: str, useremail: str, delivery_date: str):
        _body = {
            "cityId": city_id,
            "shipment":{
                "type":"shop",
                 "id": 19,
                 "pointId": point_id
            },
            "paymentType": payment_type,
            "useAmountBonusPay":0,
            "user":{
                "type":"individual",
                "name": username,
                "phone": userphone,
                "email": useremail,
                "emailNotifications": True,
                "smsNotifications": True
            },
            "legalEntity": None,
            "address":{
                "index": None,
                "street": None,
                "house": None,
                "building": None,
                "block": None,
                "apartment": None,
                "fullAddress": None,
                "comment": None
            },
            "shelf":"",
            "listName":"",
            "deliveryDate": delivery_date,
            "orderType":"order",
            "bonusPayment":0
        }

        response = self.post_request(self.url + '/orders-calculate', body=_body, headers={'Content-Type': 'application/json'})
        return response.status_code
    
    def create_shop_order(self, city_id:int, point_id:int, payment_type: str, username: str, userphone: str, useremail: str, delivery_date: str):
        _body = {
            "cityId": city_id,
            "shipment":{
                "type":"shop",
                 "id": 19,
                 "pointId": point_id
            },
            "paymentType": payment_type,
            "useAmountBonusPay":0,
            "user":{
                "type":"individual",
                "name": username,
                "phone": userphone,
                "email": useremail,
                "emailNotifications": True,
                "smsNotifications": True
            },
            "legalEntity": None,
            "address":{
                "index": None,
                "street": None,
                "house": None,
                "building": None,
                "block": None,
                "apartment": None,
                "fullAddress": None,
                "comment": None
            },
            "shelf":"",
            "listName":"",
            "deliveryDate": delivery_date,
            "orderType":"order",
            "bonusPayment":0
        }

        response = self.post_request(self.url + '/orders', body=_body, headers={'Content-Type': 'application/json'})
        return response.status_code
    


