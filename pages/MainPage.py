import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class MainPage:
    def __init__(self, browser, config) -> None:
        self.url = config.get('data', 'ui_url')
        self.browser = browser
    
    @allure.step("Перейти на главную страницу")
    def go_to_page(self):
        self.browser.get(self.url)

    def search(self, input: str):
        field = self.browser.find_element(By.CSS_SELECTOR, '[class="header-search__input"]')
        input = field.send_keys(input)
        btn = self.browser.find_element(By.CSS_SELECTOR, '[class="header-search__button"]')
        btn.click()

    def add_to_cart(self):
        buy_btn = self.browser.find_element(By.CSS_SELECTOR, '[class="button action-button blue"]')
        act = ActionChains(self.browser)
        act.move_to_element(buy_btn).perform()
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '[class="button action-button blue"]')))
        buy_btn.click()

    def get_current_url(self):
        WebDriverWait(self.browser, 5).until(
            EC.any_of(
                EC.presence_of_element_located
                ((By.CSS_SELECTOR, '[class="catalog-empty-result__icon"]')), 
            EC.presence_of_element_located
                ((By.CSS_SELECTOR, '[class="search-page__found-message"]'))))
        return self.browser.current_url
