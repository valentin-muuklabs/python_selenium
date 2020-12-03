"""Factory to create new instance of web driver."""
import os
from selenium import webdriver


__COMMON_DIR = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR = os.path.dirname(__COMMON_DIR)
__CHROME_PATH = os.path.join(ROOT_DIR, 'drivers', 'chromedriver')
__FIREFOX_PATH = os.path.join(ROOT_DIR, 'drivers', 'geckodriver')


def create_driver_instance(browser_name: str):
    """Create a new web driver instance.

    :param browser_name: Browser name (chrome|firefox)
    :return: New web driver instance
    """
    if browser_name.lower() == 'chrome':
        chrome_opt = __create_chrome_options()
        return webdriver.Chrome(executable_path=__CHROME_PATH, chrome_options=chrome_opt)
    elif browser_name.lower() == 'firefox':
        firefox_driver = webdriver.Firefox(executable_path=__FIREFOX_PATH)
        firefox_driver.maximize_window()
        return firefox_driver
    elif browser_name.lower() == 'chrome-remote':
        from selenium.webdriver.remote.file_detector import LocalFileDetector
        driver = webdriver.Remote(command_executor='url')
        driver.file_detector = LocalFileDetector()
        raise NotImplemented('Not working...')
    else:
        raise ValueError(f'Invalid browser selected: {browser_name}!')


def __create_chrome_options():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    return options
