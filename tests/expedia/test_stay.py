"""Test Demo Form"""
import os
import pytest
from common.webdriver_factory import create_driver_instance, ROOT_DIR
from pages.expedia.home_page import HomePage

DATES_DATA = [
    (10,20),
    (5,11),
    (9,19)
]
@pytest.mark.expedia
@pytest.mark.parametrize("start_date, end_date", DATES_DATA)
def test_set_dates(start_date, end_date):
    """Test form"""
    driver = create_driver_instance('chrome')
    page = HomePage(driver, 2)
    page.open()
    page.wait_until_loaded()
    calendar = page.stay.click_check_in()
    calendar.select_dates(10,20)
    page.stay.click_check_in()
    assert calendar.get_start_date() == start_date
    assert calendar.get_end_date() == end_date
    page.close()
