"""Test Demo Form"""
import os
import pytest
from common.webdriver_factory import create_driver_instance, ROOT_DIR
from pages.demoqa.login_page import LoginPage

LOGIN_DATA =[
    ('fulano@gmail.com','145515'),
    ('valentin@muuk.com','pass.pot.14151'),
    ('','')
]
@pytest.mark.parametrize("username, password",LOGIN_DATA)
def test_login_write(username:str, password:str):
    driver = create_driver_instance("chrome")
    page = LoginPage(driver,10)
    page.open()
    page.setUserName(username)
    page.setPassword(password)
    assert page.get_user_name() == username
    assert page.get_password() == password

@pytest.mark.parametrize("username, password",LOGIN_DATA)
def test_login_fail(username:str, password:str):
    driver = create_driver_instance("chrome")
    page = LoginPage(driver,10)
    page.open()
    page.setUserName(username)
    page.setPassword(password)
    page.clickLogin()
    assert page.checkInvalidUser()