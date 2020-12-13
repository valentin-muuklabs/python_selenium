"""Test Demo Form"""
import os
import pytest
from common.webdriver_factory import create_driver_instance, ROOT_DIR
from pages.expedia.home_page import HomePage
RENT_DATES_DATA = [
    ("Mexico", "Canada", 10, 15, "0100PM", "1000PM"),
    ("Toronto", "Ontario", 1, 27, "0600AM", "0500PM"),
    ("Austin", "Dallas",21, 22, "0300AM", "0100AM"),
    ("San Diego", "Los Angeles", 11, 11, "1100AM", "1100PM"),

]

@pytest.mark.cars
@pytest.mark.parametrize("location, destination, pickup_date, dropoff_date, pickup_time, dropoff_timeime", RENT_DATES_DATA)
def test_set_dates(location, destination, pickup_date, dropoff_date, pickup_time, dropoff_timeime):
    """Test form"""

    driver = create_driver_instance('chrome')
    try:
        page = HomePage(driver, 2)
        page.open()
        page.wait_until_loaded()
        page.select_tab("cars")
        page.cars.select_pickup_location(location)
        page.cars.select_dropoff_location(destination)
        page.cars.set_pickup_time(pickup_time)
        page.cars.set_dropoff_time(dropoff_timeime)
        page.cars.set_pickup_date(pickup_date, dropoff_date)
        page.cars.submit()
    finally:
        page.close()

def test_error_message_on_fail():
    driver = create_driver_instance('chrome')
    page = HomePage(driver, 2)
    page.open()
    page.wait_until_loaded()
    page.select_tab("cars")
    page.cars.submit()
    page.cars.get_error_message()
