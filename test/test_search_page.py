import pytest
from ..pages.SearchPage import SearchPage

@pytest.mark.parametrize('input',
['Test',
 'Дюна',
 '123',
 ',,']
)
def test_positive_search(browser, config, input):
    search = SearchPage(browser, config)
    search.go_to_page()
    search.search(input)
    assert search.search_no_product_found != None or search.search_product_found != None

@pytest.mark.xfail()
@pytest.mark.parametrize('input',
['$%^',
 '',
 '😀😀😀',
 None]
)
def test_negative_search(browser, config, input):
    search = SearchPage(browser, config)
    search.go_to_page()
    search.search(input)
    assert search.search_no_product_found != None or search.search_product_found != None