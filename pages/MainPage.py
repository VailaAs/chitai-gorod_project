from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class MainPage:
    def __init__(self, browser, config) -> None:
        self.url = config.get('urls', 'ui_url')
        self.browser = browser

    def go_to_page(self):
        self.browser.get(self.url)

    def search(self, input: str):
        str = self.browser.find_element(By.CSS_SELECTOR, '[class="header-search__input"]')
        str.send_keys(input)
        btn = self.browser.find_element(By.CSS_SELECTOR, '[class="header-search__button"]')
        btn.click()

    def search_no_product_found(self):
        result = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '[class="catalog-empty-result__icon"]')))
        return result
    
    def search_product_found(self):
        result = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '[class="search-page__found-message"]')))
        return result

    def add_to_cart(self):
        buy_btn = self.browser.find_element(By.CSS_SELECTOR, '[class="button action-button blue"]')
        act = ActionChains(self.browser)
        act.move_to_element(buy_btn).perform()
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '[class="button action-button blue"]')))
        buy_btn.click()
    
    def cookie_close(self):
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '[class="button cookie-notice__button white"]'))).click()

    def popup_close(self):
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '[class="popmechanic-close"]'))).click()

    def get_current_url(self):
        return self.browser.current_url