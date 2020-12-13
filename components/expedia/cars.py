from components.base_component import BaseComponent
from selenium import webdriver
from components.expedia.calendar import Calendar
from components.expedia.input import Input
from components.expedia.location_button import LocationButton
from components.expedia.time_select import TimeSelect

class Cars(BaseComponent):
    """Represent stay form from Expedia."""

    __DESTINATION_XPATH = "//*[@data-testid='location-field-destination-container']"
    __SUBMIT_BUTTON = "//button[@data-testid='submit-button']"
    __ERROR_MESSAGE = "//*[@data-testid='lob-error-summary']"
    __CALENDAR_ROOT_XPATH = "//*[contains(@class, 'uitk-new-date-picker-menu uitk-menu uitk-menu-mounted')]"
    __PICKUP_DATE = "//*[@id='d1-btn']"
    __DROPOFF_DATE = "//*[@id='d2-btn']"

    def __init__(self, driver: webdriver, root_locator: str, timeout: int = 10):
        super().__init__(driver, root_locator, timeout)
        self.destination = Input(self._driver, self.__DESTINATION_XPATH)
        self.timeSelection  = TimeSelect(self._driver, self._root_locator)
        self.calendar = Calendar(self._driver, self.__CALENDAR_ROOT_XPATH)

    def select_pickup_location(self, value:str):
        location_button = LocationButton(self._driver, self._root_locator)
        location_button.click_pikcup_location()
        location_button.select_pickup_location(value)

    def select_dropoff_location(self, value: str):
        location_button = LocationButton(self._driver, self._root_locator)
        location_button.click_dropoff_location()
        location_button.select_dropoff_location(value)

    def submit(self):
        "Function that returns the text on the error message div"
        button = self.get_descendant_element(self.__SUBMIT_BUTTON)
        button.click()

    def get_error_message(self):
        error_message = self.get_descendant_element(self.__ERROR_MESSAGE)
        return error_message.text

    def set_pickup_time(self, value:str):
        self.timeSelection.set_pickup_time(value)

    def set_dropoff_time(self, value:str):
        self.timeSelection.set_dropoff_time(value)

    def set_pickup_date(self,first_date, second_date):
        calendar_button = self.get_descendant_element(self.__PICKUP_DATE)
        calendar_button.click()
        self.calendar.select_dates(first_date, second_date)