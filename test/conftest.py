import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import configparser

@pytest.fixture
def browser():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.implicitly_wait(3)
    browser.maximize_window()
    # browser.get(config.get('data', 'ui_url'))
    # browser.delete_all_cookies()
    # token = 'Bearer%20' + config.get('data', 'access_token')
    # cookie = {'name': 'access_token', 'value': token}
    # browser.add_cookie(cookie)
    # browser.refresh()
    yield browser
    browser.quit()

@pytest.fixture
def config():
    config = configparser.ConfigParser()
    config.read("conf.ini")
    return config
