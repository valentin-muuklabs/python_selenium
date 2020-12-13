from components.base_component import BaseComponent
from selenium import webdriver
from components.expedia.calendar import Calendar
from components.expedia.input import Input


class Stay(BaseComponent):
    """Represent stay form from Expedia."""

    __DESTINATION_XPATH = "//*[@data-testid='location-field-destination-container']"

    def __init__(self, driver: webdriver, root_locator: str, timeout: int = 10):
        super().__init__(driver, root_locator, timeout)
        self.destination = Input(self._driver, self.__DESTINATION_XPATH)

    __CHECKIN_XPATH = "//*[@id='d1-btn']"

    __CHECKOUT_XPATH = "//*[@id='d2-btn']"

    __CALENDAR_ROOT_XPATH = "//*[contains(@class, 'uitk-new-date-picker-menu-container')]"

    __SEARCH_XPATH = "//*[@data-testid='submit-button']"

    def click_check_in(self) -> Calendar:
        """Click check in button."""
        check_in = self.get_descendant_element(self.__CHECKIN_XPATH)
        check_in.click()
        return self._create_calendar()

    def click_check_out(self) -> Calendar:
        """Click check out button."""
        check_out = self.get_descendant_element(self.__CHECKOUT_XPATH)
        check_out.click()
        return self._create_calendar()

    def search(self):
        """Search for results"""
        search_btn = self.get_descendant_element(self.__SEARCH_XPATH)
        search_btn.click()

    def _create_calendar(self):
        return Calendar(self._driver, self.__CALENDAR_ROOT_XPATH)