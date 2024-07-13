from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

class CartPage:
    def __init__(self, browser, config) -> None:
        self.url = config.get('data', 'ui_url') + '/cart'
        self.browser = browser

    def go_to_cart(self):
        self.browser.get(self.url)

    def go_to_order_page(self):
        order_btn = self.browser.find_element(By.CSS_SELECTOR, '[class="button cart-sidebar__order-button blue"]')
        act = ActionChains(self.browser)
        act.move_to_element(order_btn).perform()
        order_btn.click()

    
    
