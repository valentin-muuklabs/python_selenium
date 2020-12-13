"""Test Demo Form"""
import os
import pytest
from common.webdriver_factory import create_driver_instance, ROOT_DIR
from pages.demoqa.book_store import BookStore



SEARCH_DATA = [
    ('speaking',1),
    ('learning',1),
    ('javascript', 4),

]

@pytest.mark.parametrize("search, results",SEARCH_DATA)
def test_busqueda(search:str, results:int):
    driver = create_driver_instance("chrome")
    page = BookStore(driver,10)
    page.open()
    page.search(search)
    table_info = page.get_table_info()
    assert len(table_info) == results
    page.close()