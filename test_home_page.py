from common.webdriver_factory import create_driver_instance
from pages.expedia.home_page import HomePage


try:
    driver = create_driver_instance('chrome')
    page = HomePage(driver)
    page.open()
    page.wait_until_loaded()

    page.stay.wait_until_loaded()
finally:
    driver.quit()
