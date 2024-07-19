import allure
import requests

class MainPage:
    def __init__(self, config) -> None:
        self.url = config.get('data', 'api_url')
        self.access_token = 'Bearer ' + config.get('data', 'access_token')
        self.auth = {'Authorization': self.access_token}
        self.productID = int(config.get('data', 'productID'))

        self.session = requests.Session()
        self.session.headers.update(self.auth)

    def add_to_cart(self):
        body = {"id": self.productID,"adData":{"item_list_name":"catalog-main-category","product_shelf":""}}
        response = self.session.post(self.url + '/cart/product', headers = self.auth, json=body)
        return response.status_code
    
    def view_cart(self):
        response = self.session.get(self.url + '/cart', headers = self.auth)
        return response.status_code
    
    def shops_info(self, city_id:int):
        my_params = {
            'isCheckout': True,
            'userType': 'individual',
            'cityId': city_id
        }
        response = self.session.get(self.url + '/order-info/shop', params=my_params, headers = self.auth)
        return response.json()

    def orders_calculate(self, city_id:int, point_id:int, payment_type: str, username: str, userphone: str, useremail: str, delivery_date: str):
        body = {
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

        response = self.session.post(self.url + '/orders-calculate', headers = self.auth, json=body)
        return response.status_code
    
    def create_shop_order(self, city_id:int, point_id:int, payment_type: str, username: str, userphone: str, useremail: str, delivery_date: str):
        body = {
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

        response = self.session.post(self.url + '/orders', headers = self.auth, json=body)
        return response.status_code
    


