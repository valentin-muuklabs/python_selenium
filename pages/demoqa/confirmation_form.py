"""Abstract logic to interact with confirmation page"""
from pages.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ConfirmationForm(BasePage):
    """Confirmation Form"""

    __MSG_LOC = (By.ID, 'example-modal-sizes-title-lg')

    __TR_LOC = (By.XPATH, '//table//tbody//tr')

    __CLOSE_LOC = (By.ID, 'closeLargeModal')

    def __init__(self, driver: WebDriver, timeout: int = 5):
        super().__init__(driver, timeout)

    def open(self):
        """Open confirmation form"""
        raise NotImplemented('Method not implemented')

    def wait_until_loaded(self):
        """Wait until confirmation is loaded"""
        self._wait.until(EC.visibility_of_element_located(self.__MSG_LOC))

    def get_table_info(self) -> dict:
        """Get table info as dictionary"""
        info = {}
        table_rows = self._wait.until(EC.visibility_of_all_elements_located(self.__TR_LOC))
        for row in table_rows:
            cells = row.find_elements_by_tag_name('td')
            tmp_key = cells[0].text
            tmp_val = cells[1].text
            info[tmp_key] = tmp_val
        return info

    def close(self):
        """Close confirmation form"""
        element = self._wait.until(EC.element_to_be_clickable(self.__CLOSE_LOC))
        element.click()
