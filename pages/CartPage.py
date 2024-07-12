from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class CartPage:
    def __init__(self, browser, config) -> None:
        self.url = config.get('urls', 'ui_url') + '/cart'
        self.browser = browser

    def go_to_cart(self):
        self.browser.get(self.url)

    def go_to_order_page(self):
        self.browser.find_element(By.CSS_SELECTOR, '[class="button cart-sidebar__order-button blue"]').click()
    
