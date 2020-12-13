"""Parent page for all page object."""
from selenium.webdriver.remote.webdriver import WebDriver, WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BaseComponent:
    """Represents a web component in a web page"""
    def __init__(self,driver: WebDriver, root_locator:str, timeout:int=10):
        self._driver = driver
        self._timeout = timeout
        self._root_locator = root_locator
        self._wait = WebDriverWait(self._driver, self._timeout)

    def wait_until_loaded(self):
        tmp_loc = (By.XPATH, self._root_locator)
        self._wait.until(EC.presence_of_element_located(tmp_loc))

    def set_default_timeout(self, timeout:int = 10):
        if type(timeout) == int:
            self._timeout = timeout
            self._wait = WebDriverWait(self._driver,self._timeout)
        else:
            raise ValueError(f"invalid timeout value {timeout}")

    def get_default_timeout(self):
        """Get default timeout for explicit waits"""
        return self._timeout

    def get_root_element(self):
        tmp_loc = (By.XPATH, self._root_locator)
        return self._wait.until(EC.presence_of_all_elements_located(tmp_loc))

    def get_descendant_element(self, xpath) -> WebElement:
        """get descendant in element"""
        tmp_xpath = self._chain_xpath(xpath)
        tmp_loc = (By.XPATH, tmp_xpath)
        return self._wait.until(EC.visibility_of_element_located(tmp_loc))

    def get_descendant_elements(self, xpath) -> list:
        """get descendant in element"""
        tmp_xpath = self._chain_xpath(xpath)
        tmp_loc = (By.XPATH, tmp_xpath)
        return self._wait.until(EC.visibility_of_all_elements_located(tmp_loc))

    def _chain_xpath(self, xpath) -> str :
        """concat two xpath
        :param xpath: Xpath to concat to root
        :return: New chained xpath"""
        return self._root_locator + xpath