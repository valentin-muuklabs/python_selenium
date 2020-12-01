"""Abstract logic to control practice form"""
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.demoqa.confirmation_form import ConfirmationForm


class PracticeForm(BasePage):
    """Practice form logic."""

    __URL = 'https://demoqa.com/automation-practice-form'

    __FIRST_NAME_LOC = (By.ID, 'firstName')

    __LAST_NAME_LOC = (By.ID, 'lastName')

    __EMAIL_LOC = (By.ID, 'userEmail')

    __GENDER_XPATH = "//*[@name='gender' and @value='{0}']/following-sibling::label"

    __GENDER_CHECKBOX_LOC = "//*[@name='gender']"

    __MOBILE_LOC = (By.ID, 'userNumber')

    __SUBJECT_INPUT_LOC = (By.ID, 'subjectsInput')

    __HOBBIES_XPATH = "//label[contains(@for, 'hobbies') and text()='{0}']"

    ___FILE_LOC = (By.ID, 'uploadPicture')

    __SELECTED_HOBBIES_LOC = (By.XPATH, "//*[@type='checkbox' and contains(@id, 'hobbies')]")

    __SELECTED_SUBJECT_LOC = (By.XPATH, "//*[contains(@class, 'subjects-auto-complete__multi-value__label')]")

    __ADDRESS_LOC = (By.ID, 'currentAddress')

    __STATE_CITY_XPATH = "//*[@id='{0}']//*[contains(@class, '-option') and text()='{1}']"

    __STATE_CITY_VAL_XPATH = "//*[@id='{0}']//*[contains(@class, '-singleValue')]"

    __SUBMIT_LOC = (By.ID, 'submit')

    def __init__(self, driver: WebDriver, timeout: int = 20):
        super().__init__(driver, timeout, self.__URL)

    def wait_until_loaded(self):
        """Wait until body is loaded"""
        self._wait.until(EC.presence_of_element_located(PracticeForm.__SUBMIT_LOC))

    def get_first_name(self) -> str:
        """Get first name"""
        return self.__get_input_value(self.__FIRST_NAME_LOC)

    def set_first_name(self, value: str):
        """Set first name"""
        self.__set_input_value(self.__FIRST_NAME_LOC, value)

    def get_last_name(self) -> str:
        """Get last name"""
        return self.__get_input_value(self.__LAST_NAME_LOC)

    def set_last_name(self, value: str):
        """Set last name"""
        self.__set_input_value(self.__LAST_NAME_LOC, value)

    def get_email(self) -> str:
        """Get last name"""
        return self.__get_input_value(self.__EMAIL_LOC)

    def set_email(self, value: str):
        """Set last name"""
        self.__set_input_value(self.__EMAIL_LOC, value)

    def get_gender(self) -> str:
        """Get selected gender"""
        tmp_loc = (By.XPATH, self.__GENDER_CHECKBOX_LOC)
        elements = self._wait.until(EC.presence_of_all_elements_located(tmp_loc))
        for element in elements:
            if element.get_attribute('checked') == 'true':
                return element.get_attribute('value')
        return None

    def set_gender(self, value):
        """Set gender"""
        tmp_xpath = self.__GENDER_XPATH.format(value)
        tmp_loc = (By.XPATH, tmp_xpath)
        element = self._wait.until(EC.element_to_be_clickable(tmp_loc))
        element.click()

    def get_mobile(self) -> str:
        """Get last name"""
        return self.__get_input_value(self.__MOBILE_LOC)

    def set_mobile(self, value: str):
        """Set last name"""
        self.__set_input_value(self.__MOBILE_LOC, value)

    __DATE_LOC = (By.ID, 'dateOfBirthInput')

    def get_date_of_birth(self):
        """Get date of birth"""
        return self.__get_input_value(self.__DATE_LOC)

    def set_date_of_birth(self, value):
        """Set date of birth"""
        element = self._wait.until(EC.element_to_be_clickable(self.__DATE_LOC))
        self.set_value_attribute(element, value)

    def get_subject(self) -> list:
        """Get subject"""
        elements = self._driver.find_elements(*self.__SELECTED_SUBJECT_LOC)
        values = []
        for element in elements:
            values.append(element.text)
        return values

    def set_subject(self, value: str):
        """Set subject information"""
        element = self._wait.until(EC.element_to_be_clickable(self.__SUBJECT_INPUT_LOC))
        element.send_keys(value)
        tmp_xpath = f"//*[contains(@class, 'subjects-auto-complete__menu-list')]//*[text()='{value}']"
        tmp_loc = (By.XPATH, tmp_xpath)
        self._wait.until(EC.element_to_be_clickable(tmp_loc))
        element.send_keys(Keys.TAB)

    def get_hobbies(self) -> str:
        """Get selected hobbies"""
        elements = self._wait.until(EC.presence_of_all_elements_located(self.__SELECTED_HOBBIES_LOC))
        values = []
        for element in elements:
            if element.get_attribute('checked') == 'true':
                values.append(element.get_attribute('value'))
        return values

    def set_hobbies(self, value: str):
        """Set hobbies: Sports, Reading, Music"""
        tmp_xpath = self.__HOBBIES_XPATH.format(value)
        tmp_loc = (By.XPATH, tmp_xpath)
        element = self._wait.until(EC.element_to_be_clickable(tmp_loc))
        element.click()

    def get_file(self):
        """Get selected file"""
        self.__get_input_value(self.___FILE_LOC)

    def set_file(self, value):
        """Set file, provide full path"""
        self.__set_input_value(self.___FILE_LOC, value)

    def get_current_address(self) -> str:
        """Get subject"""
        return self.__get_input_value(self.__ADDRESS_LOC)

    def set_current_address(self, value: str):
        """Set subject information"""
        self.__set_input_value(self.__ADDRESS_LOC, value)

    def get_state(self) -> str:
        """Return selected state"""
        return self.__get_dropdown_value('state')

    def set_state(self, value: str):
        """Set state dropdown"""
        self.__select_dropdown('state', value)

    def __get_dropdown_value(self, e_id):
        value_loc = (By.XPATH, self.__STATE_CITY_VAL_XPATH.format(e_id))
        item = self._wait.until(EC.visibility_of_element_located(value_loc))
        return item.text

    def __select_dropdown(self, e_id, value):
        # 1. Click dropdown div
        div_loc = (By.ID, e_id)
        element = self._wait.until(EC.element_to_be_clickable(div_loc))
        element.click()

        # 2. Wait for item
        opt_loc = (By.XPATH, self.__STATE_CITY_XPATH.format(e_id, value))
        item = self._wait.until(EC.element_to_be_clickable(opt_loc))

        # 3. Click item
        item.click()

    def get_city(self) -> str:
        """Return selected city"""
        return self.__get_dropdown_value('city')

    def set_city(self, value: str):
        """Set state dropdown"""
        self.__select_dropdown('city', value)

    def submit(self) -> ConfirmationForm:
        """Submit"""
        element = self._wait.until(EC.element_to_be_clickable(self.__SUBMIT_LOC))
        element.submit()
        return ConfirmationForm(self._driver)

    def __get_input_value(self, locator):
        element = self._wait.until(EC.element_to_be_clickable(locator))
        return element.get_attribute('value')

    def __set_input_value(self, locator, value):
        element = self._wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(value)
