"""Test base page logic."""
from common.webdriver_factory import create_driver_instance
from pages.base_page import BasePage


try:
    driver = create_driver_instance('chrome')
    page = BasePage(driver, 5, 'https://demoqa.com/books')
    page.open()
    page.wait_until_loaded()
    page.refresh()
finally:
    driver.close()
