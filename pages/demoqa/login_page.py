from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class LoginPage(BasePage):
    __URL = 'https://demoqa.com/login'


    __USERNAME_LOC = "//input[@id='userName']"
    __PASSWORD_LOC = "//input[@id='password']"
    __LOGIN_LOC = "//*[@id='login']"
    __REGISTER_LOC = "/*[@id='newUser']"
    __INVALID_USER_LOC ="//p[@id='name' and text()='Invalid username or password!']"

    def __init__(self, driver, timeout=10 ):
        super().__init__(driver, timeout, self.__URL)

    def clickLogin(self):
        loginButton = self.__get_element(self.__LOGIN_LOC)
        loginButton.click()

    def setUserName(self, value):
        self.__send_keys_to_element(self.__USERNAME_LOC, value)

    def setPassword(self, value):
        self.__send_keys_to_element(self.__PASSWORD_LOC, value)

    def checkInvalidUser(self):
        invalidUserLocator = (By.XPATH,self.__INVALID_USER_LOC)
        self._wait.until(EC.presence_of_element_located(invalidUserLocator))
        return True


    def get_user_name(self):
        return self.__get_element_value(self.__USERNAME_LOC)

    def get_password(self):
        return self.__get_element_value(self.__PASSWORD_LOC)

    def __send_keys_to_element(self, locator, value):
        element = self.__get_element(locator)
        element.send_keys(value)

    def __get_element_value(self, locator):
        element = self.__get_element(locator)
        return element.get_attribute("value")

    def __get_element(self, locator):
        elementLocator = (By.XPATH, locator)
        element = self._wait.until(EC.presence_of_element_located(elementLocator))
        return element