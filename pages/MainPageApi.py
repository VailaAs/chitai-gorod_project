import allure
import requests

class MainPage:
    def __init__(self, config) -> None:
        self.url = config.get('data', 'api_url')
        self.access_token = 'Bearer ' + config.get('data', 'access_token')
        self.auth = {'Authorization': self.access_token}
        self.productID = config.get('data', 'productID')

    def add_to_cart(self):
        body = {"id":{{self.productID}},"adData":{"item_list_name":"product-page"}}
        response = requests.post(self.url + '/cart/product', headers = self.auth, json=body)
        return response.status_code
