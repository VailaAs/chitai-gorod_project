from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

class CartPage:
    def __init__(self, browser, config) -> None:
        self.url = config.get('data', 'ui_url')
        self.token = 'Bearer%20' + config.get('data', 'access_token')
        self.browser = browser

    def go_to_cart(self):
        self.browser.get(self.url + '/cart')
        current_token = self.browser.get_cookie('access-token').get('value')
        if current_token == str(self.token):
            pass
        else:
            self.browser.delete_cookie('access-token')
            cookie = {'name': 'access-token', 'value': self.token}
            self.browser.add_cookie(cookie)
            self.browser.refresh()

        WebDriverWait(self.browser, 5).until( 
            EC.visibility_of_element_located(
                (By.CLASS_NAME, 'cart-content'))) 
        count = 0
        try:
            elements = self.browser.find_elements(By.CLASS_NAME, 'cart-item')
            for element in elements:
                count += 1
        except Exception as e:
            print("No elements of such class found:", e)
        
        return count

    def go_to_order_page(self):
        order_btn = self.browser.find_element(By.CSS_SELECTOR, '[class="button cart-sidebar__order-button blue"]')
        act = ActionChains(self.browser)
        act.move_to_element(order_btn).perform()
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(order_btn))
        order_btn.click()

    def choose_city_in_rus(self):
        self.browser.find_element(By.CLASS_NAME, 'order-page__city').click()
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, 'app-select__icon'))).click()
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="__layout"]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/ul/li[3]'))).click()
        self.browser.find_element(By.CLASS_NAME, 'city-modal__popular-item').click()

    def choose_pickup_point(self):
        check_mark_1 = self.browser.find_element(By.ID, "step1")
        if "checkout-step__number checkout-step__number--success" in check_mark_1.get_attribute("class").split():
            WebDriverWait(self.browser, 20).until(
                EC.element_to_be_clickable(
                    (By.CLASS_NAME, "delivery-type-block delivery-type__pickup-block"))).click()
            WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "button pvz-selected__button light-blue"))).click()
            WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "point-preview__button chg-app-button chg-app-button--primary chg-app-button--small chg-app-button--brand-blue"))).click()
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "pvz-selected__map-layout")))
        else:
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "pvz-selected__map-layout")))
        
    def choose_payment_method(self, option:str):
        pay = self.browser.find_element(By.CLASS_NAME, 'payments__list')
        act = ActionChains(self.browser)
        act.move_to_element(pay).perform()

        if option == 'sbp':
            sbp = WebDriverWait(self.browser, 15).until(
                EC.visibility_of_element_located(
                    (By.XPATH, '//*[@id="step2"]/div[2]/div/div[2]/button[2]')))
            if "payments-item payments__item payments-item--active" in sbp.get_attribute("class").split():
                pass
            else:
                sbp.click()

        elif option == 'webcard':
            card = WebDriverWait(self.browser, 15).until(
                EC.visibility_of_element_located(
                    (By.XPATH, '//*[@id="step2"]/div[2]/div/div[2]/button[1]')))
            if "payments-item payments__item payments-item--active" in card.get_attribute("class").split():
                pass
            else:
                card.click()

        elif option == 'face-to-face':
            face = WebDriverWait(self.browser, 15).until(
                EC.visibility_of_element_located(
                    (By.XPATH, '//*[@id="step2"]/div[2]/div/div[2]/button[3]')))
            if "payments-item payments__item payments-item--active" in face.get_attribute("class").split():
                pass
            else:
                face.click()
    
    def user_data(self, name:str, email:str, phone:str):
        user = self.browser.find_element(By.ID, 'step3')
        act = ActionChains(self.browser)
        act.move_to_element(user).perform()

        username = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="step3"]/div[2]/form/div[1]/div/label/input')))
        username.send_keys(Keys.CONTROL + 'a')
        username.send_keys(Keys.BACKSPACE)
        username.send_keys(name)
        act.move_to_element(username).click().perform()

        useremail = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="step3"]/div[2]/form/div[2]/div/label/input')))
        useremail.send_keys(Keys.CONTROL + 'a')
        useremail.send_keys(Keys.BACKSPACE)
        useremail.send_keys(email)
        act.move_to_element(useremail).click().perform()

        userphone = userphone = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="step3"]/div[2]/form/div[3]/div/label/input')))
        userphone.send_keys(Keys.CONTROL + 'a')
        userphone.send_keys(Keys.BACKSPACE)
        userphone.send_keys(phone)
        act.move_to_element(userphone).click().perform()

    def checkout_order(self):
        self.browser.implicitly_wait(3)
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/div[2]/div/div/div[2]/div/div[3]/button'))).click()
        
        if WebDriverWait(self.browser, 10).until(
            EC.any_of(
                EC.presence_of_element_located
                ((By.CSS_SELECTOR, '[class="pay-by-card"]')), 
            EC.presence_of_element_located
                ((By.CSS_SELECTOR, '[class="thank-you-page"]')))):
            return True
        else:
            return False
        
    def clear_cart(self):
        self.go_to_cart()
        try:
           WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, 'delete-many'))).click()
        except Exception as e:
            print('Cart is clear:', e)

    def cancel_orders(self):
        self.browser.get(self.url + '/profile/orders')
        try: 
            element = WebDriverWait(self.browser, 10).until(  
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, '[class="button order-card__cancel light-blue"]')))
            WebDriverWait(self.browser, 10).until(  
                    EC.element_to_be_clickable(element)).click()
            WebDriverWait(self.browser, 10).until(  
                    EC.element_to_be_clickable(
                        (By.CSS_SELECTOR, '[class="dialog__button chg-app-button chg-app-button--primary chg-app-button--extra-large chg-app-button--brand-blue"]'))).click()

        except Exception as e:
            print('All orders are cancelled:', e)
