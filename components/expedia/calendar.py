"""Represent calendar form from Expedia."""
from components.base_component import BaseComponent
from selenium import webdriver
from selenium.webdriver.common.by import By


class Calendar(BaseComponent):
    """Represent stay form from Expedia."""

    __SELECTED_DATES_LOCATOR = "//*[@class='uitk-new-date-picker-selection-date']"

    __MONTHS_XPATH = "//*[contains(@class, 'uitk-new-date-picker-month-name')]"

    __APPLY_XPATH = "//*[@data-stid='apply-date-picker']"

    def __init__(self, driver: webdriver, root_locator: By, timeout: int = 10):
        super().__init__(driver, root_locator, timeout)

    def wait_until_loaded(self):
        """Wait until the body element is present in the page."""
        self.get_descendant_elements(self.__SELECTED_DATES_LOCATOR)

    def get_start_date(self) -> str:
        """Get selected start date."""
        dates = self.get_descendant_elements(self.__SELECTED_DATES_LOCATOR)
        if len(dates) == 2:
            return dates[0].text
        else:
            return None

    def get_end_date(self) -> str:
        """Get selected end date."""
        dates = self.get_descendant_elements(self.__SELECTED_DATES_LOCATOR)
        if len(dates) == 2:
            return dates[1].text
        else:
            return None

    def get_first_month(self) -> str:
        """Get first month name."""
        months = self.get_descendant_elements(self.__MONTHS_XPATH)
        if len(months) == 2:
            return months[0].text
        else:
            return None

    def get_second_month(self) -> str:
        """Get second month name."""
        months = self.get_descendant_elements(self.__MONTHS_XPATH)
        if len(months) == 2:
            return months[1].text
        else:
            return None

    def apply(self):
        """Apply changes."""
        apply = self.get_descendant_element(self.__APPLY_XPATH)
        apply.click()

    def select_dates(self, first_day: int, second_day: int):
        """Select date from calendar."""
        first_day_xpath = f"//*[@data-day='{first_day}' and not(contains(@class, 'is-disabled'))]"
        first_day_element = self.get_descendant_element(first_day_xpath)
        first_day_element.click()
        second_day_xpath = f"//*[@data-day='{second_day}' and not(contains(@class, 'is-disabled'))]"
        second_day_element = self.get_descendant_element(second_day_xpath)
        second_day_element.click()
        self.apply()