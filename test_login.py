"""Run test cases for practice form."""
import os
from common.webdriver_factory import create_driver_instance, ROOT_DIR
from pages.demoqa.login_page import LoginPage


driver = create_driver_instance("chrome")
login = LoginPage(driver,10)
login.open()
login.wait_until_loaded()
login.setUserName("Valentin@fulanito.com")
print(f"USer name {login.get_user_name()}")
login.setPassword("calcetin")
login.clickLogin()
login.checkInvalidUser()
login.close()

