import allure
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class AuthPage:
    def __init__(self, browser, config) -> None:
        self.url = config.get('data', 'ui_url')
        self.browser = browser
        self.token = config.get('data', 'token')

    def add_token(self):
        my_headers = {'Content-Type':'application/json', 'Authorization': 'Bearer {}'.format(self.token)}
        res = requests.post(self.url, headers=my_headers)
        self.browser.get(self.url)
        return res.json()

    def auth_name(self):
        profile = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '[class="header-profile__title"]')))
        return profile.text
