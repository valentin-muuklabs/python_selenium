"""Expedia home page"""
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from components.expedia.stay import Stay
from components.expedia.cars import Cars
from pages.base_page import BasePage


class HomePage(BasePage):
    """Home page"""

    __URL = 'https://www.expedia.mx/'

    __LOGO_LOC = (By.XPATH, "//*[contains(@class, 'header-logo')]")

    __LIST_PROPERTY_LOC = (By.ID, 'listYourProperty')

    __SUPPORT_LOC = (By.ID, 'support-cs')

    __TRIPS_LOC = (By.ID, 'itinerary')

    __STAYS_ROOT_XPATH = "//*[@id='wizard-hotel-pwa-v2']"
    __CARS_ROOT_XPATH = "//*[@id='wizard-car-pwa-1']"

    def __init__(self, driver: WebDriver, timeout: int = 5):
        super().__init__(driver, timeout, self.__URL)
        self.stay = Stay(self._driver, self.__STAYS_ROOT_XPATH, self._timeout)
        self.cars = Cars(self._driver, self.__CARS_ROOT_XPATH, self._timeout)
    def wait_until_loaded(self):
        """Wait until page is loaded"""
        self._wait.until(EC.visibility_of_element_located(self.__LOGO_LOC))

    def click_logo(self):
        """Click logo"""
        self.__click_link(self.__LOGO_LOC)

    def list_property(self):
        """Click list property"""
        self.__click_link(self.__LIST_PROPERTY_LOC)

    def support(self):
        """Click support"""
        self.__click_link(self.__SUPPORT_LOC)

    def trips(self):
        """Click trips"""
        self.__click_link(self.__TRIPS_LOC)

    __SEARCH_TABS_LOCATOR = (By.XPATH, "//*[@id='uitk-tabs-button-container']//li")

    def select_tab(self, tab_name: str):
        """Select search tab."""
        tabs = self._wait.until(EC.visibility_of_all_elements_located(self.__SEARCH_TABS_LOCATOR))
        if tab_name.lower() == 'stays' and len(tabs) >= 1:
            tabs[0].click()
        elif tab_name.lower() == 'flights' and len(tabs) >= 2:
            tabs[1].click()
        elif tab_name.lower() == 'cars' and len(tabs) >= 3:
            tabs[2].click()
        elif tab_name.lower() == 'packages' and len(tabs) >= 4:
            tabs[3].click()
        elif tab_name.lower() == 'things_to_do' and len(tabs) >= 5:
            tabs[4].click()
        else:
            raise ValueError(f'Option not available: {tab_name}')

    def __click_link(self, locator):
        element = self._wait.until(EC.element_to_be_clickable(locator))
        element.click()


    def select_car_pickup(self, location):
        self.cars.pickup_location.select_pickup_location("texas")
