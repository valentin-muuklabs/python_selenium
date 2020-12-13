from components.base_component import BaseComponent
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class TimeSelect(BaseComponent):
    __PICKUP_TIME_SELECT = "//select[@class='uitk-field-select']"
    __DROPOFF_TIME_SELECT = "//select[@class='uitk-field-select']"

    def __init__(self,driver: webdriver, root_locator, timeout=10):
        super().__init__(driver, root_locator, timeout)

    def set_pickup_time(self,value):
        select_element = self.get_descendant_elements(self.__PICKUP_TIME_SELECT)[0]
        select = Select(select_element)
        select.select_by_value(value)

    def set_dropoff_time(self,value):
        select_element = self.get_descendant_elements(self.__DROPOFF_TIME_SELECT)[1]
        select = Select(select_element)
        select.select_by_value(value)

