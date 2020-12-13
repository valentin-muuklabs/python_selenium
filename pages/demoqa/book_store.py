from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class BookStore(BasePage):
    __URL = "https://demoqa.com/books"
    __INPUT_LOC= (By.ID, 'searchBox')
    __TABLE_ROW_LOC = (By.XPATH, "//*[@class='rt-tbody']//*[@class='rt-tr-group']")
    def __init__(self, driver, timeout):
        super().__init__(driver, timeout, self.__URL)

    def wait_until_loaded(self):
        """Wait until input is loaded"""
        self._wait.until(EC.element_to_be_clickable(self.__INPUT_LOC))

    def search(self, value:str):
        element = self._wait.until(EC.element_to_be_clickable(self.__INPUT_LOC))
        element.clear()
        element.send_keys(value)

    def get_table_info(self)->dict:
        rows = self._wait.until(EC.visibility_of_all_elements_located(self.__TABLE_ROW_LOC))
        info = {}
        for index,row in enumerate(rows):
            cells = row.find_elements_by_xpath(".//*[@role='gridcell']")
            title = cells[1].text
            author = cells[2].text
            publisher = cells[3].text
            if title!=' ':
              info[index] = {'title':title, 'author': author, 'publisher':publisher}
            print(info)
        return info