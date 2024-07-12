import pytest
from pages.MainPage import MainPage

@pytest.mark.parametrize('input', [
    'Test',
    'Дюна',
    '123',
    ',,'
])
def test_positive_search(browser, config, input: str):
    search = MainPage(browser, config)
    search.go_to_page()
    search.search(input)
    current_url = search.get_current_url()
    assert '/search?phrase=' in current_url

@pytest.mark.xfail()
@pytest.mark.parametrize('input', [
    '$%^',
    '',
    ' ',
    None
])
def test_negative_search(browser, config, input: str):
    search = MainPage(browser, config)
    search.go_to_page()
    search.search(input)
    current_url = search.get_current_url()
    assert '/search?phrase=' in current_url
