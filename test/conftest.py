import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import configparser

@pytest.fixture
def browser():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.implicitly_wait(4)
    browser.maximize_window()
    yield browser

    browser.quit()

@pytest.fixture
def config():
    config = configparser.ConfigParser()
    config.read("conf.ini")
    return config
