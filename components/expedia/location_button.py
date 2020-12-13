from components.base_component import BaseComponent
from selenium import webdriver
from selenium.webdriver.common.by import By

class LocationButton(BaseComponent):
    __PICKUP_XPATH = "//button[@data-stid='location-field-locn-menu-trigger']"
    __PICKUP_INPUT_XPATH = "//input[@id='location-field-locn']"
    __PICKUP_LOCATION_RESULT_BUTTON="//button[@data-stid='location-field-locn-result-item-button']"
    __DROPOFF_XPATH = "//button[@data-stid='location-field-loc2-menu-trigger']"
    __DROPOFF_INPUT_XPATH = "//input[@id='location-field-loc2']"
    __DROPOFF_LOCATION_RESULT_BUTTON = "//button[@data-stid='location-field-loc2-result-item-button']"


    def __init__(self, driver:webdriver, root_locator: By, timeout=10):
        super().__init__(driver, root_locator, timeout)

    def click_pikcup_location(self):
        location_button = self.get_descendant_element(self.__PICKUP_XPATH)
        location_button.click()
        return True

    def select_pickup_location(self,value):
        location_input = self.get_descendant_element(self.__PICKUP_INPUT_XPATH)
        location_input.send_keys(value)
        location_result = self.get_descendant_elements(self.__PICKUP_LOCATION_RESULT_BUTTON)
        location_result[0].click()

    def click_dropoff_location(self):
        location_button = self.get_descendant_element(self.__DROPOFF_XPATH)
        location_button.click()
        return True

    def select_dropoff_location(self,value):
        location_input = self.get_descendant_element(self.__DROPOFF_INPUT_XPATH)
        location_input.send_keys(value)
        location_result = self.get_descendant_elements(self.__DROPOFF_LOCATION_RESULT_BUTTON)
        location_result[0].click()