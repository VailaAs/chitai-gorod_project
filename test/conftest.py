import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.implicity_wait(4)
    browser.maximize_window()
    yield browser

    browser.quit()