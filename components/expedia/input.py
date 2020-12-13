from components.base_component import BaseComponent
from selenium import webdriver
from selenium.webdriver.common.by import By

class Input(BaseComponent):
    __INPUT_XPATH = "//input[@autocomplete]"
    __OPT_XPATH = "//li/button"

    def __init__(self, driver:webdriver, root_locator: By, timeout:int = 10):
        super().__init__(driver, root_locator, timeout)

    def set_value(self, value):
        self.__open()
        textbox = self.get_descendant_element(self.__INPUT_XPATH)
        textbox.send_keys(value)
        options = self.get_descendant_element(self.__OPT_XPATH)
        if len(options)>0:
            options[0].click()

    def __open(self):
        self.get_root_element().click()