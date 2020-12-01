"""Test classes"""
from common.webdriver_factory import create_driver_instance


try:
    chrome = create_driver_instance('chrome')
finally:
    chrome.quit()
