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
    def __init__(self,driver,timeout=10 ):
        super().__init__(driver,timeout, self.__URL)

    def clickLogin(self):
        loginLocator = (By.XPATH, self.__LOGIN_LOC)
        loginButton = self._wait.until(EC.element_to_be_clickable(loginLocator))
        loginButton.click()

    def setUserName(self, value):
        userNameLocator = (By.XPATH, self.__USERNAME_LOC)
        userNameInput = self._wait.until(EC.element_to_be_clickable(userNameLocator))
        userNameInput.send_keys(value)

    def setPassword(self, value):
        passwordLocator = (By.XPATH, self.__PASSWORD_LOC)
        passwordInput = self._wait.until(EC.element_to_be_clickable(passwordLocator))
        passwordInput.send_keys(value)

    def checkInvalidUser(self):
        invalidUserLocator = (By.XPATH,self.__INVALID_USER_LOC)
        self._wait.until(EC.presence_of_element_located(invalidUserLocator))
        return True
